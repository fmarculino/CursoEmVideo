""""
Faça um programa que leia três número e
mostre qual é o maior e qual é o menor.
"""
n1 = int(input('Digite o primeior numero: '))
n2 = int(input('Digite o primeior numero: '))
n3 = int(input('Digite o primeior numero: '))
# Verificando quem é o menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
# Verificando quem é o maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n2 and n3 > n1:
    maior = n3
print(f'O menor número digitado foi {menor}')
print(f'O maior número digitado foi {maior}')