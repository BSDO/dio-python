""" 
    modulo é um arquivo com varios objetos
    import webbrowser as navegador  mudando o nome do modulo 

    teste = navegador.open('https://medium.com/') abre o chorme
    print(teste)

    (modulo) - pegar apenas uma função dentro do modulo

    
# import webbrowser as navegador  

# teste = navegador.open('https://medium.com/','tab')

"""

# import time as tempo

# print(tempo.time())
# print(tempo.ctime())

# tempo_inicial = tempo.time()
# for i in range(1000000):
#     pass
# tempo_final = tempo.time()
# duracao = tempo_final - tempo_inicial
# print(f"Duração em {duracao:.2f} seg ")

#definir tempo para iniciar
# print('começando')
# tempo.sleep(10)
# print("Depois de 10 segundos vai começar")

# pegar dias,hora,segundo,minuto 
#gmtime()
# print(tempo.gmtime())

#gmtime() + parametro 


# import matplotlib.pyplot as plt 

# vendas_tecnologia = {'iphone': 15000, 'samsung galaxy': 12000, 'tv samsung': 10000, 'ps5': 14300, 'tablet': 1720, 'ipad': 1000, 'tv philco': 2500, 'notebook hp': 1000, 'notebook dell': 17000, 'notebook asus': 2450}
# for i in vendas_tecnologia:
#     # chave = i
#     # //valor = vendas_tecnologia[i]
#     plt.plot(vendas_tecnologia[i])
#     plt.show()


c = 1
for i in range(4):
   
    for j in range(3):
   
        if i == j:
            c = c + 1
            print(c)