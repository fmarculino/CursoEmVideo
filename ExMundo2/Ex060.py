"""
Faça um programa que leia um número qualquer e mostre seu
fatorial.
Ex. 5! = 5 x 4 x 3 x 2 x 1 = 120
"""
# Maneira pythonica de ser.
from math import factorial
numero = int(input('Digite o número que deseja calcular o fatorial: '))
f = factorial(numero)
print(f'O fatoria de {numero} é {f}')

# Maneira tradicional
c = numero
f = 1
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f)
