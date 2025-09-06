from dataBaseConnect import get_connection
import pandas as pd
conn=get_connection()
cursor=conn.cursor()
cursor.execute("""Select c.name AS category, Count(f.film_id) AS TotalMovies FROM
               category c JOIN film_category fc ON fc.category_id=c.category_id
               JOIN film f ON fc.film_id=f.film_id
               Group BY c.name
               ORDER BY TotalMovies desc""")
category=cursor.fetchall()
df=pd.DataFrame(category, columns=["category", "TotalMovies"])
df.to_excel(r"D:\BSIT\Python libraries\reports\categories_count.xlsx")
print("file saved")
for category, TotalMovies in category:
    print(category, " category has : ", TotalMovies)
cursor.close()
conn.close()
