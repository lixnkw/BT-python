import numpy as np

# print("Thuc hanh =========================================")
# print("Yeu cau =========================================")
# ax = np.arange(1,31)
# a = ax.reshape(5,6)
# b = ax.split

# print(a)
# a1=a.reshape(5,6)
# a_le = a[a % 2 != 0]
# a_chan = a[a % 2 == 0]
# a_3 = a[a % 3 == 0]
# print("Vecto chua so le: ", a_le)
# print("Vecto chua so chan: ", a_chan)
# print("Vecto chua so chia het cho 3: ", a_3)

# print("Thuc hanh 2.2 =========================================")
# v_height = str( np.int16(np.linspace(150, 185, 100)))
# v_weight = str(np.int16(np.linspace(45, 75, 100)))


# path = "TH05/data.txt"
# f = open(path, "r")


# # Đọc dữ liệu từ file
# data = np.loadtxt(path, dtype=np.int32)
# # Tách dữ liệu thành hai vector
# v_height = data[0, :]
# v_weight = data[1, :]
# print("du lieu dau vao: ")
# print(f.read())

# print("\ndoi chieu cao tu cm sang m và binh phuong len lam tron 2 so thap phan: ")
# v_height =  np.power(np.divide(v_height, 100), 2) 
# print(np.round(v_height,2))

# print("Thuc hanh 2.3 =========================================")

# path = "TH05/data.txt"
# f = open(path, "r")

# # Đọc dữ liệu từ file
# data = np.genfromtxt(path, dtype=np.int32)
# print(data)
# # Tách dữ liệu thành hai vector
# v_height = data[0, :]
# v_weight = data[1, :]

# # bmi = []

# # for i in range(0, len(v_weight)):
# bmi = (v_weight/((v_height/100)*(v_height/100))) 
# print(np.round(bmi,2))

# print("Thuc hanh 2.4 =========================================")
# path = "TH05/data.txt"
# f = open(path, "r")

# # Đọc dữ liệu từ file
# data = np.genfromtxt(path, dtype=np.int32)

# # Tách dữ liệu thành hai vector
# v_height = data[0, :]
# v_weight = data[1, :]

# bmi = np.round((v_weight/((v_height/100)*(v_height/100))), 2)

# temp = 0

# for i in range(0, len(bmi)):
 
#     for j in  range(1, len(bmi)):
#         if bmi[i] > bmi[j]:
#             temp = bmi[i]
#             bmi[i] = bmi[j]
#             bmi[j] = temp

# print("sap xep theo chieu tang dan: ", np.sort(bmi) , end = " ")
# print("\nsap xep theo chieu giam dan: ", -np.sort(-bmi) , end = " ")
# print("\nsap xep theo chieu giam dan: ", np.flip(np.sort(bmi)) , end = " ") # có thể dùng 1 cách

# print("\nThong ke so ngươi: ")
# underweight = np.where(bmi < 18.5)[0]
# normal = np.where((bmi >= 18.5) & (bmi < 25))[0]
# overweight = np.where((bmi >= 25) & (bmi < 30))[0]
# obese = np.where((bmi >= 30) & (bmi < 35))[0]
# extremely_obese = np.where(bmi >= 35)[0]
# print("underweight: ", len(underweight))
# print("normal: ", len(normal))
# print("overweight: ", len(overweight))
# print("obese: ", len(obese))
# print("extremely_obese: ", len(extremely_obese))


# print("Thuc hanh 3 =========================================")
# path = "TH05/data.txt"
# f = open(path, 'r')
# data = np.genfromtxt(path, delimiter="", dtype=np.int32)

# v_height = data[0,:]
# v_weight = data[1,:]
# v_height= np.round( v_height/100, 2)
# mt_weigth =v_weight.reshape(10,10)
# print("vector weight chuyen thanh ma tran weight 10 x 10: \n", mt_weigth)
# mt_weigth_nd = np.linalg.det(mt_weigth)
# print("det(ma tran weight 10x10) = ", mt_weigth_nd)
# if mt_weigth_nd == 0:
#     print("Ma tran weight có det = 0 nen kh co ma tran nghich dao")
# else: 
#     print("ma tran nghich dao cua ma tran weight 10x10 la: ",  np.linalg.inv(mt_weigth) )

# print("cach lay cac duong cheo chinh trong ma tran")
# a = np.diagonal(mt_weigth)
# print(a)
# print("a.diagonal(k): trả về vector chứa các phần tử nằm cách đường chéo chính của ma trận a, k phần tử (k>0 trên đường chéo chính, k<0 dưới đường chéo chính")

# a1 = np.diagonal(mt_weigth, offset= 1)
# a_1 = np.diagonal(mt_weigth, offset= -1)
# print(mt_weigth.diagonal(-1))
# print(a_1)

# print("ma tran tam giac (triu | tril)")
# print(np.triu(mt_weigth))
# print("\n\n", np.tril(mt_weigth))
# print("\n\n", np.tril(mt_weigth, -2))

# trace = np.diagonal(mt_weigth).sum()
# print("Trace cua ma tran weigth la: (trace la tong gia tri phan tu tren duong cheo chinh)", trace)

# print("tim gia tri lon nhat cua ma tran duong cheo tren va duoi")
# mt_tren =  np.triu(mt_weigth, 1)
# mt_duoi =  np.tril(mt_weigth, -1)

# def findMax(arr): 
#     res1 = arr[0,0]
#     for i in range(arr.shape[0]):
#         for j in range(arr.shape[1]):
#             if arr[i,j] > res1:
#                 res1 = arr[i,j]
#     return res1   

# print("gia tri lon nhat cua ma tran duong cheo tren la (kh ke duong cheo chinh): ", findMax(mt_tren))
# print("gia tri lon nhat cua ma tran duong cheo duoi la(kh ke duong cheo chinh): ", findMax(mt_duoi))


# print("Thuc hanh 4 =========================================")
# path = "TH05/data.txt"
# f = open(path, 'r')
# data = np.genfromtxt(path, delimiter="", dtype=np.int32)

# v_height = data[0,:]
# v_weight = data[1,:]
# mt_weight = v_weight.reshape(10,10)
# mt_height = v_height.reshape(10,10)
# print("vector weight chuyen thanh ma tran weight 10 x 10: \n", mt_weight)
# print("vector height chuyen thanh ma tran height 10 x 10: \n", mt_height)

# ss = np.equal(mt_weight, mt_height)
# add = np.add(mt_weight, mt_height)
# minus = np.subtract(mt_weight, mt_height)
# dot = np.dot(mt_weight, mt_height)
# print("so sanh hai ma tran: \n", ss)
# print("cong hai ma tran: \n", add)
# print("tru hai ma tran: \n", minus)
# print("nhan hai ma tran: \n", np.round(dot, 1))

print("Thuc hanh 5 =========================================")
path = "TH05/data.txt"
f = open(path, 'r')
data = np.genfromtxt(path, delimiter="", dtype=np.int32)

v_height = data[0,:]
v_weight = data[1,:]
mt_weight = v_weight.reshape(10,10)
mt_height = v_height.reshape(10,10)

print("Tính hạng của ma trận: ", np.linalg.matrix_rank(mt_height))
print("Ma trận chuyển vi: \n", mt_height.T)








