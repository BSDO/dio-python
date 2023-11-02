# Listas em py

# listar = ['Breno',['lista','teste'],['lisar']]
# print(listar[1][1])

# index para achar um dado

# listar = ['tv','cama','radio','computador','geladeira','fogao','armario','tapate']

# item = str(input("Digite o item que procura"))

# if item in listar:
#     i = listar.index(item)
#     print(f'Item: {i}')
# else:
#     print("Produto nao existe:")


#adicionar ou remove items


# listar = ['tv','cama','radio','computador','geladeira','fogao','armario','tapate']

# nmr =  input("Digite um numero: ")
# listar.append(nmr)
# print("-----------------\n")
# print(listar)

# listar.remove('fogao')
# print(listar)
# print("-----------------\n")
# print("-----------------\n")
# listar.pop(2)
# print(listar)


# #funcao try e except pra verifica 

# try:
#     listar.remove('fogaooooo')
# except:
#     print("Não existe")
   

# funcao de maior,menor e len
# listar = [20,600,588,699,7444,2563,0,36]
# print(f"Tamanho dessa listar : {len(listar)}")
# print("-----------------\n")
# item_maior = max(listar)
# print(f"O maior item: {item_maior}")
# print("-----------------\n")
# item_menor = min(listar)
# print(f"O maior item: {item_menor}")
# print("-----------------\n")
# print(f"A posicao do meu maior item: {listar.index(item_maior)}")
# print("-----------------\n")
# print(f"A posicao do meu menor item: {listar.index(item_menor)}")

# caixa_numero = []

# while (True):
#     numero = int(input("Digite um numero "))
#     print("-------------")
#     if(numero > 0):
#         caixa_numero.append(numero)
#     else:
#         print("Zero não é aceitavel")
#         break

#     print("-------------")
#     print(caixa_numero)

#juntar listar, ordernar e cuidados especiais

# lista = ['tv','maça','ipad','iphone']
# lista2 = ['tv 52p', 'iphone 11']
# lista.extend(lista2)
# print(f"Lista:  {lista}")
# print("-----")
# novo = lista + lista2
# print(novo)

#ordernar
# lista = [1,3,9,10,0,9,39,87,25,36,14,69,69742]
# lista.sort()
# print(f" Lista ordernada: {lista}")
# print("----")
# lista.sort(reverse=True)
# print(f" Lista ordernada: {lista}")

# JOIN
# lista = [1,3,9,10,0,9,39,87,25,36,14,69,69742]

# print('-'.join(lista))

# SPLIt
# produto = 'mac , apple , samsung, tesla'
# lista = produto.split(', ') # Separa os espaços
# print(lista)