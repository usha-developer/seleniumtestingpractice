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
driver.get("http://demo.automationtesting.in/Windows.html")

#driver.find_element_by_link_text('SwitchTo').click()
#driver.find_element_by_link_text('Windows').click()

driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()
print(driver.current_window_handle)
handles=driver.window_handles
for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)
    if driver.title=='Frames & windows':
        driver.close()
driver.quit()
