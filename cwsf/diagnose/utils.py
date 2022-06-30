import os
import re
import uuid
import numpy as np
from scipy import stats
from pathlib import Path

dirname = os.path.dirname(__file__)
geneFile = os.path.join(dirname, "aiassets", "geneIDs.txt")
controlFile = os.path.join(dirname, "aiassets", "control.npy")

genes = open(geneFile, "r").read().splitlines()
geneIDs = [i.split("\t")[0] for i in genes]
geneNames = [i.split("\t")[2] for i in genes]
control_arr = np.load(controlFile)


def parse_file(f):
    if not os.path.exists("media"):
        os.makedirs("media")

    filename = f"{uuid.uuid4()}.txt"
    path = Path(os.path.join("media", filename))
    path.touch(exist_ok=True)
    with open(path, "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)
        destination.seek(0)
        data = destination.read().decode()
        lines = re.split(r"[\s,]+", data)
    return list(map(float, lines))


def gene_ID(x, y):
    return geneIDs[x * 45 + y]


def gene_name(x, y):
    return geneNames[x * 45 + y]


def z_score(sample, avg_control, std_control):
    return (sample - avg_control) / std_control


def p_score(z):
    return stats.norm.sf(abs(z)) * 2


def color(x, y, threshold):
    if y >= x + threshold:
        return "red"
    if y <= x - threshold:
        return "green"
    return "gray"


def color2(x, y, threshold_x, threshold_y):
    if x <= -threshold_x and y >= threshold_y:
        return "green"
    return "red" if x >= threshold_x and y >= threshold_y else "gray"


def plotComparison(sample, control, threshold=0.301):
    log_samples = np.log10(sample)
    log_control = np.log10(control)

    x = np.arange(min(log_samples), max(log_samples), 0.001)
    y1 = x + threshold
    y2 = x - threshold

    colors = [
        color(log_samples[i], log_control[i], threshold)
        for i in range(len(log_samples))
    ]

    return log_samples, log_control, x, y1, y2, colors


def plotVolcano(sample, control, threshold_x=1.0, threshold_y=1.301):
    log_sample = np.log2(sample)
    log_control = np.log2(control)

    log2FC = log_sample - log_control

    z = z_score(sample, control)
    p = -np.log10(p_score(z))

    colors = [
        color2(log2FC[i], p[i], threshold_x, threshold_y) for i in range(len(log2FC))
    ]

    return log2FC, threshold_x, threshold_y, colors


"""
TO-DO: Convert matplotlib stuff to chart.js

Plotting Instructions
    Comparison Plot:
        plt.title('Log10 Comparison Plot')
        plt.xlabel('Healthy')
        plt.ylabel('Cancer')
        plt.show()

        plt.scatter(log_sample, log_control, s=5, c=colors)
        plt.plot(x, y1, color='black')
        plt.plot(x, y2, color='black')

    Volcano Plot:
        control_vs_target_log2(sample, control, size=25)
        plt.title('Volcano Plot')
        plt.xlabel('Log2 Fold Change')
        plt.ylabel('-log10(P-value)')
        plt.show()

        plt.scatter(log2FC, p, s=size, c=colors)
        plt.axhline(y=threshold_y, color='black')
        plt.axvline(x=threshold_x, color='black')
        plt.axvline(x=-threshold_x, color='black')
"""
