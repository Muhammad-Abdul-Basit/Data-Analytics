from dataBaseConnect import get_connection
conn=get_connection()
cursor=conn.cursor()
cursor.execute("""select i.store_id,COUNT(r.rental_id) AS Total_rental
                FROM inventory i INNER JOIN rental r 
                WHERE i.inventory_id=r.inventory_id
                GROUP BY i.store_id""")
rows=cursor.fetchall()
for store_id, Total_rental in rows:
    print(" store Id : ", store_id, " has : ", Total_rental, " rental")
cursor.close
conn.close