"""
Faça um programa que jogue par ou impaar com o computador. O jogo
só será interrompido quando o jogador PERDER, mostrando o total
de vitórias consecutivos que ele conquistou no final do jogo.
"""
from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 11)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou inpar? [P/I]')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. total de {total}')
    print('DEU PAR' if total % 2 == 0 else 'DEU INPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU')
            v += 1
        else:
            print('Você PERDEU')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU')
            v += 1
        else:
            print('Você PERDEU')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você veneu {v} vezes.')
