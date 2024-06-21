import math
# Bai6

#vowelLetters = "UEOAI"
#consonantLetters = "BCDFGHJKLMNPQRSTVWXYZ"

#charIn = input("Nhập vào một kí tự để kiểm tra: ")

#if charIn.lower() in vowelLetters.lower():
#    print("Đây là một nguyên âm")

#if charIn.lower() in consonantLetters.lower():
#    print("Đây là một phụ âm")


# Bai7

# m = float(input("Nhập vào chiều cao của bạn: "))
# kg = float(input("Nhập vào cân nặng của bạn: "))

# bmiCAL = kg / pow(m, 2)
# print("BMI: ", bmiCAL)

# if bmiCAL < 18.5:
#    print("Under Weight!!!")
# elif bmiCAL >= 18.5 and bmiCAL < 24.9: 
#    print("Nomal Weight!!!")
# elif bmiCAL >= 25 and bmiCAL < 29.5: 
#    print("Over Weight!!!")
# elif bmiCAL >= 30 : 
#    print ("Obse!!!")


# Bai8

#mOB = int(input("Nhập vào tháng sinh của bạn: "))

#if (mOB >= 1 and mOB <= 3):
#    print ("Bạn sinh vào Mùa xuân")
#elif (mOB >= 4 and mOB <= 6):
#    print ("Bạn sinh vào Mùa hạ")
#elif (mOB >= 7 and mOB <= 9):
#    print ("Bạn sinh vào Mùa thu")
#elif (mOB >= 10 and mOB <= 12):
#    print ("Bạn sinh vào Mùa đông")
#else :
#    print("Tháng sinh nhập vào không đúng!")

# Bai9

#n = int(input("Nhập bảng cửu chương bạn muốn xem [1-10]: "))
#while True:
#    if (n < 1 or n > 10):
#        n = int(input("Nhập sai, vui lòng nhập số từ 1 đến 10: "))
#    elif (n >= 1 and n <= 10):
#        break

#for i in range(1, 11):
#        print(f"{n} * {i} = {n * i}")


# Bai10
# diemHe10 = [8.4, 6.5, 7.3, 2.6, 9.0, 5.8, 6.0, 9.7, 8.1]
# diemChu = ["B+", "C+", "B", "F", "A+", "C", "C", "A+", "B+"]

# tb = int(0)

# for i in range(0, len(diemHe10)):
#    tb += diemHe10[i]

# print("tong so mon hoc la: ", len(diemHe10))
# print("diem trung binh he 10 la: ",tb/len(diemHe10))

# diem_chu_he_4 = []

# for diem in diemChu:
#   if diem == "A+":
#     diem_chu_he_4.append(4.0)
#   elif diem == "A":
#     diem_chu_he_4.append(3.7)
#   elif diem == "B+":
#     diem_chu_he_4.append(3.5)
#   elif diem == "B":
#     diem_chu_he_4.append(3.0)
#   elif diem == "C+":
#     diem_chu_he_4.append(2.5)
#   elif diem == "C":
#     diem_chu_he_4.append(2.0)
#   elif diem == "D+":
#     diem_chu_he_4.append(2.0)
#   elif diem == "D":
#     diem_chu_he_4.append(1.0)
#   else:
#     diem_chu_he_4.append(0)

# diem_trung_binh_he_4 = sum(diem_chu_he_4) / len(diem_chu_he_4)
# print("Điểm trung bình hệ 4:", diem_trung_binh_he_4)

# bai11

#def checkSNT(x):
#     if(x == 0 or x == 1): 
#         return False
#     for i in range(2, int(math.sqrt(x)) + 1):
#         if(x % i == 0):
#             return False
#     return True

#x = int(input("Nhập số bạn muốn "))

#if(checkSNT(x) == True): 
#     print("Là số nguyên tố") 
#else: 
#     print("Không phải số nguyên tố") 

# Bai12

# import math

# def checkSNT(x):
#     if(x == 0 or x == 1): 
#         return False
#     for i in range(2, int(math.sqrt(x)) + 1):
#         if(x % i == 0):
#             return False
#     return True

# x = int(input("Nhap so ban muon: "))

# for j in range(0, x + 1):
#     if(checkSNT(j) == True): print(j ) 

# Bai 13 

# def decimal_to_binary(n):
#     if n == 0:
#         return '0'
#     binary = ''
#     while n > 0:
#         binary = str(n % 2) + binary
#         n = n // 2
#     return binary


# value = int(input("nhap so tu nhien : "))
# binary_representation = decimal_to_binary(value)
# print(binary_representation)

# Bai14

# chieu_cao_sinh_vien = [1.65, 1.7, 1.55, 1.64, 1.78, 1.67, 1.59, 1.62, 1.45, 1.8, 1.69, 1.5]

# chieu_cao_cao_nhat = max(chieu_cao_sinh_vien)
# chieu_cao_thap_nhat = min(chieu_cao_sinh_vien)

# print("chieu cao cua sinh vien cao nhat:", chieu_cao_cao_nhat)
# print("chieu cao cua sinh vien thap nhat:", chieu_cao_thap_nhat)

# tong_chieu_cao = sum(chieu_cao_sinh_vien)
# so_luong_sinh_vien = len(chieu_cao_sinh_vien)
# chieu_cao_trung_binh = tong_chieu_cao / so_luong_sinh_vien

# print("chieu cao trung binh cua sinh vien", chieu_cao_trung_binh)

# so_luong_sinh_vien_cao_hon_trung_binh = 0
# for chieu_cao in chieu_cao_sinh_vien:
#   if chieu_cao >= chieu_cao_trung_binh:
#     so_luong_sinh_vien_cao_hon_trung_binh += 1

# print("Số lượng sinh viên cao hơn hoặc bằng chiều cao trung bình:", so_luong_sinh_vien_cao_hon_trung_binh)