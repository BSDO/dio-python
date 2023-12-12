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

# alterarçoes incrimentais de variaveis

# faturamento = 1000
# faturamento += 3000
# print(f"faturamento R$ {faturamento:,.2f}")
# print('-----------')

# lista = ['maça','uva']
# frutas = ['banana','teste ']
# lista += frutas
# print(lista)

#copy ou [:] copiar uma lista pra outra

# lista1 = [1,2,3,4,5,6]
# lista2 = lista1.copy()
# print(f"Lista 1 : {lista1}\nLista 2 :{lista2}")

# lista1[2] = 10
# lista2[3] = 'Breno'
# print(f"Lista 1 : {lista1}\nLista 2 :{lista2}")

# lista dentro de lista

vendedor = ['Lira','Pedro','Carlos','Alon']
produtos = ['I-phone','Macbook']
valor_produtos = [3000,8000]
vendas = [[321,350],[399,520],[400,1000],[900,300]]

index_pedro =  vendedor.index('Pedro')
index_lira =  vendedor.index('Lira')
index_carlos =  vendedor.index('Carlos')
index_alon =  vendedor.index('Alon')


total_vendas_pedro = vendas[index_pedro][0] * valor_produtos[0]
total_vendas_lira = vendas[index_lira][0] * valor_produtos[0]
total_vendas_carlos = vendas[index_carlos][0] * valor_produtos[0]
total_vendas_alon = vendas[index_alon][0] * valor_produtos[0]
print('-------------')
print('Iphones')
print('-------------')

print(f'o {vendedor[index_pedro]} vendeu {vendas[index_pedro][0]} de {produtos[0]} com o valor total de R$ {total_vendas_pedro:,.2f} ')
print('----------')
print(f'o {vendedor[index_lira]} vendeu {vendas[index_lira][0]} de {produtos[0]} com o valor total de R$ {total_vendas_lira:,.2f} ')
print('----------')
print(f'o {vendedor[index_carlos]} vendeu {vendas[index_carlos][0]} de {produtos[0]} com o valor total de R$ {total_vendas_carlos:,.2f} ')
print('----------')
print(f'o {vendedor[index_alon]} vendeu {vendas[index_alon][0]} de {produtos[0]} com o valor total de R$ {total_vendas_alon:,.2f} ')

print('-------------')
print('macbooks')
print('-------------')
total_vendas_pedro = vendas[index_pedro][1] * valor_produtos[1]
total_vendas_lira = vendas[index_lira][1] * valor_produtos[1]
total_vendas_carlos = vendas[index_carlos][1] * valor_produtos[1]
total_vendas_alon = vendas[index_alon][1] * valor_produtos[1]


print(f'o {vendedor[index_pedro]} vendeu {vendas[index_pedro][1]} de {produtos[1]} com o valor total de R$ {total_vendas_pedro:,.2f} ')
print('----------')
print(f'o {vendedor[index_lira]} vendeu {vendas[index_lira][1]} de {produtos[1]} com o valor total de R$ {total_vendas_lira:,.2f} ')
print('----------')
print(f'o {vendedor[index_carlos]} vendeu {vendas[index_carlos][1]} de {produtos[1]} com o valor total de R$ {total_vendas_carlos:,.2f} ')
print('----------')
print(f'o {vendedor[index_alon]} vendeu {vendas[index_alon][1]} de {produtos[1]} com o valor total de R$ {total_vendas_alon:,.2f} ')
