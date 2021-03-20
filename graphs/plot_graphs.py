import plotly.graph_objs as go
import plotly.offline as py
import matplotlib.pyplot as plt


def plot_graph(df, x_arg, y_arg, graph_title, x_title, y_title):
    trace = go.Scatter(x=df[x_arg], y=df[y_arg], mode="markers")

    data = [trace]

    layout = dict(
        title=graph_title,
        xaxis=dict(title=x_title),
        yaxis=dict(title=y_title),
    )

    fig = dict(data=data, layout=layout)

    py.iplot(fig)


def plot_infectous_pop(t, e, i):
    fig = plt.figure(figsize=(12, 6))
    ax = fig.add_subplot(223)
    ax.plot(t, i, lw=3, label="Infective")
    ax.set_title("Infectious Population")
    if e is not None:
        ax.plot(t, e, lw=3, label="Exposed")
    ax.set_ylim(0, 0.3)
    ax.set_xlabel("Time /days")
    ax.set_ylabel("Fraction")
    ax.legend()
