nome = input('Digite o seu nome completo: ').strip() # Para retirar os espaços de antes e depois do nome
print('Analisando o seu nome...')
print('Seu nome em maiúsculas é {}'. format(nome.upper()))
print('Seu nome em minúsculas é {}'. format(nome.lower()))
print('Seu nome tem {} letras'.format(len(nome)-nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))