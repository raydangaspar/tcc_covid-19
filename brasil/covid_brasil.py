import pandas as pd


def first_symptoms_pcr_br(df_srag):
    df1 = df_srag[["DT_SIN_PRI", "PCR_SARS2"]].copy()

    df1 = df1.groupby(["DT_SIN_PRI"], as_index=False).agg({"PCR_SARS2": sum})

    # tirar o último mês de dados
    n = 30

    # manter apenas a primeira onda
    # n = 70

    df1.drop(df1.tail(n).index, inplace=True)

    return df1


def first_symptoms_br(df_srag):
    df_class_fin = df_srag[["DT_SIN_PRI", "CLASSI_FIN"]].copy()

    # 5 -> infecção por covid-19 confirmada
    df_class_fin = df_class_fin[df_class_fin["CLASSI_FIN"] == 5]

    # agrupando e somando o número de pessoas com Covid-19 na data
    df_class_fin = (
        df_class_fin.groupby(["DT_SIN_PRI", "CLASSI_FIN"])
        .DT_SIN_PRI.agg("count")
        .to_frame("SUM")
        .reset_index()
    )

    n = 30  # tirar o último mês de dados para evitar quedas artificiais
    # n = 70 # manter apenas a primeira onda
    df_class_fin.drop(df_class_fin.tail(n).index, inplace=True)

    return df_class_fin


def lag_report_days(df_srag):
    # Gráfico: Data do resultado do exame x Confirmação diagnóstico Covid-19
    # Mostra como o dia da semana influencia na divulgação das confirmações
    # Final de semana confirmam-se menos pessoas

    df_class_fin_and_diagnosis_date = df_srag[["DT_RES", "CLASSI_FIN"]].copy()

    # 5 -> infecção por covid-19 confirmada
    df_class_fin_and_diagnosis_date = df_class_fin_and_diagnosis_date[
        df_class_fin_and_diagnosis_date["CLASSI_FIN"] == 5
    ]

    # remove linhas com valores null
    df_class_fin_and_diagnosis_date.dropna(how="any", inplace=True)

    # Uma data formatada errada está evitando que a coluna seja convertida em datetime
    # Excluir a linha com problema: 07/12/220
    df_class_fin_and_diagnosis_date = df_class_fin_and_diagnosis_date[
        df_class_fin_and_diagnosis_date.DT_RES != "07/12/220"
    ]
    df_class_fin_and_diagnosis_date["DT_RES"] = pd.to_datetime(
        df_class_fin_and_diagnosis_date["DT_RES"], dayfirst=True, errors="coerce"
    )

    df_class_fin_and_diagnosis_date["DT_RES"] = df_class_fin_and_diagnosis_date[
        (df_class_fin_and_diagnosis_date["DT_RES"].dt.year == 2020)
    ]

    # agrupando e somando o número de pessoas com Covid-19 na data
    df_class_fin_and_diagnosis_date = (
        df_class_fin_and_diagnosis_date.groupby(["DT_RES", "CLASSI_FIN"])
        .DT_RES.agg("count")
        .to_frame("SUM")
        .reset_index()
    )

    return df_class_fin_and_diagnosis_date


def age_covid_confirmed_cases_br(df_srag):
    df_idade_covid = df_srag[["NU_IDADE_N", "CLASSI_FIN"]].copy()

    # 5 -> infecção por covid-19 confirmada
    df_idade_covid = df_idade_covid[df_idade_covid["CLASSI_FIN"] == 5]

    df_idade_covid = (
        df_idade_covid.groupby(["NU_IDADE_N", "CLASSI_FIN"])
        .NU_IDADE_N.agg("count")
        .to_frame("SUM")
        .reset_index()
    )

    return df_idade_covid
