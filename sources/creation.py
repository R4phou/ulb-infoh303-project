import mysql.connector

# Se connecter au serveur MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ZQ$G7ZWr;b|rD]B",
    auth_plugin='mysql_native_password',
)


print("Successfully connected to MySQL server")


# # Créer une base de données
# cursor = conn.cursor()
# cursor.execute("CREATE DATABASE ma_base_de_donnees")
