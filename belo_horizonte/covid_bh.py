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


def infected_population_covid_bh(df_srag):
    # Quantidade de pessoas diagnosticadas por Covid-19 em BH
    df_BH = data_covid_bh(df_srag)

    df_bh_infectded = df_BH[["DT_SIN_PRI", "CLASSI_FIN"]].copy()

    # df.groupby(['A','B']).B.agg('count').to_frame('c').reset_index()
    df_bh_infectded = (
        df_bh_infectded.groupby(["DT_SIN_PRI", "CLASSI_FIN"])
        .DT_SIN_PRI.agg("count")
        .to_frame("SUM")
        .reset_index()
    )

    # tirar o último mês de dados
    n = 30
    df_bh_infectded.drop(df_bh_infectded.tail(n).index, inplace=True)

    return df_bh_infectded


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


# HOSPITAL - Houve internação? (1-sim; 2-não)
# DT_INTERNA - Data da internação por SRAG
# UTI - Internado em UTI? (1-sim; 2-não)
# DT_ENTUTI - Data de entrada na UTI
# DT_SAIDUTI - Data de saída da UTI
# SUPORT_VEN - Uso de suporte ventilatório? (1-sim, invasivo; 2-sim,não invasivo, 3-não)
# EVOLUCAO - Evolução do caso (1-cura, 2-óbito, 3-óbito por outras causas)
# DT_EVOLUCA - Data de alta ou óbito
def uti_deaths_covid_bh(df_srag):
    # Quantidade de pessoas internadas por Covid-19 em BH x Data de internação
    df_BH = data_covid_bh(df_srag)

    # Filtrando pacientes internados em UTI
    df_BH_DEATH_UTI = df_BH[df_BH["UTI"] == 1]

    # Filtrando por evolução para morte
    df_BH_DEATH_UTI = df_BH_DEATH_UTI[df_BH_DEATH_UTI["EVOLUCAO"] == 2]

    # Retira datas com valors nulos
    df_BH_DEATH_UTI = df_BH_DEATH_UTI.dropna(how="any", subset=["DT_ENTUTI"])

    # Arrumar as datas da coluna 'DT_ENTUTI' -> formato errado
    df_BH_DEATH_UTI["DT_ENTUTI"] = pd.to_datetime(
        df_BH_DEATH_UTI["DT_ENTUTI"], dayfirst=True, errors="coerce"
    )

    # df.groupby(['A','B']).B.agg('count').to_frame('c').reset_index()
    df_BH_DEATH_UTI = (
        df_BH_DEATH_UTI.groupby(["DT_ENTUTI", "CLASSI_FIN"])
        .DT_ENTUTI.agg("count")
        .to_frame("SUM")
        .reset_index()
    )

    # tirar o último mês de dados
    n = 30
    df_BH_DEATH_UTI.drop(df_BH_DEATH_UTI.tail(n).index, inplace=True)

    return df_BH_DEATH_UTI


def waiting_uti_deaths_covid_bh(df_srag):
    # Quantidade de pessoas internadas por Covid-19 em BH x Data de internação
    df_BH = data_covid_bh(df_srag)

    # Filtrando pacientes internados em UTI
    df_BH_DEATH_WAITING = df_BH[df_BH["UTI"] == 2]

    # Filtrando por evolução para morte
    df_BH_DEATH_WAITING = df_BH_DEATH_WAITING[df_BH_DEATH_WAITING["EVOLUCAO"] == 2]

    # Retira datas com valors nulos
    df_BH_DEATH_WAITING = df_BH_DEATH_WAITING.dropna(how="any", subset=["DT_ENTUTI"])

    # Arrumar as datas da coluna 'DT_ENTUTI' -> formato errado
    df_BH_DEATH_WAITING["DT_ENTUTI"] = pd.to_datetime(
        df_BH_DEATH_WAITING["DT_ENTUTI"], dayfirst=True, errors="coerce"
    )

    # df.groupby(['A','B']).B.agg('count').to_frame('c').reset_index()
    df_BH_DEATH_WAITING = (
        df_BH_DEATH_WAITING.groupby(["DT_ENTUTI", "CLASSI_FIN"])
        .DT_ENTUTI.agg("count")
        .to_frame("SUM")
        .reset_index()
    )

    # tirar o último mês de dados
    # n = 30
    # df_BH_DEATH_WAITING.drop(df_BH_DEATH_WAITING.tail(n).index, inplace=True)

    return df_BH_DEATH_WAITING
