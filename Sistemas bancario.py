# Sistema bancario simples
# Criado por: Jessé Miguel Ramos
# Data: 05/04/2025
# Versao: 1.0

saldo = 0.0
extrato = ""
limite = 500.0
saque = 0.0
LIMITE_SAQUE = 3
saques_realizados = 0

menu = """
          MENU

    [1] Deposito
    [2] Saque
    [3] Extrato
    [4] Sair
    
------------------------

"""
while True:
    print(menu)
    opcao = int(input("Digite uma opcao: "))
    if opcao == 1:
        deposito = (float(input("Digite o valor do deposito: ")))
        if deposito < 0:
            print("Valor de deposito invalido!")
            continue
        if deposito > 0:
            saldo += deposito
            extrato += f"Deposito: R$ {deposito:.2f}\n"
            print(f"Deposito de R$ {deposito:.2f} realizado com sucesso!")
        else:
            print("Valor de deposito invalido!")
            continue
    elif opcao == 2:
        saque = float(input("Digite o valor do saque: "))
        if saque > saldo:
            print("Saldo insuficiente!")
            continue
        if saque > limite:
            print("Valor de saque maior que o limite!")
            continue
        if saques_realizados >= LIMITE_SAQUE:
            print("Limite de saques diarios atingido!")
            continue
        if saque > 0:
            saldo -= saque
            extrato += f"Saque: R$ {saque:.2f}\n"
            saques_realizados += 1
            print(f"Saque de R$ {saque:.2f} realizado com sucesso!")
        else:
            print("Valor de saque invalido!")
            continue
    elif opcao == 3:
        if extrato == "":
            print("Nenhum movimento realizado!")
        else:
            print("----------Extrato----------")
            print(extrato)
            print(f"Saldo: R$ {saldo:.2f}") 
            print(f"Limite por saque: R$ {limite:.2f}")
            print(f"saques realizados: {saques_realizados}")
            print("--------------------------")
    elif opcao == 4:
        print("Saindo do sistema...")
        break
    else:
        print("Opcao invalida!")
        continue    
