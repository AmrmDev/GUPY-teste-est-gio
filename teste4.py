faturamento_estados = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

faturamento_total_dos_estados = sum(faturamento_estados.values())

percentual_dos_estados = {estado: (valor / faturamento_total_dos_estados) * 100 for estado, valor in faturamento_estados.items()}

for estado, percentual in percentual_dos_estados.items():
    print(f'{estado}: {percentual:.2f}%')