''' อ่าน CSV '''
'''
เราสามารถใช้ Pandas ในการอ่านไฟล์ CSV ได้อย่างง่ายดาย โดยใช้ฟังก์ชัน read_csv() ที่ Pandas มีให้ ซึ่งรองรับการอ่านไฟล์ CSV จากที่เก็บไฟล์ในเครื่องหรือจาก URL ได้
'''

import pandas as pd

# อ่านไฟล์ employees.csv
df = pd.read_csv('employees.csv')

# แสดงข้อมูล
print(df)

'''
คุณสมบัติอื่นๆของ read_csv()
'''
'''
1. กำหนดตัวคั่น (Delimiter): หากไฟล์ CSV ใช้ตัวคั่นที่ไม่ใช่เครื่องหมายจุลภาค (, เช่น ; หรือ |) เราสามารถกำหนดได้โดยใช้พารามิเตอร์ delimiter
'''
df = pd.read_csv('employees.csv', delimiter=';')

'''
2. เลือกเฉพาะบางคอลัมน์: หากต้องการโหลดเฉพาะบางคอลัมน์ สามารถระบุชื่อคอลัมน์ที่ต้องการได้
'''
import pandas as pd

# อ่านไฟล์ employees.csv
df = pd.read_csv('employee.csv', usecols=['Name', 'Salary'])

# แสดงข้อมูล
print(df)