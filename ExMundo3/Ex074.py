"""
Crie um programa que vai gerar cinco números aleatórios e colocar
em uma tupla.
Depois disso, mostre a listagem de números geradas e também indique
o menor e o maior valor que estão na tupla.
"""
from random import sample
numero = tuple(sample(range(0, 10), 5))
print(f'Os valores sorteados foram: {numero}')
print(f'O maior valor sorteador foi {max(numero)}')
print(f'O menor valor sorteador foi {min(numero)}')
