from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome(executable_path=r"C:\chromedriver_win32\chromedriver.exe",options=options)
browser.maximize_window()
browser.get("https://web.whatsapp.com/")

#scanning code

#input("press any key once you've scanned QR code: ")
#print("QR Code Scanned Successfully")

search_xpath = '//*[@id="side"]/div[1]/div/label/div/div[2]'
search_box = WebDriverWait(browser,400).until(EC.presence_of_element_located((By.XPATH,search_xpath)))
search_box.send_keys("Diego")