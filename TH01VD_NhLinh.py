# # slide 20
# """
# #Hiển thị thông báo chúc mừng
# print('Chào mừng bạn đến với ngôn ngữ lập trình Python!')
# #Nhập tên vào biến name
# name = input('Nhập tên của bạn:')
# #Hiển thị thông báo 
# print('Chúc bạn ', name, 'sẽ thành thạo Python sau khóa học này!')
# """

# # slide 21
# """
# # Khởi tạo biến a = 0; A = 0
# a = 0 
# A = 0
# for i in range(1,6):
#     print(i)
#     a = a + i
# #Hiển thị kết quả biến a
# print('Giá trị của biến a = ', a)
# print('-------------------------')

# for i in range (1,6,2):
#     print(i)
#     A = A + i
# # Hiển thị kết quả của biến A
# print('Giá trị của biến A = ',A)
# """

# #Slide 23
# """
# #Khởi tạo 2 biến a, b
# num_a = int(input('Nhập số thứ nhất a = '))
# num_b = int(input('Nhập số thứ hai b = '))

# # tính tổng, hiệu, tích, thương
# tong = num_a + num_b
# hieu = num_a - num_b
# tich = num_a * num_b
# thuong = num_a / num_b

# #In ra kết quả màn hình
# print('Tổng: ',tong)
# print('Hiệu ',hieu)
# print('Tích ',tich)
# print('Thương ',thuong)
# """

# #slide 38
# """
# a = 10 # Mot phep gan so nguyen
# b = 10.01 # Mot so thuc
# name = "Hoang" # Mot chuoi
# print (a)
# print (b)
# print (name)
# """

# #slide 46
# """
# #Kiểm tra kiểu dữ liệu của biến
# x = 1985
# y = 3.1415926535
# z = 'Dai hoc Mo Dia Chat'
# n = [5, 7, 9, 8]
# b = True
# print('Kiểu dữ liệu biến x: ', type(x))
# print('Kiểu dữ liệu biến y: ', type(y))
# print('Kiểu dữ liệu biến z: ', type(z))
# print('Kiểu dữ liệu biến n: ', type(n))
# print('Kiểu dữ liệu biến b: ', type(b))
# """

# #slide 47
# """
# #Kiểu dữ liệu số a = 123
# a = 123
# print('Số: ', a)
# #Kiểu dữ liệu chuỗi A = '123'
# A = '123'
# print('Chuỗi: ', A)
# """

# #slide 52
# """
# st = 'HUMG là Trường đại học hàng đầu tại Việt Nam'
# #Mặc định sẽ tách chuổi tại vị trí dấu cách
# list_st = st.split()
# print(list_st)

# st1 = 'Bùi Thị Lê Na, 2003, Nghệ An'
# #Tùy chọn vị trí tách theo tham số đưa vào
# list_st1 = st1.split(',')
# print(list_st1)
# """

# #slide 62
# """
# #Khai báo danh sách List
# hoc_sinh = ['Lê Thùy Dung','Trần Đức Hùng','Nguyễn Lan Anh','Mai Phương thúy']
# #Truy xuất dữ lieeuh trong danh sách
# #Hiển thị tên học ở vị trí thứ 3
# print('Học sinh vị trí thứ 3: ', hoc_sinh[2])

# #khai báo danh sách với nhiều kiểu dữ liệu khác nhau
# person_info = ['Mary', 1998,'Tokyo,Japan', 1.70, 65]
# #hiển thị tên người- chiều cao trong biển person_info
# print('Họ tên: ', person_info[0],' ---Chiều cao:',person_info[3])
# #khai báo danh sách gồm số nguyên
# list_so = [9,5,8,13,0,4,7,-9,11]
# #truy vấn nhiều phần tử trong danh sách
# print(list_so[3:8])
# """

# #slide 63
# """
# hoc_sinh = ['Lê Thùy Dung','Trần Đức Hùng','Nguyễn Lan Anh','Mai Phương thúy']
# print('Ban đầu: ', hoc_sinh)
# hoc_sinh[2] = 'Nguyễn Thị Lan Anh'
# print('Thay đổi: ', hoc_sinh)
# print('-------------------------')
# list_so = [9,5,8,13,0,4,7,-9,11]
# print('Ban đầu: ', list_so)
# list_so[-1] = 0
# print('Thay đổi: ', list_so)
# """

# #slide 65
# """
# list_a = [8,4,8,2]
# list_b = [3,0,7,6,5]
# #Cộng 2 danh sách
# list_ab = list_a + list_b
# #Kiểm tra phần tử có thuộc tính danh sách ko?
# print(list_ab)
# #kiểm tả phần tử 0
# bol_0 = 0 in list_ab
# print('Phần tử 0 có thuộc list_ab ? ', bol_0)
# #kiểm tả phần tử 9
# bol_9 = 9 in list_ab
# print('Phần tử 9 có thuộc list_ab ? ', bol_9)
# """

# #slide 66
# """
# list_ab = [8, 4, 8, 2, 3, 0, 7, 6, 5]
# #Thêm phần tử vào danh sách
# print('Danh sách ban đầu: \n', list_ab)
# #Thêm vào cuối danh sách
# list_ab.append(10)
# print('Danh sách thêm vào cuối: \n', list_ab)
# #Thêm vào vị trí bất kỳ trong danh sách
# list_ab.insert(1, 100)
# print('Danh sách thêm vào vị trí thứ 2: \n', list_ab)
# """

# #slide 67
# """
# list_ab = [8, 4, 8, 2, 3, 0, 7, 6, 5]
# #Xóa phần tử khỏi danh sách
# print('Danh sách ban đầu: \n', list_ab)

# #Xóa phần tử cuối
# list_ab.pop()
# print('Danh sách xóa phần tư cuối:\n', list_ab)

# # Xóa phần tử tại vị trí số 2
# del list_ab[1]
# print('Danh sách xóa phần tử ở vị trí số 2:\n', list_ab)

# #Xóa phần tử có giá trị 0 xuất hiện đầu tiên
# list_ab.remove(0)
# print('Xóa phần tử có giá trị 0 đầu tiên:\n', list_ab)
# """

# #slide 69
# """
# list_ab = [8, 4, 8, 2, 3, 0, 7, 6, 5]
# #đê,s số lần xuất hiện của một phần tử trong danh sách
# print('Danh sách ban đầu: \n', list_ab)

# #số lần xuất hiện số 8 trong danh sách
# print('Số 8 xuất hiện: ', list_ab.count(8))

# #số lần xuất hiện số 1 trong danh sách
# print('Số 1 xuất hiện: ', list_ab.count(1))
# """

# #slide 70
# """
# ds_a = [4,5,8,9] #khai báo danh sách ds_a
# ds_b = ds_a    #gán giá trị của biến ds_a cho ds_b
# ds_b[1] = 10    #thay đổi giá trị vị trí số 2 trong ds_b
# #----------------------------------------
# print('Biến ds_a: ', ds_a)
# print('Biến ds_b: ', ds_b)
# """

# #slide 71
# """
# ds_a = [4,5,8,9] #khai báo danh sách ds_a
# ds_b = ds_a.copy()   #sao chép ds_a cho ds_b
# ds_b[1] = 10    #thay đổi giá trị vị trí số 2 trong ds_b
# #----------------------------------------
# print('Biến ds_a: ', ds_a)
# print('Biến ds_b: ', ds_b)
# """

# #slide 72
# #khai báo biến kiểu dữ liệu Boolean
# x = True
# y = False
# #khai báo biến kiểu dữ liệu Boolean qua biểu thức
# z = 5>8
# w = 12 == 12
# #------------------------------------
# print('Kiểu dữ liệu của biến x:', type(x), ', Giá trị: ', x)
# print('Kiểu dữ liệu của biến y:', type(y), ', Giá trị: ', y)
# print('Kiểu dữ liệu của biến z:', type(z), ', Giá trị: ', z)
# print('Kiểu dữ liệu của biến w:', type(w), ', Giá trị: ', w)

