import pandas as pd

# สร้าง DataFrame จากดิกชันนารี
data = {'Name': ['John', 'Anna', 'Peter'],
        'Age': [28, 24, 35],
        'City': ['New York', 'London', 'Berlin']}
df = pd.DataFrame(data)

print(df)