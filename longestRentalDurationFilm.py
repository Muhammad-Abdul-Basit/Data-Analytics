from dataBaseConnect import get_connection
conn=get_connection()
cursor=conn.cursor()
cursor.execute("SELECT title from film order by rental_duration desc limit 10;")
top10Movies=cursor.fetchall()
for (i,) in top10Movies:
    print(i)