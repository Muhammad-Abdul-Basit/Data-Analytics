from dataBaseConnect import get_connection
import pandas as pd
conn=get_connection()
cursor=conn.cursor()
cursor.execute("""
                select c.name, count(f.film_id) AS Total_Film from category c JOIN
                film_category fc ON 
                fc.category_id=c.category_id
                JOIN film f ON f.film_id=fc.film_id
                group by c.name
                order by Total_Film desc
            """)
data=cursor.fetchall()
dataFile=pd.DataFrame(data, columns=["Movie Category", " Total Movies"])
dataFile.to_excel(r"D:\BSIT\Python libraries\Data-Analytics\reports\moviesperCategory.xlsx", index=False)
print("File Saved")
cursor.close()
conn.close()