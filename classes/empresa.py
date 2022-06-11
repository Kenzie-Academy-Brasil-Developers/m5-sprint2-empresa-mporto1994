from datetime import datetime
import json
import os
from traceback import print_tb
from funcionario import Funcionario
from gerente import Gerente

class Empresa:
    def __init__(self, nome, cnpj) -> None:
        self.nome = nome
        self.cnpj = cnpj
        self.contratados = []
    
    def __len__(self):
        return len(self.contratados)

    def contratar_funcionario(self,emploee):
        there_is_emploee = [pessoa for pessoa in self.contratados if pessoa.cpf == emploee.cpf]
        if there_is_emploee:
            return "Este CPF já foi cadastrado"

        email = "_".join(emploee.nome_completo.casefold().split())+"@"+"".join(self.nome.casefold().split())+".com"
        emploee.email = email
        emploee.empresa = self.nome
        
        self.contratados.append(emploee)
        return "Funcionario contratado!"


    def __str__(self) -> str:
        return f'{self.__dict__}'

    def gerar_holerite(self, funcionario):
        
        if funcionario in self.contratados:
            empresa = "_".join(self.nome.split())
            obj = {
                "nome":funcionario.nome_completo,
                "cpf":funcionario.cpf,
                "salario":funcionario.salario,
                "mes":datetime.now().strftime("%B"),
                "admissao":funcionario.admissao
            }
            nome_funcionario = "_".join(funcionario.nome_completo.split())
            os.mkdir(f"./empresas/{empresa}")

            with open(f"./empresas/{empresa}/{nome_funcionario}.json","w") as file:
                json.dump(obj,file,indent=4)

            return True
        return False

    def ler_holerite(self,funcionario):
        empresa = "_".join(self.__dict__['nome'].split())
        nome_funcionario = "_".join(funcionario.nome_completo.split())
        holerite_path = f"./empresas/{empresa}/{nome_funcionario}.json"

        holerite_exists = os.path.isfile(holerite_path)

        if not holerite_exists:
            print("Erro: Gere o holerite antes de solicita-lo")

        
        return open(holerite_path,"r").read()

    def demissao(self,funcionario):
        if funcionario in self.contratados:
            self.contratados.pop(self.contratados.index(funcionario))
        
        else:
            return "Funcionário não pertence a empresa ou não encontrado"
        
        managers = [pessoa for pessoa in self.contratados if pessoa.funcao=="Gerente"]
        if funcionario.funcao=="Funcionario":
            for manager in managers:
                if funcionario in manager.funcionarios:
                    manager.funcionarios.pop(manager.funcionarios.index(funcionario))
            return "Funcionário demitido"
        else:
            return "Gerente demitido" 

    def promocao(self, funcionario):
        self.demissao(funcionario)
        new_manager = Gerente(funcionario.nome_completo, funcionario.cpf, funcionario.salario)
        self.contratar_funcionario(new_manager)
        return new_manager
    
    def aumento_salarial(self, funcionario):
        managers = [pessoa for pessoa in self.contratados if pessoa.funcao=="Gerente"]
        for manager in managers:
                if funcionario in manager.funcionarios:
                    funcionario.salario += funcionario.salario*0.1
        print(funcionario.salario)
        if funcionario.salario>=8000:
            self.promocao(funcionario)
        return funcionario
        
rajs = Funcionario(" rajsdo da silva",1,7400)
jose = Funcionario(" jose da silva",232,7400)
kenzie = Empresa("kenzie",3332200001223)

kenzie.contratar_funcionario(rajs)
kenzie.contratar_funcionario(jose)

print(kenzie.contratados)


print(kenzie.aumento_salarial(jose))