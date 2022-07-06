# Matias I. Bofarull Oddo - 2022.06.14 - Lucent Biosciences Inc.

import matplotlib as mpl

mpl.use("Agg")

import matplotlib.pyplot as plt

plt.rcParams.update({"font.sans-serif": "Consolas"})

num_var = 5

plot_coord = []
for x_coord in range(num_var):
    for y_coord in range(num_var):
        plot_coord.append([x_coord, y_coord])

fig = plt.figure(figsize=(9, 9))

for i in range(num_var ** 2):
    ax = fig.add_subplot(num_var, num_var, i + 1)

    if plot_coord[i][0] < plot_coord[i][1]:
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
        ax.text(0.5, 0.35, str(plot_coord[i]), fontsize=15, ha="center", va="center")
        ax.text(0.5, 0.65, "↑", fontsize=25, ha="center", va="center", rotation=-45)
    elif plot_coord[i][0] > plot_coord[i][1]:
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
        ax.text(0.5, 0.35, str(plot_coord[i]), fontsize=15, ha="center", va="center")
        ax.text(0.5, 0.65, "↑", fontsize=25, ha="center", va="center", rotation=135)
    else:
        ax.axis("off")
        ax.text(
            0.5,
            0.5,
            "Feature\n" + str(plot_coord[i][0] + 1),
            fontsize=20,
            ha="center",
            va="center",
        )

# plt.show()

##############################################################################

plt.savefig("step_3.png", dpi=300)
plt.close()
