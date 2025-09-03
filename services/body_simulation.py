import plotly.graph_objects as go

def body_simulation(patient):
    """Digital body visualization with cancer site highlighting."""

    # Organs + approximate 2D coordinates (for overlay on silhouette)
    organs = {
        "Lungs": {"x": 0, "y": 2, "color": "lightblue"},
        "Heart": {"x": 0, "y": 1.2, "color": "pink"},
        "Liver": {"x": 0.6, "y": 0.5, "color": "orange"},
        "Kidney (Left)": {"x": -0.6, "y": -0.5, "color": "green"},
        "Kidney (Right)": {"x": 0.6, "y": -0.5, "color": "green"}
    }

    # Highlight based on patient condition
    highlight = {
        "Lung Cancer": ["Lungs"],
        "Breast Cancer": ["Heart"],  # approximation
        "Liver Cancer": ["Liver"],
        "Kidney Cancer": ["Kidney (Left)", "Kidney (Right)"],
        "Leukemia": ["Heart"],  # blood system → central
        "Prostate Cancer": ["Kidney (Right)"],  # lower abdomen approximation
        "Ovarian Cancer": ["Kidney (Left)"],    # lower abdomen approximation
    }

    # Prepare markers
    x, y, text, colors, sizes = [], [], [], [], []
    for organ, pos in organs.items():
        x.append(pos["x"])
        y.append(pos["y"])
        text.append(organ)

        # Default color
        c = pos["color"]
        s = 20

        # If this organ is affected, make it glow red & bigger
        if organ in highlight.get(patient.get("condition", ""), []):
            c = "red"
            s = 35

        colors.append(c)
        sizes.append(s)

    # Build figure
    fig = go.Figure()

    # Add organ markers
    fig.add_trace(go.Scatter(
        x=x, y=y,
        mode="markers+text",
        marker=dict(size=sizes, color=colors, opacity=0.8, line=dict(width=2, color="black")),
        text=text,
        textposition="top center"
    ))

    # Add body silhouette background (simple rectangle for now)
    fig.update_layout(
        title="🧍 Digital Body Simulation",
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        showlegend=False,
        plot_bgcolor="black",
        paper_bgcolor="black",
        height=600
    )

    return fig
