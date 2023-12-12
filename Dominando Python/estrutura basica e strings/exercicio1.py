menu = ("""
        ==== ESCOLHA UMA OPÇAO DO BANCON ====

        [1] DEPOSITAR
        [2] SACAR
        [3] EXTRATO
        [4] [SAIR]

        ======================================
        """)

saldo = 0
limite_saque = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUE = 3


while(True):
    
    opcao = int(input(menu))

    if(opcao == 1):
        print("Deposito: ")
        valor_deposito = int(input())

        if valor_deposito > 0:
            saldo += valor_deposito
            print(f"seu saldo {saldo:.2f}")   
            extrato += f"Valor de deposito: R$ {valor_deposito:.2f}\n"

        else:
            print("Valor tem que ser positivo")
    elif(opcao == 2):
        
        print(f"""-----------------------
                Saldo atual: {saldo}
                -------------------------
            """)

        print("Saque: ")
      
        valor_saque = int(input())

        if valor_saque > saldo:
            print(f"Sem saldo suficiente para saque.")

        elif valor_saque > limite_saque:
            print("DIGITE OUTRO VALOR PARA SACAR MENOR QUE R$ 500,00")
            

        elif numero_saque >= LIMITE_SAQUE:
            print("Limite Saque ja decido.")

        
        elif valor_saque > 0:            
            saldo -= valor_saque   
            extrato += f"Valor de saque: R$ {valor_saque:.2f}\n"
            numero_saque += 1

            print("---------------------")
            print()
            print(f"Saldo atual: {saldo}\n")
        

    
    elif(opcao == 3):
        print("--------------------")
        print("----------Extratos------------------")
        print(f"Saque" if not extrato else extrato)
        print()
        print(f"saldo: R$ {saldo:.2f}")
    
    elif(opcao == 4):
        print("Obrigado por usar nossa conta.")
        break











