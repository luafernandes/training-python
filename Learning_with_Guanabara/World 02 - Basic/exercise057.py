# Validando dados usando WHILE
sexo = input('Digite o sexo: [F/M] ').strip().upper()[0]
while sexo not in 'MF':
    sexo = input('Dados inválidos! Por favor informe o sexo: [F/M] ').strip().upper()[0]
print('Sexo {} registrado com sucesso.'.format(sexo))
