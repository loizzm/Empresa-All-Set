from Ponto import *
import copy

class PontoEstatico(Ponto):
    def __init__(self, data):
        super().__init__( data)

    def Registra_ponto(self, Data):
        self.__horario_saida=Data

    def Del_ponto(self):
        if (self.__horario_saida == None):
            self._horario_entrada=None
        else:
            self.__horario_saida=None

    @property
    def horario_saida(self):
        return self.__horario_saida

    @horario_saida.setter
    def horario_saida(self,horario_saida):
        self.__horario_saida=horario_saida

    def Calcula_horas(self): 
        aux=copy.deepcopy(self.__horario_saida)
        aux1=copy.deepcopy(self._horario_entrada)
        data_o=  aux - aux1
        output=(data_o.horas*60)+(data_o.minutos)+(data_o.segundos/60)-60
        return output

    def __str__(self):
        output="Ponto do dia: \n"
        if (self._horario_entrada != None and self.__horario_saida != None):
            output+=f' Entrada: {self._horario_entrada.horas}:{self._horario_entrada.minutos}:{self._horario_entrada.segundos}\n'
            output+=f' Saída: {self.__horario_saida.horas}:{self.__horario_saida.minutos}:{self.__horario_saida.segundos}\n'
        elif (self._horario_entrada != None):
            output+=f' Entrada: {self._horario_entrada.horas}:{self._horario_entrada.minutos}:{self._horario_entrada.segundos}\n'
        else:
            output+=f' Sem Pontos até o Momento'
        return output        