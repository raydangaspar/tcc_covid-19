# N     -> Total population (S + E + I + R)
# beta  -> Infection rate
# gamma -> Recovery rate
# delta -> Incubation period
# tay   -> Death rate
# khi   -> On average, days from infection to death
# y     -> Initial conditions vector
# t     -> Grid of time points (in days)
def deriv(y, t, N, beta, gamma, delta, tay, khi):
    S, E, I, R, D = y
    dSdt = -beta * S * I / N
    dEdt = beta * S * I / N - delta * E
    dIdt = delta * E - (1 - tay) * gamma * I - tay * khi * I
    dRdt = I * gamma * (1 - tay)
    dDdt = I * tay * khi
    return dSdt, dEdt, dIdt, dRdt, dDdt
