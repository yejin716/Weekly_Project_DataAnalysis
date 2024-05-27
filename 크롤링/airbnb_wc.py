import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.airbnb.com/rooms/24524189/reviews?adults=1&category_tag=Tag%3A8851&children=0&enable_m3_private_room=true&infants=0&pets=0&search_mode=flex_destinations_search&check_in=2024-05-29&check_out=2024-06-03&source_impression_id=p3_1715518174_V2A3pp71ULfuUlJt&previous_page_section_name=1000&federated_search_id=49613615-985c-45be-ad2e-531a99a77d1a'

response = requests.get(url)
# print(response.status_code)

soup = BeautifulSoup(response.text, 'html.parser')

# names = soup.select('body > div:nth-child(58) > div > div > section > div > div > div.p1psejvv.atm_9s_1bgihbq.dir.dir-ltr > div > div._ctwstv > div > div > div > div > div > div > section > div > div._vghwkew > div > section > div._1tqgvho')
# names = soup.find_all('span', attrs={'class' : 'lrl13de atm_kd_19r6f69_24z95b atm_kd_19r6f69_1xbvphn_1oszvuo dir dir-ltr'})
names = soup.select_one('body > div:nth-child(58) > div > div > section > div > div > div.p1psejvv.atm_9s_1bgihbq.dir.dir-ltr > div > div._ctwstv > div > div > div > div > div > div > section > div > div._vghwkew > div > section > div._1tqgvho > div > div:nth-child(1) > div:nth-child(2) > div.r1bctolv.atm_c8_1sjzizj.atm_g3_1dgusqm.atm_26_lfmit2_13uojos.atm_5j_1y44olf_13uojos.atm_l8_1s2714j_13uojos.dir.dir-ltr > div > span > span')


print(names)