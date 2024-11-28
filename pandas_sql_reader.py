''' อ่าน SQL '''

'''
แน่นอน รวมถึงข้อมูลประเภท SQL ด้วยเช่นกัน pandas สามารถอ่านข้อมูลประเภท SQL เข้า dataframe ได้

โดยการใช้ Pandas อ่านข้อมูลจาก SQL ซึ่งในทีนี้ เราจะขอใช้ SQLite database (เนื่องจากเป็น database ประเภท file ที่สามารถใช้งานได้โดยไม่จำเป็นต้องลง program อื่นๆเพิ่ม) โดย สามารถทำได้โดยใช้ library อย่าง sqlite3 หรือ sqlalchemy เพื่อเชื่อมต่อกับฐานข้อมูล จากนั้นใช้ฟังก์ชัน read_sql_query ของ Pandas เพื่อนำข้อมูลมาเก็บไว้ใน DataFrame ตัวอย่างนี้จะใช้ sqlite3 ในการเชื่อมต่อกับ SQLite database

** หัวข้อนี้เราจะแนะนำ Database ให้เห็นเป็น way ของการใช้งานก่อน สำหรับ database ฉบับเต็มเราจะมี section แยกแนะนำกันอีกที

เริ่มต้นให้เราลองสร้างไฟล์ของ SQLite ขึ้นมาก่อน โดย file สำหรับ database sqlite นั้นจะเป็นสกุล .db เช่น example.db

หลังจากนั้น ให้ลองทดสอบการเชื่อมต่อกับ database file นั้นโดยทำการเชื่อมต่อผ่าน program database manager เช่น Dbeaver (https://dbeaver.io/) เข้าไป เพื่อให้มั่นใจก่อนว่าเราสามารถเข้าถึง database ตัวนั้นได้
'''

'''
หลังจากเชื่อมต่อได้เรียบร้อย เราจะลองสร้าง table users ขึ้นมา โดย table users มี fields ดังต่อไปนี้

name = เก็บชื่อเป็น Text
age = เก็บอายุเป็นตัวเลข (Integer)
email = เก็บ email เป็น Text
เราก็จะสามารถสร้างได้จาก SQL ด้านล่างนี้

--- สร้าง table users
CREATE TABLE IF NOT EXISTS users (
  id INTEGER PRIMARY KEY,
  name TEXT,
  age INTEGER,
  email TEXT
)

เมื่อสร้าง database เรียบร้อย ให้ลอง insert ข้อมูลเข้าไปผ่าน SQL


-- insert users
INSERT INTO users (name, age, email) VALUES ('John Doe', 28, 'john@example.com');
INSERT INTO users (name, age, email) VALUES ('Jane Smith', 35, 'jane@example.com');
INSERT INTO users (name, age, email) VALUES ('Emily Davis', 22, 'emily@example.com');
'''

'''
เมื่อ insert ข้อมูลแล้ว ลองดึงข้อมูลออกมา หากได้ข้อมูลออกมาเรียบร้อยแบบเดียวกับที่ insert = ตอนนี้เรามี table users และข้อมูลอยู่ใน table users แล้วเรียบร้อย
'''

'''
หลังจากนั้น เราก็สามารถใช้ python ผ่าน library pandas ในการอ่านข้อมูลผ่าน SQL เข้ามาได้
'''

import sqlite3
import pandas as pd

# สร้างหรือเชื่อมต่อกับ SQLite database
conn = sqlite3.connect('example.db')

# อ่านข้อมูลจาก SQLite database และนำเข้า DataFrame
query = 'SELECT * FROM users'
df = pd.read_sql_query(query, conn)

# แสดงข้อมูลใน DataFrame
print(df)

# ปิดการเชื่อมต่อ
conn.close()