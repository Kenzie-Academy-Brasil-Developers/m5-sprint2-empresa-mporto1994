# Desenvolva a classe de Empresa aqui
import json
import os
from funcionario import Funcionario

class Empresa:
    def __init__(self, nome, cnpj) -> None:
        self.nome = nome
        self.cnpj = cnpj
        self.contratados = []
    
    def __len__(self):
        return len(self.contratados)

    def contratar_funcionario(self,emploee):
        email = "_".join(emploee.nome_completo.casefold())+"".join(self.nome.casefold())+".com"
    
    def __str__(self) -> str:
        return f'{self.__dict__}'

    def gerar_holerite(self, funcionario):
        empresa = "_".join(self.__dict__['nome'].split())
        nome_funcionario = "_".join(funcionario.nome_completo.split())

        os.mkdir(f"./empresas/{empresa}")

        file = open(f"./empresas/{empresa}/{nome_funcionario}.json","x")
        # file.write(f"self.__dict__")
        json.dump(self.__dict__,file)

jose = Funcionario(" jose da silva",1,2800)
kenzie = Empresa("kenzie",3332200001223)
kenzie.gerar_holerite(jose)