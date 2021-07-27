from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
#driver=webdriver.Firefox(executable_path="C:\Drivers\geckodriver.exe")
#driver=webdriver.Ie(executable_path="C:\Drivers\IEDriverServer.exe")

driver.get("https://www.facebook.com/")
driver.implicitly_wait(10)
#driver.get("http://newtours.demoaut.com")
print(driver.title) # for printing website tittle
print(driver.current_url) #returns the url
#driver.get("https://flights-in.gotogate.com/flights")
#print(driver.page_source) # returns html for the page
ele=driver.find_element_by_name("email")
print(ele.is_displayed())
print(ele.is_enabled())
#driver.close()
ele1=driver.find_element_by_name("pass")
print(ele1.is_displayed())
print(ele1.is_enabled())

#radiobut=driver.find_element_by_css_selector("input[value=TRIP_TYPE_RETURN]")
#print(radiobut.is_selected())