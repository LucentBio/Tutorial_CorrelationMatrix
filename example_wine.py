# Matias I. Bofarull Oddo - 2022.06.14 - Lucent Biosciences Inc.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

import matplotlib as mpl

mpl.use("Agg")

###############################################################################

# https://archive.ics.uci.edu/ml/datasets/wine+quality
# http://www3.dsi.uminho.pt/pcortez/wine5.pdf Table 1

# Cortez et al, 2009. Modeling wine preferences by data mining from physicochemical properties. Decision Support Systems.

wine = pd.read_csv("winequality-red.csv", sep=";")

print(wine.info())

features = [
    np.array(wine.iloc[:, 0]),  # fixed acidity
    np.array(wine.iloc[:, 1]),  # volatile acidity
    np.array(wine.iloc[:, 2]),  # citric acid
    np.array(wine.iloc[:, 3]),  # residual sugar
    np.array(wine.iloc[:, 4]),  # chlorides
    np.array(wine.iloc[:, 5]),  # free sulfur dioxide
    np.array(wine.iloc[:, 6]),  # total sulfur dioxide
    np.array(wine.iloc[:, 7]),  # density
    np.array(wine.iloc[:, 8]),  # pH
    np.array(wine.iloc[:, 9]),  # suplhates
    np.array(wine.iloc[:, 10]),  # alcohol
    np.array(wine.iloc[:, 11]),  # quality
]

feature_names = [
    "Tartaric acid (g/dm3)",
    "Acetic acid (g/dm3)",
    "Citric acid (g/dm3)",
    "Sugar (g/dm3)",
    "Chlorides (g/dm3)",
    "Sulphur dioxide (free mg/dm3)",
    "Sulphur dioxide (total mg/dm3)",
    "Density (g/cm3)",
    "Acidity (pH)",
    "Potassium sulfate (g/dm3)",
    "Alcohol (percent)",
    "Quality (scale from 0 to 10)",
]

###############################################################################

num_var = len(features)

plt.rcParams.update({"font.sans-serif": "Consolas"})
font_size = 90 / num_var

plot_coord = []
for x_coord in range(num_var):
    for y_coord in range(num_var):
        plot_coord.append([x_coord, y_coord])


def width_constrained_text(string_input, max_characters_per_line):
    count = 0
    lines_array = []
    segments = string_input.split(" ")
    for segment in segments:
        if len(segment) < max_characters_per_line:
            segment_plus = ""
            required_length = 0
            if count == 0:
                required_length = len(segment)
                segment_plus = segment
            else:
                required_length = len(segment) + 1
                segment_plus = " " + segment
            if count + required_length < max_characters_per_line:
                if count == 0:
                    lines_array.append(segment_plus)
                else:
                    lines_array[-1] += segment_plus
                count += required_length
            else:
                count = len(segment)
                lines_array.append(segment)
        else:
            lines_array.append(segment)
    return "\n".join(lines_array)


colormap = plt.cm.RdBu_r(np.linspace(0, 1, 9))  # number of colors
colormap_max = colormap[0]
colormap_min = colormap[-1]
colormap = colormap[1:-1][::-1]

colormap_threshold = 0.5


fig = plt.figure(figsize=(9, 9))

for i in range(num_var ** 2):

    title_string = width_constrained_text(feature_names[plot_coord[i][0]], 8)

    df_XY = pd.DataFrame(
        {
            "X": features[plot_coord[i][1]],
            "Y": features[plot_coord[i][0]],
        }
    )
    XY = df_XY.dropna()
    X = np.array(XY.X)
    Y = np.array(XY.Y)

    Pearson = pearsonr(X, Y)

    if Pearson[0] >= colormap_threshold:
        box_color = colormap_max
    elif Pearson[0] <= -colormap_threshold:
        box_color = colormap_min
    else:
        zeroed_Pearson = Pearson[0] + colormap_threshold
        scaling = len(colormap) / (2 * colormap_threshold)
        box_color = colormap[int(scaling * zeroed_Pearson)]

    ax = fig.add_subplot(num_var, num_var, i + 1)
    if plot_coord[i][0] < plot_coord[i][1]:

        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
        ax.spines["bottom"].set_color(box_color)
        ax.spines["top"].set_color(box_color)
        ax.spines["right"].set_color(box_color)
        ax.spines["left"].set_color(box_color)

        if Pearson[0] >= 0:
            ax.text(
                0.5,
                0.7,
                "[+]",
                fontsize=font_size,
                weight="bold",
                ha="center",
                va="center",
            )
        else:
            ax.text(
                0.5,
                0.7,
                "[-]",
                fontsize=font_size,
                weight="bold",
                ha="center",
                va="center",
            )
        if Pearson[0] >= 0.5 or Pearson[0] <= -0.5:
            ax.text(
                0.5,
                0.475,
                "%.3f" % abs(Pearson[0]),
                fontsize=font_size * 1.5,
                weight="bold",
                ha="center",
                va="center",
            )
        else:
            ax.text(
                0.5,
                0.48,
                "%.3f" % abs(Pearson[0]),
                fontsize=font_size,
                ha="center",
                va="center",
            )
        ax.text(
            0.5,
            0.3,
            "%.3f" % Pearson[1],
            fontsize=font_size * 0.9,
            ha="center",
            va="center",
        )

    elif plot_coord[i][0] > plot_coord[i][1]:

        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
        ax.spines["bottom"].set_color(box_color)
        ax.spines["top"].set_color(box_color)
        ax.spines["right"].set_color(box_color)
        ax.spines["left"].set_color(box_color)

        ax.scatter(
            X,
            Y,
            s=font_size * 1.2,
            edgecolor="none",
            color=box_color,
            alpha=colormap_threshold
            # c=[Pearson[0]] * len(X),
            # cmap="RdBu",
            # vmin=-colormap_threshold,
            # vmax=+colormap_threshold,
            # alpha=colormap_threshold,
        )

    else:
        ax.axis("off")
        ax.text(
            0.5,
            0.5,
            title_string,
            fontsize=font_size * 1.2,
            weight="bold",
            ha="center",
            va="center",
        )

margin = 0.015

fig.subplots_adjust(
    top=1 - margin,
    bottom=0 + margin,
    right=1 - margin,
    left=0 + margin,
    hspace=10 * margin,
    wspace=10 * margin,
)

# plt.show()

##############################################################################

plt.savefig("wine_correlation_matrix.png", dpi=300)
plt.close()

###############################################################################

# Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
