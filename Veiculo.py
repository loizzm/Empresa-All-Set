from Eng import Eng
from Data import Data
from Dev import Dev
from Gerente import Gerente
from Estagiario import Estagiario

class Veiculo:
     def __init__(self, placa,end,modelo,funcionarios=[]):
        self.__funcionarios=funcionarios
        self.__placa=placa
        self.__end=end
        self.__modelo=modelo
    
     @property
     def end(self):
        return self.__end
        
     @end.setter
     def end(self,endereco):
        self.__end=endereco

     @property
     def placa(self):
        return self.__placa
        
     @placa.setter
     def  placa(self, placa):
        self.__placa=placa

     @property
     def modelo(self):
        return self.__modelo
        
     @modelo.setter
     def  placa(self, modelo):
        self.__modelo=modelo
        
    
        