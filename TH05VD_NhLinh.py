import numpy as np
vector = np.array([1,2,3,4,5,6,7,8,9,6,5,4,3,7,8,9])
# print(vector)
# print("So phan tu cua vecto la: ", np.size(vector))
maxtrix = vector.reshape(4,4)
# print(f"Chuyen doi vecto sang matrix dang n x m: {maxtrix}")
# maxtrix2 = maxtrix.reshape(2,8)
# print(f"Chuyen doi vecto đã chuyển sang matrix dang 4x4 thanh dang 2x8: {maxtrix2}")
# print("So phan tu cua mang sau khi chuyen sang kich thuoc 2x8 la:  ", np.size(maxtrix2))

array = np.random.randint(1, 11, size=(4,4))
# print(array)
# print("chuyen tu matrix sang vector", np.ravel(array))
# # mặc định sẽ chuyển đổi theo hàng ngang, nếu muốn theo cột thêm thuộc tính orders ='F', mặc đinh của nó là 'C'
# print("chuyen tu matrix sang vector theo cac cot", np.ravel(array, order='F'))

concate = np.concatenate((maxtrix, array), axis=0)
# print("Ham noi 2 mang thanh 1 mang theo cot la: ")
# print(concate)

# print("Ham noi 2 mang thanh 1 mang theo hang la: ")
# print(np.concatenate((maxtrix, array), axis=1))

# print("tach 1 vector thanh nhieu vector, ma tran con")
# print("tach mang thanh 2 vecto bang nhau: ", np.split(vector, 2))
# print("tach mang thanh 3 vecto o vi tri 3 va 6: ")
# x1, x2, x3 = np.split(vector,[3,6])
# print(x1, x2, x3)

# print("Chuyen cac mang thanh cac mang, ma tran con theo hang ngang")
# vs1, vs2 = np.vsplit(array, 2)
# print(f"{vs1}\n{vs2}")
# print("Chuyen cac mang thanh cac mang, ma tran con theo cot doc")
# hs1, hs2 = np.hsplit(array, 2)
# print(f"{hs1}\n{hs2}")

# print("lat nguoc ma tran theo hang va cot")
# print(np.flip(array,0)) 
# print(np.flipud(array)) # 2 cais nayf gioongs nhau
# print("\n")
# print(np.flip(array, 1))
# print(np.fliplr(array))


