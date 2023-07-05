#Exercício Python 075: Desenvolva um programa que
# 1. leia quatro valores pelo teclado e guarde-os em uma tupla.
# No final, mostre:
#A) Quantas vezes apareceu o valor 9. ------------------OK
#B) Em que posição foi digitado o primeiro valor 3. ------------- OK
#C) Quais foram os números pares.

n1 = int(input('Insira o primeiro valor: '))
n2 = int(input('Insira o segundo valor: '))
n3 = int(input('Insira os valor: '))
n4 = int(input('Insira os valor: '))
lista = (n1, n2, n3, n4)
#RESOLUÇÃO 'A' RESOLVIDA __________________________________________________
print('-=' * 20)
print(f'\n[A] O número NOVE apareceu {lista.count(9)} Vez(es)')
print('-=' * 20)
#---------------------------------------------------------------------------
# RESOLUÇÃO B RESOLVIDA ----------------------------------------------------
if 3 not in lista:
    print('O número três não consta na tupla')
else:
    print(f'O número três aparece a primeira vez na {lista.index(3)}ºposição')
print('-=' * 20)
#------------------------------------------------------------------------------
#RESOLUÇÃO C RESOLVIDA_________________________________________________________
for p in lista:
   if p % 2 == 0:
    print(f'Os números pares digitados foram: {p}')
print('-=' * 20)
#-------------------------------------------------------------------------------
