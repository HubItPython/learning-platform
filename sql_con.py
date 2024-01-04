import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",  # Replace with your MySQL server host
  user="root",  # Replace with your MySQL username
  password="sunil kumar",  # Replace with your MySQL password
  database="db"  # Replace with the database name
)
if mydb:
    print("Connected")
else:
    print("failure")

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM tb")

# Fetch results
myresult = mycursor.fetchall()

for row in myresult:
  print(row)