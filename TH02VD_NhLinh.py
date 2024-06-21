# #slide 6
# """
# a = 10
# b = 8
# #--------------------------------------------
# tong = a + b   #Tổng của 2 số
# hieu = a - b   #hiệu của 2 số
# tích = a*b     #Tích của 2 số
# thuong = a/b   #Thuong của 2 số
# thuong_nguyen = a//b     #Phép chia lấy phần nguyên
# thuong_du = a%b          #Phép chia lấy phần dư
# mu = a**b       #Tính giá trị a lũy thừa b
# print('Tổng: ',tong)
# print('Hiệu: ',hieu)
# print('Thương: ',thuong)
# print('Thương nguyên: ',thuong_nguyen)
# print('Thương dư: ',thuong_du)
# print('Mũ: ',mu)
# """

# #slide 8
# """
# #Các toán tử so sánh 
# a = 29 
# b= 10
# #Kết quả của phép so sánh
# print('1) Lớn hơn (a > b):', a>b)
# print('2) Nhỏ hơn (a < b):', a<b)
# print('1) Bằng (a == b):', a==b)
# print('1) Lớn hơn hoặc bằng (a >= b):', a>=b)
# print('1) Nhỏ hơn hoặc bằng (a <= b):', a<=b)
# print('1) Khác (a != b):', a!=b)
# """

# #slide 9
# """
# #Các toán tử logic trong python
# x = 15
# y = True
# kt = (x>3) and (x<10)
# kt2 = (x>3) or (x<10)
# kt3 = not y
# #-----------------------
# print('1) Phép toán AND:', kt)
# print('2) Phép toán OR:', kt2)
# print('3) Phép toán NOT:', kt3)
# """
# #Ví dụ slide 11
# """
# #Câu lệnh điều kiện
# so_tien = input ('Nhập vào số tiền bạn có: ')
# so_tien = int(so_tien)
# if (so_tien >= 1000000):
#     print('Bạn là một tỷ phú')
# else:
#     print('Bạn nghèo lắm!')
# """

# #slide 12
# """num = 10
# if num > 0:
#     print(num,"Là số dương")
# print("Thông điệp này luôn được in")  
# """

# #slide13
# """
# num = 12
# if num % 2 == 0:
#     print('Số 12 là số chẵn!')
# else:
#     print('Số 12 là số lẻ!')
# """

# #slide 15
# """
# num = int(input('Nhập vào một số: '))
# if num % 2 == 0:
#     print('Đây là số chẵn!')
# else:
#     print('Đây là số lẻ!')
# """

# #slide 18
# """
# num = float(input('Nhập một số: '))
# if num >= 0:
#     if num == 0:
#         print('Số không')
#     else:
#         print('Số dương')
# else:
#     print('Số âm')
# """
# #slide 25
# """
# n = int(input('Em sinh tháng mấy?'))
# i=1
# while(i<=n):
#     print(i, ') I Love You!')
#     i=i+1

# #Câu lệnh lặp ngoài vòng lặp white
# print('------------HUMG----------')
# """

# #slide 26
# """#Lệnh BREAK
# n = int(input('Em sinh tháng mấy?'))
# i = 1
# while(i<=n):
#     print(i, ' I Love You!')
#     #Chỉ hiện thị tối đa 3 lần
#     if (i==3):
#         break; #Thoát khỏi vòng lặp while
#     i=i+1
    
# print('---------EAUT---------')   
# """

# #slide 27
# """
# n = 20
# i = 1
# while (i<=n):
#     i = i+1
#     if (i %3 != 0):
#         continue
#         #Bỏ qua các câu lệnh phía sau nếu không chia hết cho 3
#     print(i)
# #Câu lệnh lặp ngoài vòng lặp white
# print('------------HUMG------------')
# """

# #slide 28
# """
# # Chỉ cho phép nhập tháng sinh 1 - 12
# while True:
#     n = int(input('Em sinh tháng mấy?'))
#     if (1<= n <= 12):
#         #Tháng sinh nhập vào hợp lệ!
#         break;
#     print('Tháng không đúng, vui lòng nhập lại')
# #Câu lệnh ngoài vòng lặp white
# print('Chào em cô gái tháng ', n)
# """

# #slide 29
# """#Tính 10! = 1*2*3*4*5*6*7*8*9*10
# #Tổng 10 = 1+2+3+4+5+6+7+8+9+10
# n = 10
# tich = 1
# tong = 0
# for i in range (1, n+1):
#     #Mỗi lần lặp biến i tăng lên 1
#     tich = tich*i
#     tong = tong+i
    
# print('10! = ', tich)
# print('10 = ', tong)  
# """
# #slide 30
# """
# #Vòng lặp for với chuỗi ký tự:
# st = 'HUMG IN MY MIND'
# for i in st:
#     print('Ký tự: ', i)
# dem = 0
# for i in st:
#     if (i=='M'):  dem=dem+1
# print('Số ký tự M có trong chuỗi là: ', dem)
# """

# #Ví dụ slide 31
# """#Vòng lặp for với danh sách
# hoc_sinh = ['Phạm Ngọc Hưng', 'Bùi Thị Lê Na',
#             'Nguyễn Thị Huyền Trang', 'Nguyễn Minh Anh',
#             'Dương Anh Quân', 'Nguyễn Chi Quang']
# print('Danh sách học sinh gồm: ')
# tt = 1
# for i in hoc_sinh:
#     print( tt, ') ', i)
#     tt = tt+1
# """

# #slide 33
# """
# #Lệnh for với range()
# for i in range(5):
#     #Giá trị khởi đầu mặc định = 0
#     #Bước nhảy mặc định = 1
#     print('i = ',i)
# #lệnh for với range(m,n)
# for i in range(5,10):
#     #Giá trị khởi đầu m=5
#     #Giá trị kết thúc n = 10
#     #Bước nhảy mặc định = 1
#     print('i = ',i)
# ##lệnh for với range(m,n,d)
# for i in range(2,11,2):
#     #Giá trị khởi đầu m=2
#     #Giá trị kết thúc n = 11
#     #Bước nhảy d = 2
#     print('i = ',i)
# """
# #slide 34
# #Hiển thị bảng cửu chương từ 2 -> 9
# for i in range(2,10):
#     print('Bảng cửu chương ',i)
#     for j in range(1,11):
#         print(i, ' x ', j, ' = ', i*j)
#     print('-------------------------')  
