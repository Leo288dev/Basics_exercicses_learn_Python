#Exercício Python 076: Crie um programa que tenha uma
# tupla única com nomes de produtos e seus respectivos
# preços, na sequência. No final, mostre uma listagem
# de preços, organizando os dados em forma tabular.
# lista = ('Lápis',0.50, 'Caneta', 1.20, 'Estojo', 16.50, 'Caderno',23.80, 'Mochila', 230.00, 'Régua', 1.50, 'Borracha', 0.25)
# for l in range(len(lista)):
#    print('=' * 30)
#    print('*** LISTA DE MATERIAIS ***')
#    print('=' * 30)
#    print(f'{lista[0]} ---------------- R$ {lista[1]:.2f}')
#    print(f'{lista[2]} --------------- R$ {lista[3]:.2f}')
#    print(f'{lista[4]} --------------- R$ {lista[5]:.2f}')
#    print(f'{lista[6]} -------------- R$ {lista[7]:.2f}')
#    print(f'{lista[8]} -------------- R$ {lista[9]:.2f}')
#    print(f'{lista[10]} ---------------- R$ {lista[11]:.2f}')
#    print(f'{lista[12]} ------------- R$ {lista[13]:.2f}')
#    break
# print('-' * 50)
# total = lista[1] + lista[3] + lista[5] + lista[7] + lista[9] + lista[11] + lista[13]
# print(f'O TOTAL DA COMPRA FOI: R$ {total :.2f}')
# print('-' * 50)


#RESOLUÇÃO GUANABARA --------------------------------------
listagem = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90, 'Estojo',
            25, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print('-' * 40)
print(F'{"LISTAGEM DE MATERIAIS":^40}')
print('-' * 40)
for pos in range(len(listagem)):
   if pos % 2 == 0:
      print(f'{listagem[pos]:.<30}', end='')
   else:
      print(f'R$ {listagem[pos]:>7.2f}')
print('-' * 40)