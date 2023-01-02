from Dev import *
from Data import *
from PontoFlex import *

data= Data(17,7,2001,8,0,0)
data4= Data(17,7,2001,17,0,0)
data2= Data(17,7,2001,12,0,0)
data3= Data(17,7,2001,13,0,0)
lucas=Dev("lucas","154.449.996-50",data,"553198363-7417","Rua itapura 207, Saudade")
print(lucas)
lucas.Registra_ponto(data)
lucas.Registra_ponto(data2)
lucas.Registra_ponto(data3)
lucas.Registra_ponto(data4)
lucas.Print_ponto()
