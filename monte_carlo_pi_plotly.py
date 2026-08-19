"""Estimación de Pi por el método de Montecarlo, animada con plotly.

Misma idea que la versión de matplotlib: un círculo de radio 1 dentro de
un cuadrado de lado 2. pi ≈ 4 * (puntos dentro del círculo / puntos totales).
Aquí generamos los puntos de antemano y los mostramos como una animación
por "frames" con un botón de Play.
"""

import numpy as np
import plotly.graph_objects as go

NUM_POINTS = 500
POINTS_PER_FRAME = 5

x = np.random.uniform(-1, 1, NUM_POINTS)
y = np.random.uniform(-1, 1, NUM_POINTS)
inside = x**2 + y**2 <= 1

theta = np.linspace(0, 2 * np.pi, 200)
circle_x, circle_y = np.cos(theta), np.sin(theta)
square_x = [-1, 1, 1, -1, -1]
square_y = [-1, -1, 1, 1, -1]

frames = []
for n in range(POINTS_PER_FRAME, NUM_POINTS + 1, POINTS_PER_FRAME):
    pi_estimate = 4 * inside[:n].sum() / n
    frames.append(
        go.Frame(
            data=[
                go.Scatter(x=x[:n][inside[:n]], y=y[:n][inside[:n]], mode="markers",
                           marker=dict(color="green", size=5), name="Dentro"),
                go.Scatter(x=x[:n][~inside[:n]], y=y[:n][~inside[:n]], mode="markers",
                           marker=dict(color="red", size=5), name="Fuera"),
            ],
            name=str(n),
            layout=go.Layout(title=f"Puntos: {n} | Pi estimado: {pi_estimate:.5f}"),
        )
    )

fig = go.Figure(
    data=[
        go.Scatter(x=[], y=[], mode="markers", marker=dict(color="green", size=5), name="Dentro"),
        go.Scatter(x=[], y=[], mode="markers", marker=dict(color="red", size=5), name="Fuera"),
        go.Scatter(x=square_x, y=square_y, mode="lines", line=dict(color="black"), name="Cuadrado"),
        go.Scatter(x=circle_x, y=circle_y, mode="lines", line=dict(color="blue"), name="Círculo"),
    ],
    frames=frames,
)

fig.update_layout(
    title="Puntos: 0 | Pi estimado: -",
    xaxis=dict(range=[-1, 1], scaleanchor="y"),
    yaxis=dict(range=[-1, 1]),
    width=600,
    height=600,
    updatemenus=[
        dict(
            type="buttons",
            buttons=[dict(
                label="Play",
                method="animate",
                args=[None, {"frame": {"duration": 50, "redraw": True}, "fromcurrent": True}],
            )],
        )
    ],
)

fig.show()
