import requests 
import time
from py_w3c.validators.html.validator import HTMLValidator

show_ulrs = ["/dash/","/dash/boiler/","/dash/copy/","/dash/filemanager/","/dash/integrity/","/dash/plagiarism/","/dash/pyerrors/","/dash/tests/","/dash/tracking/","/dash/uml/"]
front_end_html = HTMLValidator()

for item in show_ulrs:
	url = "http://127.0.0.1:8000"+item
	print(2*"\n"+"URL ROUTE : "+url+1*"\n")
	time.sleep(2)
	response = requests.get(url)
	front_end_html.validate_fragment(response.text)
	if front_end_html.errors:
		print("Errors found:")
		for error in front_end_html.errors:
			print(f"- {error.get('message')}")
			time.sleep(1)
	else:
		print("No errors found!")
	if front_end_html.warnings:
	    print("\nWarnings:")
	    for warning in front_end_html.warnings:
	        print(f"- {warning.get('message')}")
	        time.sleep(1)