# Estrutura de repetições
#FOR
# texto = input("Informe um texto: ")

# VOGAIS = "AEIOU"

# for letra in texto:
#     if letra.upper() in VOGAIS:
#         print(letra,end="")
#     else:
#         print ("Tetxo entroui")

# range tipo de range

# for numero in range(11):
#     print(numero)


# for numero in range(1,11):1

#     print(numero)

# for numero in range(0,21,2):
#     print(numero)

#while repetir diversar vezes com a condicão


# opcao = 1



# while opcao != 0:
#     opcao = int(input("Dgite:\n [1] sacar \n [2] extratro \n [0] Sair"))
#     print()
#     if(opcao == 1):
#         print("Sacando")
#     elif(opcao == 2):
#         print("EXtrato")


# print("SAiu")

# while True:
#     numero = int(input("Digite o numero? "))

#     if numero == 50:
#         break
#     print(numero)

# para quando chegar no dose
# for numero in range(11):

#     if numero == 10:
#         break
#     print(numero)



# for numero in range(0,110,3):
#     # resto da divisao ,para retorna o impar
#     if numero % 2 == 1 :
#         print("----")
#         continue

#     print(numero)  


# numero = int(input("Digite um numero: "))

# for percorrer in range(0,101,1):

#     if percorrer == numero:
#         print("Pulamos esse numero.")
#         continue

#     print(f"Numeros atual :{percorrer}")
    

import requests

url = "https://cep.awesomeapi.com.br/json/02873420"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)