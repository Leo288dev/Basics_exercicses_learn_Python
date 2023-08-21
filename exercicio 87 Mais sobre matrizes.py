#Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados. ------------------------------------------------ ok
# B) A soma dos valores da terceira coluna. ----------------------------------------------------- ok
# C) O maior valor da segunda linha.
# num = 0
# pares = 0
# maiorValor = []
# matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# for l in range(0, 3):
#     for c in range(0, 3):
#         matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
# print('-=' * 30)
# for l in range(0, 3):
#     for c in range(0, 3):
#         print(f'[{matriz[l][c]:^5}]', end='')
#     print()
# #----------------------------------------------------------------------------------------------------------------------
# for l in range(0, 3):                                            # soma dos pares
#     for c in range(0, 3):
#         if matriz[l][c] % 2 == 0:
#             pares += matriz[l][c]
#
#
# #----------------------------------------------------------------------------------------------------------------------
# soma = matriz[0][2] + matriz[1][2] + matriz[2][2]               # soma da terrceira coluna
# #----------------------------------------------------------------------------------------------------------------------
#                                                                 # Maior valor da segunda linha
# maiorValor.append(matriz[1][0])
# if matriz[1][1] > maiorValor[0]:
#     maiorValor.append(matriz[1][1])
#     maiorValor.pop(0)
#
# if matriz[1][2] > maiorValor[0]:
#     maiorValor.append(matriz[1][2])
#     maiorValor.pop(0)
# #----------------------------------------------------------------------------------------------------------------------
# print('-=' * 30)
# print(f'A soma dos pares é {pares}')
# print(f'A soma da terceira coluna é {soma}')
# print(f'O maior valor da segunda linha é: {maiorValor[0]}')


#----------------------------------------------------------------------------------------------------
#                         ####### RESOLUÇÃO GUANABARA ########
#---------------------------------------------------------------------------------------------------
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = tcol = tcolsub = simp = men = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite o valor para a matriz [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0: #------------------------------ SOMA DOS PARES E IMPARES -----------------------------
            spar += matriz[l][c]
        if matriz[l][c] % 2 == 1:
            simp += matriz[l][c]
    print()
#-----------------------------------------------------------------------------------------------------------------------
#--------------------------------------- SOMA E SUBTRAÇÃO DA TERCEIRA COLUNA -------------------------------------------
for l in range(0, 3):
    tcol += matriz[l][2]
    tcolsub -= matriz[l][2]
#-----------------------------------------------------------------------------------------------------------------------
#----------------------------------------- MAIOR E MENOR DA SEGUNDA LINHA ----------------------------------------------
for c in range(0, 3):
    if matriz[1][c] > mai:
        mai = matriz[1][c]
    men = matriz[1][0]
    if matriz[1][c] < men:
        men = matriz[1][c]
#-----------------------------------------------------------------------------------------------------------------------
print(f'A soma dos pares é: {spar}')
print(f'A soma dos Ímpares é:{simp}')
print(f'A soma da terceira coluna é: {tcol}')
print(f'A subtração da terceira coluna é: {tcolsub}')
print(f'O maior valor da segunda linha é: {mai}')
print(f'O menor valor da segunda linha é: {men}')
