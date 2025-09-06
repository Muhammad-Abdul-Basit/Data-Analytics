from dataBaseConnect import get_connection
conn=get_connection()
cursor=conn.cursor()
cursor.execute("select count(*) AS totalFilms from film")
totalMovies=cursor.fetchone()
print("Total movoes in the table is : ", totalMovies[0])