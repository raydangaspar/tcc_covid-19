import plotly.graph_objs as go
import plotly.offline as py
import matplotlib.pyplot as plt
import seaborn as sns


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


def plot_model_data(t, e, i, d=None):
    fig = plt.figure(figsize=(12, 6))
    ax = fig.add_subplot(223)
    ax.plot(t, i, lw=3, label="Infective")
    if d is not None:
        ax.plot(t, d, lw=3, label="Dead")
        ax.set_title("Infectious/Dead Population")
    else:
        ax.set_title("Infectious Population")
    if e is not None:
        ax.plot(t, e, lw=3, label="Exposed")
    ax.set_ylim(0, 0.3)
    ax.set_xlabel("Time /days")
    ax.set_ylabel("Fraction")
    ax.legend()


def plot_model_bh_data(t, e, i, d=None):
    plt.plot(t, i, lw=3, label="Infective")
    if d is not None:
        plt.plot(t, d, lw=3, label="Dead")
        plt.title("Infectious/Dead population BH")
    else:
        plt.title("Infectious population BH")
    if e is not None:
        plt.plot(t, e, lw=3, label="Exposed")
    plt.xlabel("Days")
    plt.ylabel("Population")
    plt.xlim(right=120)
    plt.legend()
    plt.show()


def inf_dead(t, i, d=None):
    plt.plot(t, i, lw=3, label="Infective")
    if d is not None:
        plt.plot(t, d, lw=3, label="Dead")
        plt.title("Infectious/Dead population BH")
    else:
        plt.title("Infectious population BH")
    plt.xlabel("Days")
    plt.ylabel("Population")
    plt.legend()
    plt.grid("True")
    plt.show()


def death_rate_graph(df):
    f, (ax_box, ax_hist) = plt.subplots(2, sharex=True, gridspec_kw={"height_ratios": (0.2, 1)})
    mean = df["DEATH_UTI_RATE"].mean()
    median = df["DEATH_UTI_RATE"].median()
    mode = df["DEATH_UTI_RATE"].mode()[0]

    sns.boxplot(x=df["DEATH_UTI_RATE"], ax=ax_box)
    ax_box.axvline(mean, color="r", linestyle="--")
    ax_box.axvline(median, color="g", linestyle="-")
    ax_box.axvline(mode, color="b", linestyle="-")

    sns.distplot(x=df["DEATH_UTI_RATE"], ax=ax_hist)
    ax_hist.axvline(mean, color="r", linestyle="--")
    ax_hist.axvline(median, color="g", linestyle="-")
    ax_hist.axvline(mode, color="b", linestyle="-")

    plt.legend({"Mean": mean, "Median": median, "Mode": mode})

    print(f"Mean: {mean}")
    print(f"Median: {median}")
    print(f"Mode: {mode}")

    ax_box.set(xlabel="")
    plt.show()
