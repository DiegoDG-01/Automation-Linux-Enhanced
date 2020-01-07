import os
import time
import getpass
import subprocess
from sys import argv, getdefaultencoding

os.system("clear")

Pass = None
Aux = 1
Aux2 = 2

class APT():

    def Update(self, Pass):

        if(Pass is None):
            print(StyleText['fail']+"TO USE APT PASSWORD IS REQUIRED")
            time.sleep(2)
            return False
        else:
            echo = subprocess.Popen(['echo', Pass], stdout=subprocess.PIPE)
            process = subprocess.Popen(['sudo', '-S','apt-get','update'], stdin=echo.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        Out, Err = process.communicate()

        Out = Out.decode(getdefaultencoding()).strip()
        Err = Err.decode(getdefaultencoding()).strip()

        if(Err != ''):
            print(Err)

            return False
        else:
            print(Out)

            return True

    def Upgrade(self, Pass):

        if(Pass is None):
            print(StyleText['fail']+"TO USE APT PASSWORD IS REQUIRED")
            time.sleep(2)
            return False
        else:
            echo = subprocess.Popen(['echo', Pass], stdout=subprocess.PIPE)
            process = subprocess.Popen(['sudo', '-S','apt-get','upgrade'], stdin=echo.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        Out, Err = process.communicate()

        Out = Out.decode(getdefaultencoding()).strip()
        Err = Err.decode(getdefaultencoding()).strip()

        if(Err != ''):
            print(Err)

            return False
        else:
            print(Out)

            return True

    def FullUPUG(self, Pass):   
        result = self.Update(Pass)
        if(result == True):
            result = self.Upgrade(Pass)
            if(result == True):
                return True
            else:
                return False
        else:
            return False


class CP():

    def File(self,Pass):

        print(StyleText['info']+"\nCurrent file path")
        os.system("pwd")

        NamePathFile = input(StyleText['question']+"\nEnter the path and name of the file\nR= ")

        if(os.path.exists(NamePathFile)):

            NewPath = input(StyleText['question']+"\nEnter path to copy\nR= ")
            
            if(os.path.exists(NewPath)):

                if(Pass is None):
                    os.system("sudo -S cp "+NamePathFile+" "+NewPath)
                else:
                    os.system("echo "+Pass+" | sudo -S cp "+NamePathFile+" "+NewPath)
            else:
                print(StyleText['question']+"Ruta no encontrada")
        else:
            print(StyleText['question']+"Archivo no encontrado")


    def Folder(self,Pass):

        print(StyleText['info']+"\nCurrent file path")
        os.system("pwd")

        NamePathFile = input(StyleText['question']+"\nEnter the path and name of the folder\nR= ")

        if(os.path.exists(NamePathFile)):

            NewPath = input(StyleText['question']+"\nEnter path to copy\nR= ")

            if(os.path.exists(NewPath)):

                if(Pass is None):
                    os.system("sudo -S cp -r "+NamePathFile+" "+NewPath)
                else:
                    os.system("echo "+Pass+" | sudo -S cp -r "+NamePathFile+" "+NewPath)
            else:
                print(StyleText['question']+"Ruta no encontrada")
        else:
            print(StyleText['question']+"Folder no encontrado")


class PIP():

    def Install(self, Pass):       
        
        Package = input("Enter package name to install\nR= ")

        if Pass is None:
            os.system("pip install "+Package)
        else:
            os.system("echo "+Pass+" | sudo pip install "+Package)

    def Uninstall(self, Pass):
        
        Package = input("Enter package name to uninstall\nR= ")
        
        if Pass is None:
            os.system("pip uninstall "+Package)
        else:
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
              2:{1:cp.File, 2:cp.Folder},
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

                result = ListAction[sequence[0]][sequence[1]](Pass)

                if(result == True):
                    print(StyleText['complete']+"\nCOMPLETE TASK!!\n") 
                    time.sleep(2)
                    os.system("clear")
                else:
                    print(StyleText['fail']+"\nERROR COMPLETING TASK!!\n") 
                    time.sleep(2)
                    os.system("clear")                    
        else:

            print(StyleText['fail']+"There is an invalid argument")
            time.sleep(2)
            os.system('clear')

        if(Aux2 < len(argv)):
            Aux+=2
            Aux2+=2
        else:
            break


while(True):

    MenuSelection = []

    try:
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
    except ValueError:
        print(StyleText['fail']+"\nENTER NUMBERS ONLY")
        time.sleep(2)
        os.system("clear")            
    else:
        os.system("clear")
        pass