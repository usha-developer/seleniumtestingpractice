from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window()
#driver.execute_script("window.scrollBy(0,1000)","")

#flag=driver.find_element_by_xpath("//*[@id='content']/div[2]/div[2]/table[1]/tbody/tr[86]/td[1]/img")
#driver.execute_script("arguments[0].scrollIntoView();",flag)
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
