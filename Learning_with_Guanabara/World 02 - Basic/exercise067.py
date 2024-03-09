while True:
    num = int(input('Digite um número para ver a sua tabuada: '))
    if num < 0:
        break
    print('-' * 15)
    print(f'Tabuada do {num}')
    print('-' * 15)
    for c in range(1,11):
        print(f'{num} x {c:2} = {num*c}')
print('Programa finalizado!')
