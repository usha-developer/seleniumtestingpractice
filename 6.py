
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
#driver=webdriver.Firefox(executable_path="C:\Drivers\geckodriver.exe")
#driver=webdriver.Ie(executable_path="C:\Drivers\IEDriverServer.exe")
#driver.implicitly_wait(5)
driver.maximize_window()
driver.get("http://demo.automationtesting.in/Alerts.html")
driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/ul/li[2]/a').click()

driver.find_element_by_xpath('//*[@id="CancelTab"]/button').click()
time.sleep(5)
#driver.switch_to_alert().accept()
driver.switch_to_alert().dismiss()

