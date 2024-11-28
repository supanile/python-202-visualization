''' 1. Performance '''

'''
Numpy ถูกสร้างขึ้นเพื่อให้ทำงานกับข้อมูลจำนวนมากได้อย่างมีประสิทธิภาพสูง เนื่องจาก Numpy ใช้การจัดเก็บข้อมูลในรูปแบบ ndarray ซึ่งเป็นอาร์เรย์ที่เก็บข้อมูลในหน่วยความจำแบบต่อเนื่อง (contiguous memory) ต่างจาก Python list ที่เป็นโครงสร้างข้อมูลแบบเก็บค่าในลักษณะของ pointers ทำให้ Numpy สามารถเข้าถึงข้อมูลและทำการคำนวณได้เร็วกว่า

- Numpy ใช้การคำนวณเชิงเวกเตอร์ (vectorization) ซึ่งสามารถทำการคำนวณหลาย ๆ ค่าในเวลาเดียวกัน (parallel computing)
- Python list ต้องใช้ loop ในการเข้าถึงและคำนวณแต่ละรายการ ซึ่งจะช้ากว่า Numpy ที่ทำการคำนวณบนอาร์เรย์ทั้งก้อนในครั้งเดียว
'''

import numpy as np
import time

# ใช้ Numpy array
arr = np.arange(1000000)

start_time = time.time()
arr = arr * 2
print("Numpy time:", time.time() - start_time)

# ใช้ Python list
lst = list(range(1000000))

start_time = time.time()
lst = [x * 2 for x in lst]
print("List time:", time.time() - start_time)

'''
เราจะค้นพบว่า “Numpy จะทำงานได้เร็วกว่ามาก” เนื่องจากคุณสมบัติ การจัดการหน่วยความจำแบบต่อเนื่อง (Contiguous Memory Allocation) ของ Numpy

Numpy ใช้โครงสร้างข้อมูลที่เรียกว่า ndarray ซึ่งเก็บข้อมูลเป็นประเภทเดียวกันทั้งหมด (homogeneous) และเก็บในหน่วยความจำที่ต่อเนื่องกัน (contiguous memory block) ต่างจาก Python list ที่ข้อมูลแต่ละตัวสามารถมีประเภทที่ต่างกันได้และเก็บข้อมูลเป็น pointers ที่เชื่อมต่อกัน

การที่ Numpy เก็บข้อมูลในหน่วยความจำแบบต่อเนื่องทำให้การเข้าถึงข้อมูล (memory access) และการคำนวณสามารถทำได้เร็วขึ้น เนื่องจาก CPU สามารถดึงข้อมูลมาประมวลผลได้ในครั้งเดียวจากหน่วยความจำ และหลีกเลี่ยงการกระโดดไปตาม pointers เหมือนที่ Python list ทำ
'''