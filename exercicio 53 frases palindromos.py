#Exercício Python 53: Crie um programa que leia uma frase qualquer
# e diga se ela é um palíndromo, desconsiderando os espaços

#--------------------------------------------------------------
                        #método usando FOR
#--------------------------------------------------------------

# frase = str(input('Insira uma frase: ')) .strip().upper() # strip remove espaços , upper todas as letras maiúscula
# palavra = frase .split() #cria uma lista das palavras na frase
# junto = ''.join(palavra) # join remove todos os espaços da palavra
# inverso = ''
# for letra in range(len(junto) -1,-1,-1):
#     inverso += junto[letra]
# if inverso  == junto:
#     print('TEMOS UM PALÍNDROMO')
# else:
#     print('NÃO TEMOS UM PALÍNDROMO NA FRASE DIGITADA')
# print(f'O inverso de {junto} é {inverso} ')

#-----------------------------------------------------------------------
        #método utilizando o fatiamento removendo o laço for
#-----------------------------------------------------------------------

frase = str(input('Insira uma frase: ')) .strip().upper() # strip remove espaços , upper todas as letras maiúsculas
palavra = frase .split() #cria uma lista das palavras na frase
junto = ''.join(palavra) # join remove todos os espaços da palavra
inverso = junto[::-1]
if inverso  == junto:
    print('TEMOS UM PALÍNDROMO')
else:
    print('NÃO TEMOS UM PALÍNDROMO NA FRASE DIGITADA')
print(f'O inverso de {junto} é {inverso} ')