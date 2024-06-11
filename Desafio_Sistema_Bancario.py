# DEPOSITO
# SAQUE
# EXTRATO

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


while True:
    opcao = input(menu)

    if opcao == "d":
        print("Deposito")

        valor = float(input("Insira o valor do depósito: R$ "))

        if valor < 1:
            print("\n Insira um valor positivo!")
        else:
            saldo = saldo + valor
            valor = f"{valor:.2f}"
            extrato = extrato + "\n Depósito de R$ " + valor

    elif opcao == "s":
        print("Saque")

        if numero_saques < LIMITE_SAQUES:
            valor = float(input("\n Digite o valor do saque: R$ "))
            if (valor <= saldo):
                if valor <= limite:
                    saldo = saldo - valor
                    extrato = extrato + "\n Saque de R$ " + str(f'{valor:.2f}')
                    numero_saques = numero_saques + 1
                else:
                    print("Valor de saque superior ao limite de R$ 500,00")
            else:
                print("\n Saldo Insuficiente!")
        else:
            print("Você atingiu o limite de 3 saques diários")

    elif opcao == "e":
        print("### Extrato ###")
        print(extrato)
        print(f"\n Seu saldo é de: R$ {saldo:.2f}")

    elif opcao == "q":
        print("Sair")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
