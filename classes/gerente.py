from funcionario import Funcionario

class Gerente(Funcionario):
    funcao = "Gerente"
    def __init__(self, nome, cpf, salario):
        super().__init__(nome, cpf, salario)
        self.funcionarios = []
        
    def __len__(self):
        return len(self.funcionarios)

    def adicionar_funcionario(self,funcionario):
        if(self.funcionarios.count(funcionario)!=0 or funcionario.funcao=="Gerente"):
            return False
            
        self.funcionarios.append(funcionario)
        return True