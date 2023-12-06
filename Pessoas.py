class Pessoa:
    def __init__(self, nome, sexo, CPF, Nasc):
        self.nome = nome
        self.sexo = sexo
        self.CPF = CPF
        self.Nasc = Nasc
        

class Professor(Pessoa):
    professores_cadastrados = []

    def __init__(self, nome, sexo, CPF, Nasc, Matricula):
        super().__init__(nome, sexo, CPF, Nasc)
        self.Matricula = Matricula
        Professor.professores_cadastrados.append(self)

    @classmethod
    def inserir_professor(cls):
        aux = None
        while True:
            
            nome = input('Digite o nome do professor: ')
            sexo = input('Digite o sexo do professor[M/F]: ')
            CPF = input('Digite o CPF do professor: ')
            Nasc = input('Digite a data de nascimento do professor: ')
            Matricula = input('Digite a matricula do professor: ')
            
        cls(nome = nome, sexo = sexo, CPF = CPF,Nasc = Nasc, Matricula = Matricula)

        
        

class Aluno(Pessoa):

    alunos_cadastrados = []
    
    def __init__(self, nome, sexo, CPF, Nasc, Matricula):
        super().__init__(nome, sexo, CPF, Nasc)
        self.Matricula = Matricula
        Aluno.alunos_cadastrados.append(self)

    @classmethod
    def inserir_aluno(cls):
        nome = input('Digite o nome do aluno: ')
        sexo = input('Digite o sexo do aluno[M/F]: ')
        CPF = input('Digite o CPF do aluno: ')
        Nasc = input('Digite a data de nascimento do aluno: ')
        Matricula = input('Digite a matricula do aluno: ')

        cls(nome = nome, sexo = sexo, CPF = CPF,Nasc = Nasc, 
                             Matricula = Matricula)