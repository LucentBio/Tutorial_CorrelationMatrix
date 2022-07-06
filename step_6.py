# Matias I. Bofarull Oddo - 2022.06.14 - Lucent Biosciences Inc.

# import matplotlib as mpl

# mpl.use("Agg")

import matplotlib.pyplot as plt

plt.rcParams.update({"font.sans-serif": "Consolas"})

num_var = 15

plot_coord = []
for x_coord in range(num_var):
    for y_coord in range(num_var):
        plot_coord.append([x_coord, y_coord])

font_size = 90 / num_var

fig = plt.figure(figsize=(9, 9))

for i in range(num_var ** 2):
    ax = fig.add_subplot(num_var, num_var, i + 1)

    if plot_coord[i][0] < plot_coord[i][1]:
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
        ax.text(
            0.5, 0.35, str(plot_coord[i]), fontsize=font_size, ha="center", va="center"
        )
        ax.text(
            0.5,
            0.65,
            "↑",
            fontsize=font_size * 2.2,
            ha="center",
            va="center",
            rotation=-45,
        )

    elif plot_coord[i][0] > plot_coord[i][1]:
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
        ax.text(
            0.5, 0.35, str(plot_coord[i]), fontsize=font_size, ha="center", va="center"
        )
        ax.text(
            0.5,
            0.7,
            "↑",
            fontsize=font_size * 2.2,
            ha="center",
            va="center",
            rotation=135,
        )

    else:
        ax.axis("off")
        ax.text(
            0.5,
            0.5,
            "Feature\n" + str(plot_coord[i][0] + 1),
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

plt.show()

##############################################################################

# plt.savefig("step_6.png", dpi=300)
# plt.close()
