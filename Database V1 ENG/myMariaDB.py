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
        print("\nConection established sucessfully!\n")

              

    except mariadb.Error as error:
        print(f"\nError while conecting to MariaDB platform: {error}")
        getDateTime()
        nowMomentTime = getDateTime()
        logging.critical(nowMomentTime + " - Error while connecting to database \n  Error -  %s " , error )
        logging.info(nowMomentTime + "The program has been shutdown due to a critical error")
        print("\nSince you have a error while connecting to database, the program will shutdown in 5 seconds")
        sleep(5)
        quit()

    return(" ")

#***************************************************************************

def disconnect():
    global conn
    conn.close
    print("\nDisconnected with sucess!\n")


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
        logging.error(nowMomentTime + " - Error while executing the query - %s", e )
        
        
    return(" ")

def log_program_started():
    getDateTime()
    nowMomentTime = getDateTime()
    logging.info(nowMomentTime + " - The program has been started")

def log_program_ended():
    getDateTime()
    nowMomentTime = getDateTime()
    logging.info(nowMomentTime + " - The program has been run sucessfully")
    
