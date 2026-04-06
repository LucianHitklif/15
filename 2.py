input_string = input("Введите список растений: ")

plants_list = input_string.split(", ")

print("\nРастения на ферме:")
for plant in plants_list:
    print(plant)

hybrids_input = input("Введите список гибридов: ")
plants_to_cross = input("Введите два растения для скрещивания (через пробел): ").split()

hybrid_pairs = hybrids_input.strip(';').split(';')
hybrid_dict = {}

for pair in hybrid_pairs:
    if '=' not in pair:
        continue
    left, right = pair.split('=')
    plants_pair = left.split('+')
    if len(plants_pair) == 2:
        plant1, plant2 = plants_pair[0], plants_pair[1]
        key = tuple(sorted([plant1, plant2]))
        hybrid_dict[key] = right

if len(plants_to_cross) == 2:
    plant_a, plant_b = plants_to_cross[0], plants_to_cross[1]
    search_key = tuple(sorted([plant_a, plant_b]))
    if search_key in hybrid_dict:
        print(f"Получен гибрид: {hybrid_dict[search_key]}")
    else:
        print("Эти растения нельзя скрестить")
else:
    print("Ошибка: нужно ввести ровно два растения")
