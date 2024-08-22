menu = "\nBem vindo ao Sistema Bancário selecione uma opção:\n [1] Depositar \n [2] Sacar \n [3] Extrato \n [0] Sair\n"

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "1":
        print("Opção selecionada : DEPÓSITO")
        valor = float(input("Informe o valor para depósito: \n"))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
             print("Operação falhou! O valor informado é inválido...\n")
             
    
    elif opcao == "2":
        valor = float(input("Informe o valor para saque:\n "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente...\n")
            
        
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o seu limite...\n")
        
        elif excedeu_saques:
            print("Operação falhou! Você ultrapassou o limite diário de saque...\n")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques +=1
        
        else:
            print("Operação falhou! O valor informado é inválido...\n")
    
    elif opcao == "3":
        print("\n========== EXTRATO ==========")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\n Saldo: R$ {saldo:.2f}")
        print("\n=============================")
    
    elif opcao == "0":
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida, por favor selecione novamente a opção desejada...")