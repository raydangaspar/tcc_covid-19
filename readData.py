import pandas as pd


def read_data(file_name):
    # database 2019, 2020 and 2021
    database = f"data/{file_name}"

    date_columns = [
        "DT_NOTIFIC",
        "DT_SIN_PRI",
        "DT_NASC",
        "DT_VGM",
        "DT_RT_VGM",
        "DT_UT_DOSE",
        "DT_VAC_MAE",
        "DT_DOSEUNI",
        "DT_1_DOSE",
        "DT_2_DOSE",
        "DT_ANTIVIR",
        "DT_INTERNA",
        "DT_ENTUTI",
        "DT_SAIDUTI",
        "DT_RAIOX",
        "DT_TOMO",
        "DT_COLETA",
        "DT_RES_AN",
        "DT_PCR",
        "DT_CO_SOR",
        "DT_RES",
        "DT_EVOLUCA",
        "DT_ENCERRA",
        "DT_DIGITA",
    ]

    # OBES_IMC is float, but is formated with comma instead of dot (ex: 41,5)
    # COD_IDADE has a wrong row value. Should be int type
    types_dict = {
        "COD_IDADE": "string",
        "CS_ETINIA": "string",
        "OBES_IMC": "string",
        "FLUBLI_OUT": "string",
        "CLASSI_OUT": "string",
        "FLUASU_OUT": "string",
        "DS_PCR_OUT": "string",
        "OUT_ANIM": "string",
        "PAIS_VGM": "string",
        "LO_PS_VGM": "string",
        "DS_AN_OUT": "string",
    }

    df_srag = pd.read_csv(
        database, sep=";", parse_dates=date_columns, dayfirst=True, dtype=types_dict
    )

    return df_srag
