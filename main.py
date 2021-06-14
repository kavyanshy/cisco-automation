from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import pyautogui

def click2(x,y):
    pyautogui.click(x,y)


def enter_keys(keys):
    pyautogui.typewrite(keys)




def Enterkeys(element,keys,browser):
    send  = ActionChains(browser)
    send.click(on_element = element).send_keys(keys).perform() 


def click1(element,browser):
    click = ActionChains(browser)
    click.click(on_element = element)
    click.perform()


def page_open_wait(id):
    try:
     element = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID, id))
    )
    except:
        print("page_open_wait error")


driver = webdriver.Firefox()
driver.implicitly_wait(10)
# get geeksforgeeks.org
driver.get('https://signin.webex.com/join?surl=https%3A%2F%2Fsignin.webex.com%2Fcollabs%2F%23%2Fmeetings%2Fjoinbynumber%3F')
time.sleep(1)
def outer():
    meeting_number = driver.find_element_by_css_selector('.el-input__inner')
    time.sleep(2)
    Enterkeys(meeting_number,"126 498 7150",driver)

    time.sleep(3)
    meeting_number_continue = driver.find_element_by_id("continue")
    click1(meeting_number_continue,driver)
    page_open_wait('smartJoinButton')
    join_button = driver.find_element_by_id("smartJoinButton")
    click1(join_button,driver)

    time.sleep(20)
    click2(577,434)
    time.sleep(1)
    enter_keys("kavyansh yadav")

    click2(674,491)
    time.sleep(1)
    enter_keys("kavyanshy66@gmail.com")
    time.sleep(2)

    click2(671,553)

    time.sleep(3)


def website2():
    
    
        meeting_number = driver.find_element_by_css_selector('.el-input__inner')
        time.sleep(1)
        Enterkeys(meeting_number,"1844384775",driver)

        time.sleep(1)
        meeting_number_continue = driver.find_element_by_id("continue")
        click1(meeting_number_continue,driver)

        
        
       # name = driver.find_element_by_css_selector(".style-input-33p0A")
       # Enterkeys(name,"kavyansh yadav",driver)
        
        #contunue1 = driver.find_element_by_id("guest_next-btn")
       # click1(contunue1,driver)

        
website2()
time.sleep(10)
password_click = click2(664,536)
enter_keys("12345")
time.sleep(3)
ok_click = click2(551,593)
time.sleep(3)
page_open_wait('smartJoinButton')
join_button = driver.find_element_by_id("smartJoinButton")
click1(join_button,driver)
time.sleep(10)
click2(577,434)
time.sleep(1)
enter_keys("kavyansh yadav")

click2(674,491)
time.sleep(1)
enter_keys("kavyanshy66@gmail.com")
time.sleep(2)

click2(671,553)
allow_microphone_camera = click2(655,354)
time.sleep(3)
microphone = click2(519,740)
time.sleep(3)
camera = click2(655,748)
time.sleep(2)
start = click2(809,733)


mute = driver.find_element_by_css_selector(".style-center-region-1qM7r > div:nth-child(1) > div:nth-child(1) > button:nth-child(1)")


def bottom():
  unmute = driver.find_element_by_css_selector('div.style-button-container-2_tt5:nth-child(1) > div:nth-child(1) > button:nth-child(1)')
  unmute_attribute = unmute.get_attribute('data-doi')
  print(unmute)

