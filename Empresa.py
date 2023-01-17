from Eng import Eng
from Data import Data
from Dev import Dev
from Gerente import Gerente
from Estagiario import Estagiario
from Veiculo import Veiculo

class Empresa:

    _instance = None
    
    def __init__(self, Funcionarios=[],frota=[]):
        self.attr = None
        self.Funcionarios=Funcionarios
        self.frota=frota
        self.__end=str()

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def cadastra_Funcionario(self,Func,gerente):
        if (type(Func)!= Gerente):
            gerente.add_Funcionario(Func)
            self.Funcionarios.append(Func)
        else:
            raise Exception("O funcionário em questão é um gerente e deve ser inserido com outro método")          
    
    def cadastra_Veiculo(self,veiculo):
       if (veiculo in self.frota):
            raise Exception("O veículo em questão já foi adicionado")
       else:
            self.frota.append(veiculo)

    def add_Funcionario(self,veiculo,func):
        veiculo.add_Func(func)

    def cadastra_Gerente(self,Func):
        if (type(Func)!= Gerente):
            raise Exception("O funcionário em questão não é um gerente e deve ser inserido com outro método")  
            
        else:
            self.Funcionarios.append(Func)

    def find_Func(self,Func):
        return self.Funcionarios[self.Funcionarios.index(Func)]

    def desliga_Func(self,func):
        del self.Funcionarios[self.Funcionarios.index(func)]

    @property
    def end(self):
        return self.__end
        
    @end.setter
    def end(self,endereco):
        self.__end=endereco

    def __str__(self):
        outp="***Empresa*** \n"
        for Func in self.Funcionarios:
            outp += str(Func)
        return outp
    
