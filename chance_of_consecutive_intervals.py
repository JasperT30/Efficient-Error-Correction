# pylint: skip-file

import music21 as m21
import matplotlib.pyplot as plt
import numpy as np

consonant_intervals_to_bass = {1, 3, 5, 6}
consonant_intervals_inner_voices = {1, 3, 4, 5, 6}

pitches = "abcdefg"

bass_notes = []
middle_notes = []
top_notes = []

for pitch in pitches:
    bass_notes.append(m21.note.Note(pitch + "2"))
    middle_notes.append(m21.note.Note(pitch + "3"))
    top_notes.append(m21.note.Note(pitch + "4"))

diss_count = 0
cons_count = 0
all_count = 0

fract_diss_count = 0
fract_cons_count = 0
fract_all_count = 0

for i in bass_notes:
    for j in middle_notes:
        for k in top_notes:
            diss = False
            interval_1 = m21.interval.Interval(i, j)
            interval_2 = m21.interval.Interval(i, k)
            interval_3 = m21.interval.Interval(j, k)
            all_count += 3
            if interval_1.generic.mod7 not in consonant_intervals_to_bass:
                diss = True
                diss_count += 1
            else:
                cons_count += 1
            if interval_2.generic.mod7 not in consonant_intervals_to_bass:
                diss = True
                diss_count += 1
            else:
                cons_count += 1
            if interval_3.generic.mod7 not in consonant_intervals_inner_voices:
                diss = True
                diss_count += 1
            else:
                cons_count += 1
            if diss == True:
                fract_diss_count += 1
            else:
                fract_cons_count += 1
            fract_all_count += 1

print(f"{diss_count}/{all_count} dissonant, {cons_count}/{all_count} consonant")
print(
    f"{fract_diss_count}/{fract_all_count} dissonant, {fract_cons_count}/{fract_all_count} consonant"
)

frac = fract_cons_count / fract_all_count
x = range(1, 8)
y = [(frac**i) * 100 for i in x]

print(x)
print(y)

fig, ax = plt.subplots()

ax.plot(x, y, "x", markeredgewidth=2)

ax.set(xlim=(1, 8), xticks=np.arange(0, 8), ylim=(0, 30), yticks=np.arange(0, 35, 5))
yvals = ax.get_yticks()
ax.set_yticklabels(["{0}%".format(y) for y in yvals], fontsize=12)
for xy in zip(x, y):
    ax.annotate("  {:.2f}%".format(xy[1]), xy=xy, textcoords="data")
ax.set_xlabel("Number of consecutive intervals")
ax.set_ylabel("Chance of consonance")

plt.show()
