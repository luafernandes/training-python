# Exercício para procurar uma string dentro de outra
# Seu nome tem 'Silva'?
nome = input('Digite seu nome completo: ').strip()
print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))