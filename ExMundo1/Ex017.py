from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1 / 2)
print(f'A hipotenusa vai medir {hi:.2f}')

# Agora usando o módulo
# import math

# him = math.hypot(co, ca)
him = hypot(co, ca)
print(f'A hipotenusa vai medir {him:.2f}')
