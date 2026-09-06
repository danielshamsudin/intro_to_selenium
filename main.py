from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import random


NUM_TEST = random.randint(1,10)


op = Options()

op.add_argument("--headless=new") # flag
op.add_argument("--disable-gpu") # stop using gpu 

# chrome.exe --headless=new --disable-gpu


driver = webdriver.Chrome(options=op)

driver.get("https://selenium-practice.danielsam.cc")

# //*[@id="increment-btn"]

button = driver.find_element(By.XPATH, '//*[@id="increment-btn"]')

for i in range(NUM_TEST):
	button.click()

counter = driver.find_element(By.XPATH, '//*[@id="counter-value"]')

print(f"{NUM_TEST=}")
print("Counter value from page: " + counter.text)


assert NUM_TEST, counter.text



driver.quit()
