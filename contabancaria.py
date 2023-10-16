import os

import contabancaria

print('conta bancaria'.center(30, '=')) # O método center() alinhará a string ao centro, usando um caractere especificado (espaço é o padrão) como caractere de preenchimento.

nome = input("digite seu nome:  ")
sobrenome = input('digite seu ultimo sobrenome:  ')
cliente = contabancaria(nome,sobrenome)
os.system('cls') # executado. cls é o comando para limpar o texto do terminal no Windows. clear é o comando equivalente do Unix

while True:
    print("Menu:\n[1] -> Depositar\n[2] -> Sacar\n[3] -> Conta\n[0] -> Sair")
    escolha = input('\nescolha: ')

    if escolha == '1':
     os.system('cls')
     quantia = float(input('quanto deseja depositar:  '))

    if cliente.depositar.quantia:
       os.system('cls')
       print('quantia depositada com sucesso!')

    else:
       print('não é possivel depositar valor menor ou igual a zero')

    _ = input("\nAperte qualquer botão para continuar: ")
    os.system('cls')

    


