
lista = []
while True:
    n = int(input('Insira o valor: '))
    if n not in lista:
        lista.append(n)
        print('-' * 30)
        print(f'O Número {n} foi inserido na lista!!')
        print('-' * 30)
    else:
        print('=' * 60)
        print('Número já existente na lista não será adicionado !!!')
        print('=' * 60)


    cont = str(input('Deseja inserir outro valor : [S/N]: ')).upper().strip()
    while cont not in 'SN':
        cont = str(input('Insira apenas [S=Sim/N=Não]: ')).upper().strip()

    if cont == 'N':
        break
lista.sort()
print(f'Os Valores Inseridos na lista foram: {lista}')

