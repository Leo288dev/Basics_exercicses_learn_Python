#Exercício Python 39: Faça um programa que leia o ano de nascimento
# de um jovem e informe, de acordo com a sua idade, se ele ainda vai
# se alistar ao serviço militar, se é a hora exata de se alistar ou se
# já passou do tempo do alistamento. Seu programa também deverá mostrar o
# tempo que falta ou que passou do prazo.
from datetime import date

print('-' * 40)
print('ALISTAMENTO MILITAR')
print('-' * 40)

print('Para iniciar selelcione a opção no menu')
print('')
print('OPÇÕES:\n '
      '[1] MASCULINO \n'
      ' [2] FEMININO')
print('')
sexo = int(input('Digite sua orientação sexual: '))
if sexo == 2:
    print('No Brasil o alistamento é obrigatório somente para o sexo MASCULINO !!!')
while sexo != 2:
     nascimento = int(input('Digite seu ano de nascimento: '))
     anoAtual = date.today().year
     alistamento = anoAtual - nascimento
     saldo = 17 - alistamento
     print(f'Quem nasceu em {nascimento} no ano de {anoAtual} tem ',(anoAtual - nascimento),'Anos')

     if alistamento < 17:
      print('Você ainda vai se alistar !!!')
      print('Faltam',(17 - alistamento),'Anos para isso !!!')
      print(f'Seu alistamento será no ano de',(anoAtual + saldo ))
     elif alistamento <= 18:
      print('Está na hora EXATA de se alistar !!!')
      print(f'Seu ano de alistamento é {anoAtual}')


     else:
      print('Você passou da hora de se alistar !!!')
      print('Você deveria ter se alistado há',(alistamento - 18),'Anos atrás !!!')
      print('Seu ano de alistamento foi',(nascimento + 18))


