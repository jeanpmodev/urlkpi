import requests

def get_pysec_details(vuln_id):
    url = f"https://api.osv.dev/v1/vulns/{vuln_id}"
    response = requests.get(url)
    
    if response.status_code == 200:
        vuln_data = response.json()
        print(f"ID: {vuln_data.get('id')}")
        print(f"Summary: {vuln_data.get('summary')}")
        print(f"Details: {vuln_data.get('details')}")
        print("Affected Packages:")
        for affected in vuln_data.get('affected', []):
            pkg = affected.get('package', {})
            print(f"- {pkg.get('name')} ({pkg.get('ecosystem')})")
    else:
        print("Vulnerability ID not found or API error.")

get_pysec_details("PYSEC-2026-48")
