text = ''
with open("kakao.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    # 데이터 클렌징
    for line in lines[1:]: # 두번째 라인부터 읽으면 될 듯
        if 'https://' in line: # 링크 포함 안시킴
            continue
        if '","' in line:
            text += line.split('","')[1].replace('이모티콘','').replace('"','').replace('사진','').replace('ㅇ','').replace('ㅋ','')

# print(text)

# import matplotlib.font_manager as fm
from wordcloud import WordCloud
from PIL import Image
import numpy as np

mask = np.array(Image.open('cloud.png'))
wc = WordCloud(font_path='System/Library/Fonts/Supplemental/AppleGothic.ttf', background_color="white", mask=mask)
wc.generate(text)
wc.to_file("result_masked.png")

# # 경로 넣을 때 윈도우는 \를 /로 바꿔주기
# wc = WordCloud(font_path='/System/Library/Fonts/Supplemental/AppleGothic.ttf', background_color="white", width=600, height=400)
# wc.generate(text)
# wc.to_file("result.png")

# 이용 가능한 폰트 중 '고딕'만 선별
# for font in fm.fontManager.ttflist:
#     if 'Gothic' in font.name:
#         print(font.name, font.fname)

