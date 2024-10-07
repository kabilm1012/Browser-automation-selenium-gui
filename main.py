from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Define driver, options, and service
chrome_options = Options()
chrome_options.add_argument("--diasble-search-engine-choice-screen")
service = Service("chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)

# Load the page
driver.get('https://demoqa.com/login')

# Locate username, password and login
username_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
password_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'password')))
login_button = driver.find_element(By.ID, 'login')

# Fillin username and password
username_field.send_keys("kabilmk")
password_field.send_keys("Kabilm@1012")
driver.execute_script("arguments[0].click();", login_button)


input("Press enter to close the browser")
driver.quit()
