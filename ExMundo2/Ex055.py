"""
Faça um programa que leia o peso de cinco pessoas, no final, mostre qual
foi o maior e o menor peso lidos.
"""
totmaior = float(0)
totmenor = float(0)
for c in range(1, 6):
    peso = float(input(f'Digite o peso da {c}º pessoa: '))
    if peso > totmaior:
        totmaior = peso
        if totmenor == 0:
            totmenor = peso
    elif peso < totmenor:
        totmenor  = peso
print(f'O MAIOR peso digitado foi {totmaior}')
print(f'O MENOR peso digitado foi {totmenor}')
