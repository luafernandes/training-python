print('='*25)
print('PROGRESSÃO ARITMÉTICA')
print('='*25)

termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = termo + (10-1) * razao
for c in range(termo, decimo + razao , razao):
    print('{} '.format(c), end='⮕  ')
print ('ACABOU')
