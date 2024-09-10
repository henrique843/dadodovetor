import json

# Carregar os dados do arquivo JSON
with open('faturamento.json', 'r') as file:
    dados = json.load(file)

# Filtrar os dias com faturamento
faturamento = [dia['valor'] for dia in dados if dia['valor'] > 0]

# Calcular o menor e maior valor de faturamento
menor_faturamento = min(faturamento)
maior_faturamento = max(faturamento)

# Calcular a média mensal de faturamento
media_mensal = sum(faturamento) / len(faturamento)

# Contar os dias com faturamento acima da média mensal
dias_acima_media = len([valor for valor in faturamento if valor > media_mensal])

# Exibir os resultados
print(f"Menor valor de faturamento: R$ {menor_faturamento:.2f}")
print(f"Maior valor de faturamento: R$ {maior_faturamento:.2f}")
print(f"Número de dias com faturamento acima da média: {dias_acima_media}")