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

# Importacion de archivos externos
import Style
import Functions

# Importacion de elementos de python
import time
import getpass
import threading
import subprocess
from sys import argv, getdefaultencoding

# Ruta principal de componentes
PATH = "/"

# Creacion de instancias de funciones.
cp  = Functions.CP()
apt = Functions.APT()
pip = Functions.PIP()
ps  = Functions.Special()
ws  = Functions.WebServer()

# Creacion de una tupla para el nombre del script.
NameASCII = ('     ___       __       _______ ','    /   \     |  |     |   ____|','   /  ^  \    |  |     |  |__   ','  /  /_\  \   |  |     |   __|  ',' /  _____  \  |  `----.|  |____ ','/__/     \__\ |_______||_______|','\n Automation for Linux Enhanced\n')

# Creacion de un diccionario para el menu de funciones del sistema.
MenuListFunction = {1:{0:'1.- APT',1:'\t1.- Update system', 2:'\t2.- Upgrade system', 3:'\t3.- Update & Upgrade System\n'},
                    2:{0:'2.- CP', 1:'\t1.- Copy file', 2:'\t2.- Copy folder\n'},
                    3:{0:'3.- PIP', 1:'\t1.- Install package', 2:'\t2.- Uninstall package\n'},
                    4:{0:'4.- WEB server', 1:'\t1.- Initialize local server', 2:'\t2.- Stop local server\n'},
                    5:{0:'5.- ALE special menu', 1:'\t1.- Change password\n'}}

# Creacion de un diccionario el cual contendra las funciones disponibles para ser llamadas durante la ejecucion del script.
ListAction = {1:{1:apt.Update, 2:apt.Upgrade, 3:apt.FullUPUG},
              2:{1:cp.File, 2:cp.Folder},
              3:{1:pip.Install, 2:pip.Uninstall},
              4:{1:ws.ServerEnable, 2:ws.ServerDisable},
              5:{1:ps.ChangePass}}

# Creacion de una tupla la cual contendra los argumentos disponibles.
ListSpecialArg = ('-r','-s')

# Iniciamos el script limpiando la pantalla de la terminal
subprocess.call(['clear'])

# Variable que contendra la contrasena del usuario durante la ejecucion del script
Pass = None

# Variables auxiliares
Aux = 1
Aux2 = 2

# Verifica si se incio del script con el uso de argumentos, de ser asi iniciara la secuencia dada

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
                    subprocess.call(['clear'])                 
            else:

                print(Style.Text['fail']+"There is an invalid argument")
                time.sleep(2)
                subprocess.call(['clear'])

            if(Aux2 < len(argv)):
                Aux+=2
                Aux2+=2
            else:
                break
    except ValueError:
        print(Style.Text['fail']+"\nENTER NUMBERS ONLY")
        time.sleep(2)
        subprocess.call(['clear']) 

# Inicia la ejecucion del script en un ciclo infinito
while(True):

    # Variable que nos permitira guardar la serie de combinaciones para ejecturar las funciones que se encuntran en la variable 'ListFunction'
    MenuSelection = []

    try:

        # Imprime el nombre del script asi como el menu de funciones
        for i in NameASCII:
            print(Style.Text['name']+i)

        for i in MenuListFunction:
            for a in range(len(MenuListFunction[i])):
                print(Style.Text['main']+MenuListFunction[i][a])

        # Solicita la contrasena del usuario para los comandos que asi lo requieran
        if(Pass is None):
            Pass = getpass.getpass(Style.Text['question']+"\nPlease enter your password or leave the field empty\nR=")
            if(Pass == ''):
                Pass = None

        # Agrega el valor correspondiente al comando principal
        MenuSelection.append(int(input(Style.Text['question']+"\nwhat command do you want to use?\nR = ")))

        # Comapara que el valor introducido exista en MenuListFunction
        if(MenuSelection[0] in MenuListFunction):
            subprocess.call(['clear'])

            # Muestra el listado de funciones disponibles
            for i in range(len(MenuListFunction[MenuSelection[0]])):
                print(Style.Text['main']+MenuListFunction[MenuSelection[0]][i])

            # Agrega el valor correspondiente a la funcion que se deasea utilziar
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
            subprocess.call(['clear'])

    except ValueError:
        print(Style.Text['fail']+"\nENTER NUMBERS ONLY")
        time.sleep(2)
        subprocess.call(['clear'])