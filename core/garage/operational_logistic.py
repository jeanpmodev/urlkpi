# just one garage , cars, drivers and routes


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

drivers = ['octo']

vehicles = ['cg_fan', 'corvette_stingray','golf_git']

routes = ['demo_route']

driver = webdriver.Chrome()


def demo_route():
	url_demo_route = [
	'http://127.0.0.1:8000/dash/',
	'http://127.0.0.1:8000/dash/boilerplate/',
	'http://127.0.0.1:8000/dash/copyright/',
	'http://127.0.0.1:8000/dash/file-management/',
	'http://127.0.0.1:8000/dash/software-integrity/',
	'http://127.0.0.1:8000/dash/plagiarism/',
	'http://127.0.0.1:8000/dash/pep-errors/',
	'http://127.0.0.1:8000/dash/tests/',
	'http://127.0.0.1:8000/dash/datatracking/',
	'http://127.0.0.1:8000/dash/uml-management/',
	'http://127.0.0.1:8000/dash/devops/'
	]
	try:
		while True:
			for url in url_demo_route:
				driver.get(url)
				time.sleep(5)
	except KeyboardInterrupt:
		print("\nthe tour was interrupted")
	finally:
		driver.quit()

if __name__ == "__main__":
    demo_route()