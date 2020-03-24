###########################################################
###########################################################
##                                                       ##
##             ,ggg,            ,gggg,      ,ggggggg,    ## 
##            dP""8I           d8" "8I    ,dP""""""Y8b   ##
##           dP   88           88  ,dP    d8'    a  Y8   ##
##          dP    88        8888888P"     88     "Y8P'   ##
##         ,8'    88           88         `8baaaa        ##
##         d88888888           88        ,d8P""""        ##
##   __   ,8"     88      ,aa,_88        d8"             ##
##  dP"  ,8P      Y8     dP" "88P        Y8,             ##
##  Yb,_,dP       `8b,   Yb,_,d88b,,_    `Yba,,_____,    ##
##   "Y8P"         `Y8    "Y8P"  "Y88888`   "Y8888888    ##
##                                                       ##
##                          SCRIPT <3                    ##
###########################################################
###########################################################

import os
import time
import Style
import getpass
import Functions
import subprocess
from sys import argv, getdefaultencoding

os.system("clear")

Pass = None
Aux = 1
Aux2 = 2

apt = Functions.APT()
cp = Functions.CP()
pip = Functions.PIP()
ws = Functions.WebServer()

NameASCII = ('     ___       __       _______ ','    /   \     |  |     |   ____|','   /  ^  \    |  |     |  |__   ','  /  /_\  \   |  |     |   __|  ',' /  _____  \  |  `----.|  |____ ','/__/     \__\ |_______||_______|','\n Automation for Linux Enhanced\n')

ListFunction = {1:{0:'1.- APT',1:'\t1.- Update system', 2:'\t2.- Upgrade system', 3:'\t3.- Update & Upgrade System'},
                2:{0:'\n2.- CP', 1:'\t1.- Copy file', 2:'\t2.- Copy folder'},
                3:{0:'\n3.-PIP', 1:'\t1.- Install package', 2:'\t2.- Uninstall package'},
                4:{0:'\n4.- WEB server', 1:'\t1.- Initialize local server', 2:'\t2.- Stop local server'}}

ListAction = {1:{1:apt.Update, 2:apt.Upgrade, 3:apt.FullUPUG},
              2:{1:cp.File, 2:cp.Folder},
              3:{1:pip.Install, 2:pip.Uninstall},
              4:{1:ws.ServerEnable, 2:ws.ServerDisable}}

ListSpecialArg = ('-r','-s')


if len(argv) > 1:

    try:
        while(Aux < len(argv)):

            if(argv[Aux] in ListSpecialArg and argv[Aux].find("-") == 0):

                if(argv[Aux] == ListSpecialArg[0]):
                    Pass = argv[Aux+1]

                elif(argv[Aux] == ListSpecialArg[1]):   

                    sequence = list(map(int, str(argv[Aux+1])))

                    result = ListAction[sequence[0]][sequence[1]](Pass,Style.Text)

                    if(isinstance(result, bool)):
                        if(result == False):
                            Err = ' '
                    else:
                        Out = result[0].decode(getdefaultencoding()).strip()
                        Err = result[1].decode(getdefaultencoding()).strip()

                        ErrSudo = Err.find("sudo")

                        if(ErrSudo == 1):
                            Err = ''

                    if(Err != ''):
                        print(Err)
                        print(Style.Text['fail']+"\nERROR COMPLETING TASK!!\n")                
                    else:
                        print(Out)
                        print(Style.Text['complete']+"\nCOMPLETE TASK!!\n")

                    time.sleep(2)
                    os.system("clear")                 
            else:

                print(Style.Text['fail']+"There is an invalid argument")
                time.sleep(2)
                os.system('clear')

            if(Aux2 < len(argv)):
                Aux+=2
                Aux2+=2
            else:
                break
    except ValueError:
        print(Style.Text['fail']+"\nENTER NUMBERS ONLY")
        time.sleep(2)
        os.system("clear") 


while(True):

    MenuSelection = []

    try:
        for i in NameASCII:
            print(Style.Text['name']+i)

        for i in ListFunction:
            for a in range(len(ListFunction[i])):
                print(Style.Text['main']+ListFunction[i][a])
            
        if(Pass is None):
            accessroot = int(input(Style.Text['question']+"\nDo you want to execute commands like root? 1:Yes 2:No\nR= "))

            if(accessroot == 1):
                Pass = getpass.getpass("Enter your password\nR= ")
                accessroot = 0

        MenuSelection.append(int(input(Style.Text['question']+"\nwhat command do you want to use?\nR = ")))

        if(MenuSelection[0] in ListFunction):

            os.system("clear")

            for i in range(len(ListFunction[MenuSelection[0]])):
                print(Style.Text['main']+ListFunction[MenuSelection[0]][i])

            MenuSelection.append(int(input(Style.Text['question']+"\nwhat action do you want to perform?\nR = ")))

            result = ListAction[MenuSelection[0]][MenuSelection[1]](Pass, Style.Text)

            if(isinstance(result, bool)):
                if(result == False):
                    Err = ' '
            else:
                Out = result[0].decode(getdefaultencoding()).strip()
                Err = result[1].decode(getdefaultencoding()).strip()

                ErrSudo = Err.find("sudo")

                if(ErrSudo == 1):
                    Err = ''

            if(Err != ''):
                print(Err)
                print(Style.Text['fail']+"\nERROR COMPLETING TASK!!\n")                
            else:
                print(Out)
                print(Style.Text['complete']+"\nCOMPLETE TASK!!\n") 

            time.sleep(2)
            os.system("clear")
    except ValueError:
        print(Style.Text['fail']+"\nENTER NUMBERS ONLY")
        time.sleep(2)
        os.system("clear")            