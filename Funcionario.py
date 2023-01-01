from abc import ABC, abstractmethod
from Data import *
import re

class Funcionario(ABC):
     def __init__(self, nome, cpf, Data_nascimento,telefone,endereco):
        if (self.valida_cpf(cpf) == True and self.valida_telefone(telefone)==True):
            self._nome=nome
            self._cpf=cpf
            self._Data_nascimento=Data_nascimento
            self._telefone=telefone
            self._endereco=endereco
        else:
            raise ValueError("O CPF ou o Telefone não é válido.")    

     @property
     def matricula(self):
        return self._matricula

     @property
     def salario(self):
        return self._salario

     @property
     def endereco(self):
        return self._endereco

     @property
     def telefone(self):
        return self._telefone

     @property
     def Data_nascimento(self):
        return self._Data_nascimento

     @property
     def cpf(self):
        return self._cpf

     @property
     def nome(self):
        return self._nome

     @nome.setter
     def nome(self,nome):
        self._nome=nome

     @cpf.setter
     def cpf(self,cpf):
        self._cpf=cpf

     @Data_nascimento.setter
     def Data_nascimento(self,Data_nascimento):
        self._Data_nascimento=Data_nascimento

     @telefone.setter
     def telefone(self,telefone):
        self._telefone=telefone

     @endereco.setter
     def endereco(self,endereco):
        self._endereco=endereco

     @salario.setter
     def salario(self,salario):
        self._salario=salario

     @matricula.setter
     def matricula(self,matricula):
        self._matricula=matricula   

     @abstractmethod
     def __str__(self):
        pass

     def __eq__(self,other):
        if(self._nome==other._nome and self._cpf== other._cpf):
            return True
        else:
            return False

     def valida_cpf(self,cpf):
        padrao=re.compile("[0-9]{3}[.]?[0-9]{3}[.]?[0-9]{3}[-]?[0-9]{2}")
        if ( not padrao.match(cpf)):
            return False
        else:
            return True  

     def valida_telefone(self,telefone):
        padrao=re.compile("[55]?[0-9]?[0-9]?[9]?[0-9]{4}[-]?[0-9]{4}")
        if ( not padrao.match(telefone)):
            return False
        else:
            return True    



        