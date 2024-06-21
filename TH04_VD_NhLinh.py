import numpy as np
# print("thu vien Numpy, Version: ", np.__version__)

import scrapy as sc
# print("thu vien Scrapy, Version: ", sc.__version__)

a = np.array ([1, 2, 4, 6 ,5, 6, 19])
# print(a)
# print("Type a: ", type(a))
# print("Kieu du lieu: ", a.dtype)
# print("Kich thuoc: ", a.shape)
# print("so phan tu: ", a.size)
# print("So chieu cua mang: ", a.ndim)

# print("Tao mang voi cac ham san co cua NUMPY") 
# print("tao ma tran moi: ", np.zeros((4,5)))
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
# print("Vecto: ", np.arange(5,30, 5))
# print("So phan tu cua vecto la: ",  np.arange(2,30, 5).size)

# print("Slide 25")
# array = np.random.randint(1, 11, size=(10, 30))
# # print(array)
# data = np.loadtxt('TH04_data/data_vd.txt', dtype = int)
# print(data)

# print("Slide 28")
a_float = np.linspace(1, 10, 15)
# print(a_float)
# print("kieu du lieu: ", a_float.dtype)
# print("Chuyen tu float sang int")
a_int = a_float.astype(np.int16)
# print(a_int)
      
# print("Truy cap toi cac phan tu trong vecto 1D")
# print("phan tu dau tien: ", a_int[0])
# print("phan tu thu 3: ", a_int[2])
# print("phan tu cuoi cung: ", a_int[-1])
# print("phan tu dau tien den phan tu thu 3: ", a_int[:3])
# print("phan tu thu 4 den phan tu thu <8: ", a_int[3:7])

# print("Truy cap toi cac phan tu trong vecto 2D")
# array = np.random.randint(1, 11, size=(10, 30))
# # print(array)
# data = np.loadtxt('TH04_data/data_vd.txt', dtype = int)
# print(data)
# print("diem mon dau tien cua hoc sinh dau tien: ", data[0,0])
# print("diem mon 1 cua hoc sinh 3: ", data[1,3])
# print("diem mon cuoi cung cua hoc sinh cuoi cung: ", data[-1,-1])
# print("diem mon cuoi cung cua tat ca cac hoc sinh la: ", data[-1:])
# print("bang diem 5 mon hoc dau tien cua 10 hoc sinh dau tien la: ", data[:5,:10])





