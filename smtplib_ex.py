# smtplib : 이메일 보내는 패키지
# 이메일 보내는 방법 자체는 검색하면 잘 나옴

# < 실행가능 조건 > : 이게 검색이 어렵다
# 1. 보내는 사람 계정의 이중인증 같은 거 다 꺼줘야 함
#       https://myaccount.google.com/signinoptions/two-step-verification
# 2. 보내는 사람 계정의 보안 수준이 낮은 앱 엑세스 허용을 사용으로 바꾸어 주어야 함
#       https://myaccount.google.com/lesssecureapps

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

# 보내는 사람 정보
sender = "보내는 사람 아이디@gmail.com"
sender_password = "보내는 사람의 계정 비밀번호"

# 로그인하기
s = smtplib.SMTP_SSL('smtp.gmail.com')
s.login(sender, sender_password)

# 받는 사람 정보
emails = ['받는사람아이디0@아무도메인', '받는사람아이디2@아무도메인']
# receiver = "받는사람아이디0@아무도메인"

for receiver in emails:
    # 메일 기본 정보 설정
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "여기가 제목"
    msg['From'] = sender
    msg['To'] = receiver

    # 메일 내용 쓰기
    content = "여기가 내용"
    part2 = MIMEText(content, 'plain')
    msg.attach(part2)

    # 파일 첨부하기 (여기서는 만들어둔 엑셀파일 넣음)
    part = MIMEBase('application', "octet-stream")
    with open("articles.xlsx", 'rb') as file:
        part.set_payload(file.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment", filename="추석기사.xlsx")
    msg.attach(part)

    # 메일 보내기
    s.sendmail(sender, receiver, msg.as_string())

# 서버 끄기
s.quit()