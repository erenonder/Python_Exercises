from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Safari()
driver.get("https://www.netflix.com/")
# print(driver.title)
assert("Netflix Netherlands" in driver.title)

# search_button = driver.find_element_by_css_selector("icon-search")
# search_button.click()
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# cookies = driver.get_cookies()
# print(cookies)
driver.close()