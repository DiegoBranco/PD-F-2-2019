#importamos el modulo OS para crear carpetas
import os
#importamos el modulo JSON para interactuar con el archivo de configuracion
import json


class ComputerInstaller:
    def __init__(self):
        super().__init__()
        self.operatingSystem = so.upper()
        self.machineID = mid

        
    def checkOS(self):
        if(operatingSystem == "WINDOWS"):
            print("El sistema operativo esta basado en Windows.")
        else:
            if(operatingSystem == "LINUX"):
                print("El sistema operativo esta basado en Linux.")
            else:
                print("Este Sistema Operativo no esta soportado.")

    def getMachineID(self):
        print("El id de la maquina es: "+machineID)

    def startDecorator(self, so):
        return 0

#variable que muestra ciertas impresiones para facilitar el debug
debug = 0
path = os.getcwd()

with open('config.json') as config:
    info = json.load(config)
    so = info['osys']
    mid = info['machineID']    

if debug:
    print ("[DEBUG] Estas en: "+path)
    print ("[DEBUG] el os es: "+ so)
    print ("[DEBUG] el ID es: "+ mid)
 



