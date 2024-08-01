import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import time



chrome_options = Options()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)
driver.set_window_size(1900, 1000)
#yes24_url = 'http://ticket.yes24.com/Perf/50430'

yes24_url = 'http://ticket.yes24.com/Perf/50431'


driver.implicitly_wait(time_to_wait=2)  
driver.get(url=yes24_url)


driver.find_element(By.XPATH, '//*[@id="consiceLogin"]').click()
userId = driver.find_element(By.ID, "SMemberID")
userId.send_keys('touf0101')
userPwd = driver.find_element(By.ID, "SMemberPassword")
userPwd.send_keys('endud0427!')
userPwd.send_keys(Keys.ENTER)

driver.find_element(By.XPATH, '//*[@id="rncalendar"]/div/table/tbody/tr[3]/td[1]/a').click()
driver.find_element(By.XPATH, '//*[@id="PerfPlayTime"]/a/span').click()
driver.find_element(By.XPATH, '//a[@class="rn-bb03"]').click()
driver.switch_to.window(driver.window_handles[-1])
input()

driver.find_element(By.XPATH,'//*[@id="btnSeatSelect"]').click()
driver.switch_to.frame(driver.find_element(By.XPATH,'//*[@id="divFlash"]/iframe'))
driver.find_element(By.XPATH,'//*[@id="area1"]').click()


'''driver.find_element(By.XPATH,'//*[@id="divSeatArray"]/div[string-length(@title)>0]').click()
driver.find_element(By.XPATH,'//*[@id="form1"]/div[3]/div[2]/div/div[2]/p[2]/a/img').click()'''

