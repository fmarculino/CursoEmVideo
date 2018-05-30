"""
Refaça o desafio 051, lendo o primeiron termo e a razão
de uma PA, mostrando os 10 primeiros termos da progressão
usando a estrutura while.
"""
# Exerício anterior Ex051.py
termo = int(input('Digite o primeiro termos da PA: '))
razao = int(input('Digite a razão da PA: '))

# Utilizando o for
print('\nUtilizando o for')
decimo = termo + (10 - 1) * razao
for n in range(termo, decimo + razao, razao):
    print(f'{n}', end=' -> ')
print('ACABOU\n')

# Agora usando a extrura whileself.
print('Agora usando o While')
cont = 1
while cont <= 10:
    print(f'{termo} -> ', end='')
    termo += razao
    cont += 1
print('FIM\n')
