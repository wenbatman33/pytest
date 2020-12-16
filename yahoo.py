import datetime
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

chrome = webdriver.Chrome('./chromedriver')
chrome.maximize_window()
# ---------------------------------------------------------------------------------------------------------
chrome.get('https://login.yahoo.com/?.intl=tw&.lang=zh-Hant-TW&src=shp&done=https%3A%2F%2Ftw.buy.yahoo.com%2F&add=1')
# ---------------------------------------------------------------------------------------------------------
chrome.find_element_by_id('login-username').send_keys('batman33kimo')
chrome.find_element_by_id('login-signin').click()
sleep(1)
chrome.find_element_by_id('login-passwd').send_keys('pp111111')
chrome.find_element_by_id('login-signin').click()
sleep(1)
# ---------------------------------------------------------------------------------------------------------
chrome.get('https://tw.buy.yahoo.com/gdsale/PS3-%E7%84%A1%E7%B7%9A%E6%89%8B%E6%8A%8A%E5%B0%88%E7%94%A8%E9%8B%B0%E9%9B%BB%E6%B1%A0-%E5%85%85%E9%9B%BB%E9%9B%BB%E6%B1%A0-1800mA-8531430.html')
buynow = chrome.find_element_by_class_name('CheckoutBar__buyNowBtn___qgDtR')
buynow.click()
