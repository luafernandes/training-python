# Encontrar o primeiro e último nome de uma pessoa
nome = input('Digite o seu nome completo: ').strip()
separa_nome = nome.split()
print('Olá, muito prazer te conhecer!')
print('Seu primeiro nome é {}'.format(separa_nome[0].capitalize()))
print('Seu último nome é {}'.format(separa_nome[len(separa_nome)-1].capitalize()))