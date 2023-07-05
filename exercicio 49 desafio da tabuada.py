#Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número
# que o usuário escolher, só que agora utilizando um laço for.
print(':-:' * 7)
print('TABUADA DESCOMPLICADA')
print(':-:' * 7)

tabu = int(input('Insira o número que quer a tabuada: '))
cont = 0
for tab in range(1,11):
    cont = cont + 1
    mult = tabu * tab
    print(f' {tabu} X {cont} = {mult}')

#RESOLUÇÃO DO GUANABARA

# num = int(input('Digite o numero: '))
# for c in range(1,11):
#     print(f'{num} X {c} = {num * c}')