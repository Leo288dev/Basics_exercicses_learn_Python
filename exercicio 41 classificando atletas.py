#Exercício Python 041: A Confederação Nacional de Natação precisa
# de um programa que leia o ano de nascimento de um atleta e mostre
# sua categoria, de acordo com a idade:
#– Até 9 anos: MIRIM
#– Até 14 anos: INFANTIL
#– Até 19 anos: JÚNIOR
#– Até 25 anos: SÊNIOR
#– Acima de 25 anos: MASTER
print('-' * 60)
print('CONFEDERAÇÃO NACIONAL DE NATAÇÃO')
print('-' * 60)
from datetime import date

ano = int(input('Insira seu ano de nascimento: '))
anoAtual = date.today().year
categoria = anoAtual - ano
print(f'Sua idade é: {categoria}, Anos')
if categoria <= 9:
    print('Sua categoria é: MIRIM')
elif categoria <= 14:
    print('Sua categoria é: INFANTIL')
elif categoria <=19 :
    print('Sua categoria é: JÚNIOR')
elif categoria <= 25:
    print('Sua categoria é SÊNIOR')
else:
    print('Sua categoria é: MASTER')
