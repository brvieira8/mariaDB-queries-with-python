from printSplash import getDateTime
import logging
import os


name_logs = "logs.logs"

def verificador():
    global name_logs
    check_file = str(os.path.isfile(name_logs))
    if check_file == "True":
        print("O ficheiro " + name_logs + " está funcional")
        
    else: 
        open(name_logs,'w')
        print(name_logs + " foi criado")
        getDateTime()
        nowMomentTime = getDateTime()
        logging.basicConfig(filename=name_logs, encoding='utf-8', level= logging.INFO)
        logging.info(nowMomentTime + " - O ficheiro logs foi criado")









