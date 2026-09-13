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

driver.set_window_size(1920, 1080)

driver.get("https://google.com")

driver.save_screenshot("google.png")

driver.quit()
