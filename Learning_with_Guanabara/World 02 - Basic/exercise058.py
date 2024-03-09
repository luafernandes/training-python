from random import randint
comp = randint(0, 10)
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')
acertou = False
tentativa = 0
while not acertou:
    jog = int(input('Qual o seu palpite? '))
    tentativa += 1
    if jog == comp:
        acertou = True
    else:
        if jog < comp:
            print('Mais... Tente novamente!')
        else:
            print('Menos... Tente novamente')
print('Você acertou com {} palpites'.format(tentativa))
