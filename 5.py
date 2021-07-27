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
driver.get("http://demo.automationtesting.in/Register.html")
#driver.implicitly_wait(10)
inputboxes=driver.find_elements(By.CLASS_NAME,'form-control')
print(len(inputboxes))
q=driver.find_element(By.XPATH,'//*[@id="basicBootstrapForm"]/div[1]/div[1]/input').is_displayed()
q1=driver.find_element(By.XPATH,'//*[@id="basicBootstrapForm"]/div[1]/div[1]/input').is_enabled()
print(q,q1)

driver.find_element(By.XPATH,'//*[@id="basicBootstrapForm"]/div[1]/div[1]/input').send_keys("usha")
driver.find_element(By.XPATH,'//*[@id="basicBootstrapForm"]/div[1]/div[2]/input').send_keys("rani")

a=driver.find_element(By.XPATH,'//*[@id="basicBootstrapForm"]/div[5]/div/label[1]/input').is_selected()
print(a)

driver.find_element(By.XPATH,'//*[@id="basicBootstrapForm"]/div[5]/div/label[1]/input').click()
a1=a=driver.find_element(By.XPATH,'//*[@id="basicBootstrapForm"]/div[5]/div/label[1]/input').is_selected()
print(a1)

driver.find_element_by_id('checkbox1').click()
st=driver.find_element_by_id('checkbox1').is_selected()
print(st)

s=Select(driver.find_element_by_id('Skills'))
#s.select_by_visible_text('Android')
#s.select_by_index(2)
s.select_by_value('C')

s1=len(s.options)
print(s1)
allop=s.options
for op in allop:
    print(op.text)

links=driver.find_elements(By.TAG_NAME,"a")
link=len(links)
print(link)

for ll in links:
    print(ll.text)
driver.find_element(By.LINK_TEXT,'Practice Site').click()
#driver.find_element(By.PARTIAL_LINK_TEXT,'Pract').click()


