import matplotlib.pyplot as plt
import os
import io
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

def generate_colors(amount: int):
    generated_colors = [COLORS[i % len(COLORS)] for i in range(amount)]
    return generated_colors

devices = ["Entrada A", "Entrada B", "Entrada C",' Entrada D']
avg_flow = [78,68,0,73]


COLORS = ['red', 'green', 'blue' ,'yellow']

plt.bar(devices, avg_flow, color=COLORS)

plt.show()