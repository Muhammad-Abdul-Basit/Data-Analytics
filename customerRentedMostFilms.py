from dataBaseConnect import get_connection
import pandas as pd
conn=get_connection()
cursor=conn.cursor()
cursor.execute("""
                select concat( c.first_name,' ', c.last_name) AS full_name, 
                count(*) AS MoviesRented 
                from customer c JOIN
                rental r ON r.customer_id=c.customer_id
                group by full_name
                having MoviesRented>=35
                order by MoviesRented desc
               """
                )
data=cursor.fetchall()
dataFile=pd.DataFrame(data, columns=["Customer Name", " Movies Rented"])
dataFile.to_excel(r"D:\BSIT\Python libraries\Data-Analytics\reports\customerRentedMostFilms.xlsx",index=False)
print(" File Saved")
cursor.close()
conn.close()