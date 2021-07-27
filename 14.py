from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")

driver.get("http://demo.automationtesting.in/Filedownload.html")
driver.maximize_window()
#downloadingtextfile
