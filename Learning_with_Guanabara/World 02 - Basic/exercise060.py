# CALCULO DE FATORIAL
# Usando math
from math import factorial
print('- CALCULANDO O FATORIAL -')
num = int(input('Digite o número: '))
fatorial = factorial(num)
print('O fatorial do número {}! é igual a {}.'.format(num, fatorial))

# Usando for
print('- CALCULANDO O FATORIAL -')
num = int(input('Digite um número: '))
fatorial = 1
for c in range(1, num+1):
    fatorial *= c
print('O fatorial de {}! é igual a {}.'.format(num, fatorial))

# Usando while
print('- CALCULANDO O FATORIAL -')
num = int(input('Digite um número: '))
c = num
fatorial = 1
while c > 0:
    fatorial *= c
    c -= 1
print('O fatorial de {}! é igual a {}.'.format(num, fatorial))