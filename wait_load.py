from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
import random

op = Options()

op.add_argument("--headless=new") # flag
op.add_argument("--disable-gpu") # stop using gpu 

# chrome.exe --headless=new --disable-gpu


driver = webdriver.Chrome(options=op)
wait = WebDriverWait(driver, 10)


driver.get("https://selenium-practice.danielsam.cc")

# //*[@id="increment-btn"]

button = driver.find_element(By.XPATH, '//*[@id="load-btn"]')

button.click()

# wait for something to happen

#wait.until(ec.visibility_of_element_located((By.ID, "result-message")))

result_list = driver.find_element(By.ID, "result-list")

print(result_list.text) # xxx.text -> str

# assert str length > 0

assert len(result_list.text) > 0, "[ERR] Component not loaded!"


driver.quit()
