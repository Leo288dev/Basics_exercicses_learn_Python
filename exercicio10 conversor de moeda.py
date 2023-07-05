#Exercicio 10 conversor de moedas
# crie um programa que leia o valor que a pessoa tem e mostre qntos dolares
#ela pode comprar considere U$$ 1.00 = R$3.27

carteira = float(input('Digite quanto vc tem na carteira: '))
cotacao = float(input('Digite o valor do Peso argentino: '))
conversor = carteira / cotacao
print(f'Com R$ {carteira :.2f} pode comprar $ {conversor :.2f} pesos argentinos')
print(f'Cotação de R${cotacao} para cada $1.00')