from Dev import Dev
from Data import Data
from Eng import Eng
from Estagiario import Estagiario
from Gerente import Gerente
from Empresa import Empresa
from Veiculo import Veiculo

data= Data(17,7,2001,8,0,0)
data4= Data(17,7,2001,17,0,0)
data2= Data(17,7,2001,12,0,0)
data3= Data(17,7,2001,13,0,0)
lucas=Dev("lucas","154.449.996-50",data,"553198363-7417","Rua Itapurá, 207 - Saudade, Belo Horizonte - MG, 30285-070")
lucas.Registra_ponto(data)
lucas.Registra_ponto(data2)
lucas.Registra_ponto(data3)
lucas.Registra_ponto(data4)
amanda= Eng("amanda","154.568.696-32",data,"553198363-7417","R. Dante, 60 - São Lucas, Belo Horizonte - MG, 30240-290")
luiz=Estagiario("Luiz","154.568.696-32",data,"553198363-7417","Rua Darcy Vargas, 25 - Nova Suíça, Belo Horizonte - MG, 30421-093")
amanda.Registra_ponto(data4)
angelica= Gerente("angelica","154.568.696-32",data,"553198363-7417","R. Entre Rios, 132 - Carlos Prates, Belo Horizonte - MG, 30710-080")
Empresa=Empresa.instance()
Empresa.end="BR-381, 2211 - Km 02 - Bandeirantes, Contagem - MG, 32240-090"
Empresa.cadastra_Gerente(angelica)
Empresa.cadastra_Funcionario(lucas,angelica)
Empresa.cadastra_Funcionario(amanda,angelica)
Empresa.desliga_Func(lucas)
Hb20= Veiculo("hhk73","BR-381, 2211 - Km 02 - Bandeirantes, Contagem - MG, 32240-090","hb20",4)
Empresa.cadastra_Veiculo(Hb20)
Hb20.add_Func(amanda)
Hb20.add_Func(luiz)
Hb20.add_Func(lucas)
Hb20.print_rotas()










