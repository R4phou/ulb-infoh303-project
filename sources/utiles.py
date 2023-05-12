import mysql.connector as mysql
import xml.etree.ElementTree as etree
import numpy as np

"""Exécute une seule requête SQL et renvoie son résultat"""


def execute_query(cursor, query):
    result = cursor.execute(query)
    # print("Query executed successfully")
    return result


def execute_requete(file):
    db = get_connection(False)
    print("Successfully connected to MySQL")
    # Créer le curseur qui permet de faire des queries et commandes SQL
    c = db.cursor()
    try:
        requete = open(file, "r").read()
        c.execute(requete)
        result = ""
        i = 0
        for elem in c:
            i += 1
            result += str(i) + " | " + str(elem) + "<br>"
        result = str(i) + " éléments ont été sélectionnés <br>" + result
    except:
        result = "Erreur lors de l'exécution de la requête"
    return result


"""Exécute une liste de requêtes SQL et renvoie leurs résultats"""


def execute_queries(cursor, queries):
    result_list = []
    for query in queries:
        result_list.append(execute_query(cursor, query))
        print(query + " executed successfully")
    return result_list


"""
Récupère une connexion à la base de données MySQL
Args: isFirstTime (bool):
    True si c'est la première fois qu'on se connecte à la base de données, 
    False sinon.
"""


def get_connection(isFirstTime):
    if isFirstTime:
        # Connexion à la base de données MySQL pour la première fois
        db = mysql.connect(
            host="localhost",
            user="root",
            # old password="ZQ$G7ZWr;b|rD]B",
            passwd="root",
        )
        return db
    else:
        # Connexion à la base de données MySQL après la création de "systeme_medical"
        db = mysql.connect(
            host="localhost",
            user="root",
            # old password="ZQ$G7ZWr;b|rD]B",
            passwd="root",
            database="systeme_medical",
        )
        return db


"""
Sauvegarde les changements et met fin à la connexion au serveur MySQL
"""


def close_db(db, cursor):
    # Fermeture de la connexion
    db.commit()
    cursor.close()
    db.close()


"""
Récupère le contenu du fichier XML et le renvoie sous forme d'objet ElementTree
Returns: la racine de l'arbre XML
"""


def load_xml_file(path):
    with open(path, encoding="utf-8") as f:
        data = f.read()
        # Ajout d'une balise root pour que le fichier XML soit valide
        # (Etree n'attend qu'1 seul noeud à la racine)
        formated_data = "<root>" + data + "</root>"
        return etree.fromstring(formated_data)


def load_csv_file(path, skip):
    return np.loadtxt(path, delimiter=",", dtype=str, skiprows=skip, encoding="utf-8")


def get_data_as_dictionary(patient):
    dictionnary_patient = {}
    for attribute in patient:
        value = attribute.text
        if value == None:
            value = "NULL"
        if attribute.tag in dictionnary_patient:
            dictionnary_patient[attribute.tag].append(value)
        else:
            dictionnary_patient.update({attribute.tag: [value]})
    return dictionnary_patient


def get_data_as_dictionary_csv(ligne, columns):
    return {columns[i]: ligne[i] for i in range(len(columns))}


# Passe d'un format j/m/a à a-m-j


def format_to_date(date):
    reversed_date = "-".join(date.split("/")[::-1])
    sql_date = "str_to_date('" + date + "','%m/%d/%Y')"
    return sql_date


# Transforme une liste de valeurs en String de la forme "'v1','v2','v3',..."
# Les guillemets ne sont pas mis pour les arguments de type date formattés avec format_to_date


def values_to_str(value):
    result = ""
    for i in range(len(value)):
        arg = value[i]
        if "str_to_date" in str(arg):
            result += str(arg)
        else:
            result += '"' + str(arg) + '"'
        if i != len(value) - 1:
            result += ","
    return result

"""
Transforme un dictionnaire de la forme
    {key1 : [a,b,c], key2 : [d,e,f]} 
 en une liste de dictionnaires de la forme
    [{'key1': 'a', 'key2': 'd'}, {'key1': 'a', 'key2': 'e'}, {'key1': 'a', 'key2': 'f'},
      {'key1': 'b', 'key2': 'd'}, {'key1': 'b', 'key2': 'e'}, {'key1': 'b', 'key2': 'f'},
        {'key1': 'c', 'key2': 'd'}, {'key1': 'c', 'key2': 'e'}, {'key1': 'c', 'key2': 'f'}]
"""
def flatMapping(dico):
    #item: {key1 : [a,b,c], key2 : [d,e,f]}
    result = []
    matrixValues = []
    #Crée une matrice avec les valeurs
    for key in dico.keys():
        matrixValues.append(dico[key])
    
    depth = len(matrixValues)
    result = []
    recursive_flatening(matrixValues,depth,0,list(dico.keys()),result)
    return result
    #return ({key1 : a, key2 : d}, {key1 : b, key2 : e}, {key1 : c, key2 : f})

"""fonction récursive utilisée lors de la création de la liste de dictionnaires"""
def recursive_flatening(matrix,maxDepht,currentDepth,keyList,listDicos,memoDico = {}):
    if currentDepth >= maxDepht:
        listDicos.append(memoDico.copy())
        return
    else:
        for i in range(len(matrix[currentDepth])):
            #print(matrix[currentDepth][i])
            memoDico.update({keyList[currentDepth] : matrix[currentDepth][i]})
            recursive_flatening(matrix,maxDepht,currentDepth+1,keyList,listDicos,memoDico)

def recombinate():
    pass

if __name__ == "__main__":
    print("This file is not meant to be executed")
    #print(load_csv_file("Données/dossiers_patients.csv"))
    dicotTest = {'key1' : ['a','b','c'], 'key2' : ['d','e','f','g'],'key3' : ['h','i','j']}
    print(flatMapping(dicotTest))
