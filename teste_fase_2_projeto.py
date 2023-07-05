import textwrap

deposito = 0
saque = 0
saldoDep = []
saldoSaq = []
extrato = 0
cont = 0

#---------------------------------------------------BLOCO MENU INICIAL -------------------------------------------------
def menu():
    menu = """\n
    =============MENU===========
    [d] \tDeposotar 
    [s] \tSacar
    [e] \tExtrato
    [nc] \tNova Conta
    [lc] \tListar Contas
    [nu] \tNovo Usuário
    [q] \tSair"""
    return input(textwrap.dedent(menu))
#----------------------------------------------------MENU PRINCIPAL-----------------------------------------------------
def main():
    LIMITE_SAQUE = 3
    AGENCIA = '0001'

    saldo = 0
    limite = 500
    extrato = ''
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == 'd':
            valor = float(input('Informe o Valor do Depósito: '))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == 's':
            valor = float(input('Informe o Valor do Saque: '))
            saldo, extrato = sacar(saldo = saldo,
                                   valor = valor,
                                   extrato = extrato,
                                   limite = limite,
                                   numero_saques = numero_saques,
                                   Limite_saques = LIMITES_SAQUES,
               )

        elif opcao == 'e':
            exibir_extrato(saldo, extrato = extrato)

        elif opcao == 'nu':
            criar_usuarios(usuarios)

        elif opcao == 'nc':
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
        elif opcao == 'lc':
            listar_contas(contas)


        elif opcao == 'q':
            break

        else:
            print('Operação Inválida, por favor selecione novamente a operaçãoo desejada.')

#------------------------------------------------ BL DEPÓSITO ------------------------------------------------------
def depositar(saldo, valor, extrato,/):
    if valor > 0:
        saldo += valor
        extrato += f'Depósito:\tR$ {valor:.2f}\n'
        print('\n=== Depósito realizado com sucesso ! ===')
    else:
        print('\n @@@ Não realizada a operação Falha !!! O valor informado é inválido !!! @@@')

    return saldo, extrato
#--------------------------------------------------BL SACAR ------------------------------------------------------------
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print('\n @@@ Operação Falhou ! Você não te saldo suficiente. @@@')

    elif excedeu_limite:
        print('\@@@ Operação Falhou! O valor do saque excede o limite. @@@')

    elif excedeu_saques:
        print('\n@@@Operação falhou !!! Número máximo de sauqes excedido. @@@')

    elif valor > 0:
        saldo -= valor
        extrato += f'Saque: \t\tR$ {valor:.2f}\n'
        numero_saques += 1
        print('\n=== Saque realizado com sucesso !!! ===')

    else:
        print('\n@@@ Operação falhou ! O valor informado é inválido. @@@')

    return saldo, extrato

