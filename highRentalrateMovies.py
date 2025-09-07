from dataBaseConnect import get_connection
import pandas as pd
conn=get_connection()
cursor=conn.cursor()
cursor.execute(
    """
    select title , rental_rate from film
    Where rental_rate>3.99
    Limit 10;
    """
)
data=cursor.fetchall()
dataFile=pd.DataFrame(data, columns=["Movie Title", "Total Rent"])
dataFile.to_excel(r"D:\BSIT\Python libraries\Data-Analytics\reports\highRentalrateMovies.xlsx",index=False)
print(" File saved")