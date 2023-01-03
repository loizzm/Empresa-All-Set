from Data import *
from Funcionario import *

class Gerente(Funcionario):
    def __init__(self, nome, cpf, Data_nascimento,telefone,endereco,subordinados=[]):
        super().__init__( nome, cpf, Data_nascimento,telefone,endereco)
        self.__salario=0
        self.__subordinados=subordinados

    @property
    def salario(self):
        return self.__salario
        
    @salario.setter
    def salario(self,salario):
        self.__salario=salario
    
    def add_Funcionario(self,Func):
      if(len(self.__subordinados)==0):
         self.__subordinados.append(Func)
      else:
        if(self.__verica_Func(Func)):
             self.__subordinados.append(Func)
        else:
            raise ValueError("Funcionário já adicionado")

    def __verica_Func(self,Func):
        for func in self.__subordinados:
            if (Func==func):
                return False
            else:
                return True

    def calc_Salario(self):
        output=0
        for func in self.__subordinados:
            output+= func.salario
        self.salario=output

    def __str__(self):
        return f'Gerente: {self._nome}\n Cpf: {self._cpf}\n Data de Nascimento: {self._Data_nascimento}\n Telefone: {self._telefone}\n Endereço: {self._endereco}\n'

    def print_Subordinados(self):
        for func in self.__subordinados:
            print(func)

    def del_Funcionario(self,Func):
        del self.__subordinados[self.__subordinados.index(Func)]