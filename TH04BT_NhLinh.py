import numpy as np
# print("Thuc hanh 1=========================================")
# print("Yeu cau 1=========================================")
# # array = np.random.randint(0, 100, size=(12, 12))
# # print(array)
# data = 'TH04_data/data_TH04.txt'
# array_point = np.loadtxt(data, dtype=int)
# print(array_point.dtype)


# print("\nYeu cau 2=========================================")
# print("\nduong cheo chinh")
# for i in range(0,12):
#     for j in range(0,12):
#         if i == j:
#             print(f"{array_point[i,j]}", end=", " )

# print("\nduong cheo phu")
# for j in range(0,12):
#     for i in range(0, 12):
#         if i == 12 - 1 - j:
#             print(f"{array_point[i,j]}", end=", " )


# print("\n\nYeu cau 3=========================================")
# a = int(str(input("Nhap vao mot so tu 0 - 100 bat ki: ")))
# so_lon  = []
# so_be = []
# count= count1 = count2 =0
# if ((a > 0) or (a < 100)):
    
#     for j in range(0,12):
#         for i in range(0, 12):
#             if a < array_point[i,j]:
#                 count1 += 1
#                 so_lon.append(array_point[i,j])   
#             elif a > array_point[i,j]:
#                 count2 += 1                
#                 so_be.append(array_point[i,j]) 
#             elif a == array_point[i,j]:
#                 count += 1

# else:print("so khong hop le")   

# print(f"\nCo {count1} so lon hon so nhap vao la: ", so_lon)
# print(f"\nCo {count2} so be hon so nhap vao la: ", so_be)
# print(f"Co {count} bang hon so nhap vao")

print("Thuc hanh 2=========================================")
print("Yeu cau 1=========================================")
# matrix = np.random.randint(0, 10, (10, 30))
array = np.random.randint(1, 11, size=(10, 30))
# print(array)
matrix = np.loadtxt('TH04_data/data_vd.txt', dtype = int)
# print(matrix.shape)
# print("ham tra ve so cot: ",matrix.shape[1])
# print("ham tra ve so hang: ",matrix.shape[0])
# for i in range (0, matrix.shape[1]):
#     print(f"Diem trung binh cua hoc sinh {i+1} trong lơp la: ", matrix[:,i].mean())

# tb_max = matrix[:,0].mean()
# for i in range (matrix.shape[1]):
#     if tb_max < matrix[:,i].mean():
#         tb_max = matrix[:,i].mean()
#         temp = i;
# print(f"Hoc sinh {temp} co diem trung binh cao nhat la: ", tb_max)
# print(f"Bang diem day du cua hoc sinh {temp} la: ", matrix[:,-temp] )

# tb_min = matrix[:,0].mean()
# for i in range (matrix.shape[1]):
#     if tb_min > matrix[:,i].mean():
#         tb_min = matrix[:,i].mean()
#         temp = i;
# print(f"Hoc sinh {temp} co diem trung binh thap nhat la: ", tb_min)
# print(f"Bang diem day du cua hoc sinh {temp} la: ", matrix[:,-temp] )
        
# print("ham tra ve so cot: ",matrix.shape[1])
# print("ham tra ve so hang: ",matrix.shape[0])
# for i in range (0, matrix.shape[1]):
#     print(f"Diem trung binh cua hoc sinh {i+1} trong lơp la: ", matrix[:,i].mean())

# print("Yeu cau 2=========================================")
# point_tb = np.round(np.mean(matrix, axis=1), 2) 
# max_index = np.argmax(point_tb)
# min_index = np.argmin(point_tb)

# max_arr = point_tb[max_index]
# min_arr = point_tb[min_index]

# print("DTB cua tung mon hoc la: ", point_tb)
 
# print(f"Mon học {max_index} co diem trung binh cao nhat la: {max_arr}")
# print(matrix[:, max_index].tolist())

# print(f"Môn hhọc {min_index} co diem trung binh thap nhat la:  {min_arr}")
# print(matrix[:, min_index].tolist())

# print("Yeu cau 3=========================================")
# print("tinh do lech chuan mon hoc")
# std = np.std(matrix, axis=1)
# most_consistent_sj = np.argmin(std)
# least_consistent_sj = np.argmax(std)
# print(f"Mon hoc co diem dong deu nhat la: {most_consistent_sj}", matrix[:, most_consistent_sj].tolist())
# print(f"Mon hoc co diem lech nhat la: {least_consistent_sj}", matrix[:, least_consistent_sj].tolist())

# print("tinh do lech chuan sinh vien")
# std = np.std(matrix, axis=0)
# most_consistent_st = np.argmin(std)
# least_consistent_st = np.argmax(std)
# print(f"Sinh vien co diem dong deu nhat la: {most_consistent_st}", matrix[:, most_consistent_st].tolist())
# print(f"Sinh vien co diem lech nhat la: {least_consistent_st}", matrix[:, least_consistent_st].tolist())

# print("thưc hanh 3=========================================")
# import matplotlib.pyplot as plt

# square_feet = np.array([1460, 2108, 1743, 1499, 1864, 2391, 1977, 1610, 1530, 1759, 1821, 2216])
# square_price = np.array([288700, 309300, 301400, 291100, 302400, 314900, 305400, 297000, 292400, 298200, 304300, 311700])

# co_square =  np.corrcoef(square_feet, square_price)
# print("He so tong quan la: ", co_square)

# plt.plot(square_feet, square_price, "go")
# plt.title("BAI THUC HANH 3")
# plt.show()