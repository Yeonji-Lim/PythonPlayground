print('hello world')

# 주의! ;금지

print('<문자열과 정수>')

first_name = 'Yeonji'
last_name = 'Lim'

a = 2
b = 3

print(first_name + last_name)
print(a+b)

# 정수와 문자열은 더하기 연산이 안된다.
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# print(a+first_name)

c = '2'
print(c+first_name)

# str()은 문자열로 변형해준다.
print(str(a)+first_name)

print('<list>')

a_list = ['사과', '감', '배']
b_list = ['연지', ['똥깡','똥깡이누나', '똥깡이엄마']]

print(a_list[1])
print(b_list[1][0])

# 동적으로 원소 추가
a_list.append('수박')
print(a_list)

print('<dictionary>')

        # key : value
a_dict = {'name':'연지', 'age':24}
print(a_dict['name'])

a_dict['height'] = 168

print(a_dict)

# 리스트와 딕셔너리의 짬뽕
a_dict['fruits'] = a_list

print(a_dict)

# 수박 가져오기
print(a_dict['fruits'][0])

# 리스트는 숫자로 찾고 딕셔너리는 키값으로 찾는 다!

print('<조건문>')

age = 24

# tab 으로 구문 내부에 있는 것을 표현함
if age > 20:
    print('성인')
else:
    print('청소년')

print('<반복문>')

fruits = ['사과','배','배','감','수박','귤','딸기','사과','배','수박']
count = 0
# fruits의 원소들이 하나씩 빼져서 fruit에 들어가서 찍힘
for fruit in fruits:
    print(fruit)
    if fruit == '사과':
        count += 1

print(count)

# 리스트 안에 딕셔너리
people = [{'name': 'bob', 'age': 20},
          {'name': 'carry', 'age': 38},
          {'name': 'john', 'age': 7},
          {'name': 'smith', 'age': 17},
          {'name': 'ben', 'age': 27}]

for person in people:
    print(person['age'])
    if person['age'] > 20:
        print(person['name'])

print('<파이썬 내장함수>')

# 문자열 자르기
my_email = 'view7186@naver.com'
result = my_email.split('@')[1].split('.')[0]
# 그 문자를 기점으로 앞이 0, 뒤가 1인 리스크가 된다고 생각하자
print(result)

# 문자열 치환
result_1 = my_email.replace('naver', 'gmail')
print(result_1)



