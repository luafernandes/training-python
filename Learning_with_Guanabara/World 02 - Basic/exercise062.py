print('='*25)
print('PROGRESSÃO ARITMÉTICA')
print('='*25)

termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
c = 1
total = 0
mais_termo = 10
while mais_termo != 0:
    total += mais_termo
    while c <= total:
        print('{} ⮕  '.format(termo), end='')
        termo += razao
        c += 1
    print ('PAUSA')
    mais_termo = int(input('Quantos termos você quer mostrar a mais? '))
print('ACABOU')
print('Programa finalizado! Foram mostrados ao todo {} termos.'.format(total))