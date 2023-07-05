#Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário
# se ele quer mostrar mais alguns termos. O programa encerrará quando
# ele disser que quer mostrar 0 termos.

# print('=-' * 10)
# print('Gerador de PA')
# print('=-' * 10)
#
# primeiro = int(input('Insira o termo: '))
# razao = int(input('Insira a razão: '))
# termo = primeiro
# cont = 1
# mais = 10
# total = 0
# while mais != 0:
#     total = total + mais
#     while cont <= total:
#         print(f'{termo} - ', end='')
#         termo = termo + razao
#         cont += 1
#     print('PAUSA')
#     mais = int(input('Quantos termos mais vc quer mostrar ?: '))
# print(f'PROGRAMA ENCERRADO FORAM MOSTRADOS {total} TERMOS...')



#-----------------------------------------------------------------------------------
print('**' * 20)
print('GERADOR DE PA PRATICANDO')
print('**' * 20)

inicio = int(input('Insira o termo: '))
razao = int(input('Insira a razão: '))
cont = 0
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{inicio} -', end='')
        inicio += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos mais quer inserir ?: '))
print(f'PROGRESSÃO ENCERRADA COM {total} TERMOS')