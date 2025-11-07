def calcular_economia(num_alunos):
    folhas = num_alunos * 2
    co2 = round(folhas * 0.0045, 3)
    return folhas, co2
