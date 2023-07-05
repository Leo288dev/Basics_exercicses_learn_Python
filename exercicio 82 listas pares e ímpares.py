#Exercício Python 082:
# a) Crie um programa que vai ler vários números e colocar em uma lista. ---- ok

# b) Depois disso, crie duas listas extras que vão conter apenas os valores
# pares e os valores ímpares digitados.

# c) Ao final, mostre o conteúdo das três listas geradas.
# ListaP = []
# ListaI = []
# lista = []
# while True:
#     n = int(input('Insira o valor: '))
#     if n % 2 == 0:
#         ListaP.append(n)
#     else:
#         ListaI.append(n)
#     menu = input('Deseja continuar [S/N]: ')
#     if menu in 'Nn':
#         break
# lista.append(ListaP)
# lista.append(ListaI)
# lista.sort()
# print(f'Todos os numeros {lista}')
# print(f'Numeros pares {ListaP}')
# print(f'Numeros Impares{ListaI}')


#-----------------------------------------------------------
# RESOLUÇÃO GUANABARA

num = []
listaP = []
listaI = []
while True:
    num.append(int(input('Digite: ')))
    resp = str(input('Deseja continuar ? S/N: '))
    if resp in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        listaP.append(v)
    else:
        listaI.append(v)
print('-=' * 30)
print(f'Lista Completa {num}')
print(f'Lista Pares {listaP}')
print(f'Lista Ímpares {listaI}')
