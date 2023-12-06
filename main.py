import sys
import Disciplinas as disc
import Funcoes_Gerais as FG
import Menu


sair = int(5)
menu_inicial = None

while True:
    
    Menu.menu_inicial()

    opcao_tmp = input()
    

    if opcao_tmp.isdigit() is True:
        
        menu_inicial = int(opcao_tmp)
        
        if menu_inicial == 0:
            print('Finalizando Sistema.')
            sys.exit()
            
        elif menu_inicial == 1:
            while True:
                Menu.menu_principal()
                
                opcao_tmp = input()
    
                if opcao_tmp.isdigit() is True:

                    opcao_menu_inicial = int(opcao_tmp)
                    
                    if opcao_menu_inicial == 0:
                        break
                        
                    elif opcao_menu_inicial == 1:
                        
                        Menu.menu_aluno()
                        opcao_aluno = input()
                        
                    elif opcao_menu_inicial == 2:
                        Menu.menu_professor()
                        opcao_professor = input()
                        
                    elif opcao_menu_inicial == 3:
                        Menu.menu_disciplina()
                        opcao_disciplina = input()
                        
                        if opcao_disciplina.isdigit() is True:
                            opcao_md = int(opcao_disciplina)
                            if opcao_md == 1:
                                disc.Disciplina.inserir_disciplina()
                            elif opcao_md ==2:
                                disc.Disciplina.listar_disciplinas()

                    elif opcao_menu_inicial == 4:
                        Menu.menu_lista()
                    else:
                        FG.valor_invalido(opcao_menu_inicial)
                        
                else:
                    FG.valor_invalido(opcao_tmp)
    
        else:
            FG.valor_invalido(menu_inicial)
            
    else:
        FG.valor_invalido(opcao_tmp)