from random import randint
from time import sleep

computador = randint(0, 5)  # Faz o computador "sortear um número"
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. TEnte adivinha...')
print('-=-' * 20)
jogador = int(input('Em qual número eu pensei? '))  # Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print(f'GANHEI! Eu pensei no número {computador} e não no {jogador}')
