"""
Crie um  programa que faça o
computadaoar jorgar jokenpô
com vocẽ
"""
from random import randint
from time import sleep
intens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('== JOKENPÔ - Meu  primeiro jogo em python ==\n')
print("""Você pode escolher essas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
""")
jogador = int(input('Qual é a sua jogada: '))
print('\nJO')
sleep(1)
print('KEN')
sleep(1)
print('PO\n')
sleep(1)
print('-=' * 11)
print(f'Computador jogou {intens[computador]}')
print(f'Sua jogada foi {intens[jogador]}')
print('-=' * 11)
if computador == 0:  # O computador jogou PEDRA
    if jogador == 0:  # O jogador jogou PEDRA
        print('EMPATOU!')
    elif jogador == 1:  # O jogador jogou PAPEL
        print('JOGADOR VENCEU!')
    elif jogador == 2:  # O  jogador jogou TESOURA
        print('COMPUTADOR VENCEU!')
    else:  # A jogada foi inválida
        print('JOGADA INVÁIDA!')
elif computador == 1:  # O compuador jogou PAPEL
    if jogador == 0:  # O jogador jogou PEDRA
        print('O COMPUTADOR VENCEU!')
    elif jogador == 1:  # O jogador jogou PAPEL
        print('EMPATOU!')
    elif jogador == 2:  # O  jogador jogou TESOURA
        print('O JOGADOR VENCEU!')
    else:  # A jogada foi inválida
        print('JOGADA INVÁIDA!')
elif computador == 2:  # O compuador jogou TESOURA
    if jogador == 0:  # O jogador jogou PEDRA
        print('O JOGADOR VENCEU!')
    elif jogador == 1:  # O jogador jogou PAPEL
        print('O COMPUTADOR VENCEU"')
    elif jogador == 2:  # O  jogador jogou TESOURA
        print('EMPATE!')
    else:  # A jogada foi inválida
        print('JOGADA INVÁIDA!')
