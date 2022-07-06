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
std_control = np.std(control_arr)


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


def getRGBA(x):
    x = float(x)
    r = 255 if x < 0.5 else 255 - (x * 2 - 1) * 255
    g = 255 if x > 0.5 else (x * 2) * 255
    return f"rgba({int(r)},{int(g)},0,0.8)"


def linear_color_map(arr):
    delta = control_arr - arr
    mn, mx = min(delta), max(delta)
    delta = (delta - mn) / (mx - mn) * 255
    return 255 - delta.astype(np.uint8)


def z_score(sample, control):
    return (sample - control) / std_control


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


def plotComparison(sample, threshold=0.301):
    sample = abs(np.array(sample))
    control = abs(control_arr)

    log_samples = np.log10(sample)
    log_control = np.log10(control)

    x = np.arange(min(log_samples), max(log_samples), 0.001)
    y1 = x + threshold
    y2 = x - threshold

    colors = [
        color(log_samples[i], log_control[i], threshold)
        for i in range(len(log_samples))
    ]

    return log_samples, log_control, colors


def plotVolcano(sample, threshold_x=1.0, threshold_y=1.301):
    sample = abs(np.array(sample))
    control = abs(control_arr)

    log_sample = np.log2(sample)
    log_control = np.log2(control)

    log2FC = log_sample - log_control

    z = z_score(sample, control)
    p = -np.log10(p_score(z))

    colors = [
        color2(log2FC[i], p[i], threshold_x, threshold_y) for i in range(len(log2FC))
    ]

    return log2FC, p, colors
