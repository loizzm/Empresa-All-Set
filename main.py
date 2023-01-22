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
Empresa=Empresa.instance()
Empresa.end="BR-381, 2211 - Km 02 - Bandeirantes, Contagem - MG, 32240-090"
Empresa.cadastra_Gerente("angelica","154.568.696-32",data,"553198363-7417","R. Entre Rios, 132 - Carlos Prates, Belo Horizonte - MG, 30710-080")
Empresa.cadastra_Funcionario("lucas","154.449.996-50",data,"553198363-7417","Rua Itapurá, 207 - Saudade, Belo Horizonte - MG, 30285-070",Empresa.find_Func("154.568.696-32"),"Eng")
Empresa.cadastra_Funcionario("amanda","941.557.396-15",data,"553198363-7417","R. Dante, 60 - São Lucas, Belo Horizonte - MG, 30240-290",Empresa.find_Func("154.568.696-32"), "Dev")
Empresa.cadastra_Funcionario("Luiz","265.679.787-32",data,"553198363-7417","Rua Darcy Vargas, 25 - Nova Suíça, Belo Horizonte - MG, 30421-093",Empresa.find_Func("154.568.696-32"), "Estagiário")
Empresa.cadastra_Veiculo("hht331","Hb20",4)
Empresa.cadastra_Veiculo("hht332","Hb20",4)
Empresa.registra_Ponto(Empresa.find_Func("154.449.996-50"),data)
Empresa.registra_Ponto(Empresa.find_Func("154.449.996-50"),data4)
Empresa.registra_Ponto(Empresa.find_Func("941.557.396-15"),data)
Empresa.registra_Ponto(Empresa.find_Func("941.557.396-15"),data2)
Empresa.registra_Ponto(Empresa.find_Func("941.557.396-15"),data3)
Empresa.registra_Ponto(Empresa.find_Func("941.557.396-15"),data4)
Empresa.find_Veiculo("hht332").add_Func(Empresa.find_Func("154.449.996-50"))
Empresa.find_Veiculo("hht332").add_Func(Empresa.find_Func("941.557.396-15"))
print(Empresa.find_Veiculo("hht332").print_rotas())
print(Empresa.find_Veiculo("hht331").print_rotas())







