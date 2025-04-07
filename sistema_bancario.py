
saldo = 2000
LIMITE_SAQUE = 3
movimentacao_conta = f''''''


def MENU(escolha):
    match escolha:
        case 1:
            MOSTRAR_EXTRATO()
            SUB_MENU_PARA_SAIR()

        case 2:
            valor_deposito = int(input('Digite o valor do seu deposito: '))
            if valor_deposito >= 0:
                DEPOSITO(valor_deposito)
                SUB_MENU_PARA_SAIR()
            else:
                print("Valor inválido para deposito!")
                SUB_MENU_PARA_SAIR()

        case 3:
            valor_saque = int(input('Digite o valor que deseja sacar: '))
            if valor_saque > 0:
                SACAR(valor_saque)
                SUB_MENU_PARA_SAIR()
            else:
                print(f'Valor inválido! \n')
                SUB_MENU_PARA_SAIR()


def CHAMAR_MENU():
    menu = int(input(f'''
                 ### Bem Vindo ao Seu Banco! ###
                 
                    [1] Extrato
                    [2] Deposito
                    [3] Sacar
                 
                    [0] Sair
                 '''))
    return menu


def SUB_MENU_PARA_SAIR():
    sub_menu_para_sair = int(input(
        f''' 
                     [1] Voltar para o menu anterior

                     [0] Sair
                                      '''))
    if sub_menu_para_sair == 1:
        MENU(CHAMAR_MENU())


def MOSTRAR_EXTRATO():
    global saldo
    global LIMITE_SAQUE
    global movimentacao_conta
    print(f'''
           ### Extrato da Conta ###

                Saldo: {saldo:.2f}

                Limite de Saque: {LIMITE_SAQUE}
                Movimentação da conta:
{movimentacao_conta}
           ''')


def DEPOSITO(acrecentar):
    global saldo
    global movimentacao_conta

    saldo += acrecentar
    movimentacao_conta += f'''Deposito: {acrecentar:.2f} R$ \n'''
    print(f"Seu novo saldo disponível é: {saldo:.2f}R$")


def SACAR(diminuir):
    global saldo
    global LIMITE_SAQUE
    global movimentacao_conta

    if LIMITE_SAQUE > 0:
        LIMITE_SAQUE -= 1
    else:
        print("Você atingiu o limite de saque diario!\n")

    if diminuir <= saldo:
        saldo -= diminuir
        movimentacao_conta += f'Saque: {diminuir:.2f} R$ \n'
        print(f"Seu saldo disponível é: {saldo: .2f}R$")
    else:
        print(f"Não foi possivel realizar a oprecação! ")


def CHECAGEM(valor):
    global saldo
    global LIMITE_SAQUE

    if LIMITE_SAQUE > 0:
        LIMITE_SAQUE -= 1
    else:
        print("Você atingiu o limite de saque diario!\n")
        return False

    if valor <= saldo:
        return True
    else:
        print(
            f'Não foi possivel realizar operação! \nO valor disponível na sua conta e: {saldo}')


MENU(CHAMAR_MENU())
