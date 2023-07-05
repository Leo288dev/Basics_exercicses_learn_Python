print('=-=' * 10)
print('        CAIXA ELETRÔNICO')
print('     $$$$ BANCO DO POVO $$$$')
print('=-=' * 10)
senha = int(input('Cadastre sua senha: '))
digite = int(input('Digite a senha para acessar os serviços do Banco: '))
conta = 0
menu = 0
while digite != senha:
    digite = int(input('Digite a senha para acessar os serviços do Banco: '))
if digite == senha:
    print('=-=' * 10)
    print('=-=' * 10)
    print('*** MENU ***')
    print('1 - DEPÓSITOS\n'
          '2 - SAQUE\n'
          '3 - SALDO\n'
          '4 -SAIR')
    print('=-=' * 10)
while menu != 4 :
    opcao = int(input('Digite a operação desejada: '))
    if opcao == 1:
        deposito = (float(input('Digite o valor do depíto:R$ ')))
        conta = deposito
        print(f'O saldo da sua conta é R$ {conta :.2f}')
        opcao = int(input('Digite a operação desejada: '))
    elif opcao == 2:
        saque = float(input('Digite o valor do saque: R$'))
        if conta < saque:
            print(f'Saldo insuficiente para realizar a operção seu Saldo é R$ {conta :.2f}!!!')
        else:
            conta = conta - saque
        opcao = int(input('Digite a operação desejada: '))
    elif opcao == 3:
        print(f'Seu saldo é de R$ {conta}')
        opcao = int(input('Digite a operação desejada: '))
    else:
        print('Obrigado por escolher nossos serviços !!!')

print('FIM')