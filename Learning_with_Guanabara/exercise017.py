# Sem a biblioteca math
co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))
hip = ((co ** 2) + (ca ** 2)) ** (1/2)
print('O valor da hipotenusa é {:.2f}'.format(hip))

# Usando a biblioteca math
import math
co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))
hip = math.hypot(co,ca)
print('O valor da hipotenusa é {:.2f}'.format(hip))