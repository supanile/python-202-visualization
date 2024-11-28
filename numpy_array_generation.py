'''
4. การสร้างข้อมูลจำลอง Numpy มี function ในการสร้างข้อมูลจำลอง (synthetic data) เช่น สุ่มตัวเลขหรือสร้างข้อมูลในช่วงที่กำหนด
'''

import numpy as np

# สร้างอาร์เรย์ของเลขสุ่ม
random_arr = np.random.rand(3, 3)  # อาร์เรย์สุ่มขนาด 3x3
print(random_arr)

# สร้างลำดับข้อมูล
sequence_arr = np.arange(0, 10, 2)  # สร้างลำดับข้อมูลจาก 0 ถึง 9 โดยเพิ่มทีละ 2
print(sequence_arr)