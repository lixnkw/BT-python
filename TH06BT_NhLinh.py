import numpy as np
import pandas as pd
import requests as rq

# print("BÀI THỰC HÀNH 2.2=======================================")
# path = "TH06/file data csv.csv"
# df = pd.read_csv(path, skiprows=1)
# # df.info()

# df_number = df.select_dtypes(include=(np.number))
# df_object = df.select_dtypes(include=("object"))

# print(df_number.head())
# print(df_object.head())


# print("BÀI THỰC HÀNH 2.3 =======================================")
# path2 = "TH06/Danh sách lớp IT12-K12.xlsx"
# ex1 = pd.read_excel(path2)
# # ex1.info()
# print(ex1.head())

url_api = 'https://dummyjson.com/products'
result_money = rq.get(url_api)
# # check status của requests
# print(result_money.status_code)

# # chuyển đổi dữ liệu sang dạng String
# data_text = result_money.text
# # chuyển đổi dữ liệu sang dạng json
# data_json = result_money.json()

# print('text: ', data_text)
# print('-------------------------')
# print('json: ', data_json)
# df = pd.DataFrame(data_json)
# print(df.head(10))

# data_json1 = result_money.json()
# # print(data_json1)
# # result_money1 = data_json1.get(url_api, params={'symbols':'id, stock'})
# # print(result_money1)
# products = data_json1.get('products', [])

# df1 = pd.DataFrame(products)
# rs = df1[['id', 'category', 'price', 'rating']]

# print(rs.head(10))

# print("BÀI THỰC HÀNH 2.5 =======================================")

# url = 'http://api.plos.org/search?q=title:VIRUS'
# result = rq.get(url)
# # print(result.status_code)

# data_json = result.json()
# rs = data_json.get('response', {}).get('docs', [])

# dtf = pd.DataFrame(rs)
# result_final = dtf[['id', 'eissn', 'author_display', 'abstract', 'title_display', 'score']]
# print(result_final)

import sklearn.datasets as datask
import pandas as pd

# Tải bộ dữ liệu
iris = datask.load_iris()

# Chuyển đổi thành DataFrame của pandas để dễ thao tác
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['target'] = iris.target

# Hiển thị vài dòng đầu tiên của DataFrame
print(df.head())
