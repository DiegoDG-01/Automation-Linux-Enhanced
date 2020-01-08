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
            print(StyleText['fail']+"\nTO USE APT PASSWORD IS REQUIRED")
            time.sleep(2)
            return False
        else:
            echo = subprocess.Popen(['echo', Pass], stdout=subprocess.PIPE)
            process = subprocess.Popen(['sudo', '-S','apt-get','update'], stdin=echo.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        Out, Err = process.communicate()

        return Out, Err

    def Upgrade(self, Pass):

        if(Pass is None):
            print(StyleText['fail']+"TO USE APT PASSWORD IS REQUIRED")
            time.sleep(2)
            return False
        else:
            echo = subprocess.Popen(['echo', Pass], stdout=subprocess.PIPE)
            process = subprocess.Popen(['sudo', '-S','apt-get','upgrade'], stdin=echo.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        Out, Err = process.communicate()

        return Out, Err

    def FullUPUG(self, Pass):   
        result = self.Update(Pass)

        Err = result[1].decode(getdefaultencoding()).strip()

        ErrSudo = Err.find("sudo")

        if(ErrSudo == 1):
            Err = ''

        if(Err == ''):
            result = self.Upgrade(Pass)
            return result
        else:
            return result


class CP():

    def File(self,Pass):

        print(StyleText['info']+"\nCurrent file path:")
        subprocess.call(["pwd"])

        print(StyleText['info']+"\nDirectory tree:")
        subprocess.call(["ls", '-1lF'])

        NamePathFile = input(StyleText['question']+"\nEnter the path and name of the file\nR= ")

        if(os.path.exists(NamePathFile)):

            NewPath = input(StyleText['question']+"\nEnter path to copy\nR= ")
            
            if(os.path.exists(NewPath)):

                if(Pass is None):
                    process = subprocess.Popen(['cp', NamePathFile, NewPath], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                else:
                    echo = subprocess.Popen(['echo', Pass], stdout=subprocess.PIPE)
                    process = subprocess.Popen(['sudo', '-S','cp', NamePathFile, NewPath], stdin=echo.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

                Out, Err = process.communicate()

                return Out, Err
            else:
                print(StyleText['question']+"Folder not found")
                return False
        else:
            print(StyleText['question']+"File not found")
            return False


    def Folder(self,Pass):

        print(StyleText['info']+"\nCurrent file path:")
        subprocess.call(["pwd"])

        print(StyleText['info']+"\nDirectory tree:")
        subprocess.call(["ls", '-1lF'])

        NamePathFile = input(StyleText['question']+"\nEnter the path and name of the folder\nR= ")

        if(os.path.exists(NamePathFile)):

            NewPath = input(StyleText['question']+"\nEnter path tcdo copy\nR= ")

            if(os.path.exists(NewPath)):

                if(Pass is None):
                    process = subprocess.Popen(['cp', '-r', NamePathFile, NewPath], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                else:
                    echo = subprocess.Popen(['echo', Pass], stdout=subprocess.PIPE)
                    process = subprocess.Popen(['sudo', '-S','cp', '-r', NamePathFile, NewPath], stdin=echo.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

                Out, Err = process.communicate()

                return Out, Err
            else:
                print(StyleText['question']+"Path not found")
                return False
        else:
            print(StyleText['question']+"Folder not found")
            return False


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
StyleText = {'main':"\x1b[1;33m", 'name':"\x1b[1;31m", 'complete':"\x1b[1;32m", 'fail':"\x1b[1;31m", 'question':"\x1b[1;34m",'info':"\x1b[1;36m"}

ListFunction = {1:{0:'1.- APT',1:'\t1.- Update system', 2:'\t2.- Upgrade system', 3:'\t3.- Update & Upgrade System'},
                2:{0:'\n2.- CP', 1:'\t1.- Copy file', 2:'\t2.- Copy folder'},
                3:{0:'\n3.-PIP', 1:'\t1.- Install package', 2:'\t2.- Uninstall package'},
                4:{0:'\n4.- WEB server', 1:'\t1.- Initialize local server', 2:'\t2.- Stop local server'}}
ListAction = {1:{1:apt.Update, 2:apt.Upgrade, 3:apt.FullUPUG},
              2:{1:cp.File, 2:cp.Folder},
              3:{1:pip.Install, 2:pip.Uninstall},
              4:{1:ws.ServerEnable, 2:ws.ServerDisable}}
ListSpecialArg = ('-r','-s') #-r Root | -s Sequence


if len(argv) > 1:

    try:
        while(Aux < len(argv)):

            if(argv[Aux] in ListSpecialArg and argv[Aux].find("-") == 0):

                if(argv[Aux] == ListSpecialArg[0]):
                    Pass = argv[Aux+1]

                elif(argv[Aux] == ListSpecialArg[1]):   

                    sequence = list(map(int, str(argv[Aux+1])))

                    result = ListAction[sequence[0]][sequence[1]](Pass)

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
                        print(StyleText['fail']+"\nERROR COMPLETING TASK!!\n")                
                    else:
                        print(Out)
                        print(StyleText['complete']+"\nCOMPLETE TASK!!\n")

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
    except ValueError:
        print(StyleText['fail']+"\nENTER NUMBERS ONLY")
        time.sleep(2)
        os.system("clear") 


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

            result = ListAction[MenuSelection[0]][MenuSelection[1]](Pass)

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
                print(StyleText['fail']+"\nERROR COMPLETING TASK!!\n")                
            else:
                print(Out)
                print(StyleText['complete']+"\nCOMPLETE TASK!!\n") 

            time.sleep(2)
            os.system("clear")
    except ValueError:
        print(StyleText['fail']+"\nENTER NUMBERS ONLY")
        time.sleep(2)
        os.system("clear")            