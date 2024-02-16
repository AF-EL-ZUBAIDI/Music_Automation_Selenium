#imports
import time
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Name of the music
number_of_songs = int(input("Enter the number of musics please: "))
name_song = input("Enter the name of your music please: ")
def asking(number): 
    global name_song
    global name_multi_songs
    
    i = 0
    if number == 1 :
        name_song = input("Enter the name of your music please: ") 
        return name_song
    else : 
        index_number = number+1
        while i < index_number :
            
            name_multi_songs = input("Enter the name of your song number: ")
            return name_multi_songs
            i += 1

# Launcher 
def chromelaucher(name_song):
    while(True):
    
        chr_options = Options()
        chr_options.add_argument("--window-size=1920,1080")
    
        
        service = Service(executable_path='./chromedriver/chromedriver')
        driver = webdriver.Chrome(options=chr_options, service=service)
        
        driver.get('https://youtube.com')
        time.sleep(6)

        try:
            searchbox = driver.find_element_by_xpath('/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[2]/ytd-searchbox/form/div[1]/div[1]/input')
            searchbox.send_keys(name_song)
            time.sleep(2)
            
            searchbutton = driver.find_element_by_xpath('/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[2]/ytd-searchbox/button')
            searchbutton.click()
            time.sleep(2)

            searchbutton = driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/ytd-thumbnail/a/yt-image/img')
            searchbutton.click()
            time.sleep(300)

            
        except:
            print("Error finding the button.")
            driver.quit()


def data():
    stock_folder = open("name of songs.txt","a")
    stock_folder.write("\n")
    stock_folder.write("The song name is ")
    stock_folder.write(name_song)
    stock_folder.close()
    

# Call
def calling():
    data()
    chromelaucher(name_song)
    
calling()
