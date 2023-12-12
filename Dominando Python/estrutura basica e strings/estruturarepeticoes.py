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
    



# produtos = ['computador', 'livro', 'tablet', 'celular', 'tv', 'ar condicionado', 'alexa', 'máquina de café', 'kindle']
# produ = []
# for item in produtos:
#     print(f'Meus Produtos: {item}')

# vendas = [1000,200,1200,3000,644,744,966,1390,944,255,1001,1070]
# bateu_meta = 0
# meta = 1000
# totais_meta = ""
# top_vendas = []
# for venda in vendas:
#     if venda >= meta:
#         bateu_meta += 1
#         print(f"Bateu a meta R$ {venda:,.2f}")
#         totais_meta += f"Valor da  meta R$ {venda:,.2f}\n"
#         top_vendas.append(venda)
        
#     else:
#         print(f"Não bateu a meta R$ {venda:,.2f}")
 
# print(top_vendas)
# print("--------------------------------------------")

    
# print(f"Maior {venda_menor:,.2f}\n")   
# print(f"Menor R$ {venda_maior:,.2f}\n")   

    
# print(f"Totais que bateram a meta: {bateu_meta}")
# print(f"{totais_meta}")


# com indice percorre o for {enumerate}
# vendas = [1000,200,1200,3000,644,744,966,1390,944,255,1001,1070]

# for i,index in enumerate(vendas):
#     print(f"{i} : {index}")

# for dentro de um for 

# estoque = [
#     [294, 125, 269, 208, 783, 852, 259, 371, 47, 102, 386, 87, 685, 686, 697, 941, 163, 631, 7, 714, 218, 670, 453],
#     [648, 816, 310, 555, 992, 643, 226, 319, 501, 23, 239, 42, 372, 441, 126, 645, 927, 911, 761, 445, 974, 2, 549],
#     [832, 683, 784, 449, 977, 705, 198, 937, 729, 327, 339, 10, 975, 310, 95, 689, 137, 795, 211, 538, 933, 751, 522],
#     [837, 168, 570, 397, 53, 297, 966, 714, 72, 737, 259, 629, 625, 469, 922, 305, 782, 243, 841, 848, 372, 621, 362],
#     [429, 242, 53, 985, 406, 186, 198, 50, 501, 870, 781, 632, 781, 105, 644, 509, 401, 88, 961, 765, 422, 340, 654],
# ]
# fabricas = ['Lira Manufacturing', 'Fábrica Hashtag', 'Python Manufaturas', 'Produções e Cia', 'Manufatura e Cia']
# nivel_minimo = 50
# fabrica = []

# for i,lista in enumerate(estoque):
#     # print(f"Index:{i} = \n{lista}\n")
#     for qtd in lista:
#         if(qtd < nivel_minimo):
#             if(fabricas[i] in fabrica):
#                 pass                
#             else:
#                 fabrica.append(fabricas[i])


#     print(f"Na empresa {fabrica[i]} tem a quantidade menor de estoque: {qtd}")            
  
                

