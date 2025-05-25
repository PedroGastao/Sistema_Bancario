from datetime import datetime


saldo = 2000
LIMITE_SAQUE = 3
movimentacao_conta = f''''''
data_e_hora_atual = datetime.now().strftime('%d/%m/%y - %H:%M:%S')
hora = int(datetime.now().strftime('%H'))
numero_Contas = 0
clientes = []


def MENU(escolha):
    global clientes
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

        case 4:
            CRIAR_USUARIO()

        case 5:
            print(clientes)
            SUB_MENU_PARA_SAIR()


def CHAMAR_MENU():
    global data_e_hora_atual
    menu = int(input(f'''
                 ### Bem Vindo ao Seu Banco! ###{data_e_hora_atual}
                 
                    [1] Extrato
                    [2] Deposito
                    [3] Sacar
                    [4] Cadastrar novo cliente
                    [5] Listar Clientes
                 
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
    global data_e_hora_atual

    saldo += acrecentar
    movimentacao_conta += f'''Deposito: {acrecentar:.2f}R$ \n{data_e_hora_atual}\n'''
    print(f"Seu novo saldo disponível é: {saldo:.2f}R$")


def SACAR(diminuir):
    global saldo
    global LIMITE_SAQUE
    global movimentacao_conta
    global hora
    global data_e_hora_atual

    if hora == 6:
        LIMITE_SAQUE = 3
    elif LIMITE_SAQUE > 0:
        LIMITE_SAQUE -= 1
    else:
        print("Você atingiu o limite de saque diario!\n")

    if diminuir <= saldo:
        saldo -= diminuir
        movimentacao_conta += f'Saque: {diminuir:.2f}R$ \n{data_e_hora_atual}\n'
        print(f"Seu saldo disponível é: {saldo: .2f}R$")
    else:
        print(f"Não foi possivel realizar a operação! ")


def CRIAR_USUARIO():
    global numero_Contas
    global clientes

    cpf = int(input("Digite o cpf do novo cadastro: \n "))
    novo_usuario = FILTRAR_USUARIO(cpf, clientes)

    if novo_usuario:
        print('Usuário já cadastrado\n')
        SUB_MENU_PARA_SAIR()

    numero_Contas += 1
    nome_cliente = {'nome': input(
        "Digite o nome do novo cliente: \n"), 'Conta Corrente': numero_Contas, 'cpf': cpf}
    clientes += [nome_cliente]

    MENU(CHAMAR_MENU())


def FILTRAR_USUARIO(cpf, usuarios):
    usuario_filtrado = [
        usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuario_filtrado[0] if usuario_filtrado else None


'''def DADOS_CLIENTES():
    try:
    dados = open('dados_clientes.txt', 'r')

    catch:
    print(dados)
'''

MENU(CHAMAR_MENU())
