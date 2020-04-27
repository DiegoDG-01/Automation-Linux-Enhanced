import os
import time
import getpass
import subprocess
from sys import getdefaultencoding

class APT():

    def Update(self, Pass, StyleText):

        if(Pass is None):
            print(StyleText['fail']+"\nTO USE APT PASSWORD IS REQUIRED")
            time.sleep(2)
            return False
        else:
            echo = subprocess.Popen(['echo', Pass], stdout=subprocess.PIPE)
            process = subprocess.Popen(#FLAG#, stdin=echo.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        Out, Err = process.communicate()

        return Out, Err

    def Upgrade(self, Pass, StyleText):

        if(Pass is None):
            print(StyleText['fail']+"TO USE APT PASSWORD IS REQUIRED")
            time.sleep(2)
            return False
        else:
            echo = subprocess.Popen(['echo', Pass], stdout=subprocess.PIPE)
            process = subprocess.Popen(#FLAG#, stdin=echo.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        Out, Err = process.communicate()

        return Out, Err

    def FullUPUG(self, Pass, StyleText):   
        result = self.Update(Pass, StyleText)

        Err = result[1].decode(getdefaultencoding()).strip()

        ErrSudo = Err.find("sudo")

        if(ErrSudo == 1):
            Err = ''

        if(Err == ''):
            result = self.Upgrade(Pass, StyleText)
            return result
        else:
            return result


class CP():

    def File(self,Pass,StyleText):

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


    def Folder(self, Pass, StyleText):

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

class Special():

    def ChangePass(self, Pass, StyleText):

        Pass = getpass.getpass(StyleText['question']+"\nPlease enter your new password\nR=")

        return Pass