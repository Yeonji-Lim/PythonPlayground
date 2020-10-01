from bs4 import BeautifulSoup
from selenium import webdriver
import dload
# 파이썬 내장함수
import time

driver = webdriver.Chrome('./chromedriver') # 웹드라이버 파일의 경로
driver.get("https://search.daum.net/search?w=img&nil_search=btn&DA=NTB&enc=utf8&q=%EC%95%84%EC%9D%B4%EC%9C%A0")
time.sleep(5) # 5초 동안 페이지 로딩 기다리기

req = driver.page_source
# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(req, 'html.parser')

###################################
# print(soup)

# 기억할 것
# 1. select
# 2. select_one

# 해당하는 이미지에 대한 코드로 가서 src만 가져오기!
thumbnails = soup.select_one('#imgList > div:nth-child(1) > a > img')['src']
print(thumbnails)

# 다른 이미지의 copy selector : #imgList > div:nth-child(2) > a > img
# nth-child(2) 이것만 다른 걸 볼 수 있음

# 이미지 여러개 가져오기
# thumbnails_1 = soup.select('#imgList > div > a > img')['src']
thumbnails_1 = soup.select('#imgList > div > a > img')

# 이미지 값만 프린트 및 저장
i = 1
for thumbnail in thumbnails_1:
    img = thumbnail['src']
    print(img)
    dload.save(img, f'img/{i}.jpg')
    i += 1
###################################

driver.quit() # 끝나면 닫아주기