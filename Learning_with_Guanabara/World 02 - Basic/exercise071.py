valor = int(input('Quanto você quer sacar? R$'))
montante = valor
cedula = 50
total_cedula = 0
while True:
    if montante >= cedula:
        montante -= cedula
        total_cedula +=1
    else:
        if total_cedula > 0:
            print(f'Total de {total_cedula} cédulas de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        total_cedula = 0
        if montante == 0:
            break
