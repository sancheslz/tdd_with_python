import os
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

geckodriver_path = os.path.join(os.getcwd(), '..', 'geckodriver')
ff_options = Options()
ff_options.add_argument('--headless')

browser = webdriver.Firefox(
    executable_path=geckodriver_path,
    options=ff_options
)

browser.get('http://localhost:8000')

assert 'Django' in browser.title

browser.quit()
