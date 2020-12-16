import datetime
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('./chromedriver')
driver.maximize_window()
# ---------------------------------------------------------------------------------------------------------
driver.get('https://www.momoshop.com.tw/mypage/MemberCenter.jsp?cid=memb&oid=checkorders&func=00&mdiv=1099800000-bt_0_150_01-bt_0_150_01_e8&ctype=B')
# ---------------------------------------------------------------------------------------------------------
driver.find_element_by_id('memId').send_keys('0920910786')
driver.find_element_by_name('passwd').send_keys('wen671002')
driver.find_element_by_id('login').click()
sleep(1)
# ---------------------------------------------------------------------------------------------------------
driver.get('https://www.momoshop.com.tw/goods/GoodsDetail.jsp?i_code=8267515&str_category_code=2900100441')
buynow = driver.find_element_by_class_name('buynow')
buynow.click()
