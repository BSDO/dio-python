# Estruturas condicionais em python

# saldo = 200.0
# saque = float(input("Digite o vaalor de saque:"))

# if(saldo > saque):
#     print("Saque concluido")
#     saldo -= saque
#     print(saldo)
# elif (saldo  == saque):
#     print('Saldo disponivel')
# else:
#     print('Sem salldo')


#exemplo de if alinhado

# conta_normal = 1
# conta_universitaria = 2

# saldo_normal = 3000.00
# saldo_universitario = 1500.00

# tipoconta = int(input('\nDigite sua conta:\n 1 - conta normal \n 2 - conta universitaria \n'))

# if(tipoconta == conta_normal):
#     print("------------------------------")
#     print("Bom dia! sua conta é a padrao do nosso banco")
#     print("Deseja sacar ou realizar um deposito")
#     tipo_operacao = input('Tipo de operacao S ou D:\n')

#     if(tipo_operacao == 'S'):
#         saque = float(input('Valor do saque: R$ '))
#         saldo_normal -= saque;
#         print("Valor atualizado: R$")
#         print(saldo_normal)

#     else:
#         valor_deposito = float(input("Valor para deposito: R$ "))
#         saldo_normal += valor_deposito
#         print("Valor atualizado: R$")
#         print(saldo_normal)
# else:
#     print("NAda")



#if ternario


saldo = 100.00
saque = float(input("Digite o valor do saque: R$ "))
status = "Sucesso"  if saldo >= saque else "Falha"
saldo-= saque
print(f"{status} ao realizar saque! \n saldo atualizado : {saque}")
