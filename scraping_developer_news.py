from openpyxl import Workbook
from bs4 import BeautifulSoup
from selenium import webdriver
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
# import dload

driver = webdriver.Chrome('./chromedriver')

url = "https://search.daum.net/search?nil_suggest=btn&w=news&DA=SBC&cluster=y&q=%EA%B0%9C%EB%B0%9C%EC%9E%90"

driver.get(url)
req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')

sender = "lyj0616cu@gmail.com"
sender_password = "as13687186as*"

receiver = "view7186@naver.com"

s = smtplib.SMTP_SSL('smtp.gmail.com')
s.login(sender, sender_password)

wb = Workbook()
ws1 = wb.active
ws1.title = "developer_news"
ws1.append(["제목", "링크", "신문사", "섬네일"])

news_list = soup.select('#clusterResultUL > li')
# i = 1
for news in news_list:
    title = news.select_one('div > div > div > a')
    url = title['href']
    title = title.text

    comp = news.select_one('div > div > span.f_nb.date')
    comp = comp.text.split('| ')[1]

    if(news.select_one('div.wrap_thumb > div > a > img')):
        thumb = news.select_one('div.wrap_thumb > div > a > img')['src']
        # dload.save(thumb, f'img/{i}.jpg')
        # i += 1
        ws1.append([title, url, comp, thumb])
        # print(title, url, comp, thumb)
    else:
        ws1.append([title, url, comp, "-"])
        # print(title, url, comp, "-")

wb.save(filename='developer_news.xlsx')

msg = MIMEMultipart('alternative')
msg['Subject'] = "[테스트 성공]개발자 관련 기사 조사 자료입니다."
msg['From'] = sender
msg['To'] = receiver

content = "엑셀 파일을 한번 열어보아요~"
part2 = MIMEText(content, 'plain')
msg.attach(part2)

part = MIMEBase('application', "octet-stream")
with open("developer_news.xlsx", 'rb') as file:
    part.set_payload(file.read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment", filename="개발자관련기사.xlsx")
msg.attach(part)

s.sendmail(sender, receiver, msg.as_string())

s.quit()
driver.quit()