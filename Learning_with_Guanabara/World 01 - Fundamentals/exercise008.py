metro = float(input('Digite uma medida em metros: '))
km = metro / 1000
hm = metro / 100
dam = metro / 10
dm = metro * 10
cm = metro * 100
mm = metro * 1000
print(f'A medida {metro} m corresponde a:')
print(f'Em quilômetro: {km} km')
print(f'Em hectômetro: {hm} hm')
print(f'Em decametro: {dam} dam')
print(f'Em decimetro: {dm} dm')
print(f'Em centímetros: {cm} cm')
print(f'Em milímetro: {mm} mm')