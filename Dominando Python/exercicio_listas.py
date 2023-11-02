# exercio faturamento de melhor e pior mes do ano

# meses do ano
meses = ['jan','fev','mar','abr','mai','jun','jul','ago','set','out','nov','dez']

vendas_1sem = [25000,29000,22200,17750,15870,19900]
vendas_2sem = [19850,20120,17540,15555,49051,9650]

# soma dos dois semestres
vendas_totais = vendas_1sem + vendas_2sem
print(vendas_totais)
print('--------')

# maior venda e menor venda 
maior_venda = max(vendas_totais)
menor_venda = min(vendas_totais)

print(f"Maior mes de venda : R$ {maior_venda:,.2f}")
print("---------------------------------------------------------")
print(f"Maior mes de venda : R$ {menor_venda:,.2f}")
print('---------------------------------------------------------')
print(vendas_totais)

# pega a posicao do maior e menor valor dentro de vendas totais
posicao_maior = vendas_totais.index(maior_venda)
print(posicao_maior)
posicao_menor = vendas_totais.index(menor_venda)
print(posicao_menor)

# mostra o valor com maior venda do mes 
print("--------------------")
print(f"O melhor mes do ano é: {meses[posicao_maior]} com R$ {maior_venda:,.2f}")
print('----------------------')
print(f"O pior mes do ano é: {meses[posicao_menor]} com R$ {menor_venda:,.2f}")

# mostrar o total de vendas e o percentual pelo melhor mes
print('----------------------')
total = sum(vendas_totais)
print(f"Totais de vendas: R$ {total:,.2f}")
print('-----------------------------')
porcentagem =  maior_venda / total
print(f"Porcentual: {porcentagem:.1%}")
print('------------------------')

# remove os  3 maiore valores e adiciona no top 3
top3 = []
top3.append(maior_venda)
print(f"Top 3: {top3}")
vendas_totais.remove(maior_venda)
print(vendas_totais)
maior_venda = max(vendas_totais)
top3.append(maior_venda)
print(f"Top 3: {top3}")
vendas_totais.remove(maior_venda)
print(vendas_totais)
maior_venda = max(vendas_totais)
top3.append(maior_venda)
print(f"Top 3: {top3}")