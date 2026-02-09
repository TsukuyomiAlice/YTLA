# encode = utf-8
from features.divination.modules.eight_characters.dataset import eight_character_data


def check_input(eight_characters: str, luck_cycle: str="", fleet_year:str="") -> list:
    eight_characters = eight_characters.strip()
    if len(eight_characters) not in (6, 8):
        return []
    hex_1 = eight_characters[0]
    hex_2 = eight_characters[1]
    hex_3 = eight_characters[2]
    hex_4 = eight_characters[3]
    hex_5 = eight_characters[4]
    hex_6 = eight_characters[5]
    if len(eight_characters) == 8:
        hex_7 = eight_characters[6]
        hex_8 = eight_characters[7]
    else:
        hex_7 = ""
        hex_8 = ""
    if (hex_1 not in eight_character_data.heavenly_stems
            or hex_3 not in eight_character_data.heavenly_stems
            or hex_5 not in eight_character_data.heavenly_stems
            or hex_7 not in eight_character_data.heavenly_stems
            or hex_2 not in eight_character_data.earthly_branches
            or hex_4 not in eight_character_data.earthly_branches
            or hex_6 not in eight_character_data.earthly_branches
            or hex_8 not in eight_character_data.earthly_branches):
        return []

    luck_cycle = luck_cycle.strip()
    if len(luck_cycle) not in (0, 2):
        return []
    if len(luck_cycle) == 2:
        hex_9 = luck_cycle[0]
        hex_10 = luck_cycle[1]
    else:
        hex_9 = ""
        hex_10 = ""
    if hex_9 not in eight_character_data.heavenly_stems or hex_10 not in eight_character_data.earthly_branches:
        return []

    fleet_year = fleet_year.strip()
    if len(fleet_year) not in (0, 2):
        return []
    if len(fleet_year) == 2:
        hex_11 = fleet_year[0]
        hex_12 = fleet_year[1]
    else:
        hex_11 = ""
        hex_12 = ""
    if hex_11 not in eight_character_data.heavenly_stems or hex_12 not in eight_character_data.earthly_branches:
        return []

    return [hex_1, hex_2, hex_3, hex_4, hex_5, hex_6, hex_7, hex_8, hex_9, hex_10, hex_11, hex_12]


def calculate_ratio_of_ten_gods(checked_input: list):
    origin_count_list = {"比肩": 0, "劫财": 0, "枭神": 0, "正印": 0, "食神": 0, "伤官": 0, "七杀": 0, "正官": 0, "偏财": 0, "正财": 0}
    origin_ratio_list = {"比肩": 0, "劫财": 0, "枭神": 0, "正印": 0, "食神": 0, "伤官": 0, "七杀": 0, "正官": 0, "偏财": 0, "正财": 0}
    ten_god_list = eight_character_data.ten_gods_relationship[checked_input[4]]
    for i in (0, 2, 4, 6):
        if checked_input[i] in eight_character_data.heavenly_stems and checked_input[i] != "":
            origin_count_list[ten_god_list[checked_input[i]]] += 10
    for i in (1, 3, 5, 7):
        if checked_input[i] in eight_character_data.earthly_branches and checked_input[i] != "":
            hidden_earth = eight_character_data.earthly_branches_relations[checked_input[i]]["hidden"]
            origin_count_list[ten_god_list[hidden_earth[0]]] += 7
            origin_count_list[ten_god_list[hidden_earth[1]]] += 2
            origin_count_list[ten_god_list[hidden_earth[2]]] += 1
    if checked_input[6] == "":
        origin_right = 60
    else:
        origin_right = 80
    for k, v in origin_ratio_list.items():
        origin_ratio_list[k] = round(origin_count_list[k] / origin_right * 100, 2)
    print(f'原始十神计数: {origin_count_list}')
    print(f'原始计算后权重: {origin_ratio_list}')

    right = origin_right
    luck_count_list = origin_count_list.copy()
    luck_ratio_list = origin_ratio_list.copy()
    if checked_input[8] != "":
        luck_count_list[ten_god_list[checked_input[8]]] += 10
        hidden_earth = eight_character_data.earthly_branches_relations[checked_input[9]]["hidden"]
        luck_count_list[ten_god_list[hidden_earth[0]]] += 7
        luck_count_list[ten_god_list[hidden_earth[1]]] += 2
        luck_count_list[ten_god_list[hidden_earth[2]]] += 1
        right = right + 20
        for k, v in luck_ratio_list.items():
            luck_ratio_list[k] = round(luck_count_list[k] / right * 100, 2)
        print(f'大运十神计数: {luck_count_list}')
        print(f'大运计算后权重: {luck_ratio_list}')

    fleet_count_list = luck_count_list.copy()
    fleet_ratio_list = luck_ratio_list.copy()
    if checked_input[10] != "":
        fleet_count_list[ten_god_list[checked_input[10]]] += 10
        hidden_earth = eight_character_data.earthly_branches_relations[checked_input[11]]["hidden"]
        fleet_count_list[ten_god_list[hidden_earth[0]]] += 7
        fleet_count_list[ten_god_list[hidden_earth[1]]] += 2
        fleet_count_list[ten_god_list[hidden_earth[2]]] += 1
        right = right + 20
        for k, v in fleet_ratio_list.items():
            fleet_ratio_list[k] = round(fleet_count_list[k] / right * 100, 2)
        print(f'流年十神计数: {fleet_count_list}')
        print(f'流年计算后权重: {fleet_ratio_list}')


def analyze_eight_characters(eight_characters: str, luck_cycle: str="", fleet_year: str=""):
    checked_input = check_input(eight_characters, luck_cycle, fleet_year)
    print(checked_input)
    if checked_input:
        print(f"日元：{checked_input[4]}")
        print(f"十神关系：{eight_character_data.ten_gods_relationship[checked_input[4]]}")
        calculate_ratio_of_ten_gods(checked_input)
    else:
        print("输入错误")

analyze_eight_characters("癸酉辛酉壬申己丑", luck_cycle="丁巳", fleet_year="丙午")
