# Inicializando as variáveis
soma_idade = 0
media_idade = 0
maior_idade_homem = 0
nome_homem_mais_velho = ''
mulher_menos_20 = 0

# Lendo e analisando os dados
for p in range(1,5):
    print('----- {}ª PESSOA -----'.format(p))
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip()
    soma_idade += idade
    if p == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        nome_homem_mais_velho = nome
    if sexo in 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_homem_mais_velho = nome
    if sexo in 'Ff' and idade < 20:
        mulher_menos_20 += 1
media_idade = soma_idade/4

# Apresentando os resultados
print('\nA média da idade do grupo é de {} anos.'.format(media_idade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maior_idade_homem,nome_homem_mais_velho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(mulher_menos_20))
