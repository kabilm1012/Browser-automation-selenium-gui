from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--diasble-search-engine-choice-screen")

service = Service("chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get('https://demoqa.com/login')

input("Press enter to close the browser")
driver.quit()
