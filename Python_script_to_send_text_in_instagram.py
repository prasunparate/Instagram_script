#PYTHON Script to open instagram and send messages 
#this is script is developed by Prasun 
#connect with me on linkedin - https://www.linkedin.com/in/prasun-kumar-parate/
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
import time
username = '' #please enter your username here
password = '' #please enter your password here
driver = webdriver.Firefox()     #You can use chrome here or anyother browser
driver.get("https://www.instagram.com")

time.sleep(3)
driver.find_element("name","username").send_keys(username)
driver.find_element("name","password").send_keys(password)
driver.find_element("id", "loginForm").click()

driver.implicitly_wait(4)

element = driver.find_element(By.LINK_TEXT, "Messages").click()

driver.implicitly_wait(10)

driver.find_element(By.XPATH, '//button[@class="_a9-- _ap36 _a9_1"]').click()

driver.implicitly_wait(4) #this is needed just to ensure the gets fully loaded, you can increase the time (in seconds) if required
wait(driver, 4).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='<Enter_the_person_username>']"))).click() #replace the placeholder with the person's username whom you want to send the message
driver.implicitly_wait(8)

wait(driver, 4).until(EC.element_to_be_clickable((By.XPATH, "//div[class()='xat24cr xdj266r']"))).send_keys("Hi this is a sample message ;)") #this line is used to enter message in the text box

wait(driver, 4).until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Send']"))).click()