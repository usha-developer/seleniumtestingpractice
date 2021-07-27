
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
#chromeOptions=Options()
#chromeOptions.add_experimental_option("prefs",{"download.default_directory": "C:\Downloadedfiles"})
driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
#driver=webdriver.Firefox(executable_path="C:\Drivers\geckodriver.exe")
driver.maximize_window()
driver.get("http://demo.automationtesting.in/FileDownload.html")

#driver.find_element_by_xpath("//*[@id='textbox']").send_keys("welcome to selenium tutorials")
#driver.find_element_by_xpath("//*[@id='createTxt']").click()
#driver.find_element_by_xpath("//*[@id='link-to-download']").click()

driver.find_element_by_xpath("//*[@id='pdfbox']").send_keys("welcome to selenium tutorials")
driver.find_element_by_xpath("//*[@id='createPdf']").click()
driver.find_element_by_xpath("//*[@id='pdf-link-to-download']").click()
