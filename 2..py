from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
#driver=webdriver.Firefox(executable_path="C:\Drivers\geckodriver.exe")
#driver=webdriver.Ie(executable_path="C:\Drivers\IEDriverServer.exe")

driver.get("http://newtours.demoaut.com/")

print(driver.title) # for printing website tittle
print(driver.current_url) #returns the url

print(driver.page_source) # returns html for the page

driver.close()