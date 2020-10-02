from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome('./chromedriver')

url = "https://search.naver.com/search.naver?where=news&sm=tab_jum&query=추석"

driver.get(url)
req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')

#####################
# print(soup)
news = soup.select_one('#sp_nws6 > dl > dt > a')
# print(news.text) # 텍스트만 가져오고 싶은 경우
# 다른 기사의 copy selector : #sp_nws9 > dl > dt > a
# 이미지의 경우와 다름!
all_news = soup.select('#main_pack > div.news.mynews.section._prs_nws > ul > li')
# print(all_news)
# 프린트 하면 [<li id="sp_nws1"> <div class="thumb">< ... 이런 식으로 출력되는데 맨 앞에 [를 보면 list라는 것을 알 수 있음

for news in all_news:
    # print(news)

    title = news.select_one('dl > dt > a')
    # print(title.text)

    url = title['href']
    # print(title.text, url)

    company = news.select_one('span._sp_each_source').text
    # print(title.text, '|', company)

    # "언론사" 와 "선정이 필요 없음
    company = company.split(' ')[0].replace('언론사', '')
    print(title.text, '|', company)
    # 크롤링은 항상 같은 답이 있는 것은 아니다. 웹사이트 마다 html이 다 다르므로 거기에 맞게 작성해야함
#####################

driver.quit()