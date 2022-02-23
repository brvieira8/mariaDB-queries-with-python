#***************************************************************************

import mysql.connector as mariadb
from tabulate import tabulate
from logs_writter import *
from time import sleep

#***************************************************************************

conn = ""

#***************************************************************************

def connect():

    try:
        global conn
        conn = mariadb.connect(
            user="datawarehouse",
            password="datawarehouse",
            host="127.0.0.1",
            port=3307,
            database="datawarehouse"
        )
        print("\nConectado com sucesso!\n")

              

    except mariadb.Error as error:
        print(f"\nErro ao conectar com a Plataforma MariaDB: {error}")
        getDateTime()
        nowMomentTime = getDateTime()
        logging.critical(nowMomentTime + " - Erro enquanto conectava a base de dados mariaDB \n  Erro -  %s " , error )
        logging.info(nowMomentTime + " O programa foi encerrado devido a um erro crítico")
        print("\nDevido ao problema de conezão com a base de daos, este programa irá encerrar dentro de 5 segundos")
        sleep(5)
        quit()

    return(" ")

#***************************************************************************

def disconnect():
    global conn
    conn.close
    print("\nLigação terminada com sucesso!\n")


#***************************************************************************

def query_table(query, headers):
    global conn
    
    cursor = conn.cursor()
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        print(tabulate(result, headers, numalign="left", floatfmt=".0f", tablefmt="psql"))
        cursor.close()

    except mariadb.Error as e:
        myError = "Erro:" + str(e.args[0]) + " " + e.args[1]
        print(myError)
        getDateTime()
        nowMomentTime = getDateTime()
        logging.error(nowMomentTime + " - Errro ao executar a query - %s", e )
        
        
    return(" ")

def log_program_started():
    getDateTime()
    nowMomentTime = getDateTime()
    logging.info(nowMomentTime + " - O programa foi iniciado")

def log_program_ended():
    getDateTime()
    nowMomentTime = getDateTime()
    logging.info(nowMomentTime + " - O programa correu com sucesso")
    
