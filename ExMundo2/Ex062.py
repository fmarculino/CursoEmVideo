"""
Melhore o desafio 061, perguntando para o usuario se ele quer
mostrar mais alguns termos. O programa encerra quando ele disser
que quer mostrar 0 termos.
"""
termo = int(input('Digite o primeiro termos da PA: '))
razao = int(input('Digite a razão da PA: '))
print('Agora usando o While')
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo} -> ', end='')
        termo += razao
        cont += 1
    print('PAUSA\n')
    mais = int(input('Quantos termos você quer a Mais: '))
print(f'Progressão finalizada com {total} termos mostrados: FIM\n')
