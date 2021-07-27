from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
driver.maximize_window()

driver.get("https://testautomationpractice.blogspot.com/")
#driver.switch_to_frame(0)
#driver.find_element_by_id("RESULT_FileUpload-10").send_keys("E:\WT BANKING\pic1.jpg")
tr=len(driver.find_elements_by_xpath("//*[@id='HTML1']/div[1]/table/tbody/tr"))
tc=len(driver.find_elements_by_xpath("//*[@id='HTML1']/div[1]/table/tbody/tr[1]/th"))
print("bookname   "+"author   "+"subject     "+"price")
for r in range(2,tr+1):
    for c in range(1,tc+1):
        data=driver.find_element_by_xpath("//*[@id='HTML1']/div[1]/table/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(data,end="   ")
    print()

