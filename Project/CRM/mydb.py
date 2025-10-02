import pymysql

dataBase = pymysql.connect(
    host="localhost",
    user="root",
    password="Rahe@$SQL"
)

cursorObject = dataBase.cursor()
cursorObject.execute("CREATE DATABASE mydatabase")
print("All Done!")
