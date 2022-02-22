from datetime import datetime
import os
import sys



#*****************************************************************************************
def getDateTime():
     now = datetime.now()  # current date and time
     date_time = now.strftime("%d/%m/%Y %H:%M:%S.%d")[:-3]
     return date_time

def printString( functionName , stringToPrint ):


     myString = "[" + getDateTime() + "]" + functionName + " " +stringToPrint
     print (myString)

def printSplash():

     _function_name = "[fn]" + "[printSplash]"

     os.system('cls' if os.name == 'nt' else 'clear')


     print ( "\n\n" )
     printString (_function_name,"***********************************************************************")
     printString ( _function_name,"System version is : " + sys.version )
     nowDateTime = getDateTime()
     printString ( _function_name,"Date and time is :" + nowDateTime )
     printString (_function_name,"***********************************************************************")
     print ( "\n" )
