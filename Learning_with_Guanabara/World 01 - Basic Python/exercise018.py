import math
angulo = float(input('Digite o ângulo: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('O ângulo de {} tem: \nSENO de {:.2f} \nCOSSENO de {:.2f} \nTANGENTE de {:.2f}'.format(angulo,seno,cosseno,tangente))