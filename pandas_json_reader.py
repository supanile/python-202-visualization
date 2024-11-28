''' อ่าน JSON '''

'''
เราสามารถใช้ Pandas และโมดูล requests ใน Python เพื่อดึงข้อมูลจาก API และนำข้อมูลที่ได้มาเข้าใน DataFrame ได้เช่นกัน

โดยในตัวอย่างนี้ เราจะลองจาก public API อย่าง https://jsonplaceholder.typicode.com/users ที่เป็นการดึงข้อมูล mock ของ user และได้ผลลัพธ์เป็น JSON ออกมา
'''

import pandas as pd
import requests

# ดึงข้อมูลจาก API
url = 'https://jsonplaceholder.typicode.com/users'
response = requests.get(url)

# ตรวจสอบว่าการดึงข้อมูลสำเร็จหรือไม่
if response.status_code == 200:
    data = response.json()  # แปลงข้อมูลจาก JSON เป็น Python object (list of dicts)

    # สร้าง DataFrame จากข้อมูลที่ได้
    df = pd.DataFrame(data)

    # แสดงข้อมูล
    print(df)
    print(df.columns)
else:
    print(f'Error: {response.status_code}')
    
'''
Idea หลักๆของ code นี้คือ

- pandas นั้นสามารถอ่านข้อมูลเป็น JSON ได้อยู่แล้ว (ดั่งที่เราได้ลองใน pandas ใน section ก่อนหน้า)
- ดังนั้น หากเราสามารถดึง API มาในรูปแบบ JSON ได้ = เราสามารถทำให้ข้อมูลมาอยู่ในรูปแบบของ dataframe ได้
- คำสั่งการยิง API เพื่อดึงข้อมูลของ python คือ library request
- ใช้คำสั่ง requests.get(url) สำหรับดึงข้อมูลมาและท้ายที่สุดก็นำผลลัพธ์ JSON นั้น load เข้า dataframe ด้วยคำสั่ง pd.DataFrame(data) ได้เช่นเดิม

ผลลัพธ์ที่ได้ ก็จะได้เป็นลักษณะแบบนี้ออกมา
'''

