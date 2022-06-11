from datetime import datetime

class Funcionario:
    funcao = "Funcionario"
    def __init__(self,nome,cpf,salario):
        self.nome_completo = nome
        self.cpf = cpf
        self.salario = salario
        self.admissao = datetime.now().strftime("%d/%m/%Y")

    def __str__(self):
        return f"<{self.funcao}: {self.nome_completo}"

jose = Funcionario("jose",1,2800)
