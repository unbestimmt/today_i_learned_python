# Bank system v2.0
# Sistema bancário v2.0

def cadastrar_usuario (lista_de_usuarios):
    nome = input("Digite seu nome completo: ")
    data_nascimento = input("Qual sua data de nascimento? (dia/mês/ano) ")
    cpf = input("Qual seu CPF? (Digite apenas números) ")
    endereco = input("Qual seu endereço? (Logradouro, n. - Bairro - Cidade/Sigla do Estado) ")

    usuario = filtrar_usuario(cpf, lista_de_usuarios)

    if usuario:
        print("Usuário já existente.")
    
    else:
        lista_de_usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
        print("Seja bem-vindo(a)!")

def filtrar_usuario(cpf, lista_de_usuarios):
    for usuario in lista_de_usuarios:
        if usuario["cpf"] == cpf:
            return usuario
    return None

def criar_conta_corrente(numero_conta, lista_de_usuarios):
    agencia = "0001"
    cpf = input("Informe o CPF do usuário: ")
    
    usuario = filtrar_usuario(cpf, lista_de_usuarios)

    if usuario:
        print("Sua conta foi criada com sucesso.")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    else:
        print("Usuário não existente.")

def depositar(deposito, saldo, extrato, /):
    if deposito > 0:
        saldo += deposito
        print(f"Depósito de R$ {deposito:.2f} efetuado com sucesso.")
        extrato += f"Depósito: R$ {deposito:.2f}\n"
    else:
        print("Valor inválido.")
    return saldo, extrato

numero_saques = 0

def sacar(*, saque, saldo, extrato):
    global numero_saques
    if numero_saques < 3:
        if saque > 0:
            if saque <= 500:
                if saldo >= saque:
                    saldo -= saque
                    print(f"Saque de R$ {saque:.2f} efetuado com sucesso.")
                    numero_saques += 1
                    extrato += f"Saque: R$ {saque:.2f}\n"
                else:
                    print(f"Não é possível sacar o valor de R$ {saque:.2f}. Saldo insuficiente.")
            else:
                print("O valor do saque excedeu o limite de R$ 500,00.")
        else:
            print("Valor inválido.")
    else:
        print("Você atingiu o seu limite de saques diário.")
    return saldo, extrato

def visualizar_extrato(saldo, /, *, extrato):
    print("-------------------")
    print("Extrato".center(19, " "))
    print()
    print("Não há movimentações bancárias realizadas." if not extrato else extrato)
    print()
    print(f"O saldo da sua conta bancária é de R$ {saldo:.2f}")
    print("-------------------")

def menu():
    saldo = 0
    extrato = ""

    lista_de_usuarios = []
    lista_de_contas = []

    while True:
        print("""
    -------------------
            MENU
        
        1. Criar Usuário
        2. Criar Conta
        3. Depósito
        4. Saque
        5. Extrato
        0. Sair
    -------------------
    """)
        
        opcao = int(input("Digite a opção desejada: "))

        if opcao == 1:
            cadastrar_usuario(lista_de_usuarios)
        
        elif opcao == 2:
            numero_conta = len(lista_de_contas) + 1
            conta = criar_conta_corrente(numero_conta, lista_de_usuarios)
            lista_de_contas.append(conta) if conta else None
        
        elif opcao == 3:
            valor_deposito = float(input("Qual valor gostaria de depositar?\n"))
            saldo, extrato = depositar(valor_deposito, saldo, extrato)


        elif opcao == 4:
            valor_saque = float(input("Qual valor gostaria de sacar?\n"))
            saldo, extrato = sacar(saque = valor_saque, saldo = saldo, extrato = extrato)

            
        elif opcao == 5:
            visualizar_extrato(saldo, extrato = extrato)

        elif opcao == 0:
            print("Saindo do aplicativo...")
            break

        else:
            print("Operação inválida")

menu()