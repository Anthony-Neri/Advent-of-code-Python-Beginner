def extract_data_file(file):
    # Lit toutes les lignes du fichier
    with open(file, 'r', encoding='utf-8') as f:
        return f.read().splitlines()

file = "data/2025_3_test.txt"

data = extract_data_file(file)


totalBanksNumber = 0

for line in data:
    max_left = -1
    best = 0

    for char in line:
        digit = int(char)

        if max_left != -1:
            best = max(best, max_left * 10 + digit)

        max_left = max(max_left, digit)

    totalBanksNumber += best

print(totalBanksNumber)
