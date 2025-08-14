# pylint: skip-file

import music21 as m21
import matplotlib.pyplot as plt
import numpy as np

prob_lig = 0.45
prob_rest = 0.25
prob_note = 0.24
prob_dot = 0.06

sym_probs = [prob_lig, prob_rest, prob_dot, prob_note]

sym_probs = [0.2, 0.8]


x = range(1, 51)

probs = []
for i in x:
    new_probs = [None] * len(sym_probs)
    curr_prob = 0
    prev_prob = 0
    for j, sym_prob in enumerate(sym_probs):
        curr_prob += sym_prob
        # to find preferred strat
        new_probs[j] = curr_prob**i - prev_prob**i
        # to find prob of all errors being found
        # new_probs[j] = curr_prob**i
        prev_prob += sym_prob
    probs.append(new_probs)
    prob_str = f"{i}, "
    for item in new_probs:
        prob_str += f"{item}, "
    print(prob_str)
fig, ax = plt.subplots()

# ax.plot(x, [i[0] * 100 for i in probs], linewidth=2, label="Only ligatures")
# ax.plot(x, [i[1] * 100 for i in probs], linewidth=2, label="Ligatures and rests")
# ax.plot(x, [i[2] * 100 for i in probs], linewidth=2, label="Ligatures, rests and dots")
# ax.plot(x, [i[3] * 100 for i in probs], linewidth=2, label="All symbols")

# ax.plot(x, [i[0] * 100 for i in probs], linewidth=2, label="Only rests")
# ax.plot(x, [i[1] * 100 for i in probs], linewidth=2, label="Rests and dots")
# ax.plot(x, [i[2] * 100 for i in probs], linewidth=2, label="All symbols")

ax.plot(x, [i[0] * 100 for i in probs], linewidth=2, label="Only dots")
ax.plot(x, [i[1] * 100 for i in probs], linewidth=2, label="All symbols")

ax.set(
    xlim=(1, 10),
    xticks=np.arange(1, 11),
    ylim=(0, 110),
    yticks=np.arange(0, 110, 10),
)
yvals = ax.get_yticks()
ax.set_yticklabels(["{0}%".format(y) for y in yvals], fontsize=12)
ax.set_xlabel("Number of errors in a staff")
ax.set_ylabel("Probability of strategy finding all errors")
ax.legend()

plt.show()
