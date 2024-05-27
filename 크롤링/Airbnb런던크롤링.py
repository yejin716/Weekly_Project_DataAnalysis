from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains 
from selenium.webdriver.common.keys import Keys

import time

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
#브라우저를 자동화한 후 >> browser window 창 유지 
chrome_options.add_experimental_option("excludeSwitches", ['enable-logging'])
#excludeSwitches : 불필요한 로깅 메시지 >> 브라우저에서 제외 


driver = webdriver.Chrome(options=chrome_options)
# 브라우저 창 크기 설정
driver.set_window_size(1920, 1080)  # 예: 1920x1080 해상도

url = "https://www.airbnb.com/rooms/1113966989586525761"

driver.get(url)
time.sleep(3)

#html 다운로드 및 bs4 로 읽기 
from bs4 import BeautifulSoup

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

#번역창 닫기 
driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(50) > div > div > section > div > div > div.p1psejvv.atm_9s_1bgihbq.dir.dir-ltr > div > div.c1lbtiq8.atm_mk_stnw88.atm_9s_1txwivl.atm_fq_1tcgj5g.atm_wq_kb7nvz.atm_tk_1tcgj5g.dir.dir-ltr > button").send_keys(Keys.ENTER)
# close_button = soup.select('body > div:nth-child(50) > div > div > section > div > div > div.p1psejvv.atm_9s_1bgihbq.dir.dir-ltr > div > div.c1lbtiq8.atm_mk_stnw88.atm_9s_1txwivl.atm_fq_1tcgj5g.atm_wq_kb7nvz.atm_tk_1tcgj5g.dir.dir-ltr > button')
# print(len(songs))
# print(close_button[0])
# etc = soup.select("#react-application > div > div > div:nth-child(1) > div > div._1i7ccu91 > div > div > div > div > div._1k81gub > div.cgx2eil.atm_mk_h2mmj6.dir.dir-ltr > div:nth-child(1) > div:nth-child(4) > div > div > div > div > div > section > div.o1kjrihn.atm_c8_km0zk7.atm_g3_18khvle.atm_fr_1m9t47k.atm_h3_1y44olf.atm_c8_2x1prs__oggzyc.atm_g3_1jbyh58__oggzyc.atm_fr_11a07z3__oggzyc.dir.dir-ltr > ol > li")
# print(etc)

#침대수, 욕실수 가져오기
etc = driver.find_element(By.XPATH, '//ol[contains(@class, "lgx66tx atm")]')
print(etc.text)
time.sleep(1)

# #스크롤 내리기
# for c in range(0,5):
#     driver.find_element(By.TAG_NAME,'body').send_keys(Keys.PAGE_DOWN)
#     time.sleep(1)

#응답률 가져오기
# res = driver.find_element(By.XPATH, '//*[@id="react-application"]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/div[2]/div[1]/div[13]/div/div/section/div/div/div/div/div[2]/div[3]/div')
# # '//div[contains(@class, "h1geptgj.atm")]'
# print(res)
# time.sleep(1)

time.sleep(1000)

#react-application > div > div > div:nth-child(1) > div > div._1i7ccu91 > div > div > div > div > div._1k81gub > div.cgx2eil.atm_mk_h2mmj6.dir.dir-ltr > div:nth-child(1) > div:nth-child(13) > div > div > section > div > div > div > div > div.s1qyrxec.atm_9s_1txwivl.atm_ar_1bp4okc.atm_cx_1vi7ecw.atm_j3_1djdi08__oggzyc.dir.dir-ltr > div:nth-child(3) > div



