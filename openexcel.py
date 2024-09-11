from mysql.connector import Error
import mysql.connector
import openpyxl
archivo_excel = openpyxl.load_workbook('data1.xlsx')
hoja_excel = archivo_excel.active
filas = []
for fila in hoja_excel.iter_rows():
    fila_lista = [celda.value for celda in fila]
    filas.append(tuple(fila_lista))

print(filas[2])
# try:
#     connection = mysql.connector.connect(
#         host='localhost',
#         port=3306,
#         user='root',
#         password='Ilov3yoursmile',
#         db='carga_m_A'
#     )

#     if connection.is_connected():
#         cursor = connection.cursor()
#         cursor.executemany("""INSERT INTO empleados(Employee_ID, Full_Name, Job_Title,
#          Department, Business_Unit, Gender,Ethnicity, Age, Annual_Salary,
#          Bonus) VALUES (%s, %s, %s, %s, %s,%s, %s, %s, %s, %s
#          )""", filas[1])
#         if (len(data) == cursor.rowcount):
#             connection.commit()
#             print("{} Filas insertadas.".format(len(filas)))
#         else:
#             connection.rollback()
# except Error as ex:
#     print("Error en la conexion: {}".format(ex))
# finally:
#     if connection.is_connected():
#         connection.close()
#         print("Conexion cerrada.")
