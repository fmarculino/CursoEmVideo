"""
Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999,
que é a condição deparada. No final, mostre quantos números foram
digitados e qual foi a soma entre eles (desconsiderando o flag).
"""
soma = cont = 0
while True:
    numero = int(input('Digite um número: '))
    if numero == 999:
        break
    cont += 1
    soma += numero
print(f'Você digitou {cont} números e a soma total é {soma}')
