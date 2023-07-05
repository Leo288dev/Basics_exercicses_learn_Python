#Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo
# e a razão de uma PA, mostrando os 10 primeiros termos da progressão
# usando a estrutura while.
# termo = int(input('Insira o termo: '))
# razao = int(input('Insira a razão: '))
# decimo = termo + (11 -1)
# while termo < decimo + 1:
#     print(termo, end='')
#     print(',' if termo < decimo else '.', end='')
#     contagem = termo + razao
#     termo = contagem


print('=-' * 10)
print('Gerador de PA')
print('=-' * 10)

primeiro = int(input('Insira o termo: '))
razao = int(input('Insira a razão: '))
termo = primeiro
cont = 1
while cont <= 10:
    print(f'{termo} - ', end='')
    termo = termo + razao
    cont += 1
print('FIM')

