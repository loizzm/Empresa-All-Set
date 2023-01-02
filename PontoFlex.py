from Ponto import *

class PontoFlex(Ponto):
    def __init__(self, data):
        super().__init__( data)
        self._ponto=[]
        self._ponto.append(data)
    
    def Registra_ponto(self, Data):
        self.__fix_mes(Data)
        self._ponto.append(Data)

    def Del_ponto(self):
        del self._ponto[len(self._ponto)-1]
    
    def Calcula_horas(self):
        output=Data()
        for data in self._ponto:
            if(self._ponto.index(data) % 2 == 0):
                data_aux=data
            else:
                data_aux= data - data_aux
                output.minutos+= ((data_aux.horas)*60) + data_aux.minutos + (data_aux._segundos/60)
        return output.minutos  

    def __fix_mes(self,Data):
        if(self._ponto[0].dia != Data.dia):
            self._ponto.clear()   

    def __str__(self):
        output="Ponto do dia: \n"
        for data in self._ponto:
            if(self._ponto.index(data) % 2 == 0):
                output+=f' Entrada: {data.horas}:{data.minutos}:{data.segundos}\n'
            else:
                output+=f' Saída: {data.horas}:{data.minutos}:{data.segundos}\n'
        return output        