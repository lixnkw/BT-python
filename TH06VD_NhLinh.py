import pandas as pd
import numpy as np
path = "TH06/file data csv.csv"
# # Sử dụng phương thức read csv
# data = pd.read_csv(path)
# # Hiển thị thông tin Data
# data.info()

# cũng có thể dùng cách này để đọc dữ liệu
# csv = pd.read_csv(path, sep =",", 
#                   encoding= None,
#                   index_col=0,
#                   low_memory=False,
#                   )

# csv.info()
# print(csv.head(5))

# sv2 = pd.read_csv(path, sep=",", nrows=10, usecols=['MSV', "Họ và tên"])

# # print(sv2.info())
# print(sv2.head(5))

# sv3 = pd.read_csv(path, names=["ID", "CODE", "NAME",], skiprows=2)
# print(sv3.head(5))

# path2 = "TH06/Danh sách lớp IT12-K12.xlsx"
# ex1 = pd.read_excel(path2)
# # ex1.info()
# print(ex1.head())

# ex2 = pd.read_excel(path2, index_col=0, sheet_name=0, usecols=[0,1,2,3,4], skiprows=2, names=['stt','code','name', 'point', 'note',])
# print(ex2.head())




