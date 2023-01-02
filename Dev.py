from Data import *
from Funcionario import *
from PontoFlex import *


class Dev(Funcionario):

     def __init__(self, nome, cpf, Data_nascimento,telefone,endereco,carga_horaria=8):
        super().__init__( nome, cpf, Data_nascimento,telefone,endereco)
        self.__carga_horaria=carga_horaria
        self.__ponto=None

     def __str__(self):
        return f'Desenvolvedor: {self._nome}\n Cpf: {self._cpf}\n Data de Nascimento: {self._Data_nascimento}\n Telefone: {self._telefone}\n Endereço: {self._endereco}\n'

     def calc_salario(self):
        pass

     @property
     def ponto(self):
        return self.__ponto
     @property
     def carga_horaria(self):
        return self.__carga_horaria

     @carga_horaria.setter
     def carga_horaria(self,carga_horaria):
        self.__carga_horaria=carga_horaria

     def Registra_ponto(self,Data):
        if(self.__ponto == None):
            self.__ponto=PontoFlex(Data)
        else:    
            self.__ponto.Registra_ponto(Data)

     def Print_ponto(self):  
        print(self.__ponto)     

         

        
        


