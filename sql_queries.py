import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sunil kumar",
    database="db"
)

mycursor = mydb.cursor()

# Retrieving data
mycursor.execute("SELECT * FROM tb")
myresult = mycursor.fetchall()

# Inserting data
sql = "INSERT INTO tb (Name, Address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)
mydb.commit()

# Updating data
sql = "UPDATE tb SET Address = %s WHERE Name = %s"
val = ("New Street 54", "John")
mycursor.execute(sql, val)
mydb.commit()

# Deleting data
sql = "DELETE FROM tb WHERE name = %s"
val = ("John",)
mycursor.execute(sql, val)
mydb.commit()

# Creating a database
mycursor.execute("CREATE DATABASE mydatabase")

# Creating a table
mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

# Dropping a database
mycursor.execute("DROP DATABASE mydatabase")

# Dropping a table
mycursor.execute("DROP TABLE customers")

# Show all databases
mycursor.execute("SHOW DATABASES")

# Show all tables in a database
mycursor.execute("SHOW TABLES")

mydb.close()

