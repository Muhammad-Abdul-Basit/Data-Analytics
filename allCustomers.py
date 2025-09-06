from dataBaseConnect import get_connection
conn=get_connection()
cursor=conn.cursor()
cursor.execute("SELECT COUNT(*) as TotalCustomers FROM customer")
customer=cursor.fetchone()
print(" Total customers are : ", customer[0])
