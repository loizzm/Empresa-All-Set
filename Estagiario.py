from Data import *
from Funcionario import *

class Estagiario(Funcionario):
     def __init__(self, nome, cpf, Data_nascimento,telefone,endereco,carga_horaria=6):
        super().__init__( nome, cpf, Data_nascimento,telefone,endereco)
        self.__carga_horaria=carga_horaria
        self.__salario=1200

     @property
     def carga_horaria(self):
        return self.__carga_horaria

     @carga_horaria.setter
     def carga_horaria(self,carga_horaria):
        self.__carga_horaria=carga_horaria

     @property
     def salario(self):
        return self.__salario

     @salario.setter
     def salario(self,salario):
        self.__salario=salario

     def calc_Salario(self):
         return self.salario

     def __str__(self):
        return f'Estagiário: {self._nome}\n Cpf: {self._cpf}\n Data de Nascimento: {self._Data_nascimento}\n Telefone: {self._telefone}\n Endereço: {self._endereco}\n'