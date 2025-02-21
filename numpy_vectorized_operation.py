''' 3. Vectorized Operations '''

'''
Numpy รองรับการทำงานแบบเชิงเวกเตอร์ ซึ่งช่วยให้สามารถทำการคำนวณกับข้อมูลทั้งก้อนพร้อมกันได้ โดยไม่ต้องใช้ loop ทำให้การคำนวณเร็วขึ้นและเขียนโค้ดได้ง่ายกว่า
'''
import numpy as np

# ใช้ Numpy ในการคูณทั้งอาร์เรย์
arr = np.array([1, 2, 3, 4, 5])
result = arr * 2  # คูณทุกค่าด้วย 2 ในครั้งเดียว
print(result)


''' ในทางตรงกันข้าม Python list ต้องใช้ loop ในการคำนวณแบบนี้: '''
# ใช้ list ในการคูณแต่ละค่า
lst = [1, 2, 3, 4, 5]
result = [x * 2 for x in lst]
print(result)

'''
ผลลัพธ์: การใช้ Numpy ทำให้โค้ดสั้นกว่าและเร็วกว่า

รวมถึง การคำนวณแบบ Vectorized Operations ใน Numpy จะเกิดขึ้นกับข้อมูลทั้งหมดในอาร์เรย์ในครั้งเดียว โดยไม่ต้องมี overhead ของการจัดการ pointers หรืออ้างอิงค่าหลายครั้ง ก็จะส่งผลบวกต่อ Performance ด้วยเช่นเดียวกัน

และนี่คือคำถามที่อาจจะสำคัญกว่า “เราควรรู้จัก Numpy ไปทำไม” คำตอบก็คือ มันเป็น library ที่อำนวยความสะดวกให้กับ Pandas ที่ถูกสร้างขึ้นโดยใช้ Numpy เป็นพื้นฐาน ทำให้ Pandas มีความสามารถในการทำงานกับข้อมูลในรูปแบบอาร์เรย์ (arrays) ซึ่งเป็นโครงสร้างข้อมูลหลักของ Numpy นอกจากนี้ Pandas ยังขยายความสามารถของ Numpy โดยเพิ่มฟีเจอร์ที่ทำให้การจัดการข้อมูลในรูปแบบตาราง (tabular data) และการทำงานกับข้อมูลเชิงสถิติทำได้ง่ายขึ้น
'''