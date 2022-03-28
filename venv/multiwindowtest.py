from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://www.google.com/")

#open tab
driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')

# Load a page
driver.get('http://stackoverflow.com/')
# Make the tests...

# close the tab
driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'w')
driver.close()