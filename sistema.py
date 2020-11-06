from menuconfig import *

banco = {}
caderno = []
# Aqui é a entrada de dados .
while True:
    print()
    resp = menu(['Cadastrar Usuários', 'Lista Usuários', 'Acessa contas', 'Sair do programa'])
    if resp == 1:
        banco['Conta'] = int(input('Numero da Conta:'))
        banco['Nome'] = str(input('Nome:'))
        banco['Idade'] = int(input('Idade:'))
        banco['CPF'] = str(input('CPF:'))
        banco['Saldo'] = float(input('Saldo:'))
        caderno.append(banco.copy())
#Aqui está a onde vai mostra a lista dos usuarios .
    if resp == 2:
        cabeçalho('LISTA DE CADASTRADOS')
        for num,pessoas in enumerate(caderno):
            print(f'{num} CONTA ({pessoas["Conta"]}) - {pessoas["Nome"]}')
# Aqui fica o acesso como acessar aconta que funciona pelo o indice começando do 0

    if resp == 3:
        i = int(input('Digite qual conta você quer acessar:'))
        print()
        cabeçalho(f'Bem Vindo Sr : {caderno[i]["Nome"]}')
        for k, v in caderno[i].items():
            print(f'{k}:{v}')
        sap = menu(['Depositar','Sacar'])
        if sap == 1:
            adc = int(input('Qual é o valor que Deseja depositar ?'))
            res = caderno[i]['Saldo'] + adc
            caderno[i]["Saldo"] = res
            print(f'O Seu novo saldo é {res}')
        if sap == 2:
            adc = int(input('Qual é o valor que Deseja sacar ?'))
            reduzir = caderno[i]['Saldo'] - adc
            caderno[i]["Saldo"] = reduzir
            print(f'O seu novo saldo é {reduzir}')
    if resp == 4:
        print('Obirgado por Usar nosso banco:')
        break
