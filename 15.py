from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
driver.switch_to_frame(0)
driver.find_element_by_id("RESULT_FileUpload-10").send_keys("E:\WT BANKING\pic1.jpg")
