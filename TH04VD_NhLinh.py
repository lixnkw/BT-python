import numpy as np
# print("thu vien Numpy, Version: ", np.__version__)

import scrapy as sc
# print("thu vien Scrapy, Version: ", sc.__version__)

a =np.array ([1, 2, 4, 6 ,5, 6, 19])
# print(a)
# print("Type a: ", type(a))
# print("Kieu du lieu: ", a.dtype)
# print("Kich thuoc: ", a.shape)
# print("so phan tu: ", a.size)
# print("So chieu cua mang: ", a.ndim)

print("Tao mang voi cac ham san co cua NUMPY") 
print("tao ma tran moi: ", np.zeros((4,5)))
# print("Type ma tran moi: ", type( np.zeros((4,5))))
# print("Kieu du lieu: ",  np.zeros((4,5)).dtype)
# print("Kich thuoc: ",  np.zeros((4,5)).shape)
# print("so phan tu: ",  np.zeros((4,5)).size)
# print("So chieu cua mang: ",  np.zeros((4,5)).ndim)

# print("cu phap nay co the tao x lan so mang len", np.ones((5,3,4), dtype = np.int16))
# print("dau - cuoi - buoc nhay", np.arange(10,50,5))
# print("6 gia tri cach deu nhau từ số 0 den 8", np.linspace(0,8,6))
# print("create a constant array", np.full((2,2), 7))
# print("", np.eye(5))
# print("", np.random.random((4,2)))
# print(np.empty((4, 2)))

# print("Khoi tao mang")
# array_eye = np.eye(5)

# print(array_eye)
# print("kieu du lieu: ", array_eye.dtype)
# print("kich thuoc cua mang: ", array_eye.shape)
# print("so phan tu cua mang: ", array_eye.size)
# print("so chieu cua mang: ", array_eye.ndim)

# print("tao mang coi cac phan tu ngau nhien")
# print(np.random.randint(low = 10, high = 30, size = 6))
# print(np.random.uniform(low = 10, high = 30, size = 6))


# print("tao vecto voi cac tham so thiet lap: ")
# print("Vecto: ", np.arange(2,30, 5))
# print("So phan tu cua vecto la: ",  np.arange(2,30, 5).size)


