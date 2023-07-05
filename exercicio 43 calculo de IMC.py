#Exercício Python 43: Desenvolva uma lógica que
# leia o peso e a altura de uma pessoa, calcule seu Índice
# de Massa Corporal (IMC) e mostre seu status, de acordo
# com a tabela abaixo:
#– IMC abaixo de 18,5: Abaixo do Peso
#– Entre 18,5 e 25: Peso Ideal
#– 25 até 30: Sobrepeso
#– 30 até 40: Obesidade
#– Acima de 40: Obesidade Mórbida
from time import sleep
print('-' * 60)                                 #Cabeçalho
print('IMC - ÍNDICE DE MASSA CORPORAL')
print('-' * 60)
print('')
#--------------------------------------------------------------------------------------------------------------------
print('IMC abaixo de 18,5: Abaixo do Peso \n'       # índice de classificação
    'Entre 18,5 e 25: Peso Ideal\n'
'25 até 30: Sobrepeso\n'
'30 até 40: Obesidade\n'
'Acima de 40: Obesidade Mórbida')
print('=-' * 30)
print('')
#---------------------------------------------------------------------------------------------------------------------

peso = float(input('Insira seu PESO(Kg): '))
altura = float(input('Insira sua ALTURA (metros): '))
sleep(2)
imc = peso / (altura ** 2)
print(f'Seu IMC é {imc :.1f}')
if imc < 18.5:
    print('Seu ÍNDICE DE MASSA CORPORAL  está ABAIXO do ideal')
elif imc >= 18.5 and imc < 25:
    print('Seu ÍNDICE DE MASS CORPORAL está DENTRO do ideal')
elif imc <= 25 and imc < 30:
    print('Seu ÍNDICE DE MASSA CORPORAL está com SOBREPESO')
elif imc <= 30 and imc < 40:
    print('Sei ÍNDICE DE MASSA CORPORAL está com OBESIDADE')
else:
    print('Seu INDICE DE MASSA CORPORAL está ACIMA DE 40 está com OBESIDADE MÓRBIDA')

