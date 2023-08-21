#Exercício Python 094:
# [1] Crie um programa que leia nome, sexo e idade de várias pessoas, ----------------------------- [ok]
# [2] guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.------ [ok]
# No final, mostre:
# [3] A) Quantas pessoas foram cadastradas -------------------------------------------------------- [ok]
# [4] B) A média de idade ------------------------------------------------------------------------- [ok]
# [5] C) Uma lista com as mulheres ---------------------------------------------------------------- [ok]
# [6] D) Uma lista de pessoas com idade acima da média--------------------------------------------- []

lista_principal = []
somaIdade = 0
mulheres = []
acimaMedia = []
while True:
#------------------------------------------------------- cria dicionario e insere dados nele -----------------------------
     dicionario = {}
     dicionario['nome'] = str(input('Nome: '))
     dicionario['sexo'] = str(input('Sexo [F]/[M]: ')).upper()
     while dicionario['sexo'] not in "FM":
          dicionario['sexo'] = str(input('Erro!!! Digite apenas [F]/[M]: ')).upper()
     dicionario['idade'] = int(input('Idade: '))

#----------------------------------------------------- adiciona dict na lista e deleta dict ---------------------------
     lista_principal.append(dicionario)
     del(dicionario)
#----------------------------------------------------- menu continuação -------------------------------------------------
     menu = str(input('Deseja continuar ? [S] ou [N]: ')).upper()
     while menu not in 'SN':
          menu = str(input('Erro !!! Digitar apenas [S] ou [N]: ')).upper()
     if menu == 'N':
        break
#--------------------------------------------------- soma e media das idades -------------------------------------------
for p, v in enumerate(lista_principal):                             # laço que soma e tira média das idades cadastradas
     somaIdade += (lista_principal[p]['idade']) / len(lista_principal)

#-------------------------------------------------- imprimir mulheres cadastradas --------------------------------------
for l, s in enumerate(lista_principal):
     if lista_principal[l]['sexo'] == 'F':
          mulheres.append(lista_principal[l]["nome"])
#----------------------------------------------------- idades acima da média -------------------------------------------
for i, m in enumerate(lista_principal):
     if lista_principal[i]['idade'] > somaIdade:
          acimaMedia.append(lista_principal[i]['nome'])
          acimaMedia.append(lista_principal[i]['sexo'])
          acimaMedia.append(lista_principal[i]['idade'])

#      falta imprimir pessoas com idade acima da media - um for enumerate compArando idade com media resolve  pode add em uma lista e imprimir a lista



print('==< PESSOAS CADASTRADAS >==')
print()
print(lista_principal)
print(f'Foram cadastrados {len(lista_principal)} pessoas na lista')
print(f'A MÉDIA DAS IDADES é: {somaIdade :.2f} Anos')
print(f'As MULHERES CADASTRADAS foram {mulheres}', end='')
print()
print(f'Pessoas cadastradas com idade ACIMA DA MÉDIA são: {acimaMedia}')
print()
print('==< PROGRAMA ENCERRADO >==')
