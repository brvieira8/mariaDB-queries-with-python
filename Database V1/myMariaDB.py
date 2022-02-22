#Modulos
#Importamos o mysql.connector para poder estabelecer a ligação com a base de dados
#Importamos o modulo tabulate (pip install tabulate) que nos permitirá gerar tabelas para as queries solicitadas
#Importamos o sys para quando der erro na conexão, o programa se desligar
#from tkinter import E


import mysql.connector as mariadb
from tabulate import tabulate
from logs_writter import *
from time import sleep



#Variavel global, esta é uma lista com o objetivo de armazenar diferentes tipos de dados
conn = ""
#logging.basicConfig(filename=name_logs, encoding='utf-8', level= logging.INFO)
#***************************************************************************
#Definição da função connect que irá estabelecer a conexão a base de dados
#Recorremos a variavél global "conn" para guardar um objeto com os campos que nos permitem fazer a conexão
#Se a ligação for bem sucedida, receberá a mensagem "Conectado com sucesso!"
#Em caso de erro na conexão, é retornada a mensagem "Erro ao conectar com a Plataforma MariaDB"

def connect():

    try:
        #conecção com a base de dados
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
        logging.critical(nowMomentTime + " - Error while connecting to MariaDB Platform \n  Error -  %s " , error )
        logging.info(nowMomentTime + " Program has been shutdown due to a critical error")
        print("\nSince you had a problem while connecting to database, this program will close in 5 seconds")
        sleep(5)
        quit()

    return(" ")

#***************************************************************************
#Definição da função disconnect que termina a ligação à base de dados
#Recorremos à variavél global de conexão à base de dados
#Desligamos a sessão e é retornada a mensagem "Ligação terminada com sucesso!"

def disconnect():
    global conn
    conn.close
    print("\nLigação terminada com sucesso!\n")


#***************************************************************************
#Definição da função tabela que necessita de 2 parâmetros
#"query" que corresponde a query que vamos executar
#"headers" que corresponde ao título de cada coluna da respetiva query
def query_table(query, headers):
    global conn
    #cursor.execute vai executar a query escolhida
    #cursor.fetchall retorna as linhas da query solicitada
    cursor = conn.cursor()
    try:
        cursor.execute(query)
        result = cursor.fetchall()

        #numaling - Alinha o conteúdo da tabela à esquerda
        #floatfmt - Devolve floats com 0 casas decimais
        #tablefmt - Coloca a tabela no formato de grelha de acordo com a library de tabulate
        print(tabulate(result, headers, numalign="left", floatfmt=".0f", tablefmt="psql"))
        cursor.close()

    #Em caso de erro é devolvido o respetivo erro em string
    except mariadb.Error as e:
        myError = "Erro:" + str(e.args[0]) + " " + e.args[1]
        print(myError)
        getDateTime()
        nowMomentTime = getDateTime()
        logging.error(nowMomentTime + " - Error performing query - %s", e )
        
        
    return(" ")

def log_program_started():
    getDateTime()
    nowMomentTime = getDateTime()
    logging.info(nowMomentTime + " - Program has been started")

def log_program_ended():
    getDateTime()
    nowMomentTime = getDateTime()
    logging.info(nowMomentTime + " - Program has been run")
    
