from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
#driver.get("http://demo.automationtesting.in/Windows.html")
#print(driver.title)
#print((driver.current_url))

#driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()

#driver.set_script_timeout(5)

#driver.close()

#navigation commands

driver.get("http://newtours.demoaut.com/")

print(driver.title)

driver.get("http://pavantestingtools.blogspot.in/")
time.sleep(5)
print(driver.title)

time.sleep(5)
driver.back()
time.sleep(5)
print(driver.title)

driver.forward()
time.sleep(5)
print(driver.title)