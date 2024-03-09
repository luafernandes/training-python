print('='*25)
print('SEQUÊNCIA DE FIBONACCI')
print('='*25)

n = int(input('Quantos termos você quer ver? '))
primeiro_termo = 0
segundo_termo = 1
c = 0
while c < n:
    print(primeiro_termo, end=' -> ' if c < n - 1 else ' Acabou')
    prox = primeiro_termo + segundo_termo
    primeiro_termo = segundo_termo
    segundo_termo = prox
    c += 1