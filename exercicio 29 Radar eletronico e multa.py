#Exercício Python 29: Escreva um programa que leia a velocidade de
# um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo
# que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
from time import sleep
velocidade = float(input('Digite a velocidade:  '))
limite = velocidade - 80
multaValor = 7
if velocidade > 80:
   multa = multaValor * limite
   print('Você foi multado, valor em consulta .....')
   sleep(3)
   print(f'O valor da multa é: R${multa :.2f}')

else:
   print('Você está dentro dos limites permitidos !!!')





