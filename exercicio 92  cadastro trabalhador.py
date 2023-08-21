#Exercício Python 092:
# [1] - Crie um programa que leia nome, ano de nascimento e carteira de trabalho ---------------------------------- ok
# [2] -  e cadastre-o (com idade) em um dicionário. --------------------------------------------------------------- ok
# [3] - Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. -
# [4] - Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.---------------------------
import datetime

anoAtual = datetime.date.today()
cadastro = dict()
cadastro['Nome'] = str(input('Nome do trabalhador: '))
cadastro['Ano'] = int(input('Ano de nascimento: '))
cadastro['Carteira'] = int(input('Número da carteira [0] se não tiver: '))
anosubtracao = anoAtual.year - cadastro['Ano']
cadastro['Idade'] = anosubtracao

if cadastro['Carteira'] != 0:
    cadastro['Data de admissão'] = int(input('Data de admissão: '))
    cadastro['Salario'] = float(input('Salário atual: R$ '))
    admissao = cadastro['Data de admissão']
    cadastro['Aposenta'] = (anoAtual.year - admissao) + anoAtual.year



print('-=' * 25)
print('            == DADOS DO TRABALHADOR ==')
print('-=' * 25)

if cadastro['Carteira'] == 0:
    print(f'Nome do trabalhador: {cadastro["Nome"]}')
    print(f'Idade atual é: {cadastro["Idade"]}')
    print(f'Este trabalhador não possui CTPS !!!')

else:
    print(f'Nome do trabalhador: {cadastro["Nome"]}')
    print(f'Idade atual é: {cadastro["Idade"]}')
    print(f'CTPS Nº:{cadastro["Carteira"]}')
    print(f'Data de admissão: {cadastro["Data de admissão"]}')
    print(f'Salário atual: R$ {cadastro["Salario"]:.2f}')
    print(f'Deverá se aposentar em: {cadastro["Aposenta"]}')

print('-=' * 25)
print('==' * 25)
print('-=' * 25)



