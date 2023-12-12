# function em iterables

# funcao map 

# def padronizar(texto):
#     texto = texto.upper()
#     texto = texto.replace(" ","")
#     texto =  texto.strip()
#     return  texto

# produtos = [' Abc ' ,' abc234','abcr257','abc257 ','bas ','bbbb']

# # uma forma de fazer pra mudar
# # for i,item in enumerate(produtos):
# #     produtos[i] =  padronizar(item)

# # print(produtos)


# # com map vai percorrer a lista e executa na funcao
# produto = list(map(padronizar,produtos)) 
# produto.sort(reverse=True)
# print(produto)


# SORT OU SORTED

# produtos = {'vinho':100,'tv':5200,'iphone':9000}

# listar_vendas = list(produtos.items())


    

# def segundo(tupla):
#     return tupla[1]

# # Sort com um funcao pra fazer ordenação
# listar_vendas.sort(key=segundo)

# print(" efc {}".format(listar_vendas))

# sorted(listar_vendas)

# print(listar_vendas)


# Lambda Expressions funcao anonima que executa uma unica ação 
# teste = funcao()

# teste = lambda num1,num2 : num1 * num2
# print(teste(10,265))


# imposto_produto = lambda preco : preco * (1.0 + 0.75)
# print(imposto_produto(30))

# #

# MAP
vendas_tecnologia = {'iphone': 2450, 'samsung galaxy': 4500, 'tv samsung': 10000, 'ps5': 14300, 'tablet': 1720, 'ipad': 1000, 'tv philco': 2500, 'notebook hp': 1000, 'notebook dell': 17000, 'notebook asus': 2450}

# def calcularimposto(item):
#     return item * (1.0 + 0.30)
# teste = list(map(calcularimposto,vendas_tecnologia.values()))
# print(teste)

# #por lambda para fazer o calculo de imposto 
# teste2 = list(map(lambda item: item * (1.0 + 0.30) ,vendas_tecnologia.values()))
# print(teste2)


# Filter retorna v ou f de uma funcao

# por funcao

# def maior(lista):
#     return lista[1] > 5000

# teste = dict(list(filter(maior,vendas_tecnologia.items())))
# print(teste)

# # Por lambada

# teste2 =  dict(list(filter(lambda lista: lista[1] > 10000,vendas_tecnologia.items())))
# print(teste2)

#Lambda pra gerar funcções :

def calculo_imposto(imposto):
    """
        o retorno se transforma uma funcao que deve ser passado um parametro
    """
    return lambda preco : preco  *  imposto

#quando passa o parametro imposto ele cria uma funcao pra pode passa o preco
cal_produto = calculo_imposto(0.37)
cal_servico = calculo_imposto(0.23)
cal_royalties = calculo_imposto(0.64)


# A partir de do retorno passa o valor pra pode calcular o imposto sobre o produto.
print(f"O imposto sobre sobre esse produto é de R$ {cal_produto(100) :,.2f}")
print(f"O imposto sobre sobre esse produto é de R$ {cal_servico(30):,.2f}")
print(f"O imposto sobre sobre esse produto é de R$ {cal_royalties(10000):,.2f}")
