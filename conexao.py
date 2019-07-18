import mysql.connector

# Conectando com o banco. alterar user ,password e port conforme o banco;
def connexao():
    user = "root"
    password = "password"
    host = "localhost"
    db = "Agenda"
    port = "3306"
    try:
        return mysql.connector.connect(user=user,password=password,host=host,database=db,port=port) # Realizar conexão
    except Exception as e:
        print(e)
