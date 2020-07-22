from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


browser = webdriver.Chrome()
browser.get('https://orteil.dashnet.org/cookieclicker/')
browser.implicitly_wait(5) # wait for 5sec

cookie= browser.find_elements_by_id('bigCookie')
cookie_count = WebDriverWait(browser,10).until(
        EC.presence_of_element_located((By.ID,'cookies'))
    )

items = [WebDriverWait(browser,10).until(
        EC.presence_of_element_located((By.ID,'productPrice'+ str(i)) for i in range(1,-1,-1)))]
items = list(items)
action = ActionChains(browser)
action.click(cookie)

for i in range(5000):
    action.perform()
    count = int(cookie_count.text.split(' ')[0])
    # print(count)
    for item in items:
        value = int(item.text)
        if value <= count:
            upgrade_action = ActionChains(browser)
            upgrade_action.move_to_element(item)
            upgrade_action.click()
            upgrade_action.perform()