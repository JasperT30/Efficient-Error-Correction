from pydoc import plain
import matplotlib.pyplot as plt
import numpy as np

all_labels = [1, 2, 3, 4, 5, 10, 13, 15, 20, 30, 50]

standard = [[10] * len(all_labels)] * 4

plain_tool = [
    [3.00, 5.09, 6.54, 7.54, 8.26, 9.67, 9.88, 9.93, 9.98, 10.00, 10.00],
    [
        1.5,
        2.76986,
        3.84802,
        4.759895,
        5.540245,
        7.979055,
        8.731675,
        9.070865,
        9.56754,
        9.90235,
        9.99401,
    ],
    [
        1,
        1.89819,
        2.7044,
        3.42907,
        4.08057,
        6.47277,
        7.40832,
        7.88836,
        8.72609,
        9.53084,
        9.93157,
    ],
    [
        0.5,
        0.97471,
        1.42572,
        1.85209,
        2.257965,
        3.998975,
        4.84767,
        5.342355,
        6.37767,
        7.8029,
        9.17921,
    ],
]

OC = [
    [0.95, 1.78, 2.50, 3.13, 3.70, 5.80, 6.68, 7.15, 8.04, 9.06, 9.78],
    [0.48, 0.92, 1.34, 1.72, 2.09, 3.62, 4.36, 4.80, 5.73, 7.08, 8.60],
    [0.32, 0.62, 0.91, 1.19, 1.45, 2.63, 3.23, 3.60, 4.41, 5.71, 7.40],
    [0.16, 0.31, 0.47, 0.61, 0.76, 1.44, 1.82, 2.05, 2.61, 3.58, 5.08],
]

EE_ligs = [
    [1.45, 2.13, 2.74, 3.31, 3.82, 5.83, 6.69, 7.15, 8.04, 9.06, 9.77],
    [1.08, 1.44, 1.78, 2.10, 2.41, 3.77, 4.46, 4.87, 5.77, 7.09, 8.60],
    [0.96, 1.20, 1.43, 1.66, 1.88, 2.88, 3.42, 3.75, 4.51, 5.74, 7.41],
    [0.84, 0.96, 1.08, 1.20, 1.31, 1.87, 2.19, 2.39, 2.87, 3.74, 5.14],
]

EE_lr = [
    [1.98, 2.57, 3.11, 3.62, 4.07, 5.94, 6.75, 7.20, 8.06, 9.06, 9.77],
    [1.67, 1.97, 2.26, 2.55, 2.82, 4.04, 4.67, 5.05, 5.88, 7.15, 8.61],
    [1.56, 1.77, 1.97, 2.17, 2.35, 3.24, 3.72, 4.03, 4.71, 5.86, 7.44],
    [1.45, 1.56, 1.66, 1.76, 1.86, 2.35, 2.62, 2.80, 3.23, 4.01, 5.31],
]

EE = [
    [2.57, 3.11, 3.60, 4.07, 4.48, 6.19, 6.94, 7.36, 8.16, 9.11, 9.78],
    [2.28, 2.56, 2.83, 3.09, 3.33, 4.45, 5.02, 5.37, 6.14, 7.32, 8.68],
    [2.19, 2.38, 2.56, 2.74, 2.91, 3.72, 4.16, 4.44, 5.07, 6.12, 7.59],
    [2.09, 2.19, 2.28, 2.38, 2.46, 2.91, 3.16, 3.32, 3.71, 4.42, 5.61],
]
dec_places = 1

tool_options = {
    0: "existing tool, pessimistic case",
    1: "existing tool, optimistic case",
    2: "improved tool, pessimistic case",
    3: "improved tool, optimistic case",
}

for curr_tool in range(len(tool_options)):
    for xxxx in range(2):
        if xxxx == 0:
            l_start = 0
            l_end = 5
        else:
            l_start = 5
            l_end = len(all_labels)
        labels = all_labels[l_start:l_end]
        x = np.arange(len(labels))  # the label locations
        width = 0.15  # the width of the bars
        multiplier = 0

        approach_names = {
            "Standard": standard[curr_tool][l_start:l_end],
            "Error Detection only": [
                round(i, dec_places) for i in plain_tool[curr_tool][l_start:l_end]
            ],
            "Error Elimination: full": [
                round(i, dec_places) for i in EE[curr_tool][l_start:l_end]
            ],
            "Error Elimination: ligatures and rests": [
                round(i, dec_places) for i in EE_lr[curr_tool][l_start:l_end]
            ],
            "Error Elimination: ligatures": [
                round(i, dec_places) for i in EE_ligs[curr_tool][l_start:l_end]
            ],
            "Ordered Correction": [
                round(i, dec_places) for i in OC[curr_tool][l_start:l_end]
            ],
        }

        fig, ax = plt.subplots(layout="constrained")

        for approach, result in approach_names.items():
            offset = width * multiplier
            rects = ax.bar(
                x + offset,
                result,
                width,
                label=approach,
            )
            ax.bar_label(rects, padding=1, size=8)
            multiplier += 1

        # Add some text for labels, title and custom x-axis tick labels, etc.
        ax.set_ylabel("Amount of staves to be checked")
        ax.set_xlabel("Number of errors in the score")
        ax.set_title(
            f"Efficacy of different approaches for {tool_options[curr_tool]}, errors from {labels[0]} to {labels[-1]}"
        )
        ax.set_xticks(x + width, [str(i) for i in labels])
        box = ax.get_position()
        ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
        ax.legend(loc="center left", bbox_to_anchor=(1, 0.5))
        ax.set_ylim(0, 10.5)

        fig.set_size_inches(8.4 * 1.8, 2.5 * 1.8)
        fig.set_dpi(300)

        fig.savefig(f"generated/app_comparison_{curr_tool}_{l_start}.png")
