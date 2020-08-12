"""
Name: Auto Like our fav. Instagrammer.
Date: 9 Aug, 2020
Author: Deep Mehta (imdeepmehta)
"""

from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("https://www.instagram.com/accounts/login/")
time.sleep(4)
element = driver.find_element_by_name('username')
element.send_keys('username')
element = driver.find_element_by_name('password')
element.send_keys('password')
element.submit()
time.sleep(4)

driver.get("https://www.instagram.com/dinojms/")
time.sleep(4)
driver.find_element_by_css_selector('.v1Nh3').click()

while True:
	time.sleep(4)
	driver.find_element_by_css_selector('.fr66n .wpO6b').click()
	driver.find_element_by_css_selector('.coreSpriteRightPaginationArrow').click()

