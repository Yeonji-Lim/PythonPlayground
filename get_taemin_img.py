import dload
from bs4 import BeautifulSoup
from selenium import webdriver
import time

driver = webdriver.Chrome('./chromedriver')
driver.get("https://search.daum.net/search?w=img&nil_search=btn&DA=NTB&enc=utf8&q=%ED%83%9C%EB%AF%BC")
time.sleep(5)

req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')

###################################
taemin_imgs = soup.select('#imgList > div > a > img')
i = 0;
for taemin_img in taemin_imgs:
    real_img = taemin_img['src']
    dload.save(real_img, f'taemin_img/{i}.jpg')
    i += 1
###################################

driver.quit() # 끝나면 닫아주기