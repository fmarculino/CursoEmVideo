"""
Escrevva um programa que leia um número inteiro qualquer e peça
para o usuario escolher qual será a base de conversão:
1 - para binário
2 - para octal
3 - para hexadecimal
"""
numero = int(input('Digite um numero inteiro: '))
print('Escolha uma das bases para onversão:\n')
print('1 - Converte para Binário')
print('2 - Converte para octal')
print('3 - Converte para Hexadecimal\n')
escolha = int(input('Escolha sua  opção de conversão: '))
if escolha == 1:
    print(f'{numero} convertido para BINÁRIO  é igual a {bin(numero)[2:]}')
elif escolha == 2:
    print(f'{numero} convertido para OCTAL é igal a {oct(numero)[2:]}')
elif escolha == 3:
    print(f'{numero} convertido para HEXADECIMAL é igual a {hex(numero)[2:]}')
else:
    print('Opção invalida tente novamente')
