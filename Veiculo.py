from Eng import Eng
from Data import Data
from Dev import Dev
from Gerente import Gerente
from Estagiario import Estagiario

class Veiculo:
     def __init__(self, placa,end,modelo,lotacao,funcionarios=[], rota ={}):
        self.__funcionarios=funcionarios
        self.__placa=placa
        self.__end=end
        self.__modelo=modelo
        self.__lotacao=lotacao
        self.__rota=rota
    
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
     def lotacao(self):
        return self.__lotacao
        
     @lotacao.setter
     def  lotacao(self, lotacao):
        self.__lotacao=lotacao

     @property
     def modelo(self):
        return self.__modelo
        
     @modelo.setter
     def  placa(self, modelo):
        self.__modelo=modelo

     def __verifica_Func(self,Func):
         if (Func in self.__funcionarios):
            return False
         else:
            return True

     def add_Func(self,Func):
         if (self.lotacao > len(self.__funcionarios and self.__verifica_Func(Func))):
            self.__funcionarios.append(Func)
            self.__fix_Rotas(Func)
         else:
            raise Exception("Lotação máxima do veículo atingida ou  Funcionário já presente no veículo")

     def __fix_Rotas(self,Func):
        pass

        
    
        