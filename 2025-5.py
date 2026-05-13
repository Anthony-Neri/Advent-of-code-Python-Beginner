def extract_data_file(file):
    # Lit toutes les lignes du fichier
    with open(file, 'r', encoding='utf-8') as f:
        return f.read().splitlines()

file = "data/2025_5_1.txt"

file2 = "data/2025_5_2.txt"

data_fresh_ingredients = extract_data_file(file)

data_ingredients = extract_data_file(file2)

fresh_ingredients = set()


for ingredient in data_ingredients :
    for line in data_fresh_ingredients:
        i, j = line.split('-')

        if int(i) <= int(ingredient) <= int(j):
            fresh_ingredients.add(ingredient)
            break


print(len(fresh_ingredients))
