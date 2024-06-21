# print("BAI 15 =================================================")
# print("BAI 15.1")
# def greeting(name, age):
#     print(f"{name} {age}")

# name = str(input("nhap ho va ten: "))
# age = str(input("nhap tuoi: "))
# greeting(name, age)

# print("BAI 15.2")
# import math
# def rabbit_count(month):
#     result = int(math.pow(2, (month+1)))
#     return result

# print("Ket qua sau khi goi ham rabbit_cout la:")
# a = int(input("so thang ban muon: "))
# print(f"sau {a} thang, so tho co duoc la: ", rabbit_count(a))

# print("BAI 15.3")
# grades = ['A', 'B', 'C', 'D', 'F', 'A', 'B', 'C', 'D', 'F', 'A', 'B', 'C', 'D', 'F', 'A', 'B', 'C', 'D', 'F']

# def count_mark(n):
#     total = len(n)
#     sv_hoclai = n.count('F')
#     return total, sv_hoclai

# print("tong so hoc sinh va so hoc sinh phai hoc la la: ", count_mark(grades))

# print("BAI 15.4")
# import math
# def bmi_show(weight, height):
#     bmi = weight/(math.pow(height, 2))
#     if bmi < 18.5:
#         print("ban thuoc the trang underweight")
#     elif bmi >=18.5 and bmi < 25:
#         print("ban thuoc the trang normalweight")
#     elif bmi >= 25 and bmi < 30:
#         print("ban thuoc the trang overweight")
#     elif bmi >=30:
#         print("ban thuoc the trang obese")
#     return round(bmi, 2) 

# print("Chi so bmi cua ban la: ", bmi_show(47, 1.59))

# print("BAI 15.5")
# def cal_point(hs10):
#     char_index = ['F', 'D', 'D+', 'C', 'C+', 'B', 'B+', 'A', 'A+']
#     hs4_index = [0, 1, 1.5, 2, 2.5, 3, 3.5, 3.7, 4]
#     hs4 = []
#     char = []
#     for i in range(len(hs10)):
#         if (hs10[i] < 4 and hs10[i] > 0):
#             hs4.append(hs4_index[0])
#             char.append(char_index[0])
#         elif (hs10[i] >= 4 and hs10[i] < 5):
#             hs4.append(hs4_index[1])
#             char.append(char_index[1])
#         elif (hs10[i] >= 5 and hs10[i] < 5.5):
#             hs4.append(hs4_index[2])
#             char.append(char_index[2])
#         elif (hs10[i] >= 5.5 and hs10[i] < 6.5):
#             hs4.append(hs4_index[3])
#             char.append(char_index[3])
#         elif (hs10[i] >= 6.5 and hs10[i] < 7):
#             hs4.append(hs4_index[4])
#             char.append(char_index[4])
#         elif (hs10[i] >= 7 and hs10[i] < 8):
#             hs4.append(hs4_index[5])
#             char.append(char_index[5])
#         elif (hs10[i] >= 8 and hs10[i] < 8.5):
#             hs4.append(hs4_index[6])
#             char.append(char_index[6])
#         elif (hs10[i] >= 8.5 and hs10[i] < 9):
#             hs4.append(hs4_index[7])
#             char.append(char_index[7])
#         elif (hs10[i] >= 9 and hs10[i] <= 10):
#             hs4.append(hs4_index[8])
#             char.append(char_index[8])
#     dtb_hs10 = round(sum(hs10)/len(hs10),2)
#     dtb_hs4 = round(sum(hs4)/len(hs4),2)

#     print("Tong so mon hoc la: ", len(hs10))
#     print("Diem TB trên thang 10 la: ", dtb_hs10)   
#     print("Diem TB trên thang 4 la: ", dtb_hs4)
#     print("Diem trên thang 4 la: ", hs4)
#     print("Diem trên thang chu la: ", char)

# hs10 = [ 9, 9.4, 5, 6.7, 7, 8.3, 8.6, 7, 10]
# cal_point(hs10)

# print("BAI 15.6")
# def list_prime(n):
#     # n = int(str(input("nhap 1 lon hon 1 so de kiem tra no co la so nguyen to: "))) 
#     if n <= 1:
#         print(f"{n} khong hop le")
#     else:
#         snt =[]
#         for a in range (n):
#             if a > 1:
#                 count = 0
#                 for i in range(1, int((a/2) + 1)):
#                     if (a % i == 0):
#                         count = count + 1
#                 if (count == 1):
#                     snt.append(a)
#         print(f"Cac so nguyen to co tu 2 den {n} la: ", snt)

# list_prime(7)

# print("BAI 15.7 - LOP DOI TUONG")
# class Rectange:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#     def getArea(self):
#         area = round(self.width * self.height, 1)
#         return area
#     def getPerimeter(self):
#         perimeter = round( (self.width + self.height)*2, 1)
#         return perimeter
    
# r1 = Rectange(10,5)
# print(f"Chieu rong: {r1.width}")
# print(f"Chieu dai: {r1.height}")

# print(f"Chuvi: {r1.getPerimeter()}")
# print(f"Dien tich: {r1.getArea()}")
        
# print("BAI 16 - LOP DOI TUONG")
# class Person: 
#     def __init__(self, name, year, height, weight):
#         self.name = name
#         self.year = year
#         self.height = height
#         self.weight = weight
        
#     def showPerson(self):
#         print(f"Ten: {self.name}")
#         print(f"Nam sinh: {self.year}")
#         print(f"Chieu cao: {self.height}")
#         print(f"Can nang: {self.weight}")
    
#     def BMI(self):
#         import math
#         bmi = self.weight/(math.pow(self.height, 2))
#         print(f"Chi so BMI cua ban la {round(bmi, 2) }")
#         if bmi < 18.5:
#             print("ban thuoc the trang underweight")
#         elif bmi >=18.5 and bmi < 25:
#             print("ban thuoc the trang normalweight")
#         elif bmi >= 25 and bmi < 30:
#             print("ban thuoc the trang overweight")
#         elif bmi >=30:
#             print("ban thuoc the trang obese")        
#         # return round(bmi, 2) 


# p1 = Person('Linh', 2003, 1.59, 46.5)
# p1.showPerson();
# p1.BMI();

# print("BAI - FLIE")
# mo file
# f = open('THO3_FILE/file.txt', 'w')

# # Doc noi dung file vao bien st
# # st = f.read()
# # print(f"Noi dung file: {st}")

# # Doc tung dong
# # st1= f.readline()
# # print(f"Noi dung file: {st1}")
# hihi ="hihi hihi"
# f.write(hihi)

# f.close()

# l = open('THO3_FILE/file.txt', 'a+')

# print(f"Ten file: {l.name}")
# print(f"Che do mo file: {l.mode}")
# print(f"trang thai dong mo: {l.closed}")

# print("BAI - FLIE - LAM VIEC VOI FILE")     
# fo = open('Lý Thuyết/data.txt', 'w')
# fo.write('python meow meow');
# fo.close()
# print("Ghi file thanh cong")

# print("BAI 17 - DOC/GHI FILE")

# file = open("TH03_FILE/dayso1_bai17.txt")
# string_file = file.read()
# array = string_file.split()
# number = []
# for num in array:
#     number.append(int(num))

# max_number = number[0]
# min_number = number[0]
# print(number)

# for i in number:
#     if i> max_number:
#         max_number = i
#     if i < min_number:
#         min_number = i

# # print(max_number)
# # print(min_number)

# # Tìm vị trí xuất hiện đầu tiên của phần tử lớn nhất và nhỏ nhất
# max_index = number.index(max_number)
# min_index = number.index(min_number)

# # Đổi chỗ phần tử lớn nhất và nhỏ nhất
# number[max_index] = min_number
# number[min_index] = max_number

# numbers = ''
# for a in number:
#     numbers += str(a) + ', '
# print(numbers)

# f = open("TH03_FILE/dayso2_bai17.txt", 'w')
# f.write(numbers)



