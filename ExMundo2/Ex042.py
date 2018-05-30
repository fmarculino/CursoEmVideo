"""
Refaça o DESAFIO Ex035 dos triângulos,acrescentando o recuro de
mostrar que tipo de triângulo será formado:
"""
r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('SIM é possivel formar um triangulo')
    if r1 == r2 == r3:
        print('Esse triângulo é EQUILÁTERO')
    elif r1 != r2 != r3 != r1:
        print('Esse triângulo é ESCALENO')
    else:
        print('Esse triângulo é ISÓCELES')
else:
    print('NÃO é possível formar um triangulo')
