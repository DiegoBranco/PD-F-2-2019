#importamos el modulo OS para crear carpetas
import os
#importamos el modulo JSON para interactuar con el archivo de configuracion
import json
#importamos ABC para usar clases abstractas
from abc import ABC, abstractmethod
#importamos shutils para copiar y pegar los iconos que representan los programas en si
import shutil
class ProgramInstaller(ABC):
    @abstractmethod
    def install(self):
        pass

class OutlookInstaller(ProgramInstaller):
    def install(self):
        shutil.copy('instaladores/Outlook.JPG', mid)
        return "Instalando Outlook"

class ProgramDecorator(ProgramInstaller):
    def install(self,progress):
        pass

class AccessDecorator(ProgramDecorator):
    def install(self,progress):
        shutil.copy('instaladores/Access.JPG', mid)
        return progress + ", Access"

class KEADecorator(ProgramDecorator):
    def install(self,progress):
        shutil.copy('instaladores/KEA.JPG', mid)
        return progress + ", KEA"

class RemedyDecorator(ProgramDecorator):
    def install(self,progress):
        shutil.copy('instaladores/Remedy.JPG', mid)
        return progress + ", REMEDY"


class ComputerInstaller:
    def __init__(self):
        super().__init__()
        self.operatingSystem = so.upper()
        self.machineID = mid

        
    def checkOS(self):
        if(self.operatingSystem == "WINDOWS"):
            print("El sistema operativo esta basado en Windows.")
            return 1
        elif(self.operatingSystem == "LINUX"):
            print("El sistema operativo esta basado en Linux.")
            return 1
        else:
            print("Este Sistema Operativo no esta soportado.")
            return 0

    def getMachineID(self):
        print("El id de la maquina es: "+self.machineID)

    def installPrograms(self, so):
        if(self.operatingSystem == "WINDOWS"):
            r = RemedyDecorator()
            k = KEADecorator()
            a = AccessDecorator()
            o = OutlookInstaller()
            return r.install(k.install(a.install(o.install())))
        elif(self.operatingSystem == "LINUX"):
            r = RemedyDecorator()
            a = AccessDecorator()
            o = OutlookInstaller()
            return r.install(a.install(o.install()))
        else:
            return 0
    def checkPrograms(self):
        onlyfiles = [f for f in os.listdir(mid) if os.path.isfile(os.path.join(mid, f))]
        listPrograms=""
        for i in onlyfiles:
            listPrograms = listPrograms + i[:-4] +", "
        return listPrograms[:-2]

#variable que muestra ciertas impresiones para facilitar el debug
debug = 0
path = os.getcwd()

with open('config.json') as config:
    info = json.load(config)
    so = info['os']
    mid = info['machineID']    

if debug:
    print ("[DEBUG] Estas en: "+path)
    print ("[DEBUG] el os es: "+ so)
    print ("[DEBUG] el ID es: "+ mid)

ci = ComputerInstaller()
try:
    os.mkdir(mid)
except OSError:
    print ("creacion del directorio %s falló" % mid)
else:
    if(ci.checkOS()):
        ci.getMachineID()
        print(ci.installPrograms(so))
        print("instalado: "+ci.checkPrograms())

 



