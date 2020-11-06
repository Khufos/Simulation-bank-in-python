# Aqui é a função que faz as linhas .
def linha(tam=30):
    return '=' * tam


# Aqui a função ja diz cabeçalho
def cabeçalho(txt):
    print(linha())
    print(txt.center(30))
    print(linha())


# Aqui é o menu com for
def menu(lista):
    cabeçalho('Banco dos Calvos')
    for k, itens in enumerate(lista):
        print(f'{k + 1} - {itens}')
    opc = int(input('Digite uma opção:'))
    return opc
