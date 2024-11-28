'''
3. การทำงานกับเมทริกซ์ การคำนวณเชิงเมทริกซ์เป็นงานที่ Numpy ทำได้อย่างมีประสิทธิภาพ เช่น การคูณเมทริกซ์ (Matrix Multiplication) การคำนวณลอการิทึม หรือลักษณะของข้อมูลอื่นๆ
'''

import numpy as np

# สร้างเมทริกซ์
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])

# การคูณเมทริกซ์
result_matrix = np.dot(matrix1, matrix2)
print(result_matrix)