import mysql.connector

mydb = mysql.connector.connect(
    host="localhost"
    ,user="root"
    ,password="cookr"
    ,database="cookr1"
)
a=input("Enter the dish:")
mycursor = mydb.cursor()

sql = "SELECT * FROM foodlist where Dish = %s"
mycursor.execute(sql,(a,))

myr=mycursor.fetchall()
for i in myr:
    print(i)