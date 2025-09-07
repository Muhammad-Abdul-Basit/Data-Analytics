import pandas as pd
from dataBaseConnect import get_connection
conn=get_connection()
cursor=conn.cursor()
cursor.execute(""" select a.first_name, a.last_name, COUNT(a.first_name) AS ApearsInMovies from actor a JOIN 
                film_actor fc ON fc.actor_id=a.actor_id JOIN
                film f ON f.film_id=fc.film_id
                Group BY a.first_name, a.last_name
                Having ApearsInMovies >= 35
                Order by ApearsInMovies desc 
               """)
data=cursor.fetchall()
df=pd.DataFrame(data, columns=["First Name", "Last Name","ApearsInMovies"])
df["Full Name"]=df["First Name"]+" "+df["Last Name"]
df=df[["Full Name", "ApearsInMovies"]]
df.to_excel(r"D:\BSIT\Python libraries\Data-Analytics\reports\actorApearsInMovies.xlsx",index=False)
print(" File saved")
cursor.close()
conn.close()