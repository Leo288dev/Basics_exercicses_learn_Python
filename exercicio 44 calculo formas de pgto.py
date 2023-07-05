#Exercício Python 44: Elabore um programa que calcule o valor a ser pago
# por um produto, considerando o seu preço normal e condição de pagamento:
#– à vista dinheiro/cheque: 10% de desconto
#– à vista no cartão: 5% de desconto
#– em até 2x no cartão: preço normal
#– 3x ou mais no cartão: 20% de juros
print('_-' * 20)
print('{:^30}'.format('LOJAS ABREU'))
print('{:^30}'.format('se vc não recebeu nem eu'))
print('_-' * 20)


print('-' * 30)
print('Formas de Pagamento: \n'
      ' [1] à Vista/ Cheque  10% de desconto\n'
      ' [2] à vista no cartão 5% de desconto \n'
      ' [3] Parcelado 2x Sem juros \n'
      ' [4] Parcelado 3x ou mais  com acréscimo de 20%')
print('-' * 30)

produto = float(input('Insira o valor da compra R$: '))
condicoes  = int(input('Insira a condição de Pagamento: '))

aVista_Cheque = produto - (produto * 0.10)  #menos 10%

parcelaDuas = produto / 2

avista_cartao = produto - (produto * 0.05) #menos 5%

parceladoTres = produto + (produto * 0.20) #mais 20%

parcela_Juros = parceladoTres / 3

if condicoes == 1:
      print (f'O valor à ser pago é de R$ {aVista_Cheque :.2f} Reais à vista DINHEIRO/CHEQUE com 10% de DESCONTO')

elif condicoes == 2:
      print(f'O valor à ser pago com 5% de DESCONTO é de R${avista_cartao :.2f} Reais à vista no CARTÃO')

elif condicoes == 3:
      print (f' O Valor de R${produto :.2f} parcelado em 2x será de R${parcelaDuas :.2f} Reais por parcela SEM JUROS')

elif condicoes == 4:
      parcelas = int(input('Digite o número de parcelas: '))
      print(f'O valor do produto  R${produto :.2f} parcelado em {parcelas}x com ACRÉSCIMO DE 20% ficará R${produto  + (produto * 0.20):.2f} no Total e ,\n '
            f'cada parcela no valor de R${produto/parcelas + (produto * 0.20/parcelas):.2f} Reais por mês.')
else:
      print('Digite uma das opções entre 1 e 4 para escolher a forma de pagamento mais adequada para seu orçamento')