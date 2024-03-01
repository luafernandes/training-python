from random import randint
from time import sleep
print('{:=^40}\n'.format(' GAME: Pedra Papel e Tesoura '))

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)

print('''Suas opções:
[0] Pedra
[1] Papel
[2] Tesoura\n''')

jogador = int(input('Qual a sua jogada? '))
if jogador < 0 or jogador > 2:
    print('Jogada inválida, tente novamente!')
    exit() # Para encerrar o programa

print('\nJO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)

print('-' * 15)
print('O computador escolheu {}'.format(itens[computador]))
print('O jogador escolheu {}'.format(itens[jogador]))
print('-' * 15)

if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('Jogador venceu')
    elif jogador == 2:
        print('Computador venceu')
elif computador == 1:
    if jogador == 0:
        print('Computador venceu')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('Jogador venceu')
elif computador == 2:
    if jogador == 0:
        print('Jogador venceu')
    elif jogador == 1:
        print('Computador venceu')
    elif jogador == 2:
        print('EMPATE')
