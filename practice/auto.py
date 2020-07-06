# Done√√√√
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://youtube.com')
searchox = driver.find_element_by_xpath('//*[@id="search"]')
searchox.send_keys('rahul kawde')

click_btn = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]/yt-icon') 
click_btn.click()