import numpy as np

x = [1, 2, 3, 4, 5, 10, 13, 15, 20, 30, 50]
trials = 100000

p = [0.45, 0.7, 0.76]


for err_count in x:
    counts = {"lig": [], "ligrest": [], "full": []}
    for i in range(trials):
        new_count = np.array([err_count] * 3)
        for error in range(err_count):
            error_found = np.random.rand()
            if error_found <= p[0]:
                new_count -= np.array([1, 1, 1])
            elif error_found <= p[1]:
                new_count -= np.array([0, 1, 1])
            elif error_found <= p[2]:
                new_count -= np.array([0, 0, 1])
        counts["lig"].append(new_count[0])
        counts["ligrest"].append(new_count[1])
        counts["full"].append(new_count[2])
    print(f"Results for {err_count} errors")
    for key in ["lig", "ligrest", "full"]:
        a, b = np.unique(counts[key], return_counts=True)
        print_str = ""
        for i in range(0, max(a) + 1):
            if i in a:
                print_str += f", {b[np.where(a == i)[0][0]]}"
            else:
                print_str += f", 0"
        print(key, print_str)
