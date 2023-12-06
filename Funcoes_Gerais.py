from datetime import date

def valor_invalido(valor):
    print('\n')
    print(f'{valor} nao é uma opcao valida.')
    print('Tente Novamente: ')
    print('\n')


def verificar_valor(valor):
    return valor.isdigit()

def verificar_semestre(string):

    elementos = string.split('.')
    qtd_elementos = len(elementos)
    if qtd_elementos != 2:
        return False
    
    if elementos[0].isdigit() is True and elementos[1].isdigit() is False:
        return False
    
    
    ano = int(elementos[0])
    
    semestre = int(elementos[1])
    
    
    if ano < 1970 or ano > date.today().year:
        return False
    
    if semestre == 1 or semestre == 2:
        return True
    
    return False