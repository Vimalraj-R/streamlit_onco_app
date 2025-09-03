import plotly.graph_objects as go
import random

def genetic_graph(patient):
    genes = patient.get("genes", ["BRCA1", "TP53", "EGFR", "KRAS"])
    x, y, z, text, color = [], [], [], [], []

    for g in genes:
        x.append(random.uniform(0, 5))
        y.append(random.uniform(0, 5))
        z.append(random.uniform(0, 5))
        text.append(g)

        if g in ["BRCA1", "TP53"]:
            color.append("red")
        elif g in ["EGFR", "KRAS"]:
            color.append("orange")
        else:
            color.append("green")

    fig = go.Figure(data=[go.Scatter3d(
        x=x, y=y, z=z,
        mode="markers+text",
        marker=dict(size=10, color=color),
        text=text,
        textposition="top center"
    )])

    fig.update_layout(
        title="Genetic Mutation Network",
        scene=dict(xaxis_title="X", yaxis_title="Y", zaxis_title="Z")
    )
    return fig
