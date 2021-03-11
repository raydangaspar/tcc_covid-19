# to do
# N     -> Total population (S + E + I + R)
# beta  -> Infection rate
# gamma -> Recovery rate
# delta -> Incubation period
# y     -> Initial conditions vector
# t     -> Grid of time points (in days)
def deriv(y, t, N, beta, gamma, delta):
    S, E, I, R = y
    dSdt = -beta * S * I / N
    dEdt = beta * S * I / N - delta * E
    dIdt = delta * E - gamma * I
    dRdt = gamma * I
    return dSdt, dEdt, dIdt, dRdt
