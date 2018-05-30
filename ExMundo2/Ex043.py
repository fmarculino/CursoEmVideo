"""
Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
calcule seu IMC e mostre seu status. de acordo com a tabela abaixo:
- Abaixo de 18.5: ABAIXO DO PESO
- Entre 18.5 e 25: PESO IDEAL
- Entre 25 até 30: SOBREPESO
- Entre 30 até 40: Obesidade
- Acima de 40: OBESIDADE MÓRBIDA
"""
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / altura ** 2
if imc < 18.5:
    print(f'Seu IMC é {imc:.2f} e você esta ABAIXO DO PESO')
elif 18.5 < imc < 25:
    print(f'Seu IMC é {imc:.2f} e você esta com o PESO IDEAL')
elif 25 < imc < 30:
    print(f'Seu IMC é {imc:.2f} e você esta com SOBREPESO')
elif 30 < imc < 40:
    print(f'Seu IMC é {imc:.2f} e você esta OBESO')
else:
    print(f'Seu IMC é {imc:.2f} e você esta com OBESIDADE MÓRBIDA')
