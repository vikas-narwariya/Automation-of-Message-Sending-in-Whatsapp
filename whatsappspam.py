import pyautogui 
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome('C:\chromedriver')

driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)

time.sleep(30)
for i in range(10):
    pyautogui.press("H")
    pyautogui.press("E") 
    pyautogui.press("L")
    pyautogui.press("L")
    pyautogui.press("O")
    pyautogui.press("enter")
    pyautogui.press("G")
    pyautogui.press("U")
    pyautogui.press("Y")
    pyautogui.press("S")
    pyautogui.press("enter")