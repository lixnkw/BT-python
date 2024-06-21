# print ("BAI 1================================================================")

# n =int(input('so keo cua co - N:'))
# m = int(input('so hoc sinh - M:'))

# a= int(n/m)

# print ('so keo moi ban la:', a)
# print (' so keo co con lai la:', (n - (m*a)))


# print ("BAI 2================================================================")

# from datetime import date

# a = str(input("nhap ho va ten: "))
# b = int(input("nhap nam sinh: "))

# current_year = date.today().year
# tuoi = current_year - b
# print(a + " nam nay" ,current_year - b)


# print ("BAI 3================================================================")
# print("ban dau co mot cap tho, biet rang sau 1 thang, so tho se nhan doi. Sau x thang, so tho la bao nhieu")
# a = int(input("so thang ban muon: "))

# print("sau "+ str(a) + " thang, so tho co duoc la: " +  str(2**(a+1)) )


# print ("BAI 4================================================================")

# vanban = "Nuoc Viet nam la mot, dan toc Viet Nam la mot. Song co the can nui co the mon, song chan ly ay khong bao gio thay doi (HO CHI MINH, 1890 - 1969)"
# print (vanban)
# dodai= len(vanban)
# print (f"Doan van tren co {dodai} ky tu")

# word1 = 'ho chi minh'
# word2 = 'non song'

# print ("\n")
# if (word1.lower() in vanban.lower()) == True:
#  print ("doan van co chua tu \"ho chi minh \"")
# else: print ("doan van khong chua tu \"ho chi minh \"")

# if (word2.lower() in vanban.lower()) == True:
#  print ("doan van co chua tu \"non song \"") 
# else: print ("doan van khong chua tu \"non song \"")

# print ("\n")
# print ("Doan van sau khi duoc phan tach sau cac dau \" . \" la: ")
# for arr in vanban.split("."):
#  print(arr.strip()) 
 
# alnum = []
# for ky_tu in vanban:
#   if not ky_tu.isalnum():
#     alnum.append(ky_tu)
# print ("\n")
# if not alnum:
#  print("doan van khong chua ki tu dac biet")
# else:  print("doan van chua ki tu dac biet la:  ", "".join(alnum))

# print ("\n")
# print("doan van sau khi thay the chu \"Viet Nam \" thanh chu \"VIET NAM \" la: ")
# print(vanban.replace("Viet Nam", "VIET NAM"))

# print ("BAI 5================================================================")
# grades = ['A', 'B', 'C', 'D', 'F', 'A', 'B', 'C', 'D', 'F', 'A', 'B', 'C', 'D', 'F', 'A', 'B', 'C', 'D', 'F']
# print("so hoc sinh la: ", len(grades))
# print("So hoc sinh bi diem F phai thi lai la: ", grades.count('F'))
# print("So hoc sinh tu diem B tro len la: ", grades.count('A') + grades.count('B') )
# del grades[0]
# grades.pop()
# print("danh sach diem moi sau khi xoa diem hoc sinh dau và cuoi la: ", grades)
