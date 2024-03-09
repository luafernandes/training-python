print('='*25)
print('PROGRESSÃO ARITMÉTICA')
print('='*25)

termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
c = 1
while c <= 10:
    print('{} ⮕  '.format(termo), end='')
    termo += razao
    c += 1
print ('ACABOU')
