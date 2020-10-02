# openpyxl은 엑셀로 저장해주는 패키지
from openpyxl import Workbook

wb = Workbook()
ws1 = wb.active
ws1.title = "students"
ws1.append(["이름", "나이", "학번"])
ws1.append(["임연지", "24", "123456778"])

wb.save(filename='students.xlsx')