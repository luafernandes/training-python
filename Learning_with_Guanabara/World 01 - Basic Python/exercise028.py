# Jogo de adivinhação
from random import randint
from time import sleep

pc = randint(0, 5)
print('-' * 30)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-' * 30)

jg = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(3)

if jg == pc:
    print('Parabéns! Você acertou!')
else:
    print('Ganhei! Eu pensei no número {} e não no {}!'.format(pc, jg))
