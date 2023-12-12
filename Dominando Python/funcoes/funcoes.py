# def teste():
#     print("Ola")  
# novo_teste = teste()
# print(novo_teste)

# def cadastrar_produto():
#     produto = input("Fale um produto")
#     return produto
# produtuo = cadastrar_produto()
# print(produtuo)



# def filtar(lista,texto):
#     lista_filtrada = []
#     for item in lista:
#         if texto in item:
#             lista_filtrada.append(item)
    
#     return lista_filtrada


# lista = ['breno@gmail.com','teste@hotmail.com','pedro@gmail.com','gmail@gamilk.com']
# text = 'gmail'

# teste = filtar(lista,text)

# print("Meus email {}".format(teste))

# retorna mais de um valor

# def somas(n1,n2):
#     soma = n1 + n2
# #     subtr = n1 - n2
# #     divisao = n1 / n2
# #     return (soma,subtr,divisao)

# # calculadora = somas(10,6)
# as .

# # DOCSTRINGS E ANNOTAIONS

# #docstrings diz o que a função faz e quais valores como argumento 
# # def soma(a,b):
    
# #     """
# #         (docstrings)
# #         funcao que soma dois valores e retorna a soma deles
# #     """
# #     return a + b


# # print(f"Soma dos valores: {soma(25,69)}")
# # #annotions diz o que os argumentos deve retorna

# # def soma(a:int , b : float):
    
    
# #     return a + b


# # print(f"Soma dos valores: {soma(25,69.7)}")


# """
#     QUANTITADE INDEFINIDA DE ARGUMENTOS NA FUNC
#     Pode receber varios argumentos dentro de uma funcao 
# """

# def soma(*args):
#     soma = 0
#     for numero in args:
#         soma += numero
#     return soma 

# print(soma(5,4,3,2,1,3,39,41,6974))

# """
#     Varios arguementos 

#     def soma(**args):
#     soma = 0
#     for numero in args:
#         soma += numero
#     return soma 

#     ODEDEM A SEGUI ARGUMENTOS UNICOS, *ARG E DEPOIDE **ARG
# """
