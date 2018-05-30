from calendar import isleap
from datetime import date
""""
Faça um programa que leia um ano qualquer
e mostre se ele é bissexto
"""
ano = int(input('Digite um ano: '))
print(f'O ano que você digitou é bissexto? {isleap(ano)}')

# Solução matematica seria

if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é BISSEXTO!')
else:
    print(f'O ano {ano} não é BISSEXTO!')
