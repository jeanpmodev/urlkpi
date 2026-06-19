import json
import subprocess
import sys


def run_rye_pip_audit():
    # Construct the command to run pip-audit via rye with JSON output
    command = ["rye", "run", "pip-audit", "-f", "json"]

    try:
        # Execute the command and capture the output
        result = subprocess.run(
            command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )

        # pip-audit returns non-zero exit codes if vulnerabilities are found.
        # We parse stdout regardless of the exit code if data is present.
        if not result.stdout.strip():
            if result.returncode != 0:
                print(f"Error running pip-audit: {result.stderr}", file=sys.stderr)
            return []

        # Parse the JSON payload
        audit_data = json.loads(result.stdout)
        vulnerabilities_list = []

        # Extract package names and PYSEC codes from the JSON structure
        # Note: Depending on your pip-audit version, the root might be a list or a dict containing a 'dependencies' key.
        dependencies = (
            audit_data.get("dependencies", [])
            if isinstance(audit_data, dict)
            else audit_data
        )

        for dep in dependencies:
            package_name = dep.get("name")
            vulns = dep.get("vulns", [])

            for vuln in vulns:
                vuln_id = vuln.get("id", "")
                # Filter specifically for PYSEC identifiers if needed,
                # though pip-audit primarily returns OSV/CVE/GHSA/PYSEC IDs here.
                if vuln_id.startswith("PYSEC-") or vuln_id:
                    vulnerabilities_list.append(
                        {"package": package_name, "vuln_id": vuln_id}
                    )

        return vulnerabilities_list

    except FileNotFoundError:
        print(
            "Error: 'rye' or 'pip-audit' command not found. Ensure they are installed and in your PATH.",
            file=sys.stderr,
        )
        return []
    except json.JSONDecodeError:
        print("Error: Failed to parse JSON output from pip-audit.", file=sys.stderr)
        return []


if __name__ == "__main__":
    vulnerabilities = run_rye_pip_audit()

    if vulnerabilities:
        print(f"Found {len(vulnerabilities)} vulnerability entries:")
        for entry in vulnerabilities:
            print(f"Package: {entry['package']} -> ID: {entry['vuln_id']}")
    else:
        print("No vulnerabilities found or an error occurred.")
