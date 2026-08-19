"""Estimación de Pi por el método de Montecarlo, animada con matplotlib.

Idea: metemos un círculo de radio 1 dentro de un cuadrado de lado 2.
Tiramos puntos al azar dentro del cuadrado y contamos cuántos caen dentro
del círculo. La proporción (puntos dentro / puntos totales) se acerca a
la razón entre el área del círculo y el área del cuadrado, que es pi/4.
Por eso: pi ≈ 4 * (puntos dentro / puntos totales)
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

NUM_POINTS = 2000
POINTS_PER_FRAME = 10

fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect("equal")

square = plt.Rectangle((-1, -1), 2, 2, fill=False, edgecolor="black")
circle = plt.Circle((0, 0), 1, fill=False, edgecolor="blue")
ax.add_patch(square)
ax.add_patch(circle)

inside_x, inside_y = [], []
outside_x, outside_y = [], []
inside_scatter = ax.scatter([], [], color="green", s=5, label="Dentro")
outside_scatter = ax.scatter([], [], color="red", s=5, label="Fuera")
ax.legend(loc="upper right")
title = ax.set_title("")

total = 0
inside = 0


def update(frame):
    global total, inside

    for _ in range(POINTS_PER_FRAME):
        x, y = np.random.uniform(-1, 1, 2)
        if x**2 + y**2 <= 1:
            inside += 1
            inside_x.append(x)
            inside_y.append(y)
        else:
            outside_x.append(x)
            outside_y.append(y)
        total += 1

    inside_scatter.set_offsets(np.c_[inside_x, inside_y])
    outside_scatter.set_offsets(np.c_[outside_x, outside_y])

    pi_estimate = 4 * inside / total
    title.set_text(f"Puntos: {total} | Pi estimado: {pi_estimate:.5f}")

    if total >= NUM_POINTS:
        ani.event_source.stop()

    return inside_scatter, outside_scatter, title


ani = FuncAnimation(fig, update, interval=20, cache_frame_data=False)
plt.show()
