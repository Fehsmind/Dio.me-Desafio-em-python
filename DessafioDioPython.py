menu = '''

[D] Deposito
[S] Saque
[E] Extrato
[Q] Sair


=> '''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "D":
        valor = float(input("Informe o valor do deposito: "))

        if valor > 0:
            saldo =+ valor
            extrato =+ f"deposito: R$ {valor:.2f}\n"

        else:
            print("Operacao falhou, tente novamente")

    elif opcao == "S":
        valor = float(input("Informe valor do saque: "))

        excedeu_saldo = valor > valor
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operacao falhou, tente novamente")

        elif excedeu_limite:
            print("Operacao falhou, tente novamente")

        elif excedeu_saques:
            print("operacao falhou, tenmte novamente")
        
        elif valor > 0:
            saldo -+ valor
            extrato += f"saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operacao falhou, tente novamente")

    elif opcao == "E":
        print("\n EXTRATO")
        print("Nao fotam realizado movimtentação" if not extrato else extrato)
        print(f"\n Saldo: R$ {saldo:.2f}")
        print("=======================")

    elif opcao == "Q":
        break
    
    else:
        print("Operação invalida, tente novamente outra opção!")