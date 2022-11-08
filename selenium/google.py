from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.google.co.kr/imghp?hl=ko&tab=ri&ogbl")
time.sleep(1)

elem = driver.find_element("name", "q")
elem.send_keys('조코딩')
elem.submit()

driver.find_elements(By.CLASS_NAME,'.rg_i.Q4LuWd')[0].click()

while True:
    pass
# assert "Python" in driver.title
# elem = driver.find_element(By.NAME, "q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()