'''
2. การคำนวณทางคณิตศาสตร์ เราสามารถใช้ Numpy เพื่อทำการคำนวณเชิงคณิตศาสตร์กับอาร์เรย์ได้ง่ายขึ้น เช่น บวก ลบ คูณ หาร เวกเตอร์ หรือแม้แต่คำนวณเมทริกซ์
'''

import numpy as np

# สร้างอาร์เรย์
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# การบวกอาร์เรย์
result_add = a + b
print(result_add)

# การคูณอาร์เรย์
result_mul = a * b
print(result_mul)

# การคำนวณค่าทางคณิตศาสตร์
mean = np.mean(a)  # ค่าเฉลี่ย
std_dev = np.std(a)  # ค่าเบี่ยงเบนมาตรฐาน
print("Mean:", mean, "Std Dev:", std_dev)