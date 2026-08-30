from datetime import datetime


def calcular_gasto_por_dia(orcamento, dias):
    return round(orcamento / dias, 2)


def classificar_orcamento(orcamento):
    if orcamento < 3000:
        return "Econômico"

    elif orcamento < 10000:
        return "Moderado"

    else:
        return "Confortável"


def calcular_dias(data_inicio, data_fim):
    inicio = datetime.strptime(
        data_inicio,
        "%Y-%m-%d"
    )

    fim = datetime.strptime(
        data_fim,
        "%Y-%m-%d"
    )

    return (fim - inicio).days