frase = 'Curso em video Python'

print(frase[9]) # Traz o conteúdo da posição 9 na lista

print(frase[9:13])# Traz o conteudo da posição 9 ao 12, o 13 não a aparece por
# ser um intervalo aberto à direita

print(frase[9:21]) # traz da posição 9 à 20 o conteudo dos espaços na memória

print(frase[0:21:3]) # Traz de zero à 21 passo três, ou seja pula 3 casas

print(frase[:5]) # indica  a posição final, ou seja traz o conteúdo
# de zero à 5

print(frase[0:]) # traz o conteudo de zero até a ultima posição da lista

print(frase[9::3])# Traz o conteudo iniciando em 9 até o último espaço
# com passo 3

#------------- COMANDOS ---------------------#

print(frase.count('o')) # traz quantas vezes aparece a string entre parênteses
# na frase

print(frase.count('o', 0, 13)) # Traz no intervalo entre zero e 13 qntas vezes
#aparece a string entre aspas

print(frase.find('deo')) # Traz a posição na lista onde esta sequencia de
# strings está localizada na lista

print('Curso' in frase) # Retorna valor booleano (True ou False) se
# existe a palavra 'Curso na variável frase

print(frase.split()) # Qebra cada palavra em frase, ou seja,  o caso de uma
# lista quebra cada palavra de uma frase em listas. COnsiederando os espaços
# entre as frases.

#----------Junção----------------------#

print(frase.replace('Python','Android')) # altera a palavra solicitada
#provisoriamente nesta intância apenas

# para fazer a subst definitiva fica
frase = frase.replace('Pyhton', 'Android')
# é necessário atribuir para que ocorra a alteração

