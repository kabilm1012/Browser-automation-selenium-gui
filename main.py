from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os

# Define driver, options, and service
chrome_options = Options()
chrome_options.add_argument("--diasble-search-engine-choice-screen")

downnload_path = os.getcwd()
prefs = {'download.default_directory': downnload_path}
chrome_options.add_experimental_option('prefs', prefs)

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

# Locate the elements dropdown and textbox
elements = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div/div[1]/div/div/div[1]/span/div')))
elements.click()
text_box = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'item-0')))
text_box.click()

# Locate the form fields ans submit button
fullname_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
email_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'userEmail')))
current_address_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'currentAddress')))
permanent_address_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'permanentAddress')))
submit_button = driver.find_element(By.ID, 'submit')

# Fill the form fields
fullname_field.send_keys("Kabil Murugan")
email_field.send_keys("kabilm1012@gmail.com")
current_address_field.send_keys("Kamaraj Nagar, PeriyanaickenPalayam, Coimbatore")
permanent_address_field.send_keys("Kamaraj Nagar, PeriyanaickenPalayam, Coimbatore")
driver.execute_script("arguments[0].click();", submit_button)

# Locate the upload and download section and download button
upload_download = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'item-7')))
upload_download.click()
download_button = driver.find_element(By.ID, 'downloadButton')
driver.execute_script("arguments[0].click();", download_button)

input("Press enter to close the browser")
driver.quit()
