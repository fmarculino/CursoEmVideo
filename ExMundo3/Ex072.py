"""
Crie um programa que tenha uma tupla totalmente preenchida
com uma contagem por extenso, de zero até vinte
Seu programa deverá ler um numero pelo teclado (entre 0 e 20)
e mostrá-lo por extenso.
"""
num_extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete',
               'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze',
               'quinze', 'deseseis', 'desesete', 'dezoito', 'dezenove',
               'vinte')
while True:
    numero = int(input('Digite um número entre 0 e 20: '))
    if numero >= 0 and numero <= 20:
        print(f'Você digitou o número {num_extenso[numero]}')
        res = input('Deseja digitar outro numero S/N? ').strip().upper()
        if res == 'N':
            break
        else:
            continue
