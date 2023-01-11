from Eng import Eng
from Data import Data
from Dev import Dev
from Gerente import Gerente
from Estagiario import Estagiario

class Empresa:

    _instance = None
    
    def __init__(self,Funcionarios=[]):
        self.attr = None
        self.Funcionarios=Funcionarios

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def cadastra_Funcionario(self,Func):
        self.Funcionarios.append(Func)
    
    def __str__(self):
        outp="***Empresa*** \n"
        for Func in self.Funcionarios:
            outp += str(Func)
        return outp
    
