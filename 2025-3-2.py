def extract_data_file(file):
    # Lit toutes les lignes du fichier
    with open(file, 'r', encoding='utf-8') as f:
        return f.read().splitlines()

file = "data/2025_3.txt"

data = extract_data_file(file)

target_battery_count = 12
total_banks_number = 0


def build_max_sequence(target_count, digits):
    total_digits = len(digits)
    remaining_slots = target_count - 1

    search_limit = total_digits - remaining_slots
    max_digit = max(digits[:search_limit])
    max_digit_index = digits.index(max_digit)

    result = ""

    if remaining_slots - 1 >= 0:
        result = build_max_sequence(
            remaining_slots,
            digits[max_digit_index + 1:]
        )

    return max_digit + result


total_joltage = 0

for line in data:
    total_joltage += int(build_max_sequence(target_battery_count, line))

print(total_joltage)
