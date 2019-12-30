import os
import time
import getpass
from sys import argv

os.system("clear")

Pass = None
Aux = 1
Aux2 = 2

class APT():

    def Update(self, Pass):

        if(Pass is None):
            os.system("sudo apt update")
        else:
            os.system("echo "+Pass+" | sudo -S apt update")

    def Upgrade(self, Pass):
        if(Pass is None):
            os.system("sudo apt upgrade")
        else:
            os.system("echo "+Pass+" | sudo -S apt upgrade -y")

    def FullUPUG(self, Pass):
        self.Update(Pass)
        self.Upgrade(Pass)


class CP():

    def CopyFile(self,Pass):

        if(Pass is None):
            print(StyleText['info']+"\nCurrent file path")
            os.system("pwd")
            
            NamePathFile = input(StyleText['question']+"\nEnter the path and name of the file\nR= ")

            if(os.path.exists(NamePathFile)):
                NewPath = input(StyleText['question']+"\nEnter path to copy\nR= ")
                if(os.path.exists(NewPath)):
                    os.system("sudo -S cp "+NamePathFile+" "+NewPath)
                else:
                    print(StyleText['question']+"Ruta no encontrada")
            else:
                print(StyleText['question']+"Archivo no encontrado")

        else:
            print(StyleText['info']+"\nCurrent file path")
            os.system("pwd")
            
            NamePathFile = input(StyleText['question']+"\nEnter the path and name of the file\nR= ")

            if(os.path.exists(NamePathFile)):
                NewPath = input(StyleText['question']+"\nEnter path to copy\nR= ")
                if(os.path.exists(NewPath)):
                    os.system("echo "+Pass+" | sudo -S cp "+NamePathFile+" "+NewPath)
                else:
                    print(StyleText['question']+"Ruta no encontrada")
            else:
                print(StyleText['question']+"Archivo no encontrado")

    def CopyFolder(self,Pass):
        if(Pass is None):
            print(StyleText['info']+"\nCurrent file path")
            os.system("pwd")
            
            NamePathFile = input(StyleText['question']+"\nEnter the path and name of the folder\nR= ")

            if(os.path.exists(NamePathFile)):
                NewPath = input(StyleText['question']+"\nEnter path to copy\nR= ")
                if(os.path.exists(NewPath)):
                    os.system("sudo -S cp -r "+NamePathFile+" "+NewPath)
                else:
                    print(StyleText['question']+"Ruta no encontrada")
            else:
                print(StyleText['question']+"Archivo no encontrado")
        else:
            print(StyleText['info']+"\nCurrent file path")
            os.system("pwd")
            
            NamePathFile = input(StyleText['question']+"\nEnter the path and name of the folder\nR= ")

            if(os.path.exists(NamePathFile)):
                NewPath = input(StyleText['question']+"\nEnter path to copy\nR= ")
                if(os.path.exists(NewPath)):
                    os.system("echo "+Pass+" | sudo -S cp -r "+NamePathFile+" "+NewPath)
                else:
                    print(StyleText['question']+"Ruta no encontrada")
            else:
                print(StyleText['question']+"Archivo no encontrado")


class PIP():

    def Install(self, Pass):       
        if Pass is None:

            Package = input("Enter package name\nR= ")

            os.system("pip install "+Package)
        else:

            Package = input("Enter package name\nR= ")

            os.system("echo "+Pass+" | sudo pip install "+Package)

    def Uninstall(self, Pass):
        if Pass is None:

            Package = input("Enter package name\nR= ")

            os.system("pip uninstall "+Package)
        else:

            Package = input("Enter package name\nR= ")

            os.system("echo "+Pass+" | sudo pip uninstall "+Package)
        

class WebServer():

    def ServerDisable(self,Pass):
        os.system("echo "+Pass+" | sudo -S service apache2 stop && service mysql stop")

    def ServerEnable(self, Pass):
        os.system("echo "+Pass+" | sudo -S service apache2 start && service mysql start")


apt = APT()
cp = CP()
pip = PIP()
ws = WebServer()

NameASCII = ('##########################','#  ____    ____     ____ #', '# |  _ \  |  _ \   / ___|#', '# | | | | | | | | | |  _ #', '# | |_| | | |_| | | |_| |#','# |____/  |____/   \____|#','##########################','\nBasic Automatication for linux\n')
ListFunction = {1:{0:'1.- APT',1:'\t1.- Update system', 2:'\t2.- Upgrade system', 3:'\t3.- Update & Upgrade System'},
                2:{0:'\n2.- CP', 1:'\t1.- Copy file', 2:'\t2.- Copy folder'},
                3:{0:'\n3.-PIP', 1:'\t1.- Install package', 2:'\t2.- Uninstall package'},
                4:{0:'\n4.- WEB server', 1:'\t1.- Initialize local server', 2:'\t2.- Stop local server'}}
ListAction = {1:{1:apt.Update, 2:apt.Upgrade, 3:apt.FullUPUG},
              2:{1:cp.CopyFile, 2:cp.CopyFolder},
              3:{1:pip.Install, 2:pip.Uninstall},
              4:{1:ws.ServerEnable, 2:ws.ServerDisable}}
ListSpecialArg = ('-r','-s') #-r Root | -s Sequence
StyleText = {'main':"\x1b[1;33m", 'name':"\x1b[1;31m", 'complete':"\x1b[1;32m", 'fail':"\x1b[1;31m", 'question':"\x1b[1;34m",'info':"\x1b[1;36m"}


if len(argv) > 1:
    while(Aux < len(argv)):
        if(argv[Aux] in ListSpecialArg and argv[Aux].find("-") == 0):
            if(argv[Aux] == ListSpecialArg[0]):
                Pass = argv[Aux+1]
            elif(argv[Aux] == ListSpecialArg[1]):               
                sequence = list(map(int, str(argv[Aux+1])))
                ListAction[sequence[0]][sequence[1]](Pass)
                print(StyleText['complete']+"\nCOMPLETE TASK!!\n") 
                time.sleep(2)
        else:
            print(StyleText['fail']+"Argumento invalido")
            time.sleep(2)
            os.system('clear')

        if(Aux2 < len(argv)):
            Aux+=2
            Aux2+=2
        else:
            break


while(True):

    MenuSelection = []

    for i in NameASCII:
        print(StyleText['name']+i)

    for i in ListFunction:
        for a in range(len(ListFunction[i])):
            print(StyleText['main']+ListFunction[i][a])
        
    if(Pass is None):
        accessroot = int(input(StyleText['question']+"\nDo you want to execute commands like root? 1:Yes 2:No\nR= "))

        if(accessroot == 1):
            Pass = getpass.getpass("Enter your password\nR= ")
            accessroot = 0


    MenuSelection.append(int(input(StyleText['question']+"\nwhat command do you want to use?\nR = ")))

    if(MenuSelection[0] in ListFunction):

        os.system("clear")

        for i in range(len(ListFunction[MenuSelection[0]])):
            print(StyleText['main']+ListFunction[MenuSelection[0]][i])

        MenuSelection.append(int(input(StyleText['question']+"\nwhat action do you want to perform?\nR = ")))

        ListAction[MenuSelection[0]][MenuSelection[1]](Pass)

        print(StyleText['complete']+"\nCOMPLETE TASK!!\n") 

        time.sleep(2)
            
    else:
        os.system("clear")
        pass