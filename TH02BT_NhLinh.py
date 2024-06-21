print("BAI 6 =================================================")
# a = str(input("Nhap chu cai bat ky: "))
# vowerl = [ 'u', 'e', 'o', 'a', 'i']
# if not a.isdigit():
#     if ( a.lower() in vowerl):
#         print ("Day la nguyen am")
#     else: 
#         print ("Day la phu am")
# else:
#     print("Day khong phai chu cai")

print("BAI 7 =================================================")
# height = float(input("nhap chieu cao cua ban (don vi m nhe!): "))
# weight = float(input("nhap can nang cua ban (don ki kg nhe): "))
# bmi = weight/(height*height)
# print("chi so BMI cua ban la: ",  bmi)
# if bmi < 18.5:
#     print("ban thuoc the trang underweight")
# elif bmi >=18.5 and bmi < 25:
#     print("ban thuoc the trang normalweight")
# elif bmi >= 25 and bmi < 30:
#     print("ban thuoc the trang overweight")
# elif bmi >=30:
#     print("ban thuoc the trang obese")

print("BAI 8 =================================================")
# print("nhap so bat ki tu 1 den 12: ")
# x = int(input())
# if x >= 1 and x <= 3:
#     print("This is spring")
# elif x > 3 and x < 7:
#     print ("This is summer")
# elif x > 6 and x < 10:
#     print ("This is autumn")   
# elif x >= 10 and x <= 12:
#     print("This is winter")
# else:
#     print("Number is not valid") 

print("BAI 9 =================================================")
# a = int(str(input("Nhap so bat ky tu 1 den 10: ")))
# if  a >= 1 and a <= 10:
#     for i in range(1,11):
#         print(f"{a} x {i} = {a*i}")
# else:
#     print("nhap so sai yeu cau roi ban oi")

print("BAI 10 =================================================")
hs10 = [ 9, 9.4, 5, 6.7, 7, 8.3, 8.6, 7, 10]
char_index = ['F', 'D', 'D+', 'C', 'C+', 'B', 'B+', 'A', 'A+']
hs4_index = [0, 1, 1.5, 2, 2.5, 3, 3.5, 3.7, 4]
hs4 = []
char = []
for i in range(len(hs10)):
    if (hs10[i] < 4 and hs10[i] > 0):
        hs4.append(hs4_index[0])
        char.append(char_index[0])
    elif (hs10[i] >= 4 and hs10[i] < 5):
        hs4.append(hs4_index[1])
        char.append(char_index[1])
    elif (hs10[i] >= 5 and hs10[i] < 5.5):
        hs4.append(hs4_index[2])
        char.append(char_index[2])
    elif (hs10[i] >= 5.5 and hs10[i] < 6.5):
        hs4.append(hs4_index[3])
        char.append(char_index[3])
    elif (hs10[i] >= 6.5 and hs10[i] < 7):
        hs4.append(hs4_index[4])
        char.append(char_index[4])
    elif (hs10[i] >= 7 and hs10[i] < 8):
        hs4.append(hs4_index[5])
        char.append(char_index[5])
    elif (hs10[i] >= 8 and hs10[i] < 8.5):
        hs4.append(hs4_index[6])
        char.append(char_index[6])
    elif (hs10[i] >= 8.5 and hs10[i] < 9):
        hs4.append(hs4_index[7])
        char.append(char_index[7])
    elif (hs10[i] >= 9 and hs10[i] <= 10):
        hs4.append(hs4_index[8])
        char.append(char_index[8])
        
avg_hs4 = sum(hs4) / len(hs4)
avg_hs10 = sum(hs10) / len(hs10)
print("Diem trên thang 10 la: ", hs10)
print("Tong so mon hoc la: ", len(hs10))
print("Diem trên thang 4 la: ",hs4)
print("Diem trên thang chu la: ",char)
print("DTB thang 10 la: " + "%.2f" % avg_hs10)
print("DTB thang 4 la: " + "%.2f" % avg_hs4)


print("BAI 11 =================================================")
# a = int(str(input("nhap 1 so de kiem tra no co la so nguyen to: "))) 
# if a <= 1:
#     print(f"{a} khong la so nguyen to")
# else:
#     count = 0
#     for i in range(1, int((a/2) + 1)):
#         if (a % i == 0):
#             count = count + 1
#     if (count == 1):
#         print(f"{a} la so nguyen to")
#     else:
#         print(f"{a} khong la so nguyen to")

print("BAI 12 =================================================")
# n = int(str(input("nhap 1 lon hon 1 so de kiem tra no co la so nguyen to: "))) 
# if n <= 1:
#     print(f"{n} khong hop le")
# else:
#     snt =[]
#     for a in range (n):
#         if a > 1:
#             count = 0
#             for i in range(1, int((a/2) + 1)):
#                 if (a % i == 0):
#                     count = count + 1
#             if (count == 1):
#                 snt.append(a)
#     print("Cac so nguyen to co tu 0 den n la: ", snt)      
   
print("BAI 13 =================================================")
# a = int(str(input("Nhap so tu nhien (>0): ")))
# nhiphan = ''
# while a > 0:
#     nhiphan = str(a % 2) + nhiphan
#     a = (a // 2) 
# print(nhiphan)


print("BAI 14 =================================================")
# height = [1.6, 1.78, 1.77, 1.85, 1.7, 1.54, 1.62, 1.59, 1.50, 1.69, 1.77, 1.63]
# max = height[0]
# for i in range (1,len(height)):
#     if height[i] > max:
#         max = height[i]
# min = height[0]
# for i in range (1,len(height)):
#     if height[i] < min:
#         min = height[i]

# print("Nguoi cao nhat lop la: ", max)
# print("Nguoi cao nhat lop la: ", min)

# print("Chieu cao trung binh la: ", sum(height)/len(height))

# print("nhung nguoi co chieu cao cao hon turng binh la: ")
# for i in range (len(height)):
#     cao = 0
#     if height[i] >  (sum(height)/len(height)):
#         cao = cao + 1
#         print(height[i])

# print("nhung nguoi co chieu cao thap hon turng binh la: ", )
# for i in range (len(height)):
#     thap = 0
#     if height[i] <=  (sum(height)/len(height)):
#         thap = thap 
#         print(height[i])

        





