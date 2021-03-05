import plotly.graph_objs as go
import plotly.offline as py


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
