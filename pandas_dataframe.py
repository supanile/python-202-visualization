''' 2. DataFrame '''
'''
DataFrame เป็นโครงสร้างข้อมูลแบบสองมิติ (เหมือนกับตาราง) โดยมีแถวและคอลัมน์ (คล้ายกับตารางใน Excel หรือฐานข้อมูล) โดยแต่ละคอลัมน์ใน DataFrame เป็น Series และคอลัมน์ต่าง ๆ สามารถเก็บข้อมูลประเภทต่างกันได้ เช่น คอลัมน์หนึ่งเก็บตัวเลข คอลัมน์หนึ่งเก็บข้อความ

ตัวอย่าง DataFrame ก็จะเป็นตัวอย่าง code แรกสุดที่เรายกตัวอย่างกันไป

โดย use case ของการใช้ DataFrame โดยทั่วไป จะมีดังต่อไปนี้
'''

'''
1. เลือก row และ column ที่ต้องการ DataFrame สามารถเลือกข้อมูลได้อย่างยืดหยุ่น โดยเราสามารถเลือกข้อมูลเฉพาะคอลัมน์หรือแถวตามต้องการได้ หรือ เลือกเฉพาะแถวออกมา
'''
import pandas as pd

# สร้าง DataFrame จากดิกชันนารี
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Los Angeles', 'Chicago']}

df = pd.DataFrame(data)

# เลือกคอลัมน์ 'Name'
print(df['Name'])

# เลือกแถวที่มี index 1
print(df.loc[1])

'''
Note

- .loc เป็นการอ้างถึงแถวหรือคอลัมน์ใน DataFrame ของ Pandas โดยใช้ label-based indexing ซึ่งหมายความว่าเราสามารถเข้าถึงข้อมูลโดยใช้ label ของ index หรือชื่อของคอลัมน์
'''

'''
2. การกรองข้อมูลตามเงื่อนไข เราสามารถกรองข้อมูลใน DataFrame โดยกำหนดเงื่อนไขที่ต้องการ เช่น การเลือกแถวที่ตรงตามเงื่อนไขเฉพาะ
'''
import pandas as pd

# สร้าง DataFrame จากดิกชันนารี
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Los Angeles', 'Chicago']}

df = pd.DataFrame(data)

# เลือกแถวที่คอลัมน์ 'Age' มากกว่า 30
filtered_df = df[df['Age'] > 30]

print(filtered_df)

''' 3. การเพิ่มคอลัมน์ใหม่ '''
import pandas as pd

# สร้าง DataFrame จากดิกชันนารี
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Los Angeles', 'Chicago']}

df = pd.DataFrame(data)

# เลือกแถวที่คอลัมน์ 'Age' มากกว่า 30
filtered_df = df[df['Age'] > 30]

print(filtered_df)

''' 4. การแก้ไขข้อมูล Pandas ช่วยให้เราสามารถแก้ไขข้อมูลภายใน DataFrame ได้ง่าย ๆ โดยการระบุข้อมูลที่ต้องการแก้ไข '''
import pandas as pd

# สร้าง DataFrame จากดิกชันนารี
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Los Angeles', 'Chicago']}

df = pd.DataFrame(data)

# แก้ไขค่าของ City ในแถวที่มี index 0
df.at[0, 'City'] = 'San Francisco'

print(df)

''' 5. การคำนวณสถิติเบื้องต้น DataFrame มีฟังก์ชันสถิติเบื้องต้นที่สามารถช่วยในการวิเคราะห์ข้อมูล เช่น การหาค่าเฉลี่ย ค่าสูงสุด ค่าต่ำสุด เป็นต้น '''
import pandas as pd

# สร้าง DataFrame จากดิกชันนารี
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Los Angeles', 'Chicago']}

df = pd.DataFrame(data)

# คำนวณค่าเฉลี่ยของคอลัมน์ Age
average_age = df['Age'].mean()

print(f"Average Age: {average_age}") # Average Age: 30.0

'''
 6. Grouping Data Pandas รองรับการจัดกลุ่มข้อมูลตามคอลัมน์ต่าง ๆ แล้วทำการคำนวณค่าทางสถิติตามที่กำหนด เช่น การหาค่าเฉลี่ย, ผลรวม, หรือจำนวน
'''
import pandas as pd

# สร้าง DataFrame จากดิกชันนารี
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Los Angeles', 'Chicago']}

df = pd.DataFrame(data)

# เพิ่มคอลัมน์ 'Salary'
df['Salary'] = [70000, 80000, 120000]
# จัดกลุ่มตาม City และหาค่าเฉลี่ยของ Salary
grouped = df.groupby('City')['Salary'].mean()

print(grouped)

'''
7. การลบคอลัมน์หรือแถว เราสามารถลบคอลัมน์หรือแถวที่ไม่ต้องการได้โดยใช้คำสั่ง drop()
'''
import pandas as pd

# สร้าง DataFrame จากดิกชันนารี
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Los Angeles', 'Chicago']}

df = pd.DataFrame(data)

# ลบคอลัมน์ City
df = df.drop(columns=['City'])

print(df)

'''
8. การเปลี่ยนชื่อคอลัมน์ เราสามารถเปลี่ยนชื่อคอลัมน์ใน DataFrame ได้โดยใช้ฟังก์ชัน rename()
'''
import pandas as pd

# สร้าง DataFrame จากดิกชันนารี
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Los Angeles', 'Chicago']}

df = pd.DataFrame(data)

# เปลี่ยนชื่อคอลัมน์ Age เป็น Years
df = df.rename(columns={'Age': 'Years'})

print(df)
