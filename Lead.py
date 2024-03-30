import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
from Dummy import Niche,UserId,passWord


driver = webdriver.Chrome()
driver.get("https://instagram.com")
driver.maximize_window()
time.sleep(10)
usernameXPath = "/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input"
usernameXPath2 = "/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input"
passXpath = "/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input"
passXpath2 = "/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input"
submitXpath = "/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button"
submitXpath2 = "/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]"
NNxpath = "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div"
NNxpath2 = "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div"
LaterBtnXpath = "/html/body/div[4]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]"
searchXpath = "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/span/div/a/div"
searchInpXpath = "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/input"
try:
    userName = driver.find_element(By.XPATH, usernameXPath)
except Exception as e:
    userName = driver.find_element(By.XPATH, usernameXPath2)
try:
    passKey = driver.find_element(By.XPATH, passXpath)
except Exception as e:
    passKey = driver.find_element(By.XPATH, passXpath2)
try:
    submitBtn = driver.find_element(By.XPATH, submitXpath)
except Exception as e:
    submitBtn = driver.find_element(By.XPATH, submitXpath2)


userName.send_keys(UserId)
passKey.send_keys(passWord)
submitBtn.click()
time.sleep(10)
try:
    NotNowBtn = driver.find_element(By.XPATH, NNxpath)
except Exception as e:
    NotNowBtn = driver.find_element(By.XPATH, NNxpath2)
NotNowBtn.click()
time.sleep(10)

# LaterBtn = driver.find_element(By.XPATH, LaterBtnXpath)
# LaterBtn.click()

searchBtn = driver.find_element(By.XPATH,searchXpath)
searchBtn.click()
time.sleep(1)
searchInBtn = driver.find_element(By.XPATH, searchInpXpath)
searchInBtn.send_keys(f"#{Niche}")
searchInBtn.send_keys(Keys.ENTER)

time.sleep(150000)

