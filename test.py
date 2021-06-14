from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
             
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys

meeting_1 = ""
#meeting_2 = input("Enter url of 2nd meeting:")
#meeting_3 = input("Enter url of 3rd meeting:")
#meeting_4 = input("Enter url of 4th meeting:")
#meeting_5 = input("Enter url of 5th meeting:")

def page_open_wait_Xpath(Xpath):
    try:
      element = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, Xpath ))
    )
    except:
        print("page_open_wait_xpath error")




def page_open_wait(id):
    try:
     element = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID, id))
    )
    except:
        print("page_open_wait error")
chromedriver =  "/home/kavyansh/Desktop/cisco automation/chromedriver"
brave_path = "/usr/bin/brave-browser"
option  = webdriver.ChromeOptions()
option.binary_location = brave_path
driver = webdriver.Chrome(executable_path=chromedriver , options = option)
driver.get('https://meetingsapac40.webex.com/webappng/sites/meetingsapac40/meeting/download/22fa8f64ec31aeae23ae7f9d63d41576?launchApp=true')
time.sleep(10)

meeting_number = driver.find_element_by_xpath('//*[@id="meetingSimpleContainer"]/div[2]/div[2]/div/input')
send  = ActionChains(driver)

send.move_to_element(meeting_number).click().send_keys("166 990 7158").perform()

