from lmfit import Parameters

# adicionar nome vary como parâmetros para deixar mais reutilizável
def create_params(S0, E0, I0, R0, D0, N, beta, gamma, delta, tay, khi):
    # determina quem vai variar
    params = Parameters()

    params.add("S0", value=S0, vary=False)
    params.add("E0", value=E0, vary=False)
    params.add("I0", value=I0, vary=False)
    params.add("R0", value=R0, vary=False)
    params.add("D0", value=D0, vary=False)
    params.add("N", value=N, vary=False)
    params.add("beta", value=beta, vary=True)
    params.add("gamma", value=gamma, vary=True)
    params.add("delta", value=delta, vary=False)
    # experimentar o tay variando
    params.add("tay", value=tay, vary=False)
    params.add("khi", value=khi, vary=False)
    # add pessoas que foram para uti
    # add mortes sem ir pra uti
    # add mortes pós uti

    # em outros arquivos...
    # Somar 2 erros quadrados: Infectados gerais (BH) +(ou média) Infectados para UTI
    # Fazer minimize das duas curvas

    return params
