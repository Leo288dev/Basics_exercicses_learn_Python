def notas(*notas, sit=True):
    '''

    :param notas: Insere as notas do aluno separado por vírgula, soma e tira média, apresenta maior e menor nota.
    :param sit: Se True printa a situação do aluno baseado nas suas médias
    :return: retorna varios parâmetros
    '''
    n = {*notas}
    Maior = 0
    Menor = 10
    total = len(n)
    for nota in n:
        if nota > Maior:
            Maior = nota

    for nota in n:
        if nota < Menor:
            Menor = nota

    media = (sum(n)) / len(n)


    if sit == True:
        if media < 6:
           sit = 'RUIM'
        elif media > 6 and media < 7:
           sit = 'REGULAR'
        else:
           sit = 'BOA'
        tot = {'Total': total, 'Maior': Maior, 'Menor': Menor, 'Média': media, 'Situação': sit}
        print(tot)
    else:
        if sit == False:
            tot = {'Total': total, 'Maior': Maior, 'Menor': Menor, 'Média': media}
            print(f'Total: {tot}')





# PROGRAMA PRINCIPAL
notas(5.5, 6.5, 8, 10, sit=False)


