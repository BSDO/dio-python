# teste = {'teste': 10,'teste1':30}
# for item in enumerate(teste):
#     print(f"{item} = {teste[item]}")



# mais_vendidos = {'tecnologia': 'iphone', 'refrigeracao': 'ar consul 12000 btu', 'livros': 'o alquimista', 'eletrodoméstico': 'geladeira', 'lazer': 'prancha surf'}

# vendas_tecnologia = {'iphone': 15000, 'samsung galaxy': 12000, 'tv samsung': 10000, 'ps5': 14300, 'tablet': 1720, 'ipad': 1000, 'tv philco': 2500, 'notebook hp': 1000, 'notebook dell': 17000, 'notebook asus': 2450}

# print(mais_vendidos['livros'])

# print(f"vendemos {vendas_tecnologia.get('ipad')}")

# # verifica se esta dentro da lista

# if 'tablet' in vendas_tecnologia:
#     print(vendas_tecnologia['tablet'])


# ------------- ADICIONAR OS VALORES ----------
# dicionario = {}
# #adicionar o valor 
# dicionario['Teste'] = 'Breno'
# print(dicionario)
# print('-----------------')
# dicionario.update({'teste1': 12})
# print(dicionario)
# print('--------------------')


# print(dicionario)
# # del item['chave'] esta excluindo 

# vendas_tecnologia = {'iphone': 15000, 'samsung galaxy': 12000, 'tv samsung': 10000, 'ps5': 14300, 'tablet': 1720, 'ipad': 1000, 'tv philco': 2500, 'notebook hp': 1000, 'notebook dell': 17000, 'notebook asus': 2450}
# total = 0

# for chave in vendas_tecnologia:
#     # chave tem dois valores dentro de um dicionario 
#     print(f"{chave} = R$ {vendas_tecnologia[chave]:,.2f}")
#     if 'notebook' in chave:
#         total += vendas_tecnologia[chave]
    
# print(f"Total {total}")

# niveis_co2 = {
#     'AC': [325,405,429,486,402],
#     'AL': [492,495,310,407,388],
#     'AP': [507,503,368,338,400],
#     'AM': [429,456,352,377,363],
#     'BA': [321,508,372,490,412],
#     'CE': [424,328,425,516,480],
#     'ES': [449,506,461,337,336],
#     'GO': [425,460,385,485,460],
#     'MA': [361,310,344,425,490],
#     'MT': [358,402,425,386,379],
#     'MS': [324,357,441,405,427],
#     'MG': [345,367,391,427,516],
#     'PA': [479,514,392,493,329],
#     'PB': [418,499,317,302,476],
#     'PR': [420,508,419,396,327],
#     'PE': [404,444,495,320,343],
#     'PI': [513,513,304,377,475],
#     'RJ': [502,481,492,502,506],
#     'RN': [446,437,519,356,317],
#     'RS': [427,518,459,317,321],
#     'RO': [517,466,512,326,458],
#     'RR': [466,495,469,495,310],
#     'SC': [495,436,382,483,479],
#     'SP': [495,407,362,389,317],
#     'SE': [508,351,334,389,418],
#     'TO': [339,490,304,488,419],
#     'DF': [376,516,320,310,518], 
# }



# for estado in niveis_co2:
#     nivel = len(niveis_co2[estado])
#     soma = sum(niveis_co2[estado]) / nivel

#     if soma >= 400:
#         print(f"O nivel de {estado} esta acima do esperado com {soma:.0f} de CO2")


# video = {'uri': '/videos/465407533', 'name': '15 Atalhos no Excel para Ficar Mais Produtivo', 'download': [{'quality': 'source', 'type': 'source', 'width': 1920, 'height': 1080, 'expires': '2020-10-07T04:00:55+00:00', 'link': 'https://player.vimeo.com/play/2064518513?s=465407533_1602043255_5f2f93dd00b66eba66d481f913383b4f&loc=external&context=Vimeo%5CController%5CApi%5CResources%5CUser%5CVideosController.&download=1&filename=15%2BAtalhos%2Bno%2BExcel%2Bpara%2BFicar%2BMais%2BProdutivosource.mp4', 'created_time': '2020-10-06T14:26:17+00:00', 'fps': 30, 'size': 402678442, 'md5': 'af09508ceceed4994554f04e8b931e22', 'public_name': 'Original', 'size_short': '384.02MB'}, {'quality': 'hd', 'type': 'video/mp4', 'width': 1920, 'height': 1080, 'expires': '2020-10-07T04:00:55+00:00', 'link': 'https://player.vimeo.com/play/2064523157?s=465407533_1602043255_ab7b8353c59b5048032396ec5d95a276&loc=external&context=Vimeo%5CController%5CApi%5CResources%5CUser%5CVideosController.&download=1&filename=15%2BAtalhos%2Bno%2BExcel%2Bpara%2BFicar%2BMais%2BProdutivo175.mp4', 'created_time': '2020-10-06T14:29:06+00:00', 'fps': 30, 'size': 173556205, 'md5': '3c05e1e69bd6b13eb1464451033907d2', 'public_name': 'HD 1080p', 'size_short': '165.52MB'}, {'quality': 'sd', 'type': 'video/mp4', 'width': 960, 'height': 540, 'expires': '2020-10-07T04:00:55+00:00', 'link': 'https://player.vimeo.com/play/2064523153?s=465407533_1602043255_f5ac38009ec5c0a13b30600c631446a3&loc=external&context=Vimeo%5CController%5CApi%5CResources%5CUser%5CVideosController.&download=1&filename=15%2BAtalhos%2Bno%2BExcel%2Bpara%2BFicar%2BMais%2BProdutivo165.mp4', 'created_time': '2020-10-06T14:29:06+00:00', 'fps': 30, 'size': 89881848, 'md5': '4a5c5c96cdf18202ed20ca534fd88007', 'public_name': 'SD 540p', 'size_short': '85.72MB'}, {'quality': 'sd', 'type': 'video/mp4', 'width': 426, 'height': 240, 'expires': '2020-10-07T04:00:55+00:00', 'link': 'https://player.vimeo.com/play/2064522788?s=465407533_1602043255_16c69872e2c4e92cc949d0b772242959&loc=external&context=Vimeo%5CController%5CApi%5CResources%5CUser%5CVideosController.&download=1&filename=15%2BAtalhos%2Bno%2BExcel%2Bpara%2BFicar%2BMais%2BProdutivo139.mp4', 'created_time': '2020-10-06T14:28:31+00:00', 'fps': 30, 'size': 27401450, 'md5': '91cc0229087ec94bf67f64b01ad8768d', 'public_name': 'SD 240p', 'size_short': '26.13MB'}, {'quality': 'sd', 'type': 'video/mp4', 'width': 640, 'height': 360, 'expires': '2020-10-07T04:00:55+00:00', 'link': 'https://player.vimeo.com/play/2064522787?s=465407533_1602043255_310b087e2fc8c5e1154ce7a33d10d60e&loc=external&context=Vimeo%5CController%5CApi%5CResources%5CUser%5CVideosController.&download=1&filename=15%2BAtalhos%2Bno%2BExcel%2Bpara%2BFicar%2BMais%2BProdutivo164.mp4', 'created_time': '2020-10-06T14:28:31+00:00', 'fps': 30, 'size': 48627155, 'md5': '548640bf79ce1552a3401726bb0e4224', 'public_name': 'SD 360p', 'size_short': '46.37MB'}]}


# for item in video:
#     print(f"\n Items : {item } = {video[item]}" )


# print(video['download'][1]['link'])
# # print(f"Meus : {download}")


# # meu_link = download['link']
# # print(f"Meu link {meu_link}")

# duas formas de acessa chave e valores

# vendas_tecnologia = {'iphone': 15000, 'samsung galaxy': 12000, 'tv samsung': 10000, 'ps5': 14300, 'tablet': 1720, 'ipad': 1000, 'tv philco': 2500, 'notebook hp': 1000, 'notebook dell': 17000, 'notebook asus': 2450}

# # transforma em uma tupla dentro do docionario
# for qtd,item in vendas_tecnologia.items():
#     print(f"{qtd} {item:,.2f}")

# print('-+-------------')
# for item in vendas_tecnologia:
#     print(f"{item} {vendas_tecnologia[item]:,.2f}")



# #metodos keys e value


# print(vendas_tecnologia.keys())
# print('-----------------')
# print(vendas_tecnologia.values())

# valor = list(vendas_tecnologia.values())
# chave = list(vendas_tecnologia.keys())
# print(valor)
# print(chave)

# maior = max(valor)
# ix = valor.index(maior)

# print(ix)

# print(f"{chave.index(ix)} com {maior:,.2f}")


#transforma lista em dicionarios
# produtos = ['iphone', 'samsung galaxy', 'tv samsung', 'ps5', 'tablet', 'ipad', 'tv philco', 'notebook hp', 'notebook dell', 'notebook asus']
# vendas = [15000, 12000, 10000, 14300, 1720, 1000, 2500, 1000, 17000, 2450]

# dicionario = zip(produtos,vendas)
# lista = dict(dicionario)
# print(f"\n{lista}")

produtos = ['iphone', 'galaxy', 'ipad', 'tv', 'máquina de café', 'kindle', 'geladeira', 'adega', 'notebook dell', 'notebook hp', 'notebook asus', 'microsoft surface', 'webcam', 'caixa de som', 'microfone', 'câmera canon']
vendas2019 = [558147,712350,573823,405252,718654,531580,973139,892292,422760,154753,887061,438508,237467,489705,328311,591120]
vendas2020 = [951642,244295,26964,787604,867660,78830,710331,646016,694913,539704,324831,667179,295633,725316,644622,994303]

ano = list(zip(vendas2019,vendas2020))
# print(ano) # trabsforna em um array de tuplas
dicionario = dict(zip(produtos,ano)) # tansforme um dicionario com tuplas
# print(dicionario)
print(dicionario)

for item in dicionario:
    ano2019,ano2020 =  dicionario[item]
    print(f"Item {item}: valor de 2019 teve  {ano2019} de unidades e ano de 2020 {ano2020} de unidades")
  