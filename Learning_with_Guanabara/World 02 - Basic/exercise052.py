num = int(input('Digite um número: '))
total_div = 0
for c in range(1,num+1):
    if num % c == 0:
        print('\033[33m', end=' ')
        total_div += 1 
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} foi divisível {} vezes'.format(num, total_div), end=' ')
if total_div == 2:
    print('e por isso ele é PRIMO')
else:
    print('e por isso ele NÃO É PRIMO')
