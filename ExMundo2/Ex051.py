"""
Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, moste os 10  primeiros termos dessa progressão
"""
termo = int(input('Digite o primeiro termos da PA: '))
razao = int(input('Digite a razão da PA: '))
decimo = termo + (10 - 1) * razao
for n in range(termo, decimo + razao, razao):
    print(f'{n}', end=' -> ')
print('ACABOU')
