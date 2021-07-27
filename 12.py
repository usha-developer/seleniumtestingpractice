from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
driver.maximize_window()
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")


source_element=driver.find_element_by_xpath("//*[@id='box6']")
target_element=driver.find_element_by_xpath("//*[@id='box106']")

actions=ActionChains(driver)

actions.drag_and_drop(source_element,target_element).perform()