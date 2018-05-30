"""
Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar. No final,
mostre:
a) Qual é o total gasto na compra.
b) Quantos produtos custam mais de R$ 1000.
c) Qual é o nome do produto mais barato.
"""
total = totmil = menor = cont = 0
barato = ' '
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$ '))
    cont += 1
    total += preco
    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar: [S/N ]')).strip().upper()[0]
    if resp == 'N':
        break
print(f'FIM DO PROGRAMA:~^40')
print(f'O total da compra foi R$ {total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$ 1.000,00')
print(f'O produto mis barato foi a {barato} e custa R$ {menor:.2f}')
