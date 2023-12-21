#Exercício Python 101: Crie um
# [1] programa que tenha uma função chamada voto()------------------------------------------------------------------[ok]
# [2] que vai receber como parâmetro o ano de nascimento de uma pessoa, --------------------------------------------[ok]
# [3] retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições. ----[]


def voto(num=0):
    '''
    -> Função para calcular a idade de uma pessoa e retornar se o
    voto é obrigatório, opcional ou se não vota.
    :param num: insere o ano de nascimento
    :return: cálculo baseado no ano atual consultado por biblioteca datetime
    '''
    from datetime import datetime
    ano = datetime.now()
    atual = ano.year
    idade = atual - n
    if idade < 16:
        print(f'Sua idade é {idade} anos: NÃO VOTA !!! ')
    elif idade == 16 and idade < 18:
        print(f'Sua idade é {idade} anos: VOTO OPCIONAL !!!')
    elif idade >= 18 and idade <= 59:
        print(f'Sua idade é {idade} anos: VOTO OBRIGATÓRIO !!!')
    else:
        print(f'Sua idade é {idade} anos: VOTO OPCIONAL !!!')


n = int(input('Qual sua idade?: '))



