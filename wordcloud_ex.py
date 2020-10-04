text = ''
with open("kakao.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        text += line

# import matplotlib.font_manager as fm
from wordcloud import WordCloud

# 경로 넣을 때 윈도우는 \를 /로 바꿔주기
wc = WordCloud(font_path='/System/Library/Fonts/Supplemental/AppleGothic.ttf', background_color="white", width=600, height=400)
wc.generate(text)
wc.to_file("result.png")

# 이용 가능한 폰트 중 '고딕'만 선별
# for font in fm.fontManager.ttflist:
#     if 'Gothic' in font.name:
#         print(font.name, font.fname)