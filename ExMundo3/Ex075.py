"""
Desenvolva um programa que leia quatro valores pelo teclado e
guarde-os em uma tupla. No final, mostre:
a) Quantas vezes apareceu o valor 9.
b) Em que posição foi digitado o primeiro valor 3.
c) Quais foram os numeros pares.
"""
valor = []
pares = []
for c in range(1, 5):
    numero = int(input(f'Digite o {c}º valor: '))
    valor.append(numero)
valor = tuple(valor)
print(f'Você digitou os numeors {valor}')
print(f'O valor 9 apareceu {valor.count(9)} na tupla')
if 3 in valor:
    print(f'O primeiro numero 3 foi digitado na posição {valor.index(3) + 1}')
else:
    print('O valor 3 não foi digitado em nenhuma posição.')
for c in range(len(valor)):
    if valor[c] % 2 == 0:
        pares.append(valor[c])
print(f'Os valores pares digitados foram {pares}')
