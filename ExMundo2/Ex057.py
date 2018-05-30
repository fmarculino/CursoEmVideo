"""
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores
M ou F caso esteja errado, peça a digitação novamente até  um valor correto
"""
sexo = str(None)
while sexo not in 'MmFf':
    sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0]
print(f'Você digitou {sexo} corretamente! ')
