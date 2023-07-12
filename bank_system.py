# Bank system
# Sistema bancário

numero_saques = 0
conta = 0
extrato = ""

while True:
    print("""
-------------------
        MENU
    
    1. Depósito
    2. Saque
    3. Extrato
    0. Sair
-------------------
""")
    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        deposito = int(input("Qual valor gostaria de depositar?\n"))
        if deposito > 0:
            conta += deposito
            extrato += f"Depósito: R$ {deposito:.2f}\n"
        else:
            print("Valor inválido.")


    elif opcao == 2:
        if numero_saques < 3:
            saque = int(input("Qual valor gostaria de sacar?\n"))
            if saque > 0:
                if saque <= 500:
                    if conta >= saque:
                        conta -= saque
                        numero_saques += 1
                        extrato += f"Saque: R$ {saque:.2f}\n"
                    else:
                        print(f"Não é possível sacar o valor de {saque}. Saldo insuficiente.")
                else:
                    print("O valor do saque excedeu o limite de R$ 500,00.")
            else:
                print("Valor inválido.")
        else:
            print("Você atingiu o seu limite de saques diário.")

        
    elif opcao == 3:
        print("-------------------")
        print("Extrato".center(19, " "))
        print()
        print("Não há movimentações bancárias realizadas." if not extrato else extrato)
        print()
        print(f"O saldo da sua conta bancária é de R$ {conta:.2f}")
        print("-------------------")

    elif opcao == 0:
        print("Saindo do aplicativo...")
        break

    else:
        print("Operação inválida")