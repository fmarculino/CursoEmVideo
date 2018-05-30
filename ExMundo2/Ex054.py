"""
Crie um programa que leia o ano de nascimento de sete pessoas. no final,
mostre quantas pessoas ainda não atingiram a maioridade e quantas já
são maiores de idade.
"""
from datetime import date
dtatual = date.today().year
idade = int(0)
nasceu = int(0)
maior = int(0)
menor = int(0)
for con in range(1, 8):
    nasceu = int(input(f'Digite o ano de nascimento da {con}º pessoa: '))
    idade = dtatual - nasceu
    if idade <= 21:
        print(f'Essa pessoa tem {idade} anos e é MENOR de idade.')
        menor += 1
    else:
        print(f'Essa pessoa tem {idade} anos e é MAIOR de idade.')
        maior += 1
print(f'Ao todo tivemos {maior} pessoas MAIORES de idade')
print(f'Ao todo tivemos {menor} pessoas MENORES de idade')
