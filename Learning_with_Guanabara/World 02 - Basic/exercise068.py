from random import randint
from time import sleep
soma = ganhou = 0
opcao = ''
print('='*25)
print('JOGANDO PAR OU ÍMPAR')
print('='*25)
while True:
    jog = int(input('Digite um número entre 0 e 10: '))
    while jog < 0 or jog > 10:
        jog = int(input('Número inválido! Digite um número entre 0 e 10: '))
    comp = randint(0,10)
    soma = comp + jog
    opcao = input('Par ou Ímpar? ').strip().upper()[0]
    print(f'Você jogou {jog} e o computador jogou {comp}.')
    sleep(1)
    print(f'A soma é de {soma} -> ', end='')
    print('DEU PAR' if soma % 2 == 0 else 'DEU ÍMPAR')
    if opcao == 'P':
        if soma % 2 == 0:
            print('Você venceu!')
            ganhou += 1
        else:
            print('Você perdeu!')
            print(f'GAME OVER! Você venceu {ganhou} vezes.')
            break
    elif opcao in 'IÍ':
        if soma % 2 == 1:
            print('Você venceu!')
            ganhou += 1
        else:
            print('Você perdeu!')
            print(f'GAME OVER! Você venceu {ganhou} vezes.')
            break