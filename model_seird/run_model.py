from scipy.integrate import odeint
from model_seird.derivative import deriv


def run_model(params, x):
    S0 = params["S0"].value
    E0 = params["E0"].value
    I0 = params["I0"].value
    R0 = params["R0"].value
    D0 = params["D0"].value
    N = params["N"].value
    beta = params["beta"].value
    gamma = params["gamma"].value
    delta = params["delta"].value
    tay = params["tay"].value
    khi = params["khi"].value
    y0 = S0, E0, I0, R0, D0
    ret = odeint(deriv, y0, x, args=(N, beta, gamma, delta, tay, khi))
    dS, dE, dI, dR, dD = ret.T

    return dS, dE, dI, dR, dD
