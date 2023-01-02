from Data import *
from abc import ABC, abstractmethod

class Ponto(ABC):
    def __init__(self, data):
        self._horario_entrada=data

    @abstractmethod
    def Registra_ponto(self,Data):
        pass

        