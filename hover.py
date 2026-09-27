from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
import time
import random

op = Options()

#op.add_argument("--headless=new") # flag
#op.add_argument("--disable-gpu") # stop using gpu 

# chrome.exe --headless=new --disable-gpu



driver = webdriver.Chrome(options=op)
driver.set_window_size(1920, 1080)

wait = WebDriverWait(driver, 10)


driver.get("https://moneylion.com")

# //*[@id="increment-btn"]
# /html/body/div[2]/div/header/div/div[1]/div[2]/button[4]/span

selector = 'body > div.Theme_root__cjHdM.Reshaped_root__rfOjL > div > header > div > div.View_root__LrrXO.View_--flex__Gptpp.View_--direction-row__d4BvM.View_--nowrap__LwWTc > div.View_root__LrrXO.View_--flex__Gptpp.View_--direction-row__d4BvM > button:nth-child(4) > span'

xp = '/html/body/div[2]/div/header/div/div[1]/div[2]/button[4]/span'

wait.until(ec.visibility_of_element_located((By.XPATH, xp)))

button = driver.find_element(By.XPATH, xp)

ActionChains(driver).move_to_element(button).perform()

time.sleep(10)


driver.quit()
