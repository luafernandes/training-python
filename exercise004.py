valor = input('Digite algo: ')
print('O tipo primitivo desse valor é', type(valor))
print('Só tem espaços?', valor.isspace())
print('É um número?', valor.isnumeric())
print('É alfabético?', valor.isalpha())
print('É alfanumérico?', valor.isalnum())
print('Está em maiúscula?', valor.isupper())
print('Está em minúscula?', valor.islower())
print('Está capitalizada?', valor.istitle())