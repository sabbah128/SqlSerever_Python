
import pypyodbc as odbc


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
print('\n*** SQL Server is connected. ***')

print('\nempid, shipperid, freight, shipcountry')
cursor = connection.cursor()
query = 'SELECT TOP (5) empid, shipperid, freight, shipcountry FROM Sales.Orders'
cursor.execute(query)
rows = cursor.fetchall()
for row in rows:
    print(row)

emp_id = 50
query = f'EXECUTE spr_emp_id {emp_id};'
cursor.execute(query)
rows = cursor.fetchall()
print('\nSum of freight: ', sum(r_col[1] for r_col in rows))

connection.close()

