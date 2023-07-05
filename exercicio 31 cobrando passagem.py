print('-=-' * 10)
print('         RODO RÁPIDO ')
print('-=-' * 10)
print('      Compre sua passagem')
print('-' * 30)
distancia = float(input('Insira a distância da sua viagem em KM: '))
valor = 0
if distancia < 200:
    print(f'O valor da viajem é : R$ {distancia * 0.50 :.2F}')
else:
    print(f'O valor da sua viagem é : R${distancia * 0.45 :.2F}')

print('AGRADECEMOS A PREFERÊNCIA E BOA VIAGEM !!!')