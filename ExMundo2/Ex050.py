"""
Desenvolva um programa que leia seis números inteiros e mostre a soma
apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o
"""
print('Vamos começar digitando ovalor dos 6 numeros.')
soma = int(0)
cont = int(0)
for n in range(1, 7):
    numero = int(input(f'Digite o valor do {n}º numero: '))
    if numero % 2 == 0:
        cont += 1
        soma += numero
print(f'A soma dos {cont} números pares digitado é: {soma}')
