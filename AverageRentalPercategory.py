from dataBaseConnect import get_connection
import pandas as pd
conn=get_connection()
cursor=conn.cursor()
cursor.execute("""select c.name, AVG(rental_rate) As averageRentalRate from category c JOIN
                  film_category fc ON fc.category_id=c.category_id JOIN
                  film f ON fc.film_id=f.film_id
                  GROUP BY c.name""")
data=cursor.fetchall()
df=pd.DataFrame(data,columns=["name", "averageRentalRate"])
df.to_excel(r"D:\BSIT\Python libraries\reports\AverageRentalPercategory.xlsx")
print("File saved")