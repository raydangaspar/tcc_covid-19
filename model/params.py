from lmfit import Parameters


def create_params(S0, E0, I0, R0, N, beta, gamma, delta):
    # determina quem vai variar
    params = Parameters()

    params.add("S0", value=S0, vary=False)
    params.add("E0", value=E0, vary=False)
    params.add("I0", value=I0, vary=False)
    params.add("R0", value=R0, vary=False)
    params.add("N", value=N, vary=False)
    params.add("beta", value=beta, vary=True)
    params.add("gamma", value=gamma, vary=True)
    params.add("delta", value=delta, vary=True)

    return params
