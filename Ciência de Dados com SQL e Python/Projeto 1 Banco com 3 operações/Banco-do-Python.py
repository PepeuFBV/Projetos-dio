dinheiroTotal = 0
opcao = 1
fim = False
extratoFinal = ""
linha = "============================================================"
menu = linha+"""\n
            Banco do Python
            
    [1] - Deposito
    [2] - Saque
    [3] - Extrato
    [0] - Sair
    
\n
"""+linha
nSaque = 0
while opcao != 0:
    
    print(menu)
    opcao = int(input("\nQual a operação que deseja realizar? --> "))
    
    if opcao == 1:
        print(linha)
        d = float(input("\nQual o valor que deseja depositar? --> R$"))
        if d <= 0:
            print("\nPor favor insira um valor válido!")
        else:
            dinheiroTotal += d
            extratoFinal += f"Depósito: R${d:.2f}\n"
    elif opcao == 2:
        print(linha)
        if nSaque == 3:
            print("\nVocê já estorou o seu limite (3) de saques diário! Escolha outra opção!")
        else:
            s = float(input("\nQual o valor que deseja sacar? --> R$"))
            if s > 500:
                confirmacao = input("\nO valor máximo do saque é de R$500,00 reais!")
            elif s > dinheiroTotal:
                if dinheiroTotal > 0:
                    msg = f"\nNão há dinheiro suficiente na sua conta! Deseja sacar o dinheiro total da conta (R${dinheiroTotal:.2f})? --> S/N"
                    confirmacao = input(msg)
                    confirmacao = confirmacao.upper()
                    if confirmacao == 's':
                        dinheiroTotal = 0
                        nSaque += 1
                        extratoFinal += f"Saque: R${s:.2f}\n"
            else:
                dinheiroTotal -= s
                nSaque += 1
                extratoFinal += f"Saque: R${s:.2f}\n"
    elif opcao == 3:
        print("\n"+linha)
        print("\n                    EXTRATO")
        print("\nNão foi realizada nenhuma operação na conta!" if not extratoFinal else extratoFinal)
        print(f"\nSaldo atual R${dinheiroTotal:.2f}")
        print(linha+"\n")
    elif opcao == 0:
        print("\nSaindo...")
    else: 
        print("\nOpção inválida! Escolha uma opção válida!")       