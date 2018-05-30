"""
Faça um programa que mostre a tabuada de vários números, um de
cada vez, para cada valor digitado pelo usuário. O programa será
interrompido quando o número solicitado for negativo.
"""
while True:
    numero = int(input('Digite o número desejado: '))
    if numero < 0:
        break
    for cont in range(1, 11):
        print(f'{numero} x {cont} = {numero * cont}')
print('Acabou!')
