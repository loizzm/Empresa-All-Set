from Eng import Eng
from Data import Data
from Dev import Dev
from Gerente import Gerente
from Estagiario import Estagiario
import googlemaps
from datetime import datetime

class Veiculo:
     def __init__(self, placa,end,modelo,lotacao,funcionarios=[], rota ={}):
        self.__funcionarios=funcionarios
        self.__placa=placa
        self.__end=end
        self.__modelo=modelo
        self.__lotacao=lotacao
        self.__rota=rota
    
     @property
     def end(self):
        return self.__end
        
     @end.setter
     def end(self,endereco):
        self.__end=endereco

     @property
     def placa(self):
        return self.__placa
        
     @placa.setter
     def  placa(self, placa):
        self.__placa=placa

     @property
     def lotacao(self):
        return self.__lotacao
        
     @lotacao.setter
     def  lotacao(self, lotacao):
        self.__lotacao=lotacao

     @property
     def modelo(self):
        return self.__modelo
        
     @modelo.setter
     def  modelo(self, modelo):
        self.__modelo=modelo

     def __verifica_Func(self,Func):
         if (Func in self.__funcionarios):
            return False
         else:
            return True

     def __eq__(self, other):
        if (self.__placa == other.__placa):
           return True
        else:
           return False
     
     def __str__(self):
        return f' Veículo:\n Modelo:{self.__modelo} \n Placa:{self.__placa}\n Lotação:{self.__lotacao}'
     
     def add_Func(self,Func):
         if (self.lotacao > len(self.__funcionarios) and self.__verifica_Func(Func)):
            self.__funcionarios.append(Func)
            self.__api(Func)
         else:
            raise Exception("Lotação máxima do veículo atingida ou  Funcionário já presente no veículo")

     def __fix_Rotas(self,Func):
        pass
     
     def __api(self,func):
      API_KEY= 'key'
      map_client = googlemaps.Client(API_KEY)
      r = map_client.geocode(self.__end)
      lat_empresa=r[0]['geometry']['location']['lat']
      lng_empresa=r[0]['geometry']['location']['lng']
      r = map_client.geocode(func.endereco)
      lat_home=r[0]['geometry']['location']['lat']
      lng_home=r[0]['geometry']['location']['lng']
      now=datetime.now()
      geocode_empresa=f'{lat_empresa},{lng_empresa}'
      geocode_home=f'{lat_home},{lng_home}'
      dr = map_client.directions(geocode_home,
                                          geocode_empresa,
                                          mode="driving",
                                          traffic_model='pessimistic',
                                          departure_time=now)
      self.__rota[func.nome]=dr[0]['legs'][0]['duration']['value']/60
      ##self.__fix_Rotas()

     def print_rotas(self):
           print(self.__rota)
   

        
    
        