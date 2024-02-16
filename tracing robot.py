#imports
import time
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pynput 


name_site = input("Enter the name of the site you want to trace: ") 

def launching_tracer():    
    while(True):
        pass

        chr_options = Options()
        chr_options.add_argument("--window-size=1920,1080")
        
            
        driver = webdriver.Chrome(options=chr_options)
        driver.get(name_site)
        time.sleep(3)

        undersand_button = driver.find_element_by_xpath('//*[@id="_evidon-banner-acceptbutton"]')
        time.sleep(3)
        undersand_button.click()
        
        
        button_start_speed = driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        button_start_speed.click()
        time.sleep(30)

        time.sleep(10)
        driver.close()

launching_tracer()

def google_tryout():
    while(True):
        pass
        
        chr_options = Options()
        chr_options.add_argument("--window-size=1920,1080")
        
            
        driver = webdriver.Chrome(options=chr_options)
        driver.get('https://www.google.com/')
        time.sleep(3)

        
        keyboard = Controller()
        keyboard.press('enter')
        keyboard.release('enter')
        time.sleep(15)
        searchbar_infos = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[2]/div[1]/div[1]/div/div[2]/input')
        searchbar_infos.send_keys(name_site)
        time.sleep(15)

        
        time.sleep(15)

#google_tryout()
