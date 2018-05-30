velocidade = float(input('Qual a velocidade? '))
if velocidade > 80:
    excesso = (velocidade - 80) * 7
    print('Você esta a cima da velocidade permitida')
    print(f'e será multado em R$ {excesso:.2f}')
print('Ok, tenha uma boa viagem!')
