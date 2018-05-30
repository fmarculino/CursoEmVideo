"""
Faça um programa que leia um número inteiro e diga se ele é
ou não um número primo.
"""
num = int(input('Digite um númeor: '))
tot = int(0)
for c in range(1, num + 1):
    if num % c == 0:
        print(f'\033[33m{c}', end=' ')
        tot += 1
    else:
        print(f'\033[31m{c}', end=' ')
print(f'\n\033[mO número {num} foi divisível {tot} vezes')
if tot == 2:
    print('Portante ele é um número PRIMO')
else:
    print('Portanto ele NÃO é um númeor primo')
