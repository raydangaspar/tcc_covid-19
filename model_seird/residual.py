from model_seird.run_model import run_model


def get_residual(params, data, x):
    dS, dE, dI, dR, dD = run_model(params, x)

    return data - dI
