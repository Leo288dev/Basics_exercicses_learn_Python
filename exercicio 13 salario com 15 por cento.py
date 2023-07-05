#Exercício Python 13: Faça um algoritmo que leia
# o salário de um funcionário e mostre seu novo
# salário, com 15% de aumento.

# salario = float(input('Digite seu salário: R$  '))
# acrescimo = salario * 0.15
# novoSalario = salario + acrescimo
# print('-' * 60)
# print('********** REAJUSTE SALARIAL ***********')
# print('-' * 60)
# print(f'Salário atual R$ {salario :.2f}, acréscimo R$ {acrescimo :.2f}')
# print(f'Salário com reajuste de 15% R$ {novoSalario :.2f}')
# print('-' * 60)

preco = float(input('Insira o valor: R$ '))
avista = preco - (preco * 5 / 100)  # método para calcular porcentagem
aprazo =  preco + (preco * 8 /100)
print (f'Valor à vista com 5% de desconto é: R$ {avista :.2f}')
print(f'O valor à prazo com 8% de acréscimo é: R$ {aprazo :.2f}')