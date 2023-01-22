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

    def cadastra_Funcionario(self,nome, cpf, Data_nascimento,telefone,endereco,gerente,cargo):
        if (type(gerente) == Gerente and self.__verifica_Func(cpf)):
            if (cargo == "Eng"):
                Func = Eng(nome, cpf, Data_nascimento,telefone,endereco)
            elif (cargo == "Dev"):
                Func = Dev(nome, cpf, Data_nascimento,telefone,endereco)
            else:
                Func = Estagiario(nome, cpf, Data_nascimento,telefone,endereco)
            gerente.add_Funcionario(Func)
            self.Funcionarios.append(Func)
        else:
            raise Exception("Inserção inválida")          
    
    def __verifica_Func(self,cpf):
        for Func in self.Funcionarios:
            if (Func.cpf == cpf):
                return False
            else:
                return True

    def __verifica_Veiculo(self,placa):
        for car in self.frota:
            if (car.placa == placa):
                return False
            else:
                return True    
            
    def cadastra_Veiculo(self,placa,modelo,lotacao):
       if (self.__verifica_Veiculo(placa)== False):
            raise Exception("O veículo em questão já foi adicionado")
       else:
            V = Veiculo(placa,self.__end,modelo,lotacao)
            self.frota.append(V)


    def cadastra_Gerente(self,nome, cpf, Data_nascimento,telefone,endereco):
        if (self.__verifica_Func(cpf) == False):
            raise Exception("O gerente em questão já foi adicionado")  
            
        else:
            Func = Gerente(nome, cpf, Data_nascimento,telefone,endereco)
            self.Funcionarios.append(Func)

    def find_Veiculo(self,placa):
        indice=0
        for V in self.frota:
            if (V.placa == placa):
                indice=self.frota.index(V)

        return self.frota[indice]
    
    def find_Func(self,cpf):
        for Func in self.Funcionarios:
            if (Func.cpf ==cpf):
                indice=self.Funcionarios.index(Func)

        return self.Funcionarios[indice]

    def desliga_Func(self,func):
        del self.Funcionarios[self.Funcionarios.index(func)]

    def registra_Ponto(self,Func,Data):
        Func.Registra_ponto(Data)
    
    @property
    def end(self):
        return self.__end
        
    @end.setter
    def end(self,endereco):
        self.__end=endereco

    def __str__(self):
        outp="***Empresa*** \n"
        outp += "**Funcinários:**\n"
        for Func in self.Funcionarios:
            outp += str(Func)
        outp += "**Frota:**\n"
        for V in self.frota:
            outp += str(V)
        return outp