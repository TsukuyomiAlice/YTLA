# encode = utf-8
from features.divination.modules.eight_characters.dataset import eight_character_data
from core.classic.frame.router.instance.instanceProcessToRoutes import Response


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
    """
    计算十神权重
    :param checked_input: check_input 校验后的输入列表
    :return: dict - 包含原始十神计数、原始权重、大运十神计数、大运权重、流年十神计数、流年权重
    """
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

    return {
        "origin_count": origin_count_list,
        "origin_ratio": origin_ratio_list,
        "luck_count": luck_count_list,
        "luck_ratio": luck_ratio_list,
        "fleet_count": fleet_count_list,
        "fleet_ratio": fleet_ratio_list
    }


def analyze(eight_characters: str, luck_cycle: str = "", fleet_year: str = ""):
    """
    分析八字，返回结构化结果
    :param eight_characters: 八字字符串（如 "癸酉辛酉壬申己丑"）
    :param luck_cycle: 大运（如 "丁巳"）
    :param fleet_year: 流年（如 "丙午"）
    :return: Response 对象
    """
    checked_input = check_input(eight_characters, luck_cycle, fleet_year)
    if not checked_input:
        return Response(success=False, data={}, code=400, msg="输入错误：八字格式不正确")

    ten_god_relations = eight_character_data.ten_gods_relationship[checked_input[4]]
    ten_god_results = calculate_ratio_of_ten_gods(checked_input)

    eight_characters_parts = {
        "year": {"heavenly_stem": checked_input[0], "earthly_branch": checked_input[1]},
        "month": {"heavenly_stem": checked_input[2], "earthly_branch": checked_input[3]},
        "day": {"heavenly_stem": checked_input[4], "earthly_branch": checked_input[5]},
        "hour": {"heavenly_stem": checked_input[6], "earthly_branch": checked_input[7]}
    }

    data = {
        "input": {
            "eight_characters": eight_characters,
            "luck_cycle": luck_cycle,
            "fleet_year": fleet_year
        },
        "checked_input": checked_input,
        "eight_characters_parts": eight_characters_parts,
        "day_master": checked_input[4],
        "ten_god_relations": ten_god_relations,
        "ten_god_results": ten_god_results
    }

    return Response(success=True, data=data, code=200, msg="success")


def convert_solar_to_bazi(year: int, month: int, day: int, hour_branch: str = "", gender: str = ""):
    """
    将公历日期转换为八字（四柱）
    :param year: 公历年份
    :param month: 公历月份 (1-12)
    :param day: 公历日 (1-31)
    :param hour_branch: 时辰地支 (如 "子", "丑", ..., "亥")，可选
    :param gender: 性别 ("male" / "female")，可选，提供后返回大运表和流年表
    :return: Response 对象，包含 eight_characters 字符串和 four_pillars 结构
    """
    hs = eight_character_data.heavenly_stems
    eb = eight_character_data.earthly_branches
    sixty = eight_character_data.sixty_loop

    # 1. 年柱: (year - 4) % 10/12
    year_stem = hs[(year - 4) % 10 + 1]   # +1 因为 hs[0] 为空
    year_branch = eb[(year - 4) % 12 + 1]  # +1 因为 eb[0] 为空

    # 2. 月柱: 节气月 + 五虎遁
    # 节气近似日期 (月, 日) → 月支索引 (0=寅, 1=卯, ..., 11=丑)
    # 按历法顺序排列：小寒(隔年1月) → 立春(2月) → ... → 大雪(12月)
    term_starts = [
        (1, 6, 11),  # 小寒 → 丑(12月)
        (2, 4, 0),   # 立春 → 寅(1月)
        (3, 6, 1),   # 惊蛰 → 卯(2月)
        (4, 5, 2),   # 清明 → 辰(3月)
        (5, 6, 3),   # 立夏 → 巳(4月)
        (6, 6, 4),   # 芒种 → 午(5月)
        (7, 7, 5),   # 小暑 → 未(6月)
        (8, 7, 6),   # 立秋 → 申(7月)
        (9, 8, 7),   # 白露 → 酉(8月)
        (10, 8, 8),  # 寒露 → 戌(9月)
        (11, 7, 9),  # 立冬 → 亥(10月)
        (12, 7, 10), # 大雪 → 子(11月)
    ]

    # 确定节气月支索引：从后往前找最后一个已过的节气
    month_branch_idx = 11  # 默认丑月
    for term_m, term_d, branch_idx in term_starts:
        if month > term_m or (month == term_m and day >= term_d):
            month_branch_idx = branch_idx

    # 月支: branch_idx 0=寅→eb[3], 1=卯→eb[4], ..., 10=子→eb[1], 11=丑→eb[2]
    _eb_idx = (month_branch_idx + 3) % 12
    month_branch = eb[12 if _eb_idx == 0 else _eb_idx]  # 月支

    # 五虎遁: 年干0-based索引 → 月干起始索引(0=甲)
    # 甲己→丙(2), 乙庚→戊(4), 丙辛→庚(6), 丁壬→壬(8), 戊癸→甲(0)
    year_stem_0based = (year - 4) % 10
    # 0=甲, 1=乙, ..., 9=癸
    month_stem_start = (year_stem_0based * 2 + 2) % 10
    # 2=丙, 4=戊, 6=庚, 8=壬, 0=甲
    month_stem = hs[(month_stem_start + month_branch_idx) % 10 + 1]  # 月干

    # 3. 日柱: 从1900-01-01(甲戌日=sixty[10]) 计数
    def days_between(y1, m1, d1, y2, m2, d2):
        """计算两个日期之间的天数差"""
        days = 0
        # 从参考年到目标年
        for y in range(y1, y2):
            is_leap = (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)
            days += 366 if is_leap else 365
        # 参考年内的天数（1月1日到参考日期）
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        for m in range(1, m1):
            days -= days_in_month[m - 1]
            if m == 2 and ((y1 % 4 == 0 and y1 % 100 != 0) or (y1 % 400 == 0)):
                days -= 1
        days -= d1 - 1  # 从1日开始算
        # 目标年内的天数
        for m in range(1, m2):
            days += days_in_month[m - 1]
            if m == 2 and ((y2 % 4 == 0 and y2 % 100 != 0) or (y2 % 400 == 0)):
                days += 1
        days += d2 - 1
        return days

    day_diff = days_between(1900, 1, 1, year, month, day)
    day_ganzhi_idx = (day_diff + 10) % 60  # 1900-01-01 = 甲戌=sixty[10]
    day_stem = sixty[day_ganzhi_idx][0]
    day_branch = sixty[day_ganzhi_idx][1]

    # 4. 时柱: 五鼠遁 + 时辰地支
    hour_stem = ""
    hour_branch_value = ""
    if hour_branch and hour_branch in eb:
        hour_branch_value = hour_branch
        # 五鼠遁: 日干0-based索引 → 时干起始索引(0=甲)
        day_stem_0based = hs.index(day_stem) - 1  # 0=甲, 1=乙, ..., 9=癸
        hour_stem_start = (day_stem_0based * 2) % 10  # 0=甲, 2=丙, 4=戊, 6=庚, 8=壬
        hour_branch_idx = eb.index(hour_branch) - 1  # 0=子, 1=丑, ..., 11=亥
        hour_stem = hs[(hour_stem_start + hour_branch_idx) % 10 + 1]

    # 构建八字字符串
    eight_char = f"{year_stem}{year_branch}{month_stem}{month_branch}{day_stem}{day_branch}"
    if hour_stem and hour_branch_value:
        eight_char += f"{hour_stem}{hour_branch_value}"

    # 构建四柱结构
    four_pillars = {
        "year": {"heavenly_stem": year_stem, "earthly_branch": year_branch},
        "month": {"heavenly_stem": month_stem, "earthly_branch": month_branch},
        "day": {"heavenly_stem": day_stem, "earthly_branch": day_branch},
        "hour": {"heavenly_stem": hour_stem, "earthly_branch": hour_branch_value}
    }

    data = {
        "eight_characters": eight_char,
        "four_pillars": four_pillars
    }

    if gender:
        month_ganzhi = f"{month_stem}{month_branch}"
        hour_ganzhi = f"{hour_stem}{hour_branch_value}" if hour_stem and hour_branch_value else ""
        data["luck_cycle_table"] = calculate_luck_cycle_table(year, month, day, year_stem, month_ganzhi, gender, hour_ganzhi)
        # 根据大运表计算完整流年范围（从小运起始年到最后一个大运结束年）
        if data["luck_cycle_table"]:
            fy_start = data["luck_cycle_table"][0]["start_year"]
            fy_end = data["luck_cycle_table"][-1]["end_year"]
            data["fleet_years"] = calculate_fleet_years_list(fy_start, fy_end)
        else:
            data["fleet_years"] = calculate_fleet_years_list()

    return Response(success=True, data=data, code=200, msg="success")


# ---- 大运计算相关 ----

# 阳干：甲(1)、丙(3)、戊(5)、庚(7)
# 注：壬按用户规则属阴，从阳干中移除
YANG_STEMS = {"甲", "丙", "戊", "庚"}


def _is_yang_stem(stem: str) -> bool:
    """判断天干是否为阳"""
    return stem in YANG_STEMS


# 节令近似日期 (月, 日) —— 排大运时找"节"用
# 按历法顺序排列：小寒(1月) → 立春(2月) → ... → 大雪(12月)
LUCK_TERMS = [
    (1, 6),   # 小寒
    (2, 4),   # 立春
    (3, 6),   # 惊蛰
    (4, 5),   # 清明
    (5, 6),   # 立夏
    (6, 6),   # 芒种
    (7, 7),   # 小暑
    (8, 7),   # 立秋
    (9, 8),   # 白露
    (10, 8),  # 寒露
    (11, 7),  # 立冬
    (12, 7),  # 大雪
]


def _find_nearest_term(birth_year: int, birth_month: int, birth_day: int, forward: bool):
    """
    找到最近的"节"（顺排找下一个，逆排找上一个）

    使用 LUCK_TERMS 中的近似日期，仅精确到年/月（不含时辰时分）。

    :param birth_year: 出生年份
    :param birth_month: 出生月份 (1-12)
    :param birth_day: 出生日 (1-31)
    :param forward: True=顺排（找下一个节），False=逆排（找上一个节）
    :return: (term_year, term_month, term_day)
    """
    import datetime

    term_dates = []
    for term_m, term_d in LUCK_TERMS:
        try:
            term_dates.append(datetime.date(birth_year, term_m, term_d))
        except ValueError:
            pass

    birth_date = datetime.date(birth_year, birth_month, birth_day)

    if forward:
        # 顺排：找下一个节
        for td in term_dates:
            if birth_date < td:
                return td.year, td.month, td.day
        # 当年没有找到 → 下一年的小寒(1月6日)
        return birth_year + 1, 1, 6
    else:
        # 逆排：找上一个节
        for td in reversed(term_dates):
            if birth_date > td:
                return td.year, td.month, td.day
        # 当年没有找到 → 上一年的冬至(12月7日)
        return birth_year - 1, 12, 7


def _calculate_start_age(birth_year: int, birth_month: int, birth_day: int,
                         year_stem: str, gender: str):
    """
    计算起运年龄（虚岁）和起运时间（年/月）

    规则：
    - 阳男阴女 → 顺数至下一个节
    - 阴男阳女 → 逆数至上一个节
    - 3天 = 1年，1天 = 4个月（精确到年/月，不含天数）
    - 起运虚岁 = ceil(days_diff / 3) + 1

    :param birth_year: 出生年份
    :param birth_month: 出生月份
    :param birth_day: 出生日
    :param year_stem: 年干（用于判断阴阳）
    :param gender: 性别 ("male" / "female")
    :return: (start_age, years, months)
             start_age: 起运虚岁
             years: 起运年数（用于显示，如 1年）
             months: 起运月数（用于显示，如 4个月）
    """
    import datetime

    is_yang = _is_yang_stem(year_stem)
    is_male = (gender == "male")
    forward = (is_yang and is_male) or (not is_yang and not is_male)

    term_y, term_m, term_d = _find_nearest_term(birth_year, birth_month, birth_day, forward)

    birth_date = datetime.date(birth_year, birth_month, birth_day)
    term_date = datetime.date(term_y, term_m, term_d)

    if forward:
        days_diff = (term_date - birth_date).days
    else:
        days_diff = (birth_date - term_date).days

    # 换算：3天=1年，1天=4个月
    years = days_diff // 3
    remain_days = days_diff % 3
    months = remain_days * 4

    # 起运虚岁 = ceil(days_diff / 3) + 1
    # 虚岁从1开始，且从出生到起运经过 days_diff 天 ÷ 3 = 年数，取上整 + 1
    start_age = (days_diff + 2) // 3 + 1

    return start_age, years, months


def calculate_minor_luck(hour_ganzhi: str, year_stem: str, gender: str,
                         birth_year: int, start_age: int) -> list:
    """
    计算小运（从时柱起算，到起运年龄之前）

    规则：
    - 小运以时柱干支为起点
    - 阳男阴女 → 顺排（从时柱往后推六十甲子）
    - 阴男阳女 → 逆排（从时柱往前推六十甲子）
    - 每10年一柱，从1岁（虚岁）开始覆盖到起运年龄

    :param hour_ganzhi: 时柱干支（如 "己丑"）
    :param year_stem: 年干（用于判断阴阳）
    :param gender: 性别 ("male" / "female")
    :param birth_year: 出生年份
    :param start_age: 起运年龄（虚岁，由大运计算得出）
    :return: [{ "type": "minor", "index": 1, "ganzhi": "己丑",
                 "start_age": 1, "end_age": 2,
                 "start_year": 1990, "end_year": 1991 }, ...]
    """
    if not hour_ganzhi or len(hour_ganzhi) != 2:
        return []

    from features.divination.modules.eight_characters.dataset import eight_character_data
    sixty = eight_character_data.sixty_loop

    # 判断顺逆（同大运规则）
    is_yang = _is_yang_stem(year_stem)
    is_male = (gender == "male")
    forward = (is_yang and is_male) or (not is_yang and not is_male)

    hour_idx = sixty.index(hour_ganzhi)

    # 计算需要几柱小运才能覆盖到起运
    # 小运从虚岁1到起运前（start_age - 1），每柱10年
    # start_age=1 → 无需小运（直接起运）
    # start_age=3 → need=1（1-2岁，1柱）
    # start_age=12 → need=2（1-10 + 11-11，2柱）
    need_cycles = (start_age + 8) // 10

    table = []
    for i in range(need_cycles):
        if forward:
            luck_idx = (hour_idx + i) % 60
        else:
            luck_idx = (hour_idx - i) % 60
        luck_ganzhi = sixty[luck_idx]

        age_start = i * 10 + 1  # 虚岁，从1开始
        age_end = age_start + 9
        year_start = birth_year + age_start - 1  # 虚岁1 = 出生年份
        year_end = birth_year + age_end - 1

        table.append({
            "type": "minor",
            "index": i + 1,
            "ganzhi": luck_ganzhi,
            "start_age": age_start,
            "end_age": age_end,
            "start_year": year_start,
            "end_year": year_end,
        })

    # 最后一柱小运不能超过起运年龄（起运后进入大运）
    if table:
        last = table[-1]
        if last["end_age"] >= start_age:
            last["end_age"] = start_age - 1
            last["end_year"] = birth_year + last["end_age"] - 1

    return table


def calculate_luck_cycle_table(birth_year: int, birth_month: int, birth_day: int,
                                year_stem: str, month_ganzhi: str, gender: str,
                                hour_ganzhi: str = "") -> list:
    """
    计算大运排盘表（含小运）

    返回顺序：小运（若有）→ 10个大运，每个元素包含 type 字段区分

    起运规则（适用于年/月精度，不含天数）：
    - 阳男阴女 → 顺数至下一个节
    - 阴男阳女 → 逆数至上一个节
    - 3天 = 1年，1天 = 4个月
    - 起运虚岁 = ceil(days_diff / 3) + 1

    :param birth_year: 出生年份
    :param birth_month: 出生月份 (1-12)
    :param birth_day: 出生日 (1-31)
    :param year_stem: 年干（如 "癸"）
    :param month_ganzhi: 月柱干支（如 "辛酉"）
    :param gender: 性别 ("male" / "female")
    :param hour_ganzhi: 时柱干支（如 "己丑"），提供后计算小运
    :return: [{ "type": "minor"/"major", "index": 1, "ganzhi": "...",
                 "start_age": ..., "end_age": ...,
                 "start_year": ..., "end_year": ... }, ...]
    """
    from features.divination.modules.eight_characters.dataset import eight_character_data

    sixty = eight_character_data.sixty_loop

    # 1. 判断顺排/逆排
    is_yang = _is_yang_stem(year_stem)
    is_male = (gender == "male")
    forward = (is_yang and is_male) or (not is_yang and not is_male)
    # 阳男阴女→顺排, 阴男阳女→逆排

    # 2. 计算起运年龄（虚岁）
    start_age, _, _ = _calculate_start_age(birth_year, birth_month, birth_day, year_stem, gender)

    # ---- 合并结果：小运 + 大运 ----

    result = []

    # 3. 小运（从时柱起算，到起运年龄之前）
    if hour_ganzhi:
        minor_luck = calculate_minor_luck(hour_ganzhi, year_stem, gender, birth_year, start_age)
        result.extend(minor_luck)

    # 4. 排大运干支（从月柱开始，排10个大运，每柱10年）
    month_idx = sixty.index(month_ganzhi)

    for i in range(10):
        if forward:
            luck_idx = (month_idx + 1 + i) % 60
        else:
            luck_idx = (month_idx - 1 - i) % 60
        luck_ganzhi = sixty[luck_idx]

        age_start = start_age + i * 10
        age_end = age_start + 9
        year_start = birth_year + age_start - 1  # 虚岁转公历：year = birth_year + age - 1
        year_end = birth_year + age_end - 1

        result.append({
            "type": "major",
            "index": i + 1,
            "ganzhi": luck_ganzhi,
            "start_age": age_start,
            "end_age": age_end,
            "start_year": year_start,
            "end_year": year_end,
        })

    return result


def calculate_fleet_years_list(start_year: int = None, end_year: int = None) -> list:
    """
    计算流年列表
    :param start_year: 起始年份（默认当前年份-5）
    :param end_year: 结束年份（默认当前年份+14）
    :return: [{ "year": 2021, "ganzhi": "辛丑" }, ...]
    """
    from features.divination.modules.eight_characters.dataset import eight_character_data

    if start_year is None:
        current_year = 2026
        start_year = current_year - 5
    if end_year is None:
        end_year = start_year + 19  # 默认共20年

    hs = eight_character_data.heavenly_stems
    eb = eight_character_data.earthly_branches

    result = []
    for y in range(start_year, end_year + 1):
        stem = hs[(y - 4) % 10 + 1]
        branch = eb[(y - 4) % 12 + 1]
        result.append({
            "year": y,
            "ganzhi": f"{stem}{branch}"
        })

    return result


def save_history(plan_id: int, module_id: int, birthday: str, birth_time: str, gender: str,
                 eight_characters: str, luck_cycle: str = "", fleet_year: str = "",
                 analysis_result: str = "", annotations: str = "",
                 lunar_date: str = "", creator: str = ""):
    """
    保存八字分析结果到历史记录（按 eight_characters + gender 去重，存在则覆盖更新）
    :param plan_id: 计划ID
    :param module_id: 模块ID
    :param birthday: 出生日期（公历）
    :param birth_time: 出生时辰
    :param gender: 性别
    :param eight_characters: 八字
    :param luck_cycle: 大运
    :param fleet_year: 流年
    :param analysis_result: 分析结果
    :param annotations: 用户批注
    :param lunar_date: 农历日期
    :param creator: 创建者
    :return: Response 对象
    """
    from features.divination.modules.eight_characters.dao.daoModuleEightCharacters import (
        insert_history, update_history, select_history_by_eight_characters_and_gender
    )

    data_dict = {
        "BIRTHDAY": birthday,
        "LUNAR_DATE": lunar_date,
        "BIRTH_TIME": birth_time,
        "GENDER": gender,
        "EIGHT_CHARACTERS": eight_characters,
        "LUCK_CYCLE": luck_cycle,
        "FLEET_YEAR": fleet_year,
        "ANALYSIS_RESULT": analysis_result,
        "ANNOTATIONS": annotations,
        "CREATOR": creator,
        "UPDATER": creator
    }

    # 按 eight_characters + gender 查重
    existing = select_history_by_eight_characters_and_gender(plan_id, module_id, eight_characters, gender)
    if existing:
        # 存在则覆盖更新（保留原 RECORD_ID）
        record_id = existing["RECORD_ID"]
        success = update_history(plan_id, module_id, record_id, data_dict)
        if success:
            return Response(success=True, data={"record_id": record_id}, code=200, msg="更新成功")
        else:
            return Response(success=False, data={}, code=500, msg="更新失败")
    else:
        # 不存在则插入新记录
        record_id = insert_history(plan_id, module_id, data_dict)
        if record_id:
            return Response(success=True, data={"record_id": record_id}, code=200, msg="保存成功")
        else:
            return Response(success=False, data={}, code=500, msg="保存失败")


def get_history_list(plan_id: int, module_id: int, creator: str = "", limit: int = 20, offset: int = 0):
    """
    获取历史记录列表
    :param plan_id: 计划ID
    :param module_id: 模块ID
    :param creator: 创建者用户名
    :param limit: 每页条数
    :param offset: 偏移量
    :return: Response 对象
    """
    from features.divination.modules.eight_characters.dao.daoModuleEightCharacters import select_history_list

    records = select_history_list(plan_id, module_id, creator, limit, offset)
    return Response(success=True, data={"records": records, "total": len(records)}, code=200, msg="success")


def get_history_detail(plan_id: int, module_id: int, eight_characters: str, gender: str):
    """
    获取单条历史记录详情（按 EIGHT_CHARACTERS + GENDER 查询）
    :param plan_id: 计划ID
    :param module_id: 模块ID
    :param eight_characters: 八字字符串
    :param gender: 性别
    :return: Response 对象
    """
    from features.divination.modules.eight_characters.dao.daoModuleEightCharacters import select_history_by_eight_characters_and_gender

    record = select_history_by_eight_characters_and_gender(plan_id, module_id, eight_characters, gender)
    if record:
        return Response(success=True, data={"record": record}, code=200, msg="success")
    else:
        return Response(success=False, data={}, code=404, msg="记录未找到")


def delete_history(plan_id: int, module_id: int, eight_characters: str, gender: str):
    """
    逻辑删除历史记录（按 EIGHT_CHARACTERS + GENDER）
    :param plan_id: 计划ID
    :param module_id: 模块ID
    :param eight_characters: 八字字符串
    :param gender: 性别
    :return: Response 对象
    """
    from features.divination.modules.eight_characters.dao.daoModuleEightCharacters import soft_delete_history_by_eight_characters_and_gender

    result = soft_delete_history_by_eight_characters_and_gender(plan_id, module_id, eight_characters, gender)
    if result:
        return Response(success=True, data={}, code=200, msg="删除成功")
    else:
        return Response(success=False, data={}, code=500, msg="删除失败")
