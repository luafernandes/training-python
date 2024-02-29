# Exercício para verificar as primeiras letras de um texto
# A cidade que você nasceu, começa com 'Santo'?
cidade = input('Digite a cidade em que você nasceu: ').strip()
print(cidade[:5].capitalize() == 'Santo')