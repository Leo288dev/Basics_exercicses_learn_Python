# Crie um programa que vai ler vários números e colocar em uma lista. ------------------------------ ok
# Depois disso, mostre:
# A) Quantos números foram digitados.          ------------------------------------------------------ ok
# B) A lista de valores, ordenada de forma decrescente. --------------------------------------------- ok
# C) Se o valor 5 foi digitado e está ou não na lista.
N = []
while True:
    n = int(input('Insira um valor:'))
    print(f'Número {n} inserido na lista com sucesso !!! ')
    N.append(n)
    menu = input('Deseja continuar ??? [S/N]').upper()
    if menu == 'N':
        break
N.sort(reverse=True)
#---------------------------------------------------------------------
print('-=' * 20)
print(f'Os números digitados foram {N}')
print(f'Foram digitados {len(N)} Números e inseridos na lista.')
if 5 in N:
    print('O valor 5 consta na lista !!!')
else:
    print('O valor 5 NÃO consta na lista !!!')
print('-=' * 20)
