def extract_data_file(file):
    # Lit toutes les lignes du fichier
    with open(file, 'r', encoding='utf-8') as f:
        return f.read().splitlines()

file = "data/2025_5_1.txt"


data_fresh_ingredients_intervals = extract_data_file(file)

data_intervals = []

for interval in data_fresh_ingredients_intervals:
    i, j = interval.split('-')
    data_intervals.append((int(i),int(j)))


def get_new_interval(intervals):
    intervals = sorted(intervals)
    intervals_merged = []

    for a, b in intervals:
        if not intervals_merged:
            intervals_merged.append((a, b))
        else:
            x, y = intervals_merged[-1]

            if a <= y: #Le nouvel intervalle commence avant ou pendant la fin du précédent
                intervals_merged[-1] = (x, max(y, b))
            else:
                intervals_merged.append((a, b))

    return intervals_merged

new_intervals = get_new_interval(data_intervals)

response = 0
for interval in new_intervals:
    e,f = interval
    response += f-e +1

print(response)
