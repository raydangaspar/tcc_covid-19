from lmfit import Parameters


# tuple (<value>, <vary>)
def create_params(S0, E0, I0, R0, N, beta, gamma, delta):
    # determina quem vai variar
    params = Parameters()

    params.add("S0", value=S0[0], vary=S0[1])
    params.add("E0", value=E0[0], vary=E0[1])
    params.add("I0", value=I0[0], vary=I0[1])
    params.add("R0", value=R0[0], vary=R0[1])
    params.add("N", value=N[0], vary=N[1])
    params.add("beta", value=beta[0], vary=beta[1])
    params.add("gamma", value=gamma[0], vary=gamma[1])
    params.add("delta", value=delta[0], vary=delta[1])

    return params
