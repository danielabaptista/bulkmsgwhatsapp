from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pyperclip
import pandas
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome(executable_path=r"C:\chromedriver_win32\chromedriver.exe",options=options)
browser.maximize_window()
browser.get("https://web.whatsapp.com/")

#scanning code

#input("press any key once you've scanned QR code: ")
#print("QR Code Scanned Successfully")

#Gmail Contacts CSV
df = pandas.read_csv('contacts.csv', encoding='latin')
contacts = df['Name'].to_list()

names=[]
for i in contacts:
    name=i.split()
    names.append(name[1])

#print(names)
num_msg=0
for (contact,name) in zip(contacts,names):
    print(f'Contacto: {contact}, Nombre: {name}')
    #msg=f'Probando Probando .. \n{contact}\nHola {name} 😁\n'
    msg=(f'Hola {name}')
    
    #print(msg)

    search_xpath = '//*[@id="side"]/div[1]/div/label/div/div[2]'
    search_box = WebDriverWait(browser,600).until(EC.presence_of_element_located((By.XPATH,search_xpath)))
    search_box.send_keys(contact)
    browser.implicitly_wait(5)
    #time.sleep(2)

    contact_xpath = f'//span[@title="{contact}" and @class="emoji-texttt _ccCW FqYAR i0jNr"]'
    contact_title = browser.find_element_by_xpath(contact_xpath)
    browser.implicitly_wait(10)
    #time.sleep(2)
    #click 
    contact_title.click()
    #time.sleep(2)

    input_xpath = '//*[@id="main"]/footer/div[1]/div/div/div[2]/div[1]/div/div[2]'
    input_box = browser.find_element_by_xpath(input_xpath)
    #copy and paste paste msg
    pyperclip.copy(msg)
    input_box.send_keys(Keys.SHIFT, Keys.INSERT)  # Keys.CONTROL + "v"
    browser.implicitly_wait(10)
    #time.sleep(2)

    #click to send msg
    input_box.send_keys(Keys.ENTER)
    num_msg=num_msg+1
    print(f'Mensaje enviado con éxito a {contact}\nMensaje núm: {num_msg}\n\n')
    time.sleep(5)

