#Exercício Python 34: Escreva um programa que pergunte o salário de
# um funcionário e calcule o valor do seu aumento. Para salários
# superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores
# ou iguais, o aumento é de 15%.

print('=-' * 30)
print('               PROJEÇÃO SALARIAL POR FAIXAS')
print('=-' * 30)

salario = float(input('Digite o salario à ser ajustado: '))

if salario <= 1250:
    ajuste = salario * 0.15
    reajuste = salario + ajuste
    print(f'O valor de ajuste é: R${ajuste :.2f} equivalente à 15%')
    print(f'O salario de R${salario :.2f} foi ajustado para R${reajuste :.2f}')

else:
    ajuste = salario * 0.10
    reajuste = salario + ajuste
    print(f'O valor de ajuste é: R${ajuste :.2f} equivalente à 10%')
    print(f'O salario de R${salario :.2f} foi ajustado para R${reajuste :.2f}')