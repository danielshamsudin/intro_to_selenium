from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import random

op = Options()

op.add_argument("--headless=new") # flag
op.add_argument("--disable-gpu") # stop using gpu 

# chrome.exe --headless=new --disable-gpu


driver = webdriver.Chrome(options=op)

driver.get("https://selenium-practice.danielsam.cc")



# 1st case - username and password valid
# //*[@id="username"]  username field
# //*[@id="password"]  password field

username = driver.find_element(By.XPATH, '//*[@id="username"]')
password = driver.find_element(By.XPATH, '//*[@id="password"]')
login_btn = driver.find_element(By.ID, 'login-btn')
login_status = driver.find_element(By.ID, 'login-status')

username.send_keys("daniel@daniel.com")
password.send_keys("123123123")
login_btn.click()
print(f"[PAGE LOG] -> {login_status.text}")

assert login_status.text == "Welcome, daniel@daniel.com!", "Banner success message is wrong"

# 2nd case - no username and password entered

username.clear()
password.clear()

login_btn.click()
print(f"[PAGE LOG] -> {login_status.text}")

assert login_status.text == "Please enter your username and password."


driver.quit()
