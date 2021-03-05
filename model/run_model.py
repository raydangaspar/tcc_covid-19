from scipy.integrate import odeint
from model.derivative import deriv


def run_model(params, x):
    S0 = params["S0"].value
    E0 = params["E0"].value
    I0 = params["I0"].value
    R0 = params["R0"].value
    N = params["N"].value
    beta = params["beta"].value
    gamma = params["gamma"].value
    delta = params["delta"].value
    y0 = S0, E0, I0, R0
    ret = odeint(deriv, y0, x, args=(N, beta, gamma, delta))
    dS, dE, dI, dR = ret.T

    return dS, dE, dI, dR
