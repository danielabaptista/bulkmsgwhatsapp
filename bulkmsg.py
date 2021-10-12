from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pyperclip
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome(executable_path=r"C:\chromedriver_win32\chromedriver.exe",options=options)
browser.maximize_window()
browser.get("https://web.whatsapp.com/")

#scanning code

#input("press any key once you've scanned QR code: ")
#print("QR Code Scanned Successfully")
contact="Diego Alemania"
msg="Msje enviado con Python"

search_xpath = '//*[@id="side"]/div[1]/div/label/div/div[2]'
search_box = WebDriverWait(browser,400).until(EC.presence_of_element_located((By.XPATH,search_xpath)))
search_box.send_keys(contact)

time.sleep(2)

contact_xpath = f'//span[@title="{contact}"]'
contact_title = browser.find_element_by_xpath(contact_xpath)
contact_title.click()

time.sleep(2)

input_xpath = '//*[@id="main"]/footer/div[1]/div/div/div[2]/div[1]/div/div[2]'
input_box = browser.find_element_by_xpath(input_xpath)

pyperclip.copy(msg)
input_box.send_keys(Keys.SHIFT, Keys.INSERT)  # Keys.CONTROL + "v"
input_box.send_keys(Keys.ENTER)