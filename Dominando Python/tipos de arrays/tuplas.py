# tuplas é imutavel/Proteção de dados

# tuplas = (10,20,30,50,50)

# lista de tuplas

# arr = [[(1,0),(2,2),(4,3)],[(1,0),(2,2),(4,3)]]
# for i,index in enumerate(arr):
#     print(f"{i}")

# meta = 10000
# vendas = [('joao',15000),('Julia',27000),('Marcus',9900),('maria',3750),('Ana',10300),('Alon',7878)]

# for index in vendas:
#     nome,venda = index
#     if venda >= meta:
#         print(f"O Nome: {nome} vendeu R$ {venda:,.2f}")




vendas_produtos = [('iphone', 558147, 951642), ('galaxy', 712350, 244295), ('ipad', 573823, 26964), ('tv', 405252, 787604), ('máquina de café', 718654, 867660), ('kindle', 531580, 78830), ('geladeira', 973139, 710331), ('adega', 892292, 646016), ('notebook dell', 422760, 694913), ('notebook hp', 154753, 539704), ('notebook asus', 887061, 324831), ('microsoft surface', 438508, 667179), ('webcam', 237467, 295633), ('caixa de som', 489705, 725316), ('microfone', 328311, 644622), ('câmera canon', 591120, 994303)]

crescimento = 0
for item in vendas_produtos:
    produto,venda2019,venda2020 = item
    if(venda2020 >= venda2019):
        crescimento = (venda2020 / venda2019)  - 1
        print(f"O produto {produto} teve mais vendas em 2020 do que 2019 com o crescimento de {crescimento:.1%}")
    else:
        crescimento = (venda2020 / venda2019)  - 1
        print(f"O produto {produto} teve maenos vendas em 2020 do que 2019 com o crescimento de {crescimento:.1%}")

