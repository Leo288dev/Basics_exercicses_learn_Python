# num = [1, 2, 3, 4, 5]
# print(f'Lista impressa {num}')
# num.append(6)
# print(f'Lista {num} com APPEND adição do número 6')
# num.insert(0, 0)
# print(f'Lista  {num} INSERT inseriu zero na posição zero')
# num.pop()
# print(f'Lista POP s/ parâmetro remove o último ítem da lista {num}')
# num.pop(0)
# print(f'Lista POP[0]{num} removeu o ítem da lista no índice zero')
# num.sort()
# print(f'a função SORT ordena a lista {num}')
# num.sort(reverse=True)
# print(f'SORT REVERSE inverte os valores nos índices{num}')
# print(f'Esta lista possui {len(num)} elementos')
# num.insert(2, 0)
# print(f'INSERT (2, 0 ) vai inserir o numero 2 na posição zero{num}')
# num.pop()
# print(f'A função POP() {num}s/ parametro remove o ultimo otem do elemento')
# num.insert(2, 2)
# print(f'O insert (2, 2) insere duas vezes o num 2 na lista{num}')
# num.remove(2)
# print(f'O remove(2) verifica na lista a primeira ocorrencia e a retira da lista {num}')
# if 10 in num :
#     num.remove(10)
#     print(f'Em caso de tentativa de exclusão de itens que não constam na lista gerará erro\n'
#           f'para isso é necessário a condicionaç IF estruturada')
# else:
#     print(f'Em caso de tentativa de exclusão de itens que não constam na lista gerará erro\n'
#           f'para isso é necessário a condicional IF estruturada')
#     print(f'O número 10 não conta em lista {num}')

# lista = []
# lista.append(5)
# lista.append(9)
# lista.append(4)
#
# for c, v in enumerate(lista):
#     print(f'Na posição {c} encontrei o valor são: {v}')
# print('Cheguei ao final da lista.')

valores = list()
for cont in range(0,5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista !')
