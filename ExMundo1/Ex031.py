distancia = float(input('Qual a distancia da sua viagem? '))
if distancia > 200:
    preco = distancia * .45
else:
    preco = distancia * .50
print(f'O preço da sua passagem será R$ {preco:.2f}')
