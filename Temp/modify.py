import json
from sys import argv

if len(argv) > 1:

    path = '/home/'+argv[2]+"/Basic-Automatication-for-linux"

    try:
        with open(path+'/Temp/Commands.json') as file:
            commands = json.load(file)

        funtionsIn = open(path+"/Temp/Functions_Temp.py", "rt")
        funtionsOut = open(path+"/Functions.py", "wt")

        for line in funtionsIn:
            funtionsOut.write(line.replace("#FLAG#", str(commands[argv[1]]['update'].split())))

        funtionsIn.close()
        funtionsOut.close()

        print(True)
    except FileNotFoundError:
        print("False")
    except NameError:
        print("False")
else:
    print("False")