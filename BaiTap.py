# def Bai1_chia_keo ():
#     so_keo = int(input("Nhập số kẹo : "))
#     so_hoc_sinh = int(input("Nhập số học sinh : "))
#     chia_deu = so_keo // so_hoc_sinh
#     so_con_lai = so_keo % so_hoc_sinh
#     print("Kết quả là ", chia_deu, "cái")
#     print("Số kẹo còn ", so_con_lai,)
# Bai1_chia_keo()

##########################################################

# def Bai2_tinh_tuoi():
#     Ten = str(input("Nhập tên của bạn :"))
#     nam_sinh = int(input("Nhập năm sinh :"))
#     nam_hien_tai = int(input("Nhập năm hiện tại: "))
#     tuoi = nam_hien_tai - nam_sinh
#     print("Bạn ",Ten,"năm nay",tuoi,)
# Bai2_tinh_tuoi()

##########################################################

# def Bai3_tinh_tho():
#     thang = int(input("Nhập vào số tháng :"))
#     tho = thang * 2
#     print("Trong rừng có ",tho, "con thỏ")
# Bai3_tinh_tho()

##########################################################
def Bai4_chuoi_van_ban():
    str = 'Nước Việt Nam là một, dân tộc Việt Nam là một. Sông có thể cạn núi có thể mòn, song chân lý ấy không bao giờ thay đổi. (HỒ CHÍ MINH, 1890-1969)'
    x = 'hồ chí minh' in str
    y = 'non sông' in str
    list_str = str.split('.')
    list_str2 = str.isalnum()
    print("Số ký tự trong chuỗi là ",len(str))
    print("Kết quả kiểm tra -hồ chí minh-",x)
    print("Kết quả kiểm tra -non sông-",y)
    print(list_str)
    print(list_str2)

# Bai4_chuoi_van_ban()