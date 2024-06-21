import pyodbc as odbc
# import test.sql as ts
# print(pyodbc.drivers())

# print("Kết nối database, kiểm tra kết nối và thực hiện truy vấn")
# define the connection variables
# DRIVER_NAME = 'SQL Server'
# SERVER_NAME = 'LAPTOP-MGFO2570\\NHATLINH'
# DATABASE_NAME = 'giohang'
# UID = 'sa'
# PWD = '123456'


# # Define the connection string
# conn_string = f'DRIVER={DRIVER_NAME};SERVER={SERVER_NAME};DATABASE={DATABASE_NAME};UID={UID};PWD={PWD}'

# def is_connected():
#     try:
#         # Attempt to establish a connection
#         conn = odbc.connect(conn_string)
#         conn.close()
#         return True
#     except odbc.Error as e:
#         print(f'Error: {e}')
#         return False
# def getData(query):
#     cursor = odbc.connect(conn_string).cursor().execute(query)
#     return cursor


# # Kiểm tra kết nối
# if is_connected():
#     print("Connected to SQL Server database")
# else:
#     print("Failed to connect to SQL Server database")

# query = "select * from sanpham"
# getData(query)
# # cursor = odbc.connect(conn_string).cursor().execute(query)
# for row in getData(query):
#     print(row)

print("tạo database")
DRIVER_NAME = 'ODBC Driver 17 for SQL Server'
SERVER_NAME = 'localhost\\NHATLINH'  # Tên server có thể khác tùy vào cấu hình của bạn
DATABASE_NAME = 'giohang'  # Chúng ta sẽ kết nối tới cơ sở dữ liệu 'master' để tạo cơ sở dữ liệu mới
UID = 'sa'
PWD = '123456'

# conn_str = f'DRIVER={DRIVER_NAME};SERVER={SERVER_NAME};DATABASE={DATABASE_NAME};UID={UID};PWD={PWD}'

def connect_sql_server():
    conn_str = f'DRIVER={DRIVER_NAME};SERVER={SERVER_NAME};DATABASE={DATABASE_NAME};UID={UID};PWD={PWD}'
    return odbc.connect(conn_str)

def is_connected():
    try:
        # Attempt to establish a connection
        conn = connect_sql_server()
        conn.close()
        return True
    except odbc.Error as e:
        print(f'Error: {e}')
        return False


def getData(query): 
    conn = connect_sql_server()
    cursor = conn.cursor().execute(query)
    conn.commit()
    # conn.close()  # Đóng kết nối
    # cursor.close()
    return cursor  # Trả về kết quả

def execute_query(conn, query, params=None):
    # Hàm thực thi truy vấn SQL
    cursor = conn.cursor()
    if params:
        cursor.execute(query, params)
    else:
        cursor.execute(query)
    return cursor

# Kiểm tra kết nối
# if is_connected():
#     print("Connected to SQL Server database")
# else:
#     print("Failed to connect to SQL Server database")

# conn =  connect_sql_server()
# cursor = conn.cursor()
# name_tb = 'table1'

# sql.create_tbl()

# insert_data_query = f'''
# INSERT INTO {name_tb} (id, name_product, decribles) VALUES (1, 'Product1', 'Desc1'),
#                                                           (2, 'Product2', 'Desc2'),
#                                                           (3, 'Product3', 'Desc3'),
#                                                           (4, 'Product4', 'Desc4'),
#                                                           (5, 'Product5', 'Desc5')
# '''

# getData(insert_data_query)

# dt_tbl =  getData('select * from table1')

# print("ID NAME NOTE")
# for row in dt_tbl:
#     print("%s  %s  %s" %(row[0], row[1], row[2]))