import json
import urllib.request

url = "https://api.osv.dev/v1/vulns/PYSEC-2026-48"

try:
    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read().decode())
        
        # Get the database_specific import source URL
        import_source = data.get('database_specific', {}).get('import_source')
        print(f"Import Source: {import_source}")
        
        # Get the primary reference URL
        references = [ref['url'] for ref in data.get('references', [])]
        print(f"Advisory References: {references}")


except urllib.error.URLError as e:
    print(f"Error fetching vulnerability: {e.reason}")

for item in references:
    print(item)