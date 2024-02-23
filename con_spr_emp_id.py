
import pypyodbc as odbc
import matplotlib.pyplot as plt
import numpy as np


driver = 'SQL SERVER'
s_name = 'DESKTOP-B12PD05'
db_name = 'TSQL2012'

conn = f"""
    DRIVER={{{driver}}};
    SERVER={s_name};
    DATABASE={db_name};
    Trust_Connection=yes;
    """

connection = odbc.connect(conn)
cursor = connection.cursor()
print('\n*** SQL Server is connected. ***')

print('\nempid, shipperid, freight, shipcountry')
query = 'SELECT TOP (5) empid, shipperid, freight, shipcountry FROM Sales.Orders'
cursor.execute(query)
rows = cursor.fetchall()
for row in rows:
    print(row)

emp_id = 2
query = f'EXECUTE spr_emp_id {emp_id};'
cursor.execute(query)
rows = cursor.fetchall()
print('\nSum of freight: ', sum(r_col[1] for r_col in rows))

query = 'SELECT * FROM Sum_freight'
cursor.execute(query)
rows_veiw = cursor.fetchall()
print()
for row in rows_veiw:
    print(row)

rows_value = np.array(rows_veiw)

fig = plt.figure(figsize = (4, 3))
plt.bar(rows_value[:, 0], rows_value[:, 1], width=0.5)
plt.show()

connection.close()

