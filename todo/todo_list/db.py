import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'barezia12',
    auth_plugin = 'mysql_native_password'
)

cursorObject = db.cursor()


cursorObject.execute("CREATE DATABASE Users")

print("Database created!")