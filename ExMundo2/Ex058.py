"""
Melhore o jogo do desafio 28 onde o computador vai pensar em um número
0 a 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando
no final quantos palpites foram necessários para vencer.
"""
from random import randint
from time import sleep

computador = randint(0, 10)  # Faz o computador "sortear um número"
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 10. Tente adivinha...')
print('-=-' * 20)
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Em qual número eu pensei? '))  # Jogador tenta adivinhar
    palpites += 1
    print('PROCESSANDO...')
    sleep(1)
    if jogador == computador:
        print('PARABÉNS! Você conseguiu me vencer!')
        acertou = True
    else:
        if jogador < computador:
            print('Mais, tente novamente')
        else:
            print('Menos, tenten novamente')
print(f'Você acertou com {palpites} tentativas.')
