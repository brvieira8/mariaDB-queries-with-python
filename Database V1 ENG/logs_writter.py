from printSplash import getDateTime
import logging
import os


name_logs = "logs.logs"

def verificator():
    global name_logs
    check_file = str(os.path.isfile(name_logs))
    if check_file == "True":
        print("The file " + name_logs + " its working")
        
    else: 
        open(name_logs,'w')
        print(name_logs + " has been created")
        getDateTime()
        nowMomentTime = getDateTime()
        logging.basicConfig(filename=name_logs, encoding='utf-8', level= logging.INFO)
        logging.info(nowMomentTime + " - The logs files has been created")









