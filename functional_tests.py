from selenium import webdriver

browser = webdriver.Chrome()
#browser = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application")

browser.get('http://localhost:8000')

assert 'Django' in browser.title
