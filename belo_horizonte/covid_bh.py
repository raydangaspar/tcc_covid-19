import pandas as pd


def data_covid_bh(df_srag):
    # Filtrar pacientes de BH
    # Filtrar pacientes diagnosticados com Covid-19

    # SG_UF_NOT -> UF da solicitação
    # ID_MUNICIP -> Município
    # DT_SIN_PRI -> Data dos primeiros sintomas
    # CLASSI_FIN -> Diagnóstico final paciente (igual a 5 é Covid)
    # EVOLUCAO -> Evolução do caso (1-cura; 2-óbito; 3-óbito por outras causas)
    # UTI -> Paciente internado em UTI?
    # DT_ENTUTI -> Data entrada UTI
    # DT_SAIDUTI -> Data saída UTI
    df_BH = df_srag[
        [
            "SG_UF_NOT",
            "ID_MUNICIP",
            "DT_SIN_PRI",
            "CLASSI_FIN",
            "EVOLUCAO",
            "UTI",
            "DT_ENTUTI",
            "DT_SAIDUTI",
        ]
    ].copy()

    # 5 -> infecção por covid-19 confirmada
    df_BH = df_BH[df_BH["CLASSI_FIN"] == 5]

    # Filtrando pelo Estado de Minas Gerais
    df_BH = df_BH[df_BH["SG_UF_NOT"] == "MG"]

    # Filtrando pela cidade de Belo Horizonte
    df_BH = df_BH[df_BH["ID_MUNICIP"] == "BELO HORIZONTE"]

    return df_BH


def uti_data_covid_bh(df_srag):
    # Quantidade de pessoas internadas por Covid-19 em BH x Data de internação
    df_BH = data_covid_bh(df_srag)

    # Filtrando pacientes internados em UTI
    df_BH_UTI = df_BH[df_BH["UTI"] == 1]

    # Retira datas com valors nulos
    df_BH_UTI = df_BH_UTI.dropna(how="any", subset=["DT_ENTUTI"])

    # Arrumar as datas da coluna 'DT_ENTUTI' -> formato errado
    df_BH_UTI["DT_ENTUTI"] = pd.to_datetime(df_BH_UTI["DT_ENTUTI"], dayfirst=True, errors="coerce")

    # df.groupby(['A','B']).B.agg('count').to_frame('c').reset_index()
    df_BH_UTI = (
        df_BH_UTI.groupby(["DT_ENTUTI", "CLASSI_FIN"])
        .DT_ENTUTI.agg("count")
        .to_frame("SUM")
        .reset_index()
    )

    # tirar o último mês de dados
    n = 30
    df_BH_UTI.drop(df_BH_UTI.tail(n).index, inplace=True)

    return df_BH_UTI
