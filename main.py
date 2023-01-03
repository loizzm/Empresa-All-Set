from Dev import *
from Data import *
from PontoFlex import *
from Eng import *
from Estagiario import *
from Gerente import *

data= Data(17,7,2001,8,0,0)
data4= Data(17,7,2001,17,0,0)
data2= Data(17,7,2001,12,0,0)
data3= Data(17,7,2001,13,0,0)
lucas=Dev("lucas","154.449.996-50",data,"553198363-7417","Rua itapura 207, Saudade")
lucas.Registra_ponto(data)
lucas.Registra_ponto(data2)
lucas.Registra_ponto(data3)
lucas.Registra_ponto(data4)
amanda= Eng("amanda","154.568.696-32",data,"553198363-7417","Rua Dante 60, São Lucas")
luiz=Estagiario("Luiz","154.568.696-32",data,"553198363-7417","Rua Dante 60, São Lucas")
amanda.Registra_ponto(data)
amanda.Registra_ponto(data4)
amanda.Print_ponto()
amanda.del_Ponto()
amanda.Print_ponto()
#amanda.Print_ponto()







