import mysql.connector

"""Exécute une seule requête SQL et renvoie son résultat"""
def execute_query(cursor,query):
    result = cursor.execute(query)
    print("Query executed successfully")
    return result

"""Exécute une liste de requêtes SQL et renvoie leurs résultats"""
def execute_queries(cursor,queries):
    result_list = []
    for query in queries:
        result_list.append(execute_query(cursor,query))
    return result_list

"""
Récupère une connexion à la base de données MySQL
Args: isFirstTime (bool):
    True si c'est la première fois qu'on se connecte à la base de données, 
    False sinon.
"""
def get_connection(isFirstTime):
    if isFirstTime:
        #Connexion à la base de données MySQL pour la première fois
        db = mysql.connector.connect(
        host="localhost",
        user="root",
        # old password="ZQ$G7ZWr;b|rD]B",
        passwd="root")
        return db
    else:
        #Connexion à la base de données MySQL après la création de "systeme_medical"
        db = mysql.connector.connect(
        host="localhost",
        user="root",
        # old password="ZQ$G7ZWr;b|rD]B",
        passwd="root",
        database="systeme_medical")
        return db

def close_db(db,cursor):
    # Fermeture de la connexion
    db.commit()
    cursor.close()
    db.close()