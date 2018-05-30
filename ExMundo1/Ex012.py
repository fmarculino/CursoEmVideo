preco = float(input('Qual é o preço do produto? R$ '))
desc = preco - (preco * 5) / 100
print(f'O produto que custava R$ {preco:.2f}, na promoção com desconto de 5%'
      f' vai custar R$ {desc:.2f}')
