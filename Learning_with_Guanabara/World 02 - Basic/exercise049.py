num = int(input('Digite um número para ver a sua tabuada: '))
print('-' * 15)
print('Tabuada do {}'.format(num))
print('-' * 15)
for c in range(1,11):
    print('{} x {:2} = {}'.format(num, c, num*c))
print('-' * 15)
