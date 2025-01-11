import json

with open('data/dados.json', 'r') as arquivo:
    dados = json.load(arquivo)

valores = [dado['valor'] for dado in dados if dado['valor'] > 0]

menor_valor = min(valores)
maior_valor = max(valores)
media_mensal = sum(valores) / len(valores)

dias_acima_da_media = sum(1 for valor in valores if valor > media_mensal)

print(f"Menor valor de faturamento: {menor_valor:.2f}")
print(f"Maior valor de faturamento: {maior_valor:.2f}")
print(f"Numero de dias com faturamento acima da média: {dias_acima_da_media}")
