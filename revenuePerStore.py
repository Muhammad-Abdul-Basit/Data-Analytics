import pandas as pd
from dataBaseConnect import get_connection
conn=get_connection()
cursor=conn.cursor()
cursor.execute(
                """
                select s.store_id, SUM(p.amount) AS TotalAmount from payment p JOIN 
                rental r ON r.rental_id=p.rental_id JOIN
                inventory i ON r.inventory_id=i.inventory_id JOIN
                store s ON s.store_id=i.store_id
                group by s.store_id
                """
)
data=cursor.fetchall()
dataFile=pd.DataFrame(data, columns=["Store", "Total Amount"])
dataFile.to_excel(r"D:\BSIT\Python libraries\Data-Analytics\reports\rentalPerStore.xlsx", index=False)
print(" File saved")
cursor.close()
conn.close()