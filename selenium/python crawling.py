from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from urllib import request

#web settings
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)
driver.get("https://www.google.co.kr/imghp?hl=ko&tab=ri&ogbl")

# driver = webdriver.Chrome()   #(시스템에 부착된 장치가 작동하지 않습니다.)의 오류
# driver.get("https://www.google.co.kr/imghp?hl=ko&tab=ri&ogbl")
# time.sleep(1)

#search words
elem = driver.find_element("name", "q")
elem.send_keys('조코딩')
elem.submit()

imgs=driver.find_elements(By.CSS_SELECTOR,".rg_i.Q4LuWd")

#scroll
SCROLL_PAUSE_TIME = 0.5

        # Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

#images download
for i in range(10):
    imgs[i].click()
    time.sleep(1)
    img=(driver.find_element(By.CSS_SELECTOR,".n3VNCb.KAlRDb").get_attribute("src"))
    request.urlretrieve(img, str(i)+".jpg")


 
# assert "Python" in driver.title
# elem = driver.find_element(By.NAME, "q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()