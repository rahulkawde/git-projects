# nevigation:    click button / serach 

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


browser = webdriver.Chrome()

browser.get('https://www.codewithharry.com')


elem = browser.find_element_by_name('query')  # Find the search box
elem.send_keys('python' + Keys.RETURN)

try :
    element = WebDriverWait(browser,10).until(
        EC.presence_of_element_located((By.LINK_TEXT,'Python Tutorial In Hindi'))
    )
    element.click()
    browser.back()
    browser.back()
    browser.forward()
    element = WebDriverWait(browser,10).until(
        EC.presence_of_element_located((By.LINK_TEXT,'I automated Dinosaur Game in Chrome'))
    )
    element.click()
    element = WebDriverWait(browser,10).until(
        EC.presence_of_element_located((By.XPATH,'//*[@id="overview"]/div/pre/button'))
    ) # click button using xpath
    element.click()



except:
    browser.quit()
