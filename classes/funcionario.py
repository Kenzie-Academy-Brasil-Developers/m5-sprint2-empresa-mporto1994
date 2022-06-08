# Desenvolva a classe de Funcionario aqui

from datetime import datetime


class Funcionario:
    funcao = "Funcionário"
    def __init__(self,nome,cpf,salario):
        self.nome_completo = nome
        self.cpf = cpf
        self.salario = salario
        self.admissao = datetime.now()

    def __str__(self):
        return self.__dict__["nome_completo"], self.funcao

jose = Funcionario("jose",1,2800)
print(jose.__str__())
