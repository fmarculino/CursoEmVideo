"""
Escreva um programa que leia dois números inteiro s e compare-o
mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são igurais
"""
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Diginte o segundo número: '))
if num1 > num2:
    print('O PRIMEIRO número é maior.')
elif num2 > num1:
    print('O SEGUNDO valor é maior')
else:
    print('Não EXISTE VALOR MAIOR os dois numeros são iguais.')
