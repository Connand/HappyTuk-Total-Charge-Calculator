from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


options = Options()
options.add_argument("start-maximized")
options.add_argument("--disable-notifications")

chrome = webdriver.Chrome('./chromedriver', chrome_options=options)
chrome.get("https://www.mangot5.com/Index/Billing/History?cPage=1")

#Wait for login
WebDriverWait(chrome, 600).until(EC.presence_of_element_located((By.XPATH, "//table[@class='table table-small-font table-striped']")))

#After login

total = 0
lastPage = False
btn = chrome.find_element_by_xpath("//*[text()='»']")
while(btn):
    #Find table
    table = chrome.find_element_by_xpath("//table[@class='table table-small-font table-striped']")
    trlist = table.find_element_by_tag_name('tbody')
    trlist = trlist.find_elements_by_tag_name('tr')
    
    #Find table elements of "XXX TWD"
    for row in trlist:
        tdlist = row.find_elements_by_tag_name('td')
        txt = tdlist[1].text
        total = total + int(txt[0:txt.find(" TWD")])
        print("編號", tdlist[0].text, ":", txt)
    
    if lastPage: break

    #Click and wait for loading
    try:
        btn.click()
        WebDriverWait(chrome, 5).until(
            EC.presence_of_element_located((By.XPATH, "//table[@class='table table-small-font table-striped']")))
    except TimeoutException:
        print("Timed out waiting for page to load")
        
    try:
        btn = chrome.find_element_by_xpath("//*[text()='»']")
    except:
        lastPage = True
        
jscommand = "alert('ㄋ總共課了" + str(total) + "元')"
print("\n\nㄋ總共課了", total, "元")
chrome.execute_script(jscommand)

#btn = chrome.find_element_by_xpath("//*[text()='»']")
#btn = chrome.find_element_by_xpath("//*[text()='«']")
#if not btn: