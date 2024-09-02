import json

faturamento = {
    "faturamento": {
        "1": 1500,
        "2": 2000,
        "3": None,
        "4": 1800,
        "5": 2200,
        "6": None,
        "7": 1600,
        "8": 2400,
        "9": None,
        "10": 3000
    }
}

def salvar_json(arquivo_json, dados):
    with open(arquivo_json, 'w') as file:
        json.dump(dados, file, indent=1)
    print('salvo com sucesso')

def calculo_do_faturamento(arquivo_json):
    with open(arquivo_json, 'r') as file:
        dados = json.load(file)

    faturamento_diario = dados['faturamento']

    valores_faturamento = [valor for valor in faturamento_diario.values() if valor is not None]
    
    if not valores_faturamento:
        return "impossivel resgatar valor."
    
    # Cálculos
    menor_faturamento = min(valores_faturamento)
    maior_faturamento = max(valores_faturamento)
    media_faturamento = sum(valores_faturamento) / len(valores_faturamento)
    
    # Contar dias com faturamento acima da média
    dias_acima_da_media = sum(1 for valor in valores_faturamento if valor > media_faturamento)

    # Resultados
    return {
        "menor_faturamento": menor_faturamento,
        "maior_faturamento": maior_faturamento,
        "dias_acima_da_media": dias_acima_da_media
    }

# 4. Executar o salvamento e o cálculo
arquivo_json = 'faturamento.json'
salvar_json(arquivo_json, faturamento)

resultado = calculo_do_faturamento(arquivo_json)

# 5. Exibir resultados
print("menor faturamento:", resultado["menor_faturamento"])
print("maior faturamento:", resultado["maior_faturamento"])
print("número de dias acima da média:", resultado["dias_acima_da_media"])