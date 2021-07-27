from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com")
driver.find_element_by_xpath("//*[@id='txtUsername']").send_keys("Admin")
driver.find_element_by_xpath("//*[@id='txtPassword']").send_keys("admin123")
driver.find_element_by_xpath("//*[@id='btnLogin']").click()
admin=driver.find_element_by_xpath("//*[@id='menu_admin_viewAdminModule']")
admin1=driver.find_element_by_xpath("//*[@id='menu_admin_UserManagement']")
admin2=driver.find_element_by_xpath("//*[@id='menu_admin_viewSystemUsers']")
actions=ActionChains(driver)

actions.move_to_element(admin).move_to_element(admin1).move_to_element(admin2).click().perform()
