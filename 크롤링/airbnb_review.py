# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By 

# chrome_options = Options()
# chrome_options.add_experimental_option("detach", True)
# #브라우저를 자동화한 후 >> browser window 창 유지 
# chrome_options.add_experimental_option("excludeSwitches", ['enable-logging'])
# #excludeSwitches : 불필요한 로깅 메시지 >> 브라우저에서 제외 

# driver = webdriver.Chrome(options=chrome_options)

# import time
# import pandas as pd 
# from selenium.common.exceptions import NoSuchElementException

# def get_movie_reviews(url,page_num=10):

#     wd = driver
#     wd.get(url)

#     writer_list = []
#     review_list = []
#     date_list = []



#     for page_no in range(10): 
#         writers = wd.find_elements(By.CLASS_NAME, 'hpipapi atm_7l_1kw7nm4 atm_c8_1x4eueo atm_cs_1kw7nm4 atm_g3_1kw7nm4 atm_gi_idpfg4 atm_l8_idpfg4 atm_kd_idpfg4_pfnrn2 dir dir-ltr')
#         writer_list += [writer.text for writer in writers]

#         reviews = wd.find_elements(By.CLASS_NAME, 'lrl13de atm_kd_19r6f69_24z95b atm_kd_19r6f69_1xbvphn_1oszvuo dir dir-ltr')
#         review_list += [review.text for review in reviews]

#         dates = wd.find_elements(By.CLASS_NAME, 'a8jt5op atm_3f_idpfg4 atm_7h_hxbz6r atm_7i_ysn8ba atm_e2_t94yts atm_ks_zryt35 atm_l8_idpfg4 atm_mk_stnw88 atm_vv_1q9ccgz atm_vy_t94yts dir dir-ltr')
#         date_list += [date.text for date in dates]

#         movie_review_df = pd.DataFrame({'writer': writer_list, 
#                                 'review': review_list, 
#                                 'date': date_list})
#         return movie_review_df
		

# url = 'https://www.airbnb.co.kr/rooms/38822606/reviews?adults=1&children=0&enable_m3_private_room=true&infants=0&pets=0&check_in=2024-06-15&check_out=2024-06-20&source_impression_id=p3_1715508472_1p45Jqe2Myo46dmd&previous_page_section_name=1000&federated_search_id=5cafb493-0416-4a91-9193-f587d5774279'
# movie_review_df = get_movie_reviews(url)
# print(movie_review_df)


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import time
import pandas as pd
from bs4 import BeautifulSoup 
options = Options()
chrome_options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option("excludeSwitches", ['enable-logging'])

driver = webdriver.Chrome(options=chrome_options)

def get_reviews(url):
    wd = driver
    wd.get(url)

    writer_list = []
    review_list = []
    date_list = []

    for page_no in range():
        WebDriverWait(wd, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'hpipapi')))
        writers = wd.find_elements(By.CLASS_NAME, 'hpipapi')
        writer_list += [writer.text for writer in writers]

        WebDriverWait(wd, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'lrl13de')))
        reviews = wd.find_elements(By.CLASS_NAME, 'lrl13de')
        review_list += [review.text for review in reviews]

        WebDriverWait(wd, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'a8jt5op')))
        dates = wd.find_elements(By.CLASS_NAME, 'a8jt5op')
        date_list += [date.text for date in dates]

    review_df = pd.DataFrame({'writer': writer_list, 
                                    'review': review_list, 
                                    'date': date_list})
    return review_df

url = 'https://www.airbnb.co.kr/rooms/38822606/reviews?adults=1&children=0&enable_m3_private_room=true&infants=0&pets=0&check_in=2024-06-15&check_out=2024-06-20&source_impression_id=p3_1715508472_1p45Jqe2Myo46dmd&previous_page_section_name=1000&federated_search_id=5cafb493-0416-4a91-9193-f587d5774279'
movie_review_df = get_reviews(url)
print(movie_review_df)
