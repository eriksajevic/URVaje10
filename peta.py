###INDEKS TELESNE TEŽE###

h = int(input('Visina [cm]? '))
m = int(input('Masa [kg]? '))

bmi = m / (h / 100) ** 2

print(f'Indeks telesne mase: {bmi}')