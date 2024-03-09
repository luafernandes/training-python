sexo = ' '
cont = ' '
mais_18 = 0
total_homem = 0
mulher_menos_20 = 0
p = 1
print('='*25)
print('CADASTRO DE PESSOAS')
print('='*25)
while True:
    print(f'Dados da {p}ª pessoa')
    idade = int(input('Digite a idade: '))
    if idade >= 18:
        mais_18 += 1
    sexo = input('Digite o sexo: [M/F] ').upper().strip()[0]
    while sexo not in 'MF':
        sexo = input('Dado inválido. Digite o sexo: [M/F] ').upper().strip()[0]
    if sexo == 'M':
        total_homem += 1
    if sexo == 'F' and idade < 20:
        mulher_menos_20 += 1
    cont = input('Você quer continuar? [S/N] ').upper().strip()[0]
    while cont not in 'SN':
        cont = input('Entrada inválida. Você quer continuar? [S/N] ').upper().strip()[0]
    if cont == 'N':
        break
    print('='*25)
    p += 1
print('-'*40)
print(f'Foram cadastradas {mais_18} pessoas com mais de 18 anos.')
print(f'Foram cadastrados {total_homem} homens.')
print(f'Foram cadastradas {mulher_menos_20} mulheres com menos de 20 anos.')
