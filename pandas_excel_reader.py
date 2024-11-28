''' อ่าน Excel '''
'''
เราสามารถใช้ Pandas ใน Python เพื่ออ่านไฟล์ Excel ได้อย่างง่ายดายโดยใช้ฟังก์ชัน read_excel ของ Pandas ด้านล่างนี้คือตัวอย่างโค้ดสำหรับการอ่านไฟล์ Excel
'''

import pandas as pd

# อ่านไฟล์ Excel
file_path = 'employees_data.xlsx'  # เปลี่ยนเป็น path ที่เก็บไฟล์
df = pd.read_excel(file_path)

# แสดงข้อมูลที่อ่านมา
print(df)

'''
สังเกตนะครับว่า ในตัวอย่างนี้:

- เราใช้ read_excel() เพื่อโหลดข้อมูลจากไฟล์ CSV ที่มีชื่อว่า employees_data.xlsx เข้ามา
- จากนั้นใช้ print(df) เพื่อแสดงข้อมูลทั้งหมดที่อยู่ใน DataFrame (ที่เป็นวิธีเดียวกันกับ csv)
'''