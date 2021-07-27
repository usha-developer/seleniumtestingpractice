from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
driver.maximize_window()
driver.get("http://swisnl.github.io/jQuery-contextMenu/demo.html")
button=driver.find_element_by_xpath("/html/body/div/section/div/div/div/p/span")
actions=ActionChains(driver)
actions.context_click(button).perform()
