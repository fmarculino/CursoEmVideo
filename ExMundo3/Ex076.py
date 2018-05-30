"""
Crie um programa que tenha uma tupla única com nomes de produtos
e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços, organizando os dados em
forma tabular.
"""
tabela = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo',
          25.00, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila',
          120.32, 'Canetas', 22.30, 'Livros', 34.90)
print(f'-' * 40)
print(f'{" LISTAGEM DE PREÇOS ":^40}')
print(f'-' * 40)
for c in range(0, len(tabela), 2):
    print(f'{tabela[c]:.<27} R${tabela[c + 1]:>10,.2f}')
print(f'-' * 40)
