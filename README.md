# Python 201 Data Analysis

โปรเจกต์นี้เป็นส่วนหนึ่งของการเรียนรู้ Python สำหรับการวิเคราะห์ข้อมูล จากคอร์ส [Python Series โดย Mikelopster](https://docs.mikelopster.dev/c/python-series/201/intro)

## 📚 เนื้อหาที่ได้เรียนรู้

### NumPy Fundamentals
1. **NumPy Array Basics** (numpy_array_examples.py)
   - การสร้าง NumPy Array
   - การเข้าถึงและจัดการข้อมูลใน Array

2. **Array Operations** (numpy_array_operations.py)
   - การดำเนินการทางคณิตศาสตร์กับ Array
   - Broadcasting
   - Universal Functions (ufuncs)

3. **Array Generation** (numpy_array_generation.py)
   - สร้าง Array ด้วยฟังก์ชันต่างๆ
   - arange, linspace, zeros, ones

4. **Matrix Operations** (numpy_matrix_multiplication.py)
   - การคูณเมทริกซ์
   - Linear Algebra operations

5. **Performance Optimization** (numpy_memory_efficiency.py, numpy_vs_list_performance.py)
   - การจัดการหน่วยความจำที่มีประสิทธิภาพ
   - เปรียบเทียบประสิทธิภาพระหว่าง NumPy และ Python List

6. **Vectorized Operations** (numpy_vectorized_operation.py)
   - การใช้ Vectorization เพื่อเพิ่มประสิทธิภาพ

### Pandas Fundamentals
1. **Data Reading** (pandas_csv_reader.py, pandas_excel_reader.py, pandas_json_reader.py, pandas_sql_reader.py)
   - อ่านข้อมูลจากไฟล์ CSV
   - อ่านข้อมูลจาก Excel
   - อ่านข้อมูลจาก JSON
   - อ่านข้อมูลจาก SQL Database

2. **Data Frame Basics** (pandas_dataframe.py)
   - การสร้างและจัดการ DataFrame
   - การเลือกและกรองข้อมูล
   - การจัดการข้อมูลที่หายไป

3. **Data Series** (pandas_series.py)
   - การทำงานกับ Pandas Series
   - การดำเนินการกับข้อมูลอนุกรม

4. **Data Analysis Examples** (pandas_df_example.py)
   - ตัวอย่างการวิเคราะห์ข้อมูลจริง
   - การใช้ข้อมูล Employees (employees.csv, employees_data.xlsx)

## 🛠 การติดตั้ง Dependencies

```bash
pip install numpy pandas openpyxl sqlalchemy
```

## 🚀 การใช้งาน

1. Clone repository:
```bash
git clone https://github.com/yourusername/python-201-data.git
```

2. เข้าไปยังโฟลเดอร์โปรเจกต์:
```bash
cd python-201-data
```

3. ติดตั้ง dependencies:
```bash
pip install -r requirements.txt
```

4. รันไฟล์ตัวอย่างที่ต้องการ:
```bash
python filename.py
```

## 📊 ตัวอย่างข้อมูล
- employees.csv - ข้อมูลพนักงานสำหรับฝึกวิเคราะห์
- employees_data.xlsx - ข้อมูลในรูปแบบ Excel
- example.db - ฐานข้อมูล SQLite สำหรับการฝึกดึงข้อมูล

## 🎯 เป้าหมายของโปรเจกต์
- เรียนรู้การใช้งาน NumPy สำหรับการคำนวณเชิงตัวเลข
- เข้าใจการจัดการข้อมูลด้วย Pandas
- ฝึกทักษะการวิเคราะห์ข้อมูลเบื้องต้น
- เรียนรู้การอ่านข้อมูลจากแหล่งต่างๆ

## 💡 Tips
- ใช้ Jupyter Notebook เพื่อการทดลองและเรียนรู้แบบ Interactive
- ศึกษาเพิ่มเติมจาก Official Documentation ของ NumPy และ Pandas
- ฝึกใช้ Vectorization แทน Loop เพื่อเพิ่มประสิทธิภาพ

## 📝 Credit
เรียนรู้จากคอร์ส [Python Series - Data Analysis](https://docs.mikelopster.dev/c/python-series/201/intro) โดย Mikelopster

---
⭐️ ถ้าเนื้อหานี้เป็นประโยชน์ สามารถกด Star ให้กำลังใจได้นะครับ
