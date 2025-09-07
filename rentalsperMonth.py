from dataBaseConnect import get_connection
import pandas as pd
conn=get_connection()
cursor=conn.cursor()
cursor.execute("""
                    select MONTHName(rental_date) AS rentalMonth,
                    count(*) AS TotalRentals from rental
                    Where year(rental_date)=2005
                    group by rentalMonth
                    order by rentalMonth
                    """)
data=cursor.fetchall()
dataFile=pd.DataFrame(data, columns=["Rental Month", "Total Rentals"])
dataFile.to_excel(r"D:\BSIT\Python libraries\Data-Analytics\reports\rentalsperMonth.xlsx",index=False)
print("File saved")