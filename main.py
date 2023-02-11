#Cal poly fishbowl reservation bot
#automatically reserves fishbowls at a given run time.
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import time


def main():
    firstname = "Andy"
    lastname = "Lim"
    email = "alim30@calpoly.edu"
    orgname = "Korean American Student Association"
    url = "https://schedule.lib.calpoly.edu/rooms.php?i=2015"

    
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.maximize_window()
    browser.get(url)
    browser.implicitly_wait(10)
    #if December of 2022 and want to move to Jan 2023
    nxt = browser.find_element(By.XPATH, "//*[@id='s-lc-rm-cal']/div/div/a[2]")
    nxt.click()
    time.sleep(4)

    #uncomment to select correct month in 2023
    #month_select = browser.find_element(By.XPATH, "//*[@id='s-lc-rm-cal']/div/div/div/select")
    #drop = Select(month_select)
    #drop.select_by_visible_text("Feb")
    #time.sleep(4)

    #make an input where the txt '4' gets changed to whatever date you wish
    date = browser.find_element(By.XPATH, "//a[text()='4']")
    date.click()
    time.sleep(2)

    #select three first available slots'
    avail_times = browser.find_elements(By.XPATH, "//table[@id='s-lc-rm-scrolltb']//a")
    slots = 0
    while slots < 3:
        avail_times[slots].click()
        slots += 1
        time.sleep(1)

    #filling in texts
    #first name
    fname = browser.find_element(By.XPATH, "//*[@id='fname']")
    fname.send_keys(firstname)
    time.sleep(1)
    #last name
    lname =browser.find_element(By.XPATH, "//*[@id='lname']")
    lname.send_keys(lastname)
    time.sleep(1)
    #email
    mail = browser.find_element(By.XPATH, "//*[@id='email']")
    mail.send_keys(email)
    time.sleep(1)
    #group name
    gname = browser.find_element(By.XPATH, "//*[@id='nick']")
    gname.send_keys(orgname)
    time.sleep(1)

    #submission
    #submit = browser.find_element(By.XPATH, "//*[@id='s-lc-rm-sub']")
    #submit.click()
    time.sleep(3)

    browser.quit()



if '__main__':
    main()