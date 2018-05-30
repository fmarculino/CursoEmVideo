km = float(input('Quantos kilometos foi percorrido? '))
dias = int(input('Quantos dias ficou com o carro? '))
aluguel = dias * 60
rodagem = km * 0.15
total = aluguel + rodagem
print(f'Você passou {dias} dias com o carro e percorreu {km:.2f} Km, o custo da locação foi {total:.2f}')
