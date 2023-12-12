# exercio faturamento de melhor e pior mes do ano

# meses do ano
# meses = ['jan','fev','mar','abr','mai','jun','jul','ago','set','out','nov','dez']
# vendas_1sem = [25000,29000,22200,17750,15870,19900]
# vendas_2sem = [19850,20120,17540,15555,49051,9650]

# # soma dos dois semestres
# vendas_totais = vendas_1sem + vendas_2sem
# print(vendas_totais)
# print('--------')

# # maior venda e menor venda 
# maior_venda = max(vendas_totais)
# menor_venda = min(vendas_totais)

# print(f"Maior mes de venda : R$ {maior_venda:,.2f}")
# print("---------------------------------------------------------")
# print(f"Maior mes de venda : R$ {menor_venda:,.2f}")
# print('---------------------------------------------------------')
# print(vendas_totais)

# # pega a posicao do maior e menor valor dentro de vendas totais
# posicao_maior = vendas_totais.index(maior_venda)
# print(posicao_maior)
# posicao_menor = vendas_totais.index(menor_venda)
# print(posicao_menor)

# # mostra o valor com maior venda do mes 
# print("--------------------")
# print(f"O melhor mes do ano é: {meses[posicao_maior]} com R$ {maior_venda:,.2f}")
# print('----------------------')
# print(f"O pior mes do ano é: {meses[posicao_menor]} com R$ {menor_venda:,.2f}")

# # mostrar o total de vendas e o percentual pelo melhor mes
# print('----------------------')
# total = sum(vendas_totais)
# print(f"Totais de vendas: R$ {total:,.2f}")
# print('-----------------------------')
# porcentagem =  maior_venda / total
# print(f"Porcentual: {porcentagem:.1%}")
# print('------------------------')

# # remove os  3 maiore valores e adiciona no top 3
# top3 = []
# top3.append(maior_venda)
# print(f"Top 3: {top3}")
# vendas_totais.remove(maior_venda)
# print(vendas_totais)
# maior_venda = max(vendas_totais)
# top3.append(maior_venda)
# print(f"Top 3: {top3}")
# vendas_totais.remove(maior_venda)
# print(vendas_totais)
# maior_venda = max(vendas_totais)
# top3.append(maior_venda)
# print(f"Top 3: {top3}")

# exercio 2 - Mudança de Carga tributaria

produtos = ['computador', 'livro', 'tablet', 'celular', 'tv', 'ar condicionado', 'alexa', 'máquina de café', 'kindle']

#cada item da lista dos produtos corresponde a quantidade de vendas no mês e preço, nessa ordem
produtos_ecommerce = [
    [10000, 2500],
    [50000, 40],
    [7000, 1200],
    [20000, 1500],
    [5800, 1300],
    [7200, 2500],
    [200, 800],
    [3300, 700],
    [1900, 400]
]

if 'livro' in produtos:
    i_livro = produtos.index('livro')
    print(produtos_ecommerce[i_livro])
    produtos_ecommerce[i_livro][1] = produtos_ecommerce[i_livro][1] * 1.1
    print(produtos_ecommerce[i_livro])
    total = produtos_ecommerce[i_livro][0] * produtos_ecommerce[i_livro][1]
    print(f"Total : {total:,.2f}")
  