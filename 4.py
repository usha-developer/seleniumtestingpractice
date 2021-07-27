
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
#driver=webdriver.Firefox(executable_path="C:\Drivers\geckodriver.exe")
#driver=webdriver.Ie(executable_path="C:\Drivers\IEDriverServer.exe")
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("http://demo.automationtesting.in/Register.html")
driver.implicitly_wait(10)

radiobtn=driver.find_element_by_css_selector("input[value=Male]")
print(radiobtn.is_selected())
driver.find_element_by_xpath("//*[@id='header']/nav/div/div[2]/ul/li[1]/a").click()
driver.find_element_by_xpath("//*[@id='btn2']").click()
driver.find_element_by_xpath("//*[@id='basicBootstrapForm']/div[1]/div[1]/input").send_keys("usha")

driver.find_element_by_xpath("//*[@id='basicBootstrapForm']/div[1]/div[2]/input").send_keys("rani")



