"""
Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:
- À vista dinheiro/cheque: 10% desconto
- À vista cartão: 5% de desconto
- Até 2x no cartão: preço normmal
- 3x oumais no cartão: 20% de juros
"""
print(f'{" LOJAS GUANABARA ":=^40}')
preco = float(input('Qual o preço dos produtos: R$ '))
print("""Escolha como quer pagar
1 - À vista dinheiro/cheque
2 - À vista Cartão
3 - Parcelado 2x no cartão
4 - Parcelado em 3x ou mais cartão
""")
opcao = int(input('Escolha como quer pagar: '))
if opcao == 1:
    total = preco - preco * 10 / 100
elif opcao == 2:
    total = preco - preco * 5 / 100
elif opcao == 3:
    parcela = preco / 2
    total = preco
    print(f'Sua compra será parcelada em 2x de R$ {parcela:.2f} sem júros')
elif opcao == 4:
    total = preco + preco * 20 / 100
    totalparcela = int(input('Em quantas parcelas: '))
    parcela = total / totalparcela
    print(f'Sua compra será parcelada em {totalparcela} de R$ {parcela:.2f}')
    (f' com júros')
else:
    print('Opção inválida refaça operação.')

print(f'Sua compra de R$ {preco:.2f} vai custar R$ {total:.2f} no final')
