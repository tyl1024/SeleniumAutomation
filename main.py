from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def main():
    intro()
    PATH = r"C:\Users\PenguinVibes\Downloads\chromedriver_win32\chromedriver.exe"
    #driver = webdriver.Chrome(PATH)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.tiktok.com/")
    time.sleep(9)
    
    
    
    
def intro():
    print("Creating TikTok bots")    
    
    
    
main()