#Escreva um programa para aprovar o empréstimo bancário para a
# compra de uma casa. Pergunte o valor da casa, o salário do comprador
# e em quantos anos ele vai pagar. A prestação mensal não pode exceder
# 30% do salário ou então o empréstimo será negado.

print('=-=' * 40)
print('SIMULADOR DE FINANCIAMENTO BANCO DO POVO')
print('=-=' * 40)
imovel = float(input('Insira o valor do imóvel:R$ '))
salario = float(input('Insira o valor do seu salario:R$ '))
anos = int(input('Insira em quantos anos quer pagar: '))

anos_meses = anos * 12

valorPrestacao = salario * 0.30

compra = valorPrestacao * anos_meses

print('-_-' * 40)
print('Resumo da Proposta')
print('-_-' * 40)
print('' * 40)
print(f'Com base na sua renda o valor da prestação poderá ser até R${valorPrestacao :.2f} Reais')
print(f'A prestação será em: {anos_meses} meses')
print(f'As condições propostas trariam em {anos} anos  o total de R${compra :.2f} Reais')

print('' * 40)
print('_=_' * 40)
print('RESULTADO DA ANÁLISE DE CRÉDITO')
print('_=_' * 40)
print('' * 40)
if imovel <= compra:
    print('Empréstimo Aprovado')
    print('Parabéns seu sonho da casa própria esta mais perto !!!!')
else:
    print('Emprestimo Negado recurso insuficiente para compra')

print('-=-' * 40)
print('CONDIÇÕES MÍNIMAS PARA APROVAÇÃO')
print('' * 40)

print(f'O valor mínimo da prestação considerando o valor do imóvel de:R${imovel :.2f}')
print(f'Considerando o total de {anos} Anos seria de:', (imovel / anos_meses))

