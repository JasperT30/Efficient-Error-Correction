import numpy as np
import matplotlib.pyplot as plt


def get_staff_at_timing(voice, timing):
    if len(voice) <= 1:
        return None
    for i in range(len(voice) - 1):
        if voice[i] <= timing and voice[i + 1] >= timing:
            return i
    return None


x = [1, 2, 3, 4, 5, 10, 13, 15, 20, 30, 50]
trials = 10000
data = []
# pessimistic case & improved tool 1
# voices = [np.linspace(0, 1, 5), np.linspace(0, 1, 4), np.linspace(0, 1, 4)]
# optimistic case & improved tool 2
voices = [np.linspace(0, 1, 9), np.linspace(0, 1, 7), np.linspace(0, 1, 7)]

for err_count in x:
    piece_data = []
    clustered_errors = {}
    for i in range(trials):

        errors = []
        for i in range(0, err_count):
            voice = np.random.randint(0, len(voices))
            timing = np.random.random()
            errors.append((voice, timing))

        staves_to_check = []
        for error in errors:
            timing = error[1]
            # pessimistic and optimistic case
            # for i, voice in enumerate(voices):
            #     staves_to_check.append((i, get_staff_at_timing(voice, timing)))
            # improved tool 1 & 2:
            staves_to_check.append(
                (error[0], get_staff_at_timing(voices[error[0]], timing))
            )
        uniques_to_check, staff_counts = np.unique(
            staves_to_check, return_counts=True, axis=0
        )
        piece_data.append(len(uniques_to_check))
        keys, counts = np.unique(staff_counts, return_counts=True)
        for i, key in enumerate(keys):
            if key not in clustered_errors.keys():
                clustered_errors[int(key)] = 0
            clustered_errors[int(key)] += int(counts[i])
    # pessimistic case & improved tool 1
    # data.append(np.mean(piece_data))
    # optimistic case & improved tool 2
    data.append(np.mean(piece_data) / 2)
    dict_string = f"{err_count}, {data[-1]}"
    for i in range(1, max(clustered_errors.keys()) + 1):
        if i in clustered_errors.keys():
            dict_string += f", {clustered_errors[i]}"
        else:
            dict_string += ", 0"
    print(dict_string)


fig, ax = plt.subplots()
ax.plot(x, data, "x", markeredgewidth=2)
yvals = ax.get_yticks()
for xy in zip(x, data):
    ax.annotate("  {:.2f}".format(xy[1]), xy=xy, textcoords="data")
ax.set_xlabel("Number of errors")
ax.set_ylabel("Average amount of staves to be checked")
plt.show()
