f = open("test.txt", "w", encoding="utf-8")
f.write("안녕, 파이썬!\n")
for i in [1, 2, 3, 4, 5]:
    f.write(f"{i}번째\n")
f.close()

text = ''
# test 파일을 열고 다끝나면 닫아라 하는 거임
with open("test.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        # print(line) # 개행을 포함함
        text += line

print(text)