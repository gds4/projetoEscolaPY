import Funcoes_Gerais as FG


class Disciplina:

    Disc_cadastradas = []
    
    def __init__(self, Nome, Codigo, Semestre, Prof):
        self.nome = Nome
        self.codigo = Codigo
        self.semestre = Semestre
        self.professor = Prof
        Disciplina.Disc_cadastradas.append(self)

    @classmethod
    def inserir_disciplina(cls):
        
        print('Insira o nome da disciplina: ')
        nome = str(input())
        
        print('Insira o codigo da disciplina')
        while True:
            
            aux_code = str(input())

            if aux_code.isdigit() is True:
                break
            else:
                print('O codigo deve conter apenas numeros, Tente novamente: ', end=' ')

        codigo = int(aux_code)

        print('Insira o semestre da disciplina [Ano.Semestre]: ', end = ' ')
        while True:

            aux_semestre = str(input())
            if FG.verificar_semestre(aux_semestre) is True:
                break
            else:
                print('Formato inválido, Tente novamente: ', end=' ')
        semestre = aux_semestre

        print('Insira o nome do professor: ')
        
        nome_prof = str(input())
        
        n_dsc = cls(Nome = nome, Codigo = codigo, Semestre = semestre, Prof = nome_prof)
        
        return n_dsc
        
    @classmethod
    def listar_disciplinas(cls):


        for disciplina in cls.Disc_cadastradas:
            
            print(f'Nome: {disciplina.nome} Codigo: {disciplina.codigo} Semestre: {disciplina.semestre} Professor: {disciplina.professor}')






