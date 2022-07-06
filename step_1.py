# Matias I. Bofarull Oddo - 2022.06.14 - Lucent Biosciences Inc.

import matplotlib as mpl

mpl.use("Agg")

import matplotlib.pyplot as plt

plt.rcParams.update({"font.sans-serif": "Consolas"})

num_var = 5

fig = plt.figure(figsize=(9, 9))

for i in range(num_var ** 2):
    ax = fig.add_subplot(num_var, num_var, i + 1)
    ax.text(0.5, 0.5, str(i + 1), fontsize=20, ha="center", va="center")

# plt.show()

##############################################################################

plt.savefig("step_1.png", dpi=300)
plt.close()
