
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

browser.get('http://www.facebook.com')
# assert 'Yahoo' in browser.title

elem = browser.find_element_by_name('email')  # Find the search box
elem.send_keys('kawderahul291@gmail.com'+ Keys.TAB + 'rahul321' + Keys.RETURN)

# pas = browser.find_elements_by_xpath('//*[@id="mount_0_0"]/div/div/div[1]/div[2]/div[2]/div/div/div[1]/div/div[3]/label/input')
# pas.send_keys('sachin'+ Keys.RETURN )



# browser.quit()