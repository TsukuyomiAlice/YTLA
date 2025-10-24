# encode = utf-8

article_treasure = """
# 第 7 章：宝藏 Treasure
冒险者们为各种东西奋斗，包括荣耀、知识和正义。许多的冒险者同时也追求着更多实在的东西：财富。麻绳一样粗的金链，大堆的铂金币，镶有宝石的王冠，珐琅般多彩的权杖，大捆的丝绸，以及强大的魔法物品等所有的一切，都在等待着勇敢寻宝的冒险者们前来探索和夺取。
本章详述了魔法物品和冒险中的藏宝地、魔法物品和普通物品，以及除此之外的其他奖励方案
"""

article_types_of_treasure = """
# 宝藏类型 Types of Treasure
宝藏有许多种形式。
硬币 Coins。最基本的宝藏类型就是钱，包括铜币（cp）、银币（sp）、银金币（ep）、金币（gp）和铂金币（pp）。50 枚任何类型的硬币都有 1 磅重。
宝石 Gemstones。宝石小巧轻便且比同样价值的硬币更易于保存。下文“宝石”小节中有介绍可用作被发现宝藏的各种奇石、宝石和珠宝。
艺术品物件 Art Objects。纯金的神像、镶满宝石的项链、古代国王的绘画、散发着珠光宝气的盘碟等艺术品。下文“艺术品物件”中有介绍可用作被发现宝藏的各种有价值和装饰性的艺术品。
魔法物品 Magic Items。魔法物品类型包括护甲、魔药、卷轴、戒指、权杖、法杖、魔杖、武器和奇物。魔法物品还设定了稀有度：普通、非普通、珍稀，极珍稀和传说。
经常会有一些持有并使用魔法物品的智能怪物，而其他的怪物则会将这些物品藏起来一面弄丢或被盗。比如说，如果一个大地精不足宝库里库存这一把+1长剑 longsword 和炼金壶alchemy jug，该部族的军阀可能会持用这把宝剑，而壶则会被安放在安全的地方。
"""

article_random_treasure = """
# 随机宝藏 Random Treasure
你可以使用以下数页中附带的表格随机生成若干宝藏，以让怪物携带、巢穴贮藏或其他地方藏匿。宝藏所在位置由你决定。关键在于要确保玩家们能够感觉到自己以游戏中的角色战胜危险并获得奖励。

# 宝藏表 Treasure Tables
你可以根据怪物的挑战等级来随机分配宝藏。表格分为挑战等级 0 至 4，挑战等级 5 至 10，挑战等级 11 至 16 和挑战等级 17 或更高。你还可以使用这些随机表格来确定某个怪物携带了多少钱（相当于 D&D 中的零花钱）或在某个较大的宝库中发现的财富总金额。

# 使用个体宝藏表 Using the Individual Treasure Tables
一张“个体宝藏”表可以帮你随机选定单个生物自身携带的宝藏。你可以在处理一些不喜欢收藏财宝的怪物时使用这些表格来确定怪物的被害人意外遗留下的宝藏。
使用对应怪物挑战等级的“个体宝藏”表，然后骰 d100并参考相应结果来确定怪物携带什么类型多少数量钱币。如果你想节省时间不掷骰，该表格还在括号内列出了平均值。在确定一组同类怪物的宝藏总量时，你还可以掷骰一次再与生物数量相乘来得出结果以节省时间。
如果觉得怪物们带着一大堆钱币没有意义，你还可以将钱币转换成宝石或同等价值的艺术品。

# 使用库藏宝藏表 Using the Treasure Hoard Tables
一张“库藏宝藏”表帮你随机选定的宝藏可应用于藏品量大的宝藏，一大群生物共同积累的财富（比如一个兽人部族或大地精军队），一个喜强大生物因个人兴趣而聚敛的宝库（比如一条龙），或者在队伍完成一项任务后作为报答者的馈赠奖励。你也可以将这些宝藏分开存放，以让冒险者们分几次寻获这些财宝。
选定某种怪物个体收藏的宝藏时，要先选择对应怪物挑战等级的表格。而掷骰选定某怪物群体库藏的宝藏时，则选择与怪物头领挑战等级相应的表格。如果宝库不属于任何人，则使用你所设置的当前地下城或巢穴中栖息怪物的挑战等级。
如果该宝库是某个报答者的赠礼，则使用与队伍平均等级相当的挑战等级。
每个宝库都包含了一些随机数量的钱币（如每个表格开头所述）。骰一次 d100 然后参考该表格以选定宝库中可能存在的宝石与艺术品数量。并用同样的骰来选定宝库中可能存在的魔法物品。
这些表格与个体宝藏表一样在括号中列出了相应的平均值，以便你直接使用来节省掷骰时间。
如果觉得骰出的宝库藏品不够多时，你也可以重复进行掷骰。传奇生物会比普通生物积聚更多的财宝，因此你可以对为些生物至少进行两次掷骰并将结果相加。
你可以随意准备或多或少的宝藏。一场典型的战役中，队伍可以收获七次 0~4 战等表格的宝库，以及十八次 5~10 战等，二十次 11~16 战等，八次 17+战等的宝库。
"""

dice_table_individual_treasure_0_4 = """
# d-100 个体宝藏：挑战等级 0~4
d100 CP SP EP GP PP
01~30 5d6（17） — — — —
31~60 — 4d6（14） — —
61~70 — — 3d6（10） — —
71~95 — — — 3d6（10） —
96~00 — — — — 1d6（3）
"""

dice_table_individual_treasure_5_10 = """
# d-100 个体宝藏：挑战等级 5~10
d100 CP SP EP GP PP
01~30 4d6x100（1400） — 1d6x10（35） — —
31~60 — 6d6x10（210） 2d6x10（70） — —
61~70 — — 3d6x10（105） 2d6x10（70） —
71~95 — — — 4d6x10（140） —
96~00 — — — 2d6x10（70） 3d6（10）
"""

dice_table_individual_treasure_11_16 = """
# d-100 个体宝藏：挑战等级 11~16
d100 CP SP EP GP PP
01~20 – 4d6x100（1400） – 1d6x100（350） –
21~35 – – 1d6x100（350） 1d6x100（350） –
36~75 – – – 2d6x100（700） 1d6x10（35）
76~00 – – – 2d6x100（700） 2d6x10（70）
"""

dice_table_individual_treasure_17 = """
# d-100 个体宝藏：挑战等级 17+
d100 CP SP EP GP PP
01~15 – – 2d6x1000（7000） 8d6x100（2800） –
16~55 – – – 1d6x1000（3500） 1d6x100（350）
56~00 – – – 1d6x1000（3500） 2d6x100（700）
"""

dice_table_treasure_hoard_0_4 = """
# d-100 库藏宝藏：挑战等级 0~4
CP SP EP GP PP
钱币 6d6x100（2100） 3d6x100（1050） – 2d6x10（70） –
d100 宝石或艺术品 魔法物品
01~06 – –
07~16 2d6（7）枚价值 10 gp 的宝石 –
17~26 2d4（5）件价值 25 gp 的艺术品 –
27~36 2d6（7）枚价值 50gp 的宝石 –
37~44 2d6（7）枚价值 10 gp 的宝石 骰 1d6 对应魔法物品表 A
45~52 2d4（5）件价值 25 gp 的艺术品 骰 1d6 对应魔法物品表 A
53~60 2d6（7）枚价值 50 gp 的宝石 骰 1d6 对应魔法物品表 A
61~65 2d6（7）枚价值 10 gp 的宝石 骰 1d4 对应魔法物品表 B
66~70 2d4（5）件价值 25 gp 的艺术品 骰 1d4 对应魔法物品表 B
71~75 2d6（7）枚价值 50 gp 的宝石 骰 1d4 对应魔法物品表 B
76~78 2d6（7）枚价值 10 gp 的宝石 骰 1d4 对应魔法物品表 C
79~80 2d4（5）件价值 25 gp 的艺术品 骰 1d4 对应魔法物品表 C
81~85 2d6（7）枚价值 50 gp 的宝石 骰 1d4 对应魔法物品表 C
86~92 2d4（5）件价值 25 gp 的艺术品 骰 1d4 对应魔法物品表 F
93~97 2d6（7）枚价值 50 gp 的宝石 骰 1d4 对应魔法物品表 F
98~99 2d4（5）件价值 25 gp 的艺术品 骰一次魔法物品表 G
00 2d6（7）枚价值 50 gp 的宝石 骰一次魔法物品表 G
"""

dice_table_treasure_hoard_5_10 = """
# d-100 库藏宝藏：挑战等级 5~10
CP SP EP GP PP
钱币 2d6x100（700） 2d6x100（7000） – 6d6x100（2100） 3d6x10（105）
d100 宝石或艺术品 魔法物品
01~04 – –
05~10 2d4（5）价值 25 gp 的艺术品 –
11~16 3d6（10）枚价值 50 gp 的宝石 –
17~22 3d6（10）枚价值 100 gp 的宝石 –
23~28 2d4（5）件价值 250 gp 的艺术品 –
29~32 2d4（5）件价值 25 gp 的艺术品 骰 1d6 对应魔法物品表 A
33~36 3d6（10）枚价值 50 gp 的宝石 骰 1d6 对应魔法物品表 A
37~40 3d6（10）枚价值 100 gp 的宝石 骰 1d6 对应魔法物品表 A
41~44 3d6（10）枚价值 100 gp 的宝石 骰 1d6 对应魔法物品表 A
45~49 2d4（5）件价值 25 gp 的艺术品 骰 1d4 对应魔法物品表 B
50~54 3d6（10）枚价值 50 gp 的宝石 骰 1d4 对应魔法物品表 B
55~59 3d6（10）枚价值 100 gp 的宝石 骰 1d4 对应魔法物品表 B
60~63 2d4（5）件价值 250 gp 的艺术品 骰 1d4 对应魔法物品表 B
64~66 2d4（5）件价值 25 gp 的艺术品 骰 1d4 对应魔法物品表 C
67~69 3d6（10）枚价值 50 gp 的宝石 骰 1d4 对应魔法物品表 C
70~72 3d6（10）枚价值 100 gp 的宝石 骰 1d4 对应魔法物品表 C
73~74 2d4（5）件价值 250 gp 的艺术品 骰 1d4 对应魔法物品表 C
75~76 2d4（5）件价值 25 gp 的艺术品 骰一次魔法物品表 D
77~78 3d6（10）枚价值 50 gp 的宝石 骰一次魔法物品表 D
79 3d6（10）枚价值 100 gp 的宝石 骰一次魔法物品表 D
80 2d4（5）件价值 250 gp 的艺术品 骰一次魔法物品表 D
81~84 2d4（5）件价值 25 gp 的艺术品 骰 1d4 对应魔法物品表 F
85~88 3d6（10）枚价值 50 gp 的宝石 骰 1d4 对应魔法物品表 F
89~91 3d6（10）枚价值 100 gp 的宝石 骰 1d4 对应魔法物品表 F
92~94 2d4（5）件价值 250 gp 的艺术品 骰 1d4 对应魔法物品表 F
95~96 2d4（5）件价值 25 gp 的艺术品 骰 1d4 对应魔法物品表 G
97~98 3d6（10）枚价值 50 gp 的宝石 骰 1d4 对应魔法物品表 G
99 3d6（10）枚价值 100 gp 的宝石 骰一次魔法物品表 H
00 2d4（5）件价值 250 gp 的艺术品 骰一次魔法物品表 H
"""

dice_table_treasure_hoard_11_16 = """
# d-100 库藏宝藏：挑战等级 11~16
CP SP EP GP PP
钱币 – – – 4d6x1000（14000） 5d6x100（1750）
d100 宝石或艺术品 魔法物品
01~03 – –
04~06 2d4（5）件价值 250 gp 的艺术品 –
07~09 2d4（5）件价值 750 gp 的艺术品 –
10~12 3d6（10）枚价值 500 gp 的宝石 –
13~15 3d6（10）枚价值 1000 gp 的宝石 –
16~19 2d4（5）件价值 250 gp 的艺术品 骰 1d4 对应魔法物品表 A 或骰 1d6 对应魔法物品表 B
20~23 2d4（5）件价值 750 gp 的艺术品 骰 1d4 对应魔法物品表 A 或骰 1d6 对应魔法物品表 B
24~26 3d6（10）枚价值 500 gp 的宝石 骰 1d4 对应魔法物品表 A 或骰 1d6 对应魔法物品表 B
27~29 3d6（10）枚价值 1000 gp 的宝石 骰 1d4 对应魔法物品表 A 或骰 1d6 对应魔法物品表 B
30~35 2d4（5）件价值 250 gp 的艺术品 骰 1d6 对应魔法物品表 C
36~40 2d4（5）件价值 750 gp 的艺术品 骰 1d6 对应魔法物品表 C
41~45 3d6（10）枚价值 500 gp 的宝石 骰 1d6 对应魔法物品表 C
46~50 3d6（10）枚价值 1000 gp 的宝石 骰 1d6 对应魔法物品表 C
51~54 2d4（5）件价值 250 gp 的艺术品 骰 1d4 对应魔法物品表 D
55~58 2d4（5）件价值 750 gp 的艺术品 骰 1d4 对应魔法物品表 D
59~62 3d6（10）枚价值 500 gp 的宝石 骰 1d4 对应魔法物品表 D
63~66 3d6（10）枚价值 1000 gp 的宝石 骰 1d4 对应魔法物品表 D
67~68 2d4（5）件价值 250 gp 的艺术品 骰一次魔法物品表 E
69~70 2d4（5）件价值 750 gp 的艺术品 骰一次魔法物品表 E
71~72 3d6（10）枚价值 500 gp 的宝石 骰一次魔法物品表 E
73~74 3d6（10）枚价值 1000 gp 的宝石 骰一次魔法物品表 E
75~76 2d4（5）件价值 250 gp 的艺术品 骰一次魔法物品表 F 或骰 1d4 对应魔法物品表 G
77~78 2d4（5）件价值 750 gp 的艺术品 骰一次魔法物品表 F 或骰 1d4 对应魔法物品表 G
79~80 3d6（10）枚价值 500 gp 的宝石 骰一次魔法物品表 F 或骰 1d4 对应魔法物品表 G
81~82 3d6（10）枚价值 1000 gp 的宝石 骰一次魔法物品表 F 或骰 1d4 对应魔法物品表 G
83~85 2d4（5）件价值 250 gp 的艺术品 骰 1d4 对应魔法物品表 H
86~88 2d4（5）件价值 750 gp 的艺术品 骰 1d4 对应魔法物品表 H
89~90 3d6（10）枚价值 500 gp 的宝石 骰 1d4 对应魔法物品表 H
91~92 3d6（10）枚价值 1000 gp 的宝石 骰 1d4 对应魔法物品表 H
93~94 2d4（5）件价值 250 gp 的艺术品 骰一次魔法物品表 I
95~96 2d4（5）件价值 750 gp 的艺术品 骰一次魔法物品表 I
97~98 3d6（10）枚价值 500 gp 的宝石 骰一次魔法物品表 I
99~00 3d6（10）枚价值 1000 gp 的宝石 骰一次魔法物品表 I
"""

dice_table_treasure_hoard_17 = """
# d-100 库藏宝藏：挑战等级 17+
CP SP EP GP PP
钱币 – – – 12d6x1000（42000） 8d6x1000（28000）
d100 宝石或艺术品 魔法物品
01~02 – –
03~05 3d6（10）枚价值 1000 gp 的宝石 骰 1d8 对应魔法物品表 C
06~08 1d10（5）件价值 2500 gp 的艺术品 骰 1d8 对应魔法物品表 C
09~11 1d4（2）件价值 7500 gp 的艺术品 骰 1d8 对应魔法物品表 C
12~14 1d8（4）枚价值 5000 gp 的宝石 骰 1d8 对应魔法物品表 C
15~22 3d6（10）枚价值 1000 gp 的宝石 骰 1d6 对应魔法物品表 D
23~30 1d10（5）件价值 2500 gp 的艺术品 骰 1d6 对应魔法物品表 D
31~38 1d4（2）件价值 7500 gp 的艺术品 骰 1d6 对应魔法物品表 D
39~46 1d8（4）枚价值 5000 gp 的宝石 骰 1d6 对应魔法物品表 D
47~52 3d6（10）枚价值 1000 gp 的宝石 骰 1d6 对应魔法物品表 E
53~58 1d10（5）件价值 2500 gp 的艺术品 骰 1d6 对应魔法物品表 E
59~63 1d4（2）件价值 7500 gp 的艺术品 骰 1d6 对应魔法物品表 E
64~68 1d8（4）枚价值 5000 gp 的宝石 骰 1d6 对应魔法物品表 E
69 3d6（10）枚价值 1000 gp 的宝石 骰 1d4 对应魔法物品表 G
70 1d10（5）件价值 2500 gp 的艺术品 骰 1d4 对应魔法物品表 G
71 1d4（2）件价值 7500 gp 的艺术品 骰 1d4 对应魔法物品表 G
72 1d8（4）枚价值 5000 gp 的宝石 骰 1d4 对应魔法物品表 G
73~74 3d6（10）枚价值 1000 gp 的宝石 骰 1d4 对应魔法物品表 H
75~76 1d10（5）件价值 2500 gp 的艺术品 骰 1d4 对应魔法物品表 H
77~78 1d4（2）件价值 7500 gp 的艺术品 骰 1d4 对应魔法物品表 H
79~80 1d8（4）枚价值 5000 gp 的宝石 骰 1d4 对应魔法物品表 H
81~85 3d6（10）枚价值 1000 gp 的宝石 骰 1d4 对应魔法物品表 I
86~90 1d10（5）件价值 2500 gp 的艺术品 骰 1d4 对应魔法物品表 I
91~95 1d4（2）件价值 7500 gp 的艺术品 骰 1d4 对应魔法物品表 I
96~00 1d8（4）枚价值 5000 gp 的宝石 骰 1d4 对应魔法物品表 I
"""

article_gemstones = """
# 宝石 Gemstones
如果一个宝库的藏品包含宝石，则你可以使用下列表格并按其价值来随机选定被找到的是宝石种类。你可以设定其内只有一种宝石然后只骰一次，或者多次掷骰来创造一个包含多种宝石的宝石堆。
"""

dice_table_gemstones_10gp = """
# d-12 价值 10gp 的宝石
d12 宝石说明
1 蓝铜矿 azurite（深蓝色斑驳纹理不透明宝石）
2 条纹玛瑙 banded agate（棕色、蓝色、白色或红色条纹的透明宝石）
3 蓝水晶 blue quartz（淡蓝色透明宝石）
4 眼纹玛瑙 eye agate（灰色、白色、棕色、蓝色或绿色的半透明圆形宝石）
5 赭石 hematite（灰黑色不透明宝石）
6 天青石 lapis lazuli（带黄斑的深浅蓝混色不透明宝石）
7 孔雀石 malachite（带条纹的深浅绿混色不透明宝石）
8 藓纹玛瑙 moss agate（带灰色或绿色藓状斑点的粉色或黄白色透明宝石）
9 黑曜石 obsidian（黑色不透明宝石）
10 红纹石 rhodochrosite（浅粉色不透明宝石）
11 虎眼石 tiger eye（棕色中部夹金的透明宝石）
12 绿松石 turquoise（浅青绿色不透明宝石）
"""

dice_table_gemstones_50gp = """
# d-12 价值 50gp 的宝石
d12 宝石说明
1 血石 bloodstone（带红斑的深灰色不透明宝石）
2 红玉髓 carnelian（橙色到棕红色的不透明宝石）
3 蓝玉髓 chalcedony（乳白色不透明宝石）
4 绿玉髓 chrysoprase（绿色不透明宝石）
5 黄水晶 citrine（浅黄褐色透明宝石）
6 碧玉 jasper（蓝色、黑色或褐色的不透明宝石）
7 月长石 monstone（带淡蓝光芒的白色透明宝石）
8 缟玛瑙 onyx（黑白相间或纯黑、纯白色的不透明宝石）
9 石英 quartz（白色、烟灰色或黄色的透明宝石）
10 缠丝玛瑙 sardonyx（带红色和白色带状条纹的不透明宝石）
11 星光粉晶 star rose quartz（中央闪着白星的玫瑰色透明宝石）
12 锆石 zircon（淡青绿色的透明宝石）
"""

dice_table_gemstones_100gp = """
# d-10 价值 100gp 的宝石
d10 宝石说明
1 琥珀 amber（水金色到油金色的透明宝石）
2 紫晶 amethyst（深紫色的透明宝石）
3 金绿玉 chrysoberyl（黄绿色到淡绿色的透明宝石）
4 珊瑚 coral（深红色的不透明宝石）
5 石榴石 garnet（红色、棕绿色或紫色的透明宝石）
6 翡翠 jade（浅绿色、深绿色或白色的透明宝石）
7 黑玉 jet（深黑色的不透明宝石）
8 珍珠 pearl（带光泽的白色、黄色或粉红色不透明宝石）
9 尖晶石 spinel（红色、红褐色或深绿色的透明宝石）
10 电气石 tourmaline（淡绿色、蓝色、棕色或红色的透明宝石）
"""

dice_table_gemstones_500gp = """
# d-6  价值 500gp 的宝石
d6 宝石说明
1 紫翠玉 alexandrite（深绿色的透明宝石）
2 蓝晶 aquamarine（淡青绿色的透明宝石）
3 黑珍珠 black pearl（纯黑色的不透明宝石）
4 蓝尖晶石 blue spinel（深蓝色的透明宝石）
5 橄榄石 peridot（油橄榄绿色的透明宝石）
6 黄玉 topaz（金黄色的透明宝石）
"""

dice_table_gemstones_1000gp = """
# d-8 价值 1000gp 的宝石
d8 宝石说明
1 黑蛋白石 black opal（带黑影和金斑的深绿色透明宝石）
2 蓝色蓝宝石 blue sapphire（蓝白色到中蓝色的透明宝石）
3 绿宝石 emerald（深翠绿色的透明宝石）
4 火蛋白石 fire opal（火红色的透明宝石）
5 蛋白石 opal（带绿点和金点的淡蓝色透明宝石）
6 星彩红宝石 star ruby（中央带白色星形的透明红宝石）
7 星彩蓝宝石 star sapphire（中央带白色星形的透明蓝宝石）
8 黄色蓝宝石 yellow sapphire（焰黄色或黄绿色的透明宝石）
"""

dice_table_gemstones_5000gp = """
# d-4 价值 5000gp 的宝石
d4 宝石说明
1 ⿊蓝宝⽯ black sapphire（闪耀⾼光带光泽的⿊⾊半透明宝⽯）
2 钻⽯ diamond（蓝⽩⾊、鲜⻩⾊、粉红⾊、棕⾊或蓝⾊的透明宝⽯）
3 红锆⽯ jacinth（焰橘⾊的透明宝⽯）
4 红宝⽯ ruby（红⾊到深红⾊的通透宝⽯）
"""

article_art_objects = """
# 艺术品 Art Objects
如果一个宝库的藏品包含艺术品，则你可以使用下列表格并按其价值来随机选定被找到的艺术品。你可以多次掷骰来确定宝库中的艺术品藏品。而同个宝库里也会存在多件相同的艺术品。
"""

dice_table_art_objects_25gp = """
# d-10 价值 25gp 的艺术品
d10 艺术品
1 银水壶 ewer
2 骨制雕像 statuette
3 金制小手镯 bracelet
4 金丝织制的法衣 vestments
5 由银丝缝制的黑天鹅绒面具 mask
6 点缀着银丝的铜制酒杯 chalice
7 成对的骨制骰子 dice
8 镶在彩绘木框中的小镜子 mirror
9 绣花丝绸手帕 handkerchief
10 内里画着彩绘肖像的金质链坠盒 locket
"""

dice_table_art_objects_250gp = """
# d-10 价值 250gp 的艺术品
d10 艺术品
1 镶有血石 bloodstones 的金戒指 ring
2 象牙制雕像 statuette
3 金质大手镯 bracelet
4 带宝石坠饰的银项链 necklace
5 青铜王冠 crown
6 带金色刺绣的丝绸长袍 robe
7 造工精良的大壁毯 tapestry
8 镶有翡翠 jade 的黄铜马克杯 mug
9 装着绿松石 turquoise 动物塑像的盒子 box
10 带银金 electrum 装饰的黄金鸟笼 bird cage
"""

dice_table_art_objects_750gp = """
# d-10 价值 750gp 的艺术品
d10 艺术品
1 镶有月长石 moonstones 的银酒杯 chalice
2 剑柄上镶嵌着黑玉 jet 的钢质镀银长剑 longsword
3 由异国木材精雕而成，以锆石 zircon 和象牙装饰的竖琴 harp
4 金质小型神像 idol
5 镶有红色石榴石 garnets 作双眼的金龙行梳子 comb
6 压印着金箔并镶有紫晶 amethysts 的软木瓶塞 cork
7 柄端镶着黑珍珠 black pearl 的银金质 electrum 仪式匕首 dagger
8 由白银和黄金制成的胸针 brooch
9 带黄金配件和嵌体的黑曜石 obsidian 雕像 statuette
10 涂成金色的战争面具 mask
"""

dice_table_art_objects_2500gp = """
# d-10 价值 2500gp 的艺术品
d10 艺术品
1 镶有火蛋白石 fire opal 的纯金链条 chain
2 古老的油画杰作 masterpiece painting
3 镶有众多月长石 moonstones 且由绣花丝绸和天鹅绒织造而成的披风 mantle
4 镶一枚蓝宝石 sapphire 的铂金 platinum 手镯 bracelet
5 镶着碎宝石的绣花手套 glove
6 宝石脚镯 anklet
7 黄金音乐盒 music box
8 镶有四颗蓝晶 aquamarines 的黄金头饰 circlet
9 用蓝色蓝宝石 blue Sapphire 和月长石 moonstone 来模仿眼睛的眼罩 eye patch
10 串有小粒粉红珍珠的项链 necklace
"""

dice_table_art_objects_7500gp = """
# d-8 价值 7500gp 的艺术品
d8 艺术品
1 镶有宝石的黄金王冠 crown
2 镶有宝石的铂金 platinum 戒指 ring
3 镶有红宝石 rubies 的小型黄金雕像 statuette
4 镶有绿宝石 emeralds 的金杯 cup
5 饰有铂金 platinum 丝的黄金首饰盒 jewely box
6 涂成金色的儿童石棺 sarcophagus
7 翡翠 jade 游戏盘和纯金棋子 playing pieces
8 镶有宝石的金丝象牙角杯 drinking horn
"""

article_magic_items = """
# 魔法物品 Magic Items
魔法物品通常从被打败的怪物身上，以及发掘出的失落地窖里搜刮而来。这些物品能够为角色们发挥一些难以替代的作用，又或者以奇异的方式来辅助角色本身的能力。
"""

article_rarity = """
# 稀有度 Rarity
每件魔法物品都有一个稀有度：普通、非普通、珍稀，极珍稀或传说。常见的魔法物品（比如治疗药水 potion of healing）供给量最充足。而一些传说物品（比如夸力许装置 apparatusof Kwalish）往往都是独一无二的物品。游戏中设定了那些最强大的物品在数个世纪前秘密制成，随后却因战争、灾难和意外而逐渐遗失下落。因而就算非普通级的物品也难以轻易制成，而许多魔法物品则作为古董被完好的保存了下来。
稀有度可以用来粗略评估不同魔法物品之间的力量差异。
如表格“魔法物品稀有度”中所示，每个稀有度对应着不同的角色等级。比如，一个角色在达到 5 级前后的阶段通常不会找到一件珍稀的魔法物品。换言之，这些物品不应该成为战役故事的阻碍。不过你也可以将让一枚隐身戒指 ring ofinvisibility 落到一个 1 级角色的手中。而这个事件也会毫无疑问的引出一堆故事。
如果你允许在战役中交易魔法物品，稀有度也有可以帮你为其设定价格。作为 DM，你可以按稀有度标准来设定某些魔法物品的价值。表格“魔法物品稀有度”中也提供了相应的的建议价值。药水或卷轴这类消耗品的价值通常是同样稀有度永久性魔法物品的一半。
"""

table_magic_item_rarity = """
# 魔法物品稀有度 Magic Item Rarity
稀有度 角色等级 价值
普通 common 1 级或以上 50~100 gp
非普通 uncommon 1 级或以上 101~500 gp
珍稀 rare 5 级或以上 501~5000 gp
极珍稀 very rare 11 级或以上 5001~50000 gp
传说 legendary 17 级或以上 50001+ gp
"""

article_buying_and_selling = """
# 购买与出售 Buying and Selling
大多数魔法物品极珍稀而无法买到，但你仍可以在你战役中自行设定其买卖状况。普通的物品（比如一瓶治疗药水potion of healing）可以从炼金师、草药师或者施法者手中购买，但很少会以商店购物的简单形式实现，此时卖方或许会要求为其提供一项服务而不是以钱币来进行交易。
你可以指定一座开设了魔法学院或重点神庙的大城市来允许买卖魔法物品。如果你设定的世界中大量的冒险者从事挖掘这些古老魔法物品的工作，那这些物品的购买和出售可能会更为常见。即便如此，这种交易可能更类似于现实世界中的艺术品市场，只有受邀请的人能够参与拍卖且很容易会引来盗贼。
D&D 世界中出售魔法物品的主要困难是寻找买家。很多人都想得到一把魔法剑，但却很少有人能买得起。而那些买得起这些物品的人通常都会把钱花到更实在的地方。具体可见第 6 章“冒险之余”中各种处理魔法物品销售的方法。
在你的战役世界中，魔法物品可以普遍存在，而冒险者们可以在通过某些方法找到买卖的渠道。出售魔法物品的集市或拍卖行可能出现在各种奇幻地点中，比如黄铜之城 City ofBrass，位面大都会的印记城 Sigil，甚至其他更普通一点的城市。销售魔法物品可能被严令禁止，同时也滋生了一众高度繁荣的黑市。而艾伯伦 Eberron 世界的机关术士们或许也会为军队或冒险者们制造魔法物品。你也可以如第 6 章讨论所述允许角色们自己制作魔法物品。
"""

article_identifying_a_magic_item = """
# 鉴定魔法物品 Identifying a Magic Item
一些魔法物品与某些非魔法物品非常相似而难以鉴别，而另一些魔法物品则毫不掩饰的散发着自己的魔法性质。无论魔法物品的外观如何，处理这些物品的角色都会感觉到其本身的非凡之处。不过你还是必须进行某些处理才能获知一件魔法物品的属性。
法术鉴定术 identify 是揭晓物品属性最快捷的方法。另一种方法是让一名角色在一次短休过程中对该魔法物品维持专注，并同时保持与该物品进行物理接触。休息完成后，该角色将获知该物品的属性并知晓其使用方式。药水则较为例外，稍微尝一下味道就可以知晓这是什么药水。
有时候，魔法物品也会带着一些与其属性相关的线索。激活戒指的命令语可能用细小的字符铭刻在戒指的内侧，羽毛造型的设计可能表明这是一枚羽落戒指 ring of feather falling。
穿戴或试验物品也可以获得与其属性相关的提示。例如，如果一名角色戴上了跳跃戒指 ring of jumping，你可以说“你踏步时感觉有种奇异的弹跳力。”也许该角色随后会试着上下跳跃来感觉会发生何时，而此时你可以告诉该角色他跳出非比寻常的高度。
# 变体：更难鉴定 More Difficult Identification
如果你喜欢魔法物品更有神秘感，则可以考虑排除掉短休鉴别魔法物品属性的设定，并要求必须通过法术鉴定术identify 或测试，或者两者兼备才可解释魔法物品的属性。
"""

article_attunement = """
# 同调 Attunement
一些魔法物品需要一个生物与自己形成某种联结后才能使用其魔法属性。这种称为同调 attunement 的联结通常还有某些先决条件。如果同调某件魔法物品的先决条件是某个职业，则尝试与该物品同调的生物必须是该职业才能与之进行同调。如果该职业限制为施法职业，而拥有法术位且使用相应职业法术列表的怪物也具备与之同调的资格。如果先决条件为施法者，而生物某特质或特性令其可施展至少一项法术（不能利用魔法物品或相似状况），则该生物也具备同调资格。
未与物品完成同调的生物只能使用该物品的非魔法增益，除非其描述另有说明。比如，一面需要同调的魔法盾牌在未与之同调的生物手中可以用作为一面非魔法的盾牌，而其魔法属性均无法生效。
一个生物与一件魔法物品同调时，需要该生物在短休期间对该物品进行专注并保持与之物理接触（你不能以同一次短休来获知该魔法物品的属性）。这种专注的形式可以是武器训练（用于武器），冥想（用于奇物）或其他适当的活动形式。
如果短休被打断，所进行的同调也将失败。否则短休完成时，该生物将直觉性的获知如何激活该魔法物品的所有属性，包括其中所需的任何命令语。
同一件魔法物品一次只能与一个生物同调，而一个生物不能同时与三件以上的魔法物品同调。除非该生物先终止某个已同调物品的联结，否则与第四件魔法物品的同调必定失败。此外，一个生物不能与多于一件相同的魔法物品进行同调。
例如，一个生物不能与数枚防护戒指 ring of protection 同调。
如果一个生物不再满足同调的先决条件，或者该物品离开该生物 100 尺并维持至少 24 小时，又或者该生物死亡或另一生物与该物品完成同调，都将终止先前的同调联结。生物也可以利用一次短休期间对物品进行专注来主动终止同调联结，除非该物品受到诅咒。
"""

article_cursed_items = """
# 被诅咒物品 Cursed Items
某些被诅咒的魔法物品会困扰其使用者，有时甚至使用者不再使用该物品也会在很长时间里受其影响。魔法物品的描述中会详细说明该物品是否被诅咒。虽然一些逸闻学识中会提及这些诅咒，但大多数鉴定物品的方法（包括法术鉴定术identify）都无法揭示这些诅咒。而这些诅咒的效应显露时，往往都会让其使用者感到十分意外。
与一件被诅咒物品同调后其同调联结在诅咒被破除前无法被终止，破除诅咒的方式之一便是对其施展法术移除诅咒remove curse。
"""

article_magic_item_categories = """
# 魔法物品类别 Magic Item Categories
每件魔法物品都属于一个类别：护甲、魔药、戒指、权杖、卷轴、法杖、魔杖、武器或奇物。

# 护甲 Armor
除非一件护甲的描述另有说明，否则护甲必须着装才能让其魔法发挥作用。
一些魔法护甲会指定其护甲类型，例如链甲或板甲。如果一件魔法护甲没有指定其护甲类型，则你可以随意或随机为其指定一个类型。

# 魔药 Potions
不同种类的魔法液体被归类为几个种类的魔药：由魔法草药调制的药剂，来自魔泉或圣泉的水，以及用于生物或物件的油。大多数魔药都盛装的一盎司液体。
魔药是可消耗的魔法物品。喝药水或给其他角色服用药剂需要花费一个动作，而应用油类可能需要更长时间（具体见相应描述）。魔药使用过后即被耗尽且立即生效。

# 戒指 Rings
魔法戒指为那些有幸找到它们的人提供神奇的魔力。除非戒指的描述另有说明，否则戒指必须着装在手指或类似的肢体结构上，才能发挥其魔法作用。

# 权杖 Rods
一根魔法权杖可以是一支节杖或一支沉重的圆棒，其实体通常由金属、木头或骨头制成。其外形大约 2 到 3 尺长，1寸厚，2 到 5 磅重。

# 卷轴 Scrolls
大多数卷轴都是以文书形式保存的法术，而少数的卷轴所蕴含的独特咒语还可以生成某些强效的结界。无论其内容是什么，卷轴的实体都是一卷纸，有时会附在木棒上，通常都保存在由象牙、翡翠、皮革、金属或木材等材料制作的管筒中。
卷轴是一种消耗性的魔法物品。无论卷轴中所包含魔法的本质为何是，释放该魔法需要使用动使用一个动作来读取卷轴。魔法被调用后的卷轴无法再使用。而其内的文字也会随之消失，或整个化作尘土。
任何理解一种书写语言的生物都可以阅读卷轴上的奥法文书，并尝试将其激活。

# 法杖 Staffs
一根法杖大约 5 到 6 尺长。法杖的外形千差万别：有的直径均匀而光滑，有的则扭曲变形，有的由木头制成，有的则由抛光的金属或水晶组装而成。根据材质的不同，一根法杖的重量介于 2 到 7 磅之间。
除非法杖的描述另有说明，否则法杖都可以被用作一根长棍 quarterstaff。

# 魔杖 Wands
一根魔杖大约长 15 寸，由金属、骨头或木头制成。其末端由金属、水晶、石头或其他一些材料制成。

# 武器 Weapons
不管是因某些堕落目标制成，还是为最崇高的骑士精神而铸造，所有的魔法武器都是无数冒险者们趋之若鹜的宝贝。
一些魔法武器在其描述中明确指定了其所属类型，比如长剑 longsword 或长弓 longbow。如果一件魔法武器没有指定武器类型，则你可以随意或随机指定其类型。
如果一件魔法武器具有弹药属性，则从该武器发射的弹药视为具有魔法，并因此得以穿透目标的非魔法攻击的抗性并造成伤害。

# 奇物 Wondrous Items
奇物包括一些着装物品如靴子 boots、腰带 belts、披肩capes、手套 gloves，以及各种珠宝 jewelry 和装饰品如护身符 amulets、胸针 brooches 和饰环 circlets 等。袋子 bags、地毯 carpets、水晶球 crystal balls、塑像 figurines、号角 horns、乐器 musical instruments 和其他物件也属于这一类别。

# 变体：混合药水 Mixing Potions
角色可能会在正处于某个药水的效应期间喝下另一种药水，或者会将几种药水倒进同一个容器中。而那些用来制造药水的奇异成分可能会导致不可预知的相互作用。
当角色把两种药水混合在一起时，你可以按表格“可混合药水”所示进行掷骰。如果两个以上的组合混一起，则为随后每份加入的药水再进行一次掷骰并将结果结合。除非其效应会立即显现，否则你可以在其需要显现效应时才揭晓这些结果。
"""

dice_table_potion_miscibility = """
# d-100 可混合药水 Potion Miscibility
d100 结果
01 混合物发生了一场魔法爆炸，混合者受到 6d10 的力场伤害，其周边 5 尺内的每个生物受到 1d10 的力伤害。
02~08 混合物变成一种被服用的毒药，其具体种类由 DM决定。
09~15 两种药水都失去其效应。
16~25 其中一种药剂失去其效应。
26~35 这两种药剂都有效，但其效应数值和持续时间都减半。如果效应不能以这种方式减半，则该药水失去其效应。
36~90 两种药水都正常生效。
91~99 一种药剂的效应数值和持续时间加倍。如果两种药水都不能以这种方式翻倍，则两者都正常生效。
00 只有一种药水有效，但其效应变为永久性。选择其中最简单，或者看起来最有趣的效应成为永久效应。例如，一个治疗药水 potion of healing 可以使饮用者的生命值上限提升 4，或者以太化之油 oil of etherealness 可以令使用者永远性的困在以太位面里。你可以自行设定哪些法术可以终止该效应（比如法术解除魔法 dispel magic 或移除诅咒 removecurse）。
"""

article_wearing_and_wielding_items = """
# 着装与持用物品 Wearing and Wielding Items
一些魔法物品需要着装或持用才能使用其属性。一件需要着装的魔法物品必须按照预定的方式穿戴：靴子必须穿在脚上，手套必须戴在手上，帽子和头盔必须戴在头上，戒指必须戴在手指。魔法护甲必须着装完备，盾牌必须在手臂上固定妥当，斗篷必须系在肩上。武器则必须拿在手中。
在大多数情况里，一件要求着装的魔法物品可以适应标准体格和体型的生物。许多魔法服装都可以轻松的进行调整，或者在着装时因魔法而自动调整妥当。
也有一些罕见的例外。如果故事中给出一个恰当的理由让某物品只适合某个体型或形体的生物，你就可以判定其无法调整。例如，由卓尔制造的护甲可能只适合精灵。矮人们制作的物品也可能只适用于体型和外形与矮人相仿的角色。
一个非类人生物试着穿一件物品时，你可以根据自己的意愿来判断物品是否按预定的方式生效。放在触须上的戒指可能会起作用，但长着蛇尾而不是腿的蛇人 yuan-ti 就肯定不能穿靴子。
"""

article_multiple_items_of_the_same_kind = """
# 复数同类物品 Multiple Items of the Same Kind
用常识来判断是否可以着装多于一件的同类魔法物品。
一名角色通常无法穿多于一双鞋靴 footwear、护手 gauntlet、手套 gloves、护腕 bracers，也无法穿多于一套的护甲 armor、头饰 circlet 和斗篷 cloak。你也可以设置一些例外。比如，一名角色可以在头盔下着装一个头饰，或者能够将两层斗篷层穿在身上。

# 成对物品 Paired Items
成对的物品（比如靴子boots、护腕bracers、护手gauntlets 和手套gloves）只有当它们的两件都被着装时才能让相应的增益生效。例如，一名单脚穿着跳跑之靴 boot of striding and springing，另一脚却踏着一只精灵之靴 bootofelvenkind 的角色无法获得这些靴子提供的任何增益。
"""

article_activating_an_items = """
# 激活物品 Activating an Item
一些魔法物品需要其使用者做一些特别的事情才能激活，比如拿着物品说出相应的命令语。每个物品品类或单个物品的描述中都详述了激活该物品的方法。而某些特定的物品会使用下列其一或多项作为其激活规则。
如果某物品需要用一个动作激活，则该动作本身并不作为“使用物品 Use an Item”动作，因此一些特性，如游荡者的“快手 Fast Hands”特性就无法用于激活这些物品。

# 命令语 Command Word
命令语以说话方式发出的一个单词或短句，用以驱使物品开始工作。需要命令语的魔法物品无法在声音被压制的区域里激活，比如法术沉默术 silence 的效应范围里。

# 消耗品 Consumables
一些物品被激活后将被消耗殆尽。药水或灵药以服用的方式，而油类则用在相应的实体上。被阅读使用后的卷轴其上的文字消失不见。使用过后，消耗品类的物品也随之失去其魔法。

# 魔法物品图纸 Magic Item Formulas
一份魔法物品的图纸解释了如何制作某一特定的魔法物品。
如果你允许玩家角色制作魔法物品（如第 6 章“冒险之余”所述），则这种图纸会是一种绝妙的奖励。
你可以奖励一份图纸来代替某个魔法物品。这些图纸通常书写在一本书或一份卷轴中，其稀有度会比它制作的物品高一个等级。例如一张制作普通魔法物品的图纸其稀有度即为非普通。传说物品并不存在相应的图纸。
如果你的战役将制作魔法物品设定为常见的事，那么其中的图纸可以与其所制作物品的稀有度相当。普通与非普通等级的物品甚至可以买到，而每项的价格都相当于其制作魔法物品的两倍。

# 法术 Spells
一些魔法物品可以让其使用者从物品中施展法术。这些法师以法术的最低环阶施展，其不消耗使用者的法术位，也不需要任何构材，除非相应物品的描述中另有说明。这些法术使用它正常的施法时间、施法距离和持续时间，如果法术需要专注则该物品的使用者还必须对物品进行专注。许多物品（比如药水），可以直接跳过施法而直接赋予法术的效应并维持通常的持续时间。而一些特定的物品与该规则不同，会改变法术的施法时间，持续时间以及法术的其他内容。
一些魔法物品（比如某些法杖）可能会在你用其施展法术时，还会要求你使用你自身的施法能力。此时如果你拥有超过一种施法能力，则可以自行选择使用其一。如果你没有施法能力（也许你是一名有着“使用魔法装置 Use Magic Device”特性的游荡者），则此时你用该物品时的施法关键属性调整值为+0，同时你也可以使用相应的熟练加值。

# 变体：阅卷失误 Scroll Mishaps
一个尝试用法术卷轴 spell scroll 施展法术的生物，必须进行一次 DC 10 的智力豁免。如果豁免失败，则按表格“阅卷失误”进行掷骰。

# 充能 Charges
一些魔法物品需要花费充能来激活属性。一件物品保留的充能次数可以通过对其施展鉴定术 identify 来查明，与之同调的生物也可以通过直觉得知。此外，当一件物品恢复充能时，与之同调的生物也会在第一时间得知其拥有的充能总量。
"""

dice_table_scroll_mishap = """
# d-6 阅卷失误 Scroll Mishap
d6 结果
1 魔法能量的激增使施法者受伤，其数值为该法术每环阶1d6 的力场伤害。
2 该法术将影响施法者或他的一个盟友（随机决定）而不是其指定的目标，或者如果施法者是预期的目标，则该法术会影响附近一个随机的目标。
3 该法术将影响施法范围内一个随机地点。
4 法术的效应与正常的效应相反，但既不有害也不有益。例如，一个火球术 fireball 可能会产生一片无害的寒冷区域。
5 施法者受到与法术相关的轻微但怪诞的效应。这样的效应只持续到法术最初的持续时间，或者立即生效的法术持续 1d10 分钟。例如，一个火球术 fireball 可能会让施法者的耳朵冒烟，并持续 10 分钟。
6 该法术会在 1d12 小时后激活。如果施法者是预期的目标，则该法术正常生效。如果施法者不是预期的目标，且该目标已经离开其原位置，则该法术将向预期目标所在的大致方向，延伸至该法术的最远施法距离。
"""

article_magic_item_resilience = """
# 魔法物品自愈 Magic Item Resilience
大多数魔法物品都是非凡工艺的作品。精心的制作结合魔法强化，使这些魔法物品的耐用性绝不逊色于相似的非魔法物品。除药水与卷轴外的大多数魔法物品都对所有类型伤害具有抗性。神器则尤其坚不可摧，而只能通过一些极端手段才能破坏。
"""

article_special_features = """
# 专有特征 Special Features
你可以思考一件魔法物品的幕后故事来为其增加独特性。
物品由谁制成？其构造是否不同寻常？它为何制成，其原使用者又是谁？是否有什么小习性让该魔法物品有别于同类的其他物品？回答这些问题可以帮你将一件普通的魔法物品（比如一把 +l长剑 longsword），变成一件更有风味的发现。
下列表格可以帮你寻找答案。你可以随意以其掷骰。其中某些条目会更针对某些特定的物品。而某些魔法物品则只会由特定种类的生物制作而成，比如精灵斗篷 cloak of elvenkind由精灵制作而非矮人。如果你骰出一些不合理的结果，只需重新掷骰或者直接用骰得的条目作灵感自建一些新的内容。

# 变体：无法充能的魔杖 Wands That Don’t Recharge
一根典型的魔杖拥有可消耗的充能次数。如果你想让魔杖成为一种有限的资源，则你可以设定某些魔杖彻底无法充能。你可以考虑为这种魔杖设置一个保底充能次数，其最高值为 25。这些充能一旦被消耗便永远无法恢复。
"""

dice_table_who_created_it_or_was_intended_to_use_it = """
# d-20 由谁制作或是谁曾打算使用它？ Who Created It or Was Intended to Use It?
d20 制作者或预期使用者
1 异怪 Aberration。该物品由远古时期的异怪制作，很可能是做给其青睐的类人生物奴隶使用。从眼角余光观察该物品时你会看到它好像在动。
2~4 人类 Human。该物品在某个已陨落的人类王国曾经的全盛时期创造出来，或者它与一名传奇人类相关。其上可能书写着某些早已失传于历史长河的语法或字符。
5 天界生物 Celestial。该武器的重量是普通物品的一半，上面刻着有羽翼、太阳和其他象征善良的符号。邪魔生物会觉得这件物品的存在令其生厌。
6 龙类 Dragon。该物品由龙鳞和龙爪制成。也许它从龙的宝库中吸收了一些稀有金属和宝石。当它身处一条龙周围 120 尺范围内时，会变得稍暖一点。
7 卓尔精灵 Drow。该物品的重量是普通物品的一半。它通体泛黑，上面刻着蜘蛛和蛛网的图样以代表罗丝Lolth。暴露在阳光下 1 分钟或更长时间后，其性能可能会变的极差差，或者直接解体。
8~9 矮人 Dwarf。该物品经久耐用，并设计着矮人的符文。它可能与一个希望看到该物品回归自己先祖大厅的氏族联系在一起。
10 气元素 Elemental Air。该物品重量是普通物品的一半，且有一种中空的感觉。如果它是布料制成，则其质感让人感觉轻盈通透。
11 土元素 Elemental Earth。该物品可能由石头制成。其中任何布料或皮革的部件都镶嵌着精美的磨光岩块。
12 火元素 Elemental Fire。该物品摸起来可以感觉到温暖，其中任何金属部件都用黑铁制成。魔符烈焰覆盖在其表面。红色和橘色之间的渐变是其主色调。
13 水元素 Elemental Water。润泽鱼鳞取代该物品的皮革或布料部件，而由海贝制成的金属部件硬度跟真金属一样坚韧。
14~15 精灵 Elf。该物品重量是普通物品的一半。其上装饰着自然的象征：树叶，藤蔓，星星，等等。
16 精类生物 Fey。该物品用最好材料精心制作而成，它在月光下会发出淡淡的光耀，并想周边 5 尺半径范围散发出微光光照。其所有金属部件都有白银和秘银来代替原来铁和钢。
17 邪魔生物 Fiend。该物品用黑铁或角刻上符文制作而成，其所有布质或皮质部件都由邪魔的毛皮制作，它的表面触感暖和，其上装饰着斜睨的面孔或邪秽的符文。天界生物会觉得该物品令其感觉厌恶。
18 巨人 Giant。该物品比普通物品要大，由巨人为其身材细小的盟友们精心制作而成。
19 侏儒 Gnome。该物品看起来很普通，甚至感觉有点破旧。它可以和一些齿轮和机械部件结合起来，不过这些部件对物品本身的功能没什么影响。
20 不死生物 Undead。该物品包含了死亡的意象（比如骨头和头骨），它可能由尸体的残骸制成的。且摸起来可以感觉到冰冷。
"""

dice_table_what_is_a_detail_from_its_history = """
# d-8 过去是否有一些小细节？ What Is a Detail from Its History？
d8 历史
1 奥秘 Arcane。该物品由远古的施法者团体创造，并带着该团体的象征符号。
2 祸根 Bane。该物品由某个特定文明或某种生物的敌人创造。如果该文明或生物仍然存在，则他们可能会认出这个物品，并将其持有者视为敌人。
3 英雄 Heroic。一位伟大的英雄曾持用该物品。任何熟悉该物品曾经历史的人都期待着其新主人的伟大事迹。
4 修饰 Ornament。该物品为纪念一个特殊的场合而制作。它镶嵌着宝石、黄金或铂金，并以金银装饰其表面。
5 预言 Prophecy。该物品显现一则预言：它的持有者注定要在未来的事件中扮演关键角色。那些想要扮演该角色的人可能会试图窃取该物品，或者想阻止该预言被实现的人会想要杀死这个物品的持有者。
6 宗教 Religious。该物品曾被用于宗教仪式，并专门用于某个特定的神祇。其内还有神圣的符文正在生效。该神灵的追随者们可能会试图说服其主人将它捐赠给神庙，或者私自将其窃取，或者向同属于该神祇的牧师或圣武士持用者表示祝贺。
7 罪恶 Sinister。该物品与某个重大恶行相关，比如大屠杀或暗杀。它可能有一个名字，或者与一个曾使用它的反派密切相关。任何熟悉该物品过去的人都可能对其所有者表示怀疑。
8 权力象征 Symbol of Power。该物品曾被用作皇室高阶官职加冕物品的一部分。它的前主人或那个人的后代可能会想要得到该物品，或者有人可能会误以为它的新主人是该物品的合法继承人。
"""

dice_table_what_minor_property_does_it_have = """
# d-20 有哪些小得益？ What Minor Property Does It Have?
d20 小得益
1 灯塔 Beacon。持有者可以用一个附赠动作，使物品在 10尺半径范围内散发出明亮光照以及其外 10 尺微光光照，或以同样的动作熄灭这些光照。
2 指南针 Compass。持用者可以用一个动作得知哪边是北方。
3 尽责 Conscientious。该物品的持有者考虑或进行恶意行为时，该物品会增加良心的痛苦。
4 探索者 Delver。在地底时，该物品的持有者总能知道物品在地表以下的深度，以及最近的楼梯、斜坡或其他向上道路的方位。
5 闪亮 Gleaming。该物品永远不会变脏。
6 警卫 Guardian。该物品会低语对持有人发出警告，如果持有人并未陷入失能，则其项获得 +2 加值。
7 和谐 Harmonious。与该物品完成同调只须 1 分钟。
8 隐秘情报 Hidden Message。一则情报被隐藏在该物品的某个位置。它可能在一年中的某一时刻，月亮的某一月相，或在特定地点时才能看见。
9 钥匙 Key。该物品被用来解锁一个容器、房间、地窖或其他入口。
10 语言 Languages。持有人可以在该物品在身边时理解或讲说一种由 DM 选定的语言。
11 哨兵 Sentinel。选择一个生物类型，并将其设定为该物品制作者的敌人。当同类生物在物品周边 120 尺范围内时，物品将散发出微光。
12 歌唱 Song Craft。每当该物品被打到或被用来打击敌人时，它的持有者就会听到一首古老歌曲的片段。
13 奇异材质 Strange Material。该物品由一种很奇怪的材料制成，但这并不影响其耐用性。
14 温度 Temperate。持有者身处如 -20 华氏度或 120 华氏度的温度下，不会受到任何冷热环境造成的伤害。
15 牢不可破 unbreakable。该物品无法被破坏。必须用一些特殊手段才能将其摧毁。
16 战争领袖 War Leader。持有人可以用一个动作使自己的声音清晰地传递至远 300 尺距离，效应持续至该持有人自己的下一回合结束。
17 水性 Waterborne。该物品漂浮在水上和其他液体上。它的持有者以力量（运动）检定进行游泳时具有优势。
18 恶意 Wicked。当持有人有机会以自私或恶意的方式行事时，该物品会使持有人的冲动变得更加强烈。
19 幻术 Illusion。该物品充满了幻术魔法，可以让其持有人微小的改变该物品的外观。这样的改变不会改变该物品着装、携带或使用的方式，也不会对其别的魔法属性产生影响。例如，其着装者可以让红色的长袍看起来是蓝色，或者让金色的戒指看起来是象牙质。当没有人携带或着装该物品时，它就会恢复其真实的外观。
20 骰两次，每次遇到骰值 20 时重骰。
"""

dice_table_what_quirk_does_it_have = """
# d-12 有哪些小习性？
What Quirk Does It Have?
d12 习性
1 极乐 Blissful。拥有该物品时，持有人将感觉未来充满幸运与乐观。蝴蝶和其他无害的生物可能会在物品出现时在其周围嬉戏。
2 自信 Confident。该物品帮助其持有者感到自信。
3 贪婪 Covetous。该物品的持有者会沉迷于物质财富。
4 脆弱 Frail。该物品被持用、着装或激活时，会发生轻微的破碎、磨损、崩口或炸裂。这种小习性对其属性没有影响，但该物品被用的越多就会显得越破旧。
5 饥饿 Hungry。必须对该物品使用类人生物的鲜血，才能再 24 小时时间里使其魔法属性生效。它只需要一滴血便可被激活。
6 大喊 Loud。使用该物品时，它会发出响亮的声音（好比一声铿锵、一声喊叫或一声共振）。
7 变质 Metamorphic。该物品会周期性随机地细微改变其外观。持有人无法控制这些小改动，这些改变也不影响物品的使用效果。
8 嘟哝 Muttering。该物品牢骚不断，喃喃自语。一个仔细聆听的生物可能从中得知一些有用的东西。
9 痛苦 Painful。使用该物品时，持有者会经历一种无害的疼痛。
10 占有 Possessive。该物品需要同调，且第一次持用或着装该物品后，它便不允许其持有者再与其他无尽进行同调。（已经与持有人完成同调的物品维持其同调状态，直至其同调联结终止。）
11 反感 Repulsive。与该物品接触时，其持有人会感到一种厌恶感，并且会持续感觉到这种不舒服的感觉。
12 懒惰 Slothful。该物品的持有者感觉懒散且昏昏欲睡。与此同时，持有者需要花费 10 小时才能完成一次长休。
"""

article_random_magic_items = """
# 随机魔法物品 Random Magic Items
当你使用一个“库藏宝藏”表来随机选定宝库的内容物，且你的骰值示意你决定其内的魔法物品时，你可以使用这里附带的诸表格并掷骰来选定指定的魔法物品。
"""

dice_table_magic_item_table_a = """
# d-100 魔法物品表 A Magic Item Table A
d100 魔法物品
01~50 治疗药水 potion of healing
51~60 法术卷轴 spell scroll（戏法）
61~70 攀爬药水 potion of climbing
71~90 法术卷轴 spell scroll（1 环）
91~94 法术卷轴 spell scroll（2 环）
95~98 高等治疗药水 potion of greater healing
99 次元袋 bag of holding
00 漂浮之球 driftglobe
"""

dice_table_magic_item_table_b = """
# d-100 魔法物品表 B Magic Item Table B
d100 魔法物品
01~15 高等治疗药水 potion of greater healing
16~22 火焰吐息药水 potion of fire breath
23~29 抗性药水 potion of resistance
30~34 弹药 ammunition, +1
35~39 化兽为友药水 potion of animal friendship
40~44 山丘巨人之力药水 potion of hill giant strength
45~49 成长药水 potion of growth
50~54 水下呼吸药水 potion of water breathing
55~59 法术卷轴 spell scroll（2 环）
60~64 法术卷轴 spell scroll（3 环）
65~67 次元袋 bag of holding
68~70 卡夫统灵药 Keoghtom's ointment
71~73 滑溜之油 oil of slipperiness
74~75 无踪粉 dust of disappearance
76~77 干燥粉 dust of dryness
78~79 喷嚏粉 dust of sneezing and choking
80~81 元素宝石 elemental gem
82~83 迷情媚药 philter of love
84 炼金壶 alchemy jug
85 水下呼吸帽 cap of water breathing
86 蝠鲼斗篷 cloak of the manta ray
87 漂浮之球 driftglobe
88 夜视镜 goggles of night
89 通晓语言头盔 helm of comprehending languages
90 不动权杖 immovable rod
91 显像提灯 lantern of revealing
92 水手护甲 mariner's armor
93 秘银甲 mithral armor
94 毒药 potion of poison
95 善泳戒指 ring of swimming
96 杂货法袍 robe of useful items
97 攀爬绳 rope of climbing
98 铁骑马鞍 saddle of the cavalier
99 探魔魔杖 wand of magic detection
00 探秘魔杖 wand of secrets
"""

dice_table_magic_item_table_c = """
# d-100 魔法物品表 C Magic Item Table C
d100 魔法物品
01~15 强效治疗药水 potion of superior healing
16~22 法术卷轴 spell scroll（4 环）
23~27 弹药 ammunition, +2
28~32 鹰眼术药水 potion of clairvoyance
33~37 缩小药水 potion of diminution
38~42 气化形体药水 potion of gaseous form
43~47 霜巨人之力药水 potion of frost giant strength
48~52 石巨人之力药水 potion of stone giant strength
53~57 英雄气概药水 potion of heroism
58~62 坚不可摧药水 potion of invulnerability
63~67 读心药水 potion of mind reading
68~72 法术卷轴 spell scroll（5 环）
73~75 健康灵药 elixir of health
76~78 以太化之油 oil of etherealness
79~81 火巨人之力药水 potion of fire giant strength
82~84 夸尔羽符 Quaal's feather token
85~87 守护卷轴 scroll of protection
88~89 魔豆之袋 bag of beans
90~91 力场珠 bead of force
92 开门钟琴 chime of opening
93 无尽水瓶 decanter of endless water
94 微视镜片 eyes of minute seeing
95 折叠船 folding boat
96 霍华德的便利袋 Heward's handy haversack
97 加速马蹄铁 horseshoes of speed
98 火球项链 necklace of fireballs
99 保健护符 periapt of health
00 传讯石 sending stones
"""

dice_table_magic_item_table_d = """
# d-100 魔法物品表 D Magic Item Table D
d100 魔法物品
01~20 极效治疗药水 potion of supreme healing
21~30 隐身药水 potion of invisibility
31~40 加速药水 potion of speed
41~50 法术卷轴 spell scroll（6 环）
51~57 法术卷轴 spell scroll（7 环）
58~62 弹药 ammunition, +3
63~67 锐锋之油 oil of sharpness
68~72 飞行药水 potion of flying
73~77 云巨人之力药水 potion of cloud giant strength
78~82 延寿药水 potion of longevity
83~87 活力药水 potion of vitality
88~92 法术卷轴 spell scroll（8 环）
93~95 西风马蹄铁 horseshoes of a Zephyr
96~98 诺泽尔的惊奇颜料 Nolzur's marvelous pigments
99 吞噬袋 bag of devouring
00 次元洞 portable hole
"""

dice_table_magic_item_table_e = """
# d-100 魔法物品表 E Magic Item Table E
d100 魔法物品
01~30 法术卷轴 spell scroll（8 环）
31~55 风暴巨人之力药水 potion of storm giant strength
56~70 极效治疗药水 potion of supreme healing
71~85 法术卷轴 spell scroll（9 环）
86~93 万溶剂 universal solvent
94~98 屠杀箭 arrow of slaying
99~00 至尊胶 sovereign glue
"""

dice_table_magic_item_table_f = """
# d-100 魔法物品表 F Magic Item Table F
d100 魔法物品
01~15 武器 weapon, +1
16~18 盾牌 shield, +1
19~21 警戒之盾 sentinel shield
22~23 反侦护符 amulet of proof against detection and location
24~25 精灵之靴 boots of elvenkind
26~27 跳跑之靴 boots of striding and springing
28~29 射手护腕 bracers of archery
30~31 护盾胸针 brooch of shielding
32~33 飞天扫帚 broom of flying
34~35 精灵斗篷 cloak of elvenkind
36~37 防护斗篷 cloak of protection
38~39 食人魔力量护手 gauntlets of ogre power
40~41 易容帽 hat of disguise
42~43 闪电标枪 javelin of lighting
44~45 法力再生珍珠 pearl of power
46~47 契约掌控者之杖 rod of the pact keeper, +1
48~49 蛛行便鞋 slippers of spider climbing
50~51 蝰蛇法杖 staff of the adder
52~53 巨蟒法杖 staff of the python
54~55 复仇之剑 sword of vengeance
56~57 唤鱼三叉戟 trident of fish command
58~59 魔法飞弹魔杖 wand of magic missiles
60~61 战法师魔杖 wand of the war mage, +1
62~63 蛛网魔杖 wand of web
64~65 警戒武器 weapon of warning
66 精金护甲 adamantine armor (链甲)
67 精金护甲 adamantine armor (链甲衫)
68 精金护甲 adamantine armor (鳞甲)
69 魔术袋 bag of tricks (灰色)
70 魔术袋 bag of tricks (铁锈色)
71 魔术袋 bag of tricks (棕褐色)
73 爆裂头饰 circlet of blasting
74 幻象牌组 deck of illusions
75 无尽烟壶 eversmoking bottle
76 魅惑镜片 eyes of charming
77 鹰眼镜片 eyes of the eagle
78 异能塑像 figurine of wondrous power (白银渡鸦)
79 光彩夺目宝石 gem of brightness
80 辟矢夺箭手套 gloves of missile snaring
81 运动健将手套 gloves of swimming and climbing
82 窃贼手套 gloves of thievery
83 智⼒头带 headband of intellect
84 ⼼灵感应头盔 helm of telepathy
85 吟游诗人乐器 instrument of the bards (安眠鲁特琴 Doss lute)
86 吟游诗人乐器 instrument of the bards (佛克路坎三弦琴 Fochlucan bandore)
87 吟游诗人乐器 instrument of the bards (⻨克-弗瑞⽶得⻄特琴 Mac-Fuimidh cittern)
88 读心勋章 medallion of thoughts
89 适应项链 necklace of adaptation
90 愈合护符 periapt of wound closure
91 颤栗乐笙 pipes of haunting
92 唤鼠乐笙 pipes of the sewers
93 跳跃戒指 ring of jumping
94 心灵护盾戒指 ring of mind shielding
95 温暖戒指 ring of warmth
96 水行戒指 ring of water walking
97 艾罗娜的箭袋 quiver of Ehlonna
98 幸运石 stone of good luck
99 造风之扇 wind fan
00 飞翼之靴 winged boots
"""

dice_table_magic_item_table_g = """
# d-100 魔法物品表 G Magic Item Table G
01~11 武器 weapon, +2
12~14 异能塑像 figurine of wondrous power (骰 d8)
    1 青铜狮鹫 bronze griffon
    2 乌木苍蝇 ebony fly
    3 黄金狮子 golden lions
    4 象牙山羊 ivory goats
    5 大理石象 marble elephant
    6~7 玛瑙犬 onyx dog
    8 蛇纹石猫头鹰 serpentine owl
15 精金护甲 adamantine armor (胸甲)
16 精金护甲 adamantine armor (板条甲)
17 健康护符 amulet of health
18 易伤护甲 armor of vulnerability
19 吸矢盾 arrow-catching shield
20 矮人腰带 belt of dwarvenkind
21 山丘巨人之力腰带 belt of hill giant strength
22 狂战斧 berserker axe
23 浮空之靴 boots of levitation
24 速度之靴 boots of speed
25 命令元素⽔钵 bowl of commanding water elementals
26 防御护腕 bracers of defense
27 命令元素火盆 brazier of commanding fire elementals
28 郎中披肩 cape of the mountebank
29 命令元素香炉 censer of controlling air elementals
30 护甲 armor, +1 链甲
31 抗性护甲 armor of resistance (链甲)
32 护甲 armor, +1 链甲衫
33 抗性护甲 armor of resistance (链甲衫)
34 移位斗篷 cloak of displacement
35 蝙蝠斗篷 cloak of the bat
36 力场魔方 cube of force
37 迪恩的折叠要塞 Daern's instant fortress
38 淬毒⼔⾸ dagger of venom
39 次元镣铐 dimensional shackles
40 屠⻰者 dragon slayer
41 精灵链甲衫 elven chain
42 焰⾆ flame tongue
43 真视宝⽯ gem of seeing
44 巨⼈屠杀者 giant slayer
45 幻惑镶钉⽪甲 glamoured studded leather
46 传送头盔 helm of teleportation
47 ⾳爆号⾓ horn of blasting
48 ⽡尔哈拉号⾓ horn of Valhalla (白银或黄铜)
49 吟游诗人乐器 instrument of the bards (藤蔓曼陀林 Canaith mandolin)
50 吟游诗人乐器 instrument of the bards (聆听者七弦琴 Cli lyre)
51 艾恩石 Ioun stone (警觉)
52 艾恩石 Ioun stone (防护)
53 艾恩石 Ioun stone (储法)
54 艾恩石 Ioun stone (维生)
55 比拉罗的铁索 iron bands of Bilarro
56 护甲 armor, +1 皮甲
57 抗性护甲 armor of resistance (皮甲)
58 瓦解之锤 mace of disruption
59 打击之锤 mace of smiting
60 恐惧之锤 mace of terror
61 抗魔披风 mantle of spell resistance
62 念珠项链 necklace of prayer beads
63 辟毒护符 periapt of proof against poison
64 感化动物戒指 ring of animal influence
65 反射闪避戒指 ring of evasion
66 羽落戒指 ring of feather falling
67 自由行动戒指 ring of free action
68 防御戒指 ring of protection
69 抗性戒指 ring of resistance
70 法术反转戒指 ring of spell turning
71 公羊戒指 ring of the ram
72 X 射线戒指 ring of x-ray vision
73 百眼法袍 robe of eyes
74 支配权杖 rod of rulership
75 契约掌控者权杖 rod of the pact keeper, +2
76 纠缠绳 rope of entanglement
77 护甲 armor, +1 鳞甲
78 抗性护甲 armor of resistance (鳞甲)
79 盾牌 shield, +2
80 引弹盾 shield of missile attraction
81 魅惑法杖 staff of charming
82 治疗法杖 staff of healing
83 虫群法杖 staff of swarming insects
84 丛林法杖 staff of the woodlands
85 凋零法杖 staff of withering
86 命令元素石核 stone of controlling earth elementals
87 阳炎剑 sun blade
88 窃命剑 sword of life stealing
89 血光剑 sword of wounding
90 触须权杖 tentacle rod
91 恶毒武器 vicious weapon
92 定身魔杖 wand of binding
93 搜敌魔杖 wand of enemy detection
94 恐惧魔杖 wand of fear
95 火球魔杖 wand of fireballs
96 闪电束魔杖 wand of lightning bolts
97 麻痹魔杖 wand of paralysis
98 战法师魔杖 wand of the war mage, +2
99 惊异魔杖 wand of wonder
00 飞翼斗篷 wings of flying
"""

dice_table_magic_item_table_h = """
# d-100 魔法物品表 H Magic Item Table H
d100 魔法物品
01~10 武器 weapon, +3
11~12 位面护符 amulet of the planes
13~14 飞毯 carpet of flying
15~16 ⽔晶球 crystal ball (极珍稀版)
17~18 再生戒指 ring of regeneration
19~20 流星戒指 ring of shooting stars
21~22 心灵遥控戒指 ring of telekinesis
23~24 虹光法袍 robe of scintillating colors
25~26 星辰法袍 robe of stars
27~28 吸收权杖 rod of absorption
29~30 警⽰权杖 rod of alertness
31~32 庇护权杖 rod of security
33~34 契约掌控者权杖 rod of the pact keeper, +3
35~36 急速弯刀 scimitar of speed
37~38 盾牌 shield, +3
39~40 火焰法杖 staff of fire
41~42 冰霜法杖 staff of frost
43~44 威力法杖 staff of power
45~46 强袭法杖 staff of striking
47~48 雷霆法杖 staff of thunder and lightning
49~50 锋锐之剑 sword of sharpness
51~52 变形魔杖 wand of polymorph
53~54 战法师魔杖 wand of the war mage, +3
55 精⾦护甲 adamantine armor (半⾝板甲)
56 精金护甲 adamantine armor (板甲)
57 活化盾 animated shield
58 火巨人之力腰带 belt of fire giant strength
59 霜(⽯)巨⼈之⼒腰带 belt of frost (or stone) giant strength
60 护甲 armor, +1 胸甲
61 抗性护甲 armor of resistance (胸甲)
62 祈神蜡烛 candle of invocation
63 护甲 armor, +2 链甲
64 护甲 armor, +2 链甲衫
65 节肢⽃篷 cloak of arachnida
66 舞空剑 dancing sword
67 恶魔护甲 demon armor
68 ⻰鳞甲 dragon scale mail
69 矮⼈板甲 dwarven plate
70 矮⼈⻜锤 dwarven thrower
71 ⽕巨灵囚瓶 efreeti bottle
72 异能塑像 figurine of wondrous power (⿊曜⽯驹)
73 霜铭 frost brand
74 光辉头盔 helm of brilliance
75 ⽡尔哈拉号⾓ horn of Valhalla (⻘铜)
76 吟游诗人乐器 instrument of the bards (安斯翠瑟竖琴 Anstruth harp)
77 艾恩⽯ Ioun stone (吸收)
78 艾恩⽯ Ioun stone (机敏)
79 艾恩⽯ Ioun stone (坚韧)
80 艾恩⽯ Ioun stone (洞察)
81 艾恩⽯ Ioun stone (才智)
82 艾恩⽯ Ioun stone (统御)
83 艾恩⽯ Ioun stone (⼒量)
84 护甲 armor, +2 ⽪甲
85 强⾝⼿册 manual of bodily health
86 健体⼿册 manual of gainful exercise
87 魔像⼿册 manual of golems
88 灵巧⼿册 manual of quickness of action
89 摄⼼镜 mirror of life trapping
90 九转夺命剑 nine lives stealer
91 誓仇⼸ oathbow
92 护甲 armor, +2 鳞甲
93 抗法盾 spellguard shield
94 护甲 armor, +1 板条甲
95 抗性护甲 armor of resistance (板条甲)
96 护甲 armor, +1 镶钉⽪甲
97 抗性护甲 armor of resistance (镶钉⽪甲)
98 静思卷册 tome of clear thought
99 统御卷册 tome of leadership and influence
00 通晓卷册 tome of understanding
"""

dice_table_magic_item_table_i = """
# d-100 魔法物品表 I Magic Item Table I
d100 魔法物品
01~05 防御者 defender
06~10 雷神之锤 hammer of thunderbolts
11~15 吉兆之刃 luck blade
16~20 应答之剑 sword of answering
21~23 神圣复仇者 holy avenger
24~26 召唤气巨灵戒指 ring of djinni summoning
27~29 隐身戒指 ring o f invisibility
30~32 法术反转戒指 ring of spell turning
33~35 王者权杖 rod of lordly might
36~38 贤者法杖 staff of the magi
39~41 斩首剑 vorpal sword
42~43 云巨人之力腰带 belt of cloud giant strength
44~45 护甲 armor, +2 胸甲
46~47 护甲 armor, +3 链甲
48~49 护甲 armor, +3 链甲衫
50~51 隐身斗篷 cloak of invisibility
52~53 水晶球 crystal ball (传说版本)
54~55 护甲 armor, +1 半身板甲
56~57 收妖瓶 iron flask
58~59 护甲 armor, +3 皮甲
60~61 护甲 armor, +1 板甲
62~63 大法师法袍 robe of the archmagi
64~65 复活权杖 rod of resurrection
66~67 护甲 armor, +1 鳞甲
68~69 防护圣甲虫 scarab of protection
70~71 护甲 armor, +2 板条甲
72~73 护甲 armor, +2 镶钉皮甲
74~75 诸界之井 well of many worlds
76 魔法护甲 magic armor (骰 d12)
    1~2 护甲 armor, +2 半身板甲
    3~4 护甲 armor, +2 板甲
    5~6 护甲 armor, +3 镶钉皮甲
    7~8 护甲 armor, +3 胸甲
    9-10 护甲 armor, +3 板条甲
    11 护甲 armor, +3 半身板甲
    12 护甲 armor, +3 板甲
77 夸力许装置 apparatus of Kwalish
78 坚不可摧护甲 armor of invulnerability
79 风暴巨人之力腰带 belt of storm giant strength
80 异界之门魔方 cubic gate
81 万象无常牌 deck of many things
82 火巨灵链甲 efreeti chain
83 抗性护甲 armor of resistance (半身板甲)
84 瓦尔哈拉号角 horn of Valhalla (黑铁)
85 吟游诗人乐器 instrument of the bards (奥莱姆竖琴 Oiiamh harp)
86 艾恩石 Ioun stone (高等吸收)
87 艾恩石 Ioun stone (精通)
88 艾恩石 Ioun stone (再生)
89 以太化板甲 plate armor of etherealness
90 抗性 armor of resistance (板甲)
91 命令气元素戒指 ring of air elemental command
92 命令土元素戒指 ring of earth elemental command
93 命令火元素戒指 ring of fire elemental command
94 三愿戒指 ring of three wishes
95 命令水元素戒指 ring of water elemental command
96 湮灭法球 sphere of annihilation
97 纯善护符 talisman of pure good
98 法球护符 talisman of the sphere
99 至恶护符 talisman of ultimate evil
00 静语卷册 tome of the stilled tongue
"""

article_magic_items_a_z = """
# 魔法物品 A~Z
魔法物品以物品名字母顺序排列。每个魔法物品的描述都记述了物品的名字、类型、稀有度，以及它的魔法属性。
"""

magic_item_adamantine_armor = """
# 精金护甲 Adamantine Armor
护甲（中型或重型，非兽皮甲），非普通
这套护甲以一种现存最坚硬的物质——精金 adamantine强化。着装该护甲时，任何命中你的重击都会改为普通命中。
"""

magic_item_alchemy_jug = """
# 炼金壶 Alchemy Jug
奇物，非普通
这种陶制壶看起来可以承装 1 加仑的液体，但无论壶中是空还是满，其重量都是 12 磅。即使壶内空无一物，摇动它时也依然会发出液体晃动的声音。
你可以用一个动作命令此壶产生下表列出液体中的一种。
然后，你可以用一个动作打开壶，并以 2 加仑/分钟速度倒出液体。壶中产生液体的体积最大值取决于你指定的液体类型。
从此壶开始生成液体到次日黎明前，它将无法再生成超过其上限的液体或是产生另一种液体。

# table 液体名称 最大体积
强酸 8 盎司 
基础毒药 1/2 盎司 
啤酒 4 加仑 
蜂蜜 1 加仑 
蛋黄酱 2 加仑 
油 1 夸脱
醋 2 加仑
淡水 8 加仑
咸水 12 加仑
葡萄酒 1 加仑
"""

magic_item_ammunition = """
# 弹药 Ammunition，+1、+2 或+3
武器（任何弹药），非普通（+1），珍稀（+2），极珍稀（+3）
你使用此魔法弹药发动攻击检定和伤害掷骰时获得加值。
加值的数值取决于弹药的稀有度。此弹药一旦击中目标即不再具有魔法效果。
"""

magic_item_amulet_of_health = """
# 健康护符 Amulet of Health
奇物，珍稀（需同调）
着装此护符时，你的体质值变为 19。如果你的体质值在未着装护符时已经大于或等于 19，则此护符无效。
"""

magic_item_amulet_of_proof_against_detection_and_location = """
# 反侦护符 Amulet of Proof Against Detection and Location
奇物，非普通（需同调）
着装此护符时，你不会被侦测类魔法发现。你无法被指定为这类魔法的目标，魔法制造的探测器也无法觉察到你。
"""

magic_item_amulet_of_the_planes = """
# 位面护符 Amulet of The Planes
奇物，极珍稀（需同调）
着装此护符时，你可以用一个动作来点名一处你熟悉的另一存在位面地点，然后进行一次 DC 15 的智力检定。如果检定通过，则你施展出法术异界传送 plane shift。如果检定失败，你将和 15 尺内的每个生物和物件一起被传送到一个随机地点。骰一次 d100。如果骰值为 1~60，则你被传送到你点名位面中的随机地点。如果骰值为 61~100，则你被随机传送到一个存在位面。
"""

magic_item_animated_shield = """
# 活化盾 Animated Shield
护甲（盾牌），极珍稀（需同调）
你可以持握此盾时并使用附赠动作说出其命令语使其活化。盾牌将飞到空中并悬浮在你所占据空间中保护你，如同你正持用它一般，且同时解放了你的双手。
盾牌保持活化 1 分钟，或直至你陷入失能、死亡或使用一个附赠动作终止其效应。如果这时你有一只手空着，盾牌将落回你手里。否则它会掉落在地上。
"""

magic_item_apparatus_of_kwalish = """
# 夸力许装置 Apparatus of Kwalish
奇物，传说
这个物品乍一看是个重达 500 磅的密封大铁桶。成功通过一次 DC 20 的智力（调查）检定后可以发现铁桶上有一个隐藏的把手。扳动把手将打开一扇舱门，其大小可以让两名中型或更小体型的生物爬入。舱体尽头是十个拉杆。通常拉杆的位置都在中间，且可以向上推或向下拉。特定的拉杆被拉动时，装置将变形成类似巨大龙虾的外形。
夸力许装置是一个大型物件，其资料如下：
护甲等级：20生命值：200速度：30 尺，游泳 30 尺（如果装置的腿和尾巴未展开，则都为 0 尺）伤害免疫：毒素，心灵夸力许装置用作交通工具时需要一名驾驶员。装置的舱门闭合时，舱内属于气密和水密状态。舱内空气可供一个生物呼吸 10 小时，其总量由舱内生物平摊。
此装置可以在水面上漂浮，也可以潜入至多 900 尺深的水底。达到更深水域时，它将因高压而每分钟承受 2d6 的钝击伤害。
舱内的生物可以用一个动作同时推或拉至多两个拉杆。
每次操作之后，拉杆自动回到中间位置。拉杆的功能如下表所示（从左到右）：

# table 夸力许装置拉杆功能 Apparatus of Kwalish Levers
拉杆 上推 下拉
1 伸展腿和尾巴，让装置可以实现步行和游泳。 收起腿和尾巴，装置的速度降至 0，且无法获得速度加成。
2 打开前窗。 关闭前窗。
3 打开侧舷窗（每侧两扇）。 关闭侧舷窗（每侧两扇）。
4 伸展装置前部的两只钳爪。 收起钳爪。
5 每个钳爪发动一次近战。武器攻击：命中+8，触及5 尺，单一目标。伤害：（2d6）的钝击伤害 每个钳爪发动一次近战。武器攻击：命中+8，触及5 尺，单一目标。伤害：目标被擒抱（逃脱 DC 15）
6 装置向前步行或游泳。 装置向后步行或游泳。
7 装置向左转 90 度。 装置向右转 90 度。
8 眼状部件发光，提供 30 尺半径的明亮光照以其其外30尺半径的微光光照。 关闭发光部件。
9 装置在液体中下沉至多20尺。 装置在液体中上浮至多20尺。
10 解封并打开后方舱门。 关闭并密封后方舱门。
"""

magic_item_armor = """
# 护甲 Armor，+1、+2 或+3
护甲（轻型、中型或重型），珍稀（+1），极珍稀（+2），传说（+3）
你着装该护甲时 AC 获得加值。加值的数值取决于护甲的稀有度。
"""

magic_item_armor_of_invulnerability = """
# 坚不可摧护甲 Armor of Invulnerability
护甲（板甲），传说（需同调）
着装此护甲时，你对非魔法伤害拥有抗性。此外，你可以用一个动作让自己免疫非魔法伤害，持续 10 分钟或直到你不再着装该此护甲为止。使用后，直到次日黎明前你都无法再次启动该专有动作。
"""

magic_item_armor_of_resistance = """
# 抗性护甲 Armor of Resistance
护甲（轻型、中型或重型），珍稀（需同调）
着装此护甲时，你对一种伤害类型具有抗性。该伤害类型由 DM 决定或使用下表随机选定。

# d-10
d10 伤害类型
1 强酸
2 冷冻
3 火焰
4 力场
5 闪电
6 黯蚀
7 毒素
8 心灵
9 光耀
10 雷鸣
"""

magic_item_armor_of_vulnerability = """
# 易伤护甲 Armor of Vulnerability
护甲（板甲），珍稀（需同调）
着装此护甲时，你对钝击、穿刺或挥砍中的一种伤害类型具有抗性。该伤害类型由 DM 决定或随机选定。
诅咒 Curse。这是一件被诅咒的护甲，这一点只有在你同调此护甲或对它使用鉴定术 identify 时才会揭晓。同调此护甲将会使你被诅咒。卸除该护甲不会终止诅咒，只有对你施展法术移除诅咒 remove curse 或以类似的魔法才能将其移除。此诅咒使你对与护甲关联的三种伤害类型中的另两种具有易伤（即护甲提供抗性之外的另两种伤害类型）。
"""

magic_item_arrow_catching_shield = """
# 吸矢盾 Arrow-Catching Shield
护甲（盾牌），珍稀（需同调）
持用此盾牌时，你对抗远程攻击的 AC 获得 +2 加值。该加值将加在盾牌通常提供的 AC 加值上。此外，当攻击者对你身边 5 尺内的目标发动远程攻击时，你可以使用反应以替代该目标成为这次攻击的目标。
"""

magic_item_arrow_of_slaying = """
# 屠杀箭 Arrow of Slaying
武器（箭），极珍稀
屠杀箭是专门用于杀死某类生物的魔法武器。不同屠杀箭针对的范围可能不同。例如，可能同时存在一种龙类屠杀箭arrows of dragon slaying 以及一种蓝龙屠杀箭 arrows of bluedragon slaying。属于屠杀箭关联的生物类型、种族或团体的生物受到这种箭伤害时，该生物必须进行一次 DC 17 的体质豁免。豁免失败的生物将额外受到 6d10 的穿刺伤害，豁免成功则减半。
屠杀箭一旦对某生物造成了额外伤害，它就会立即变成非魔法的箭。
除箭之外也存在一些拥有类似效应的其他类型弹药，例如弩使用的屠杀矢，但箭是最常见的。
"""

magic_item_bag_of_beans = """
# 魔豆之袋 Bag of Beans
奇物，珍稀
这个沉重的布袋里装着 3d4 颗干燥的豆子。布袋重 1/2磅，外加每颗豆子重 1/4 磅。
如果你把布袋里的东西倒在地上，豆子将引发一场半径10 尺的爆炸。爆炸范围内包括你在内的每个生物必须进行一次 DC 15 的敏捷豁免，豁免失败则受到 5d4 的火焰伤害，豁免成功则伤害减半。该火焰会点燃范围内未被着装或携带的物件。
如果从布袋重取出一个豆子种到泥土或沙石中并浇上水，1 分钟后豆子将产生一个效应。DM 可以使用下表随机决定一种效应，也可以自选一种效果或自己创造一种新效应。

# d-100
d100 效应
01 长出 5d4 个毒蕈。吃掉毒蕈的生物必须掷一个任意面数的骰子。如果骰值为奇数，则食用者必须进行一次DC 15 的体质豁免，豁免失败则受 5d6 的毒素伤害并中毒 1 小时。如果骰值为偶数，则食用者获得 5d6 的临时生命值，效应持续 1 小时。
02~10 喷出一股间歇泉喷涌达 30 尺高，持续 1d12 轮，喷出的可以是水、啤酒、果汁、茶、醋、葡萄酒或者油（由DM 决定）。
11~20 长出一个树人 treant（相关资料见《怪物图鉴》）。此树人有 50%的概率属于混乱邪恶并发起攻击。
21~30 一座和你外表相仿，不可移动的活化石雕从地上升起。它会用言语威胁你。如果你离开石雕而其他人靠近它，它就会把你描述成最卑劣的反派并引导他们去攻击你。只要你和雕像身处同一位面，它就可以知道你的位置。雕像的活化状态在 24 小时后终止。
31~40 出现一团跃动着蓝色火焰的篝火，其效应持续 24 小时（或直到它熄灭）。
41~50 出现 1d6+6 的尖叫蕈 shrieker（资料见《怪物图鉴》）51~60 爬出 1d4+8 只亮粉色的蟾蜍 toads。蟾蜍被触碰时会变成一只大型或更小体型的怪物（由 DM 选择）。怪物存在 1 分钟，然后消失在一阵粉红色的烟雾中。
61~70 一只饥饿的鲨蜥兽 bulette（相关资料见《怪物图鉴》）从地下爬出来并发起攻击。
71~80 长出一棵果树。树上有 1d10+20 个水果，其中 1d8 个是相当于随机决定效应的魔法药水，但有一个是 DM决定的某种服用型毒药。果树将在 1 小时后消失，但摘下来的水果仍保留，其魔法保持 30 天。
81~90 出现一窝 1d4+3 个蛋 eggs。任何食用这些蛋的生物必须进行一次 DC 20 的体质豁免，成功则其最低一项属性永久提升 1（多个属性同为最低则随机选定）。豁免失败则该生物体内发生魔法爆炸，受到 10d6 的力场伤害。
91~99 一座占地为 60 尺方形区域的金字塔从地下升起。金字塔内有一名木乃伊领主 mummy lord（相关资料见《怪物图鉴》）的石棺。金字塔是木乃伊领主的巢穴，其棺内的宝藏由 DM 决定。
00 一颗巨大的豌豆茎从地下长出，其高度由 DM 决定。
茎的顶端通往 DM 选择的地点，例如一处宏伟的景点，一座云巨人的城堡，或是另一存在位面。
"""

magic_item_bag_of_devouring = """
# 吞噬袋 Bag of Devouring
奇物，极珍稀
这个表面上看起来像是次元袋 bag of holding 的袋子实际上是某个巨大异次元生物的进食口。将袋子内外翻转就可以关闭进食口的通道。
与这个袋子关联的异次元生物可以感知到任何放入袋中的东西。完整放入袋中的动物或植物将被吞噬而永久消失。活物的一部分被放入袋中时（例如有人把手伸入袋子里时），该生物有 50%概率被拖入袋中。进入袋中的生物可以用一个动作进行一次 DC 15 的力量检定以从中逃脱。另一个生物可以用一个动作进行一次 DC 20 的力量检定来将被吞噬的生物拉出来（前提是该生物自己没被拖入袋中）。任何在袋中开始其自己回合的生物都将被吞噬，其躯体被摧毁。
无生命物件可以存放在袋子里，袋子至多可容纳 1 立方尺的东西。此外，该袋子每日会有一次将其内的所有物件吐到另一存在位面。具体哪个位面由 DM 决定。
袋子被戳破或撕裂时即被摧毁。其内的所有东西都将被传送到星界位面的随机地点。
"""

magic_item_bag_of_holding = """
# 次元袋 Bag of Holding
奇物，非普通
这个袋子内部的实际空间比外表看起来要大。它深约 4尺，袋口直径约 2 尺，可以容纳至多 500 磅，体积不超过 64立方尺的东西。无论装了什么，这个袋子总是重 15 磅。从袋子里取出东西需要花费一个动作。
如果袋子里装的东西超过了容量，或是袋子被戳破、撕裂，它也将因此破裂并被摧毁，它所装载的东西将散落到星界位面各处。如果袋子被内外翻转，则它所装载的东西将安全的掉落出来，但再次使用袋子之前必须将它恢复原状。需要呼吸的生物可以在袋中存活的分钟数为 10 除以生物数量（至少为一分钟），此后袋内的生物便开始窒息。
把次元袋放入霍华德便利袋 Heward’s handy haversack、次元洞 portable hole 或其他类似物品内时，将会立即同时摧毁两件物品并打开一扇通往星界位面的异界之门。门扉产生于放入另一物品的第一件物品。任何在门扉周边 10 尺范围内的生物将被吸入门内，并送往星界位面中的随机地点。然后门扉即时关闭，并且门的通道属于单向性而无法被再次打开。
"""

magic_item_bag_of_tricks = """
# 魔术袋 Bag of Tricks
奇物，非普通
这种普通布袋有三种不同颜色的版本：灰色、铁锈色和棕褐色。布袋看起来是空无一物，但把手伸进去会摸到一个小小的毛绒物件。整个袋子重 1/2 磅。
你可以用一个动作取出布袋里的毛绒物件，并把它扔出至多 20 尺远。当物件落地时骰一次 d8，参考对应颜色布袋的表格决定物件变成的生物。相关生物的资料见《怪物图鉴》。
该生物在次日黎明时分消散，其生命值降至 0 时也随即消失。
扔出的生物对你和你的同伴态度友善，且会在你的回合内行动。你可以用一个附赠动作命令该生物在其下一回合执行特定的移动方式，做特定的动作。你也可以下达宽泛的命令，例如攻击你的敌人。没接到命令时，该生物按自己天性行动。

# d-8 灰色魔术袋 Gray Bag of Tricks
d8 生物 d8 生物
1 鼬鼠 weasel
2 巨鼠 giant rat
3 獾 badger
4 野猪 boar 
5 黑豹 panther
6 巨獾 giant badger
7 凶暴狼 dire wolf
8 巨大麋鹿 giant elk

# d-8 铁锈色魔术袋 Rust Bag of Tricks
d8 生物 d8 生物
1 老鼠 rat 
2 猫头鹰 owl
3 獒 mastiff
4 山羊 goat 
5 巨山羊 giant goat
6 巨野猪 giant boar
7 狮子 lion
8 棕熊 brown bear

# d-8 棕褐色魔术袋 Tan Bag of Tricks
d8 生物 d8 生物
1 豺 jackal
2 猿 ape
3 狒狒 baboon
4 斧嘴鸟 axe beak
5 黑熊 black bear
6 巨鼬 giant weasel
7 巨鬣狗 giant hyena
8 老虎 tiger
"""

magic_item_bead_of_force = """
# 力场珠 Bead of Force
奇物，珍稀
这个小型黑色球体直径 3/4 寸，重 1 盎司。通常都会有1d4+4 颗珠子保存在一起。
你可以用一个动作把珠子扔出至多 60 尺远。珠子因冲击而爆炸并被摧毁，落点周围半径 10 尺范围内的每个生物都必须进行一次 DC 15 的敏捷豁免，豁免失败则受到 5d4 的力场伤害。此外，球型的隐形力场将封闭该区域 1 分钟。任何豁免失败且完全处于范围中的生物会被困在里面。豁免成功或部分处于范围中的生物会沿着远离球型中心的方向推出范围。
攻击或其他效应无法进入球型力场，但供呼吸的空气可以顺利流通。
被困在内部的生物可以用一个动作推动力场障壁，移动至多相当于该生物步行速度一半的距离。这个球型障壁也可以被拿起。无论内部的生物有多重，它的重量都只有 1 磅。
"""

magic_item_belt_of_dwarvenkind = """
# 矮人腰带 Belt of Dwarvenkind
奇物，珍稀（需同调）
着装此腰带时，你获得以下增益：
• 你的体质增加 2，但不能超过 20。
• 你进行与矮人互动的魅力（说服）检定时具有优势。
此外，如果你与此腰带同调且能够长出胡须，则在每天的黎明时分你有 50%的概率长出一把大胡子；如果你已经长有胡须，则你的胡须会明显变得更厚。
如果你不是一名矮人，你在穿戴此腰带时获得以下额外的增益：
• 你进行对抗中毒的豁免时具有优势，并获得对毒素伤害的抗性。
• 你获得 60 尺黑暗视觉。
• 你可以说、读、写矮人语。
"""

magic_item_belt_of_giant_strength = """
# 巨人之力腰带 Belt of Giant Strength
奇物，多种稀有度（需同调）
着装此腰带时，你的力量值变为腰带赋予的数值。如果你未着装该腰带时，力量值已经大于或等于腰带赋予的数值，则该物品无效。
这类腰带共有六种，稀有度各有不同，分别对应六种巨人。石巨人之力腰带 Belt of stone giant strength 和霜巨人之力腰带 Belt of frost giant strength 外形不同但效果一样。

# table 
种类 力量值 稀有度
山丘巨人 hill 21 珍稀
石巨人 stone/霜巨人 frost 23 极珍稀
火巨人 fire 25 极珍稀
云巨人 clound 27 传说
风暴巨人 storm 29 传说
"""

magic_item_berserker_axe = """
# 狂战斧 Berserker Axe
武器（任何斧），珍稀（需同调）
你使用此魔法武器进行攻击检定和伤害掷骰时获得+1 加值。此外，与该武器同调后，你的生命值上限将增加等于你等级的数值。
诅咒 Curse。与这把受诅咒的斧子同调的生物将受到其诅咒影响。只要诅咒还在生效，你总是会把斧子放在触手可及的地方，不愿与它分开。除非你在 60 尺范围内看不到任何敌人也听不到任何敌人的声音，否则你使用这把斧子之外的任何武器发动攻击检定时具有劣势。
敌对生物在你持有斧子时对你造成伤害时，你必须进行一次 DC 15 的感知豁免，豁免失败则则陷入狂怒状态。狂怒时，你必须使用你每轮的动作以该斧子攻击离你最近的生物。
如果你的攻击 Attack 动作中包含有额外的攻击部分，则你将在击败当前目标后继续移动并攻击下一个最近的目标。如果多个目标与你的距离同为最近，则随机选择其中之一。当你在开始自己的回合时周围 60 尺范围内没有你能看到或听到声音的生物时，狂怒终止。
"""

magic_item_boots_of_elvenkind = """
# 精灵之靴 Boots of Elvenkind
奇物，非普通
着装这双靴子时，无论在何种表面上移动，你都不会发出脚步声。你进行有关无声移动的敏捷（隐匿）检定时具有优势。
"""

magic_item_boogts_of_levitation = """
# 浮空之靴 Boots of Levitation
奇物，珍稀（需同调）
着装这双靴子时，你可以用一个动作对自身施展法术浮空术 levitate，次数不限。
"""

magic_item_boots_of_speed = """
# 速度之靴 Boots of Speed
奇物，珍稀（需同调）
着装这双靴子时，你可以获得一个互击脚后跟的附赠动作项。执行该附赠动作后，你的移动速度将加倍，且任何生物对你发动借机攻击时都承受劣势。再次互击脚后跟将终止该效应。
靴子的属性持续使用 10 分钟后，其魔法效应将随之消失直至你完成一次长休才能再次使用。
"""

magic_item_boots_of_striding_and_springing = """
# 跳跑之靴 Boots of Striding and Springing
奇物，非普通（需同调）
着装这双靴子时，你的步行速度变为 30 尺，除非你原本的步行速度更快。你的速度此时不会因为受阻或者穿着护甲而减慢。此外，你跳跃的距离是通常的三倍，但不能超过你剩余的移动距离。
"""

magic_item_boots_of_winterlands = """
# 雪地之靴 Boots of the Winterlands
奇物，非普通（需同调）
这双加绒靴子温暖且舒适。着装这双靴子时，你获得以下增益：
• 你对寒冷伤害具有抗性。
• 你忽略冰或雪造成的困难地形对移动的影响。
• 你能够在没有任何其他保护的情况下忍受低至 -50 华氏度的气温。如果你穿着厚重的衣服，你能够忍受低至 -100 华氏度的气温。
"""

magic_item_bowl_of_commanding_water_elementals = """
# 命令元素水钵 Bowl of Commanding Water Elementals
奇物，珍稀
这个水钵装满水时，你可以用一个动作并说出水钵的命令语以召唤一个水元素 water elemental，其效应相当于你施展出法术召唤元素生物 conjure elemental。直到次日黎明前，该水钵都无法再次以该方式使用。
水钵直径约 1 尺，深约半尺。它的重量为 3 磅，能装承大约 3 加仑水。
"""

magic_item_bracers_of_archery = """
# 射手护腕 Bracers of Archery
奇物，非普通（需同调）
着装这对护腕时，你获得长弓 longbow 和短弓 shortbow的熟练项。你使用这些武器发动远程攻击时，其伤害掷骰获得+2 加值。
"""

magic_item_bracers_of_defense = """
# 防御护腕 Bracers of Defense
奇物，珍稀（需同调）
着装这对护腕时，如果你没有穿着护甲也没有使用盾牌，则你的 AC 获得+2 加值。
"""

magic_item_brazier_of_commanding_fire_elementals = """
# 命令元素火盆 Brazier of Commanding Fire Elementals
奇物，珍稀
当火焰在这个铜盆中燃烧时，你可以用一个动作说出火盆的命令语并以此召唤一个火元素 fire elemental，其效应相当于你施展出法术召唤元素生物 conjure elemental。直到次日黎明前，火盆都无法再次以该方式使用。
火盆的重量为 5 磅。
"""

magic_item_brooch_of_shielding = """
# 护盾胸针 Brooch of Shielding
奇物，非普通（需同调）
着装此胸针时，你获得对力场伤害的抗性，并免疫法术魔法飞弹 magic missile 的伤害。
"""

magic_item_broom_of_flying = """
# 飞天扫帚 Broom of Flying
奇物，非普通
这把扫帚平时只是一把 3 磅重的普通木制扫帚。如果你骑在它上面并说出它的命令语，它就会悬浮在你身下且可以载着你在空中飞行。它的飞行速度为 50 尺。虽然飞天扫帚最多可以搭载 400 磅的重物，但 200 磅以上的载重会将它的飞行速度降低到 30 尺。扫帚在你着陆之后便会停止悬浮。
你可以说出命令语并指明 1 里内一个你熟悉的地点，以此命令扫帚自行飞到该处。如果扫帚在你周围 1 里以内，则你可以用另一个命令语让它回到你身边。
"""

magic_item_candle_of_invocation = """
# 祈神蜡烛 Candle of Invocation
奇物，极珍稀（需同调）
每支祈神蜡烛都为一位选定的神祇定制专用，且具有与神祇相同的阵营。蜡烛的阵营可以用侦测善恶 detect evil andgood 辨别。蜡烛对应的神祇或阵营由 DM 选择或随机决定。
用一个动作点燃蜡烛时，它的魔力就会被激活。蜡烛共可以燃烧 4 小时，你也可以提前吹灭蜡烛以备将来之用。以分钟为单位计算蜡烛已燃烧时间，并从总时间内扣除。
蜡烛燃烧时散发出 30 尺半径范围的微光光照。范围内任何阵营与蜡烛相同的生物进行攻击检定、豁免检定和属性检定时具有优势。此外，范围内阵营与蜡烛相同的牧师和德鲁伊施展 1 环法术时无需消耗法术位，但法术效果仍按消耗了 1环法术位计算。
另外，你还可以在开始点燃蜡烛的同时对其施展法术异界之门 gate。这种做法可以立即摧毁祈神蜡烛。

# d-20
d20 阵营
1~2 混乱邪恶
3~4 混乱中立
5~7 混乱善良
8~9 中立邪恶
10~11 绝对中立
12~13 中立善良
14~15 守序邪恶
16~17 守序中立
18~20 守序善良
"""

magic_item_cap_of_water_breathing = """
# 水下呼吸帽 Cap of Water Breathing
奇物，非普通
在水下着装此帽时，你可以用一个动作说出其命令语以在你头部周围创造出一个供你呼吸的空气泡。空气泡持续存在，直至你再次说出命令语、摘掉帽子或是离开水下。
"""

magic_item_cape_of_the_mountbank = """
# 郎中披肩 Cape of the Mountebank
奇物，珍稀
这件披肩闻起来有一股淡淡的硫磺味。着装该披肩后，你可以用一个动作施展法术任意门 dimension door。使用该属性后直至次日黎明前都无法再次以该方式使用该物品。
以此消失时，你将在原本的位置留下一团烟雾，之后你伴随着一团类似的烟雾出现在目的地。烟雾会在你离开和到达的位置造成轻度遮蔽，并在下一个你的回合结束时消散。一阵微风或更强的风势可以将这种烟雾吹散。
"""

magic_item_carpet_of_flying = """
# 飞毯 Carpet of Flying
奇物，极珍稀
你可以用一个动作说出让飞毯起飞或悬停的命令语。只要你在飞毯周围 30 尺内，它就会按照你的口令移动。
飞毯有四种不同的尺寸，其具体如何则由 DM 进行选择或随机决定。
飞毯的载重上限为表中数值的两倍，但超过正常载重时飞毯的飞行速度减半。

# d-100
d100 尺寸 载重 飞行速度
01~20 3 尺 x 5 尺 200 磅 80 尺
21~55 4 尺 x 6 尺 400 磅 60 尺
56~80 5 尺 x 7 尺 600 磅 40 尺
81~100 6 尺 x 9 尺 800 磅 30 尺
"""

magic_item_censor_of_controlling_air_elementals = """
# 命令元素香炉 Censer of Controlling Air Elementals
奇物，珍稀
当熏香在这个香炉中燃烧时，你可以用一个动作说出香炉的命令语并以此召唤出一个气元素 air elemental，其效应相当于你施展出法术召唤元素生物 conjure elemental。直到次日黎明前，香炉都无法再次以该方式使用。
香炉宽 6 尺，高 1 尺，重 1 磅。其外形类似于一个带有精美装饰杯盖的酒杯。
"""

magic_item_chime_of_opening = """
# 开门钟琴 Chime of Opening
奇物，珍稀
这种空心金属管长约 1 尺，重 1 磅。你可以用一个动作敲击它，在将它指向 120 尺内一个能被打开的物件，比如门、盖子或锁。被敲击的钟琴会发出一个清晰的音调。只要声音可以传到目标物件处，该物件上面的一个锁或者闩就会被打开。
如果物件上没有锁闭的锁或闩，则物件本身被打开。
开门钟琴可使用 10 次。第 10 次后它将碎裂而失去用处。
"""

magic_item_circlet_of_blasting = """
# 爆裂头饰 Circlet of Blasting
奇物，非普通
着装此头饰后，你可以用一个动作施展出法术灼热射线scorching ray。使用此法术攻击的攻击加值为 +5。直到次日黎明前，头饰都无法再次以该方式使用。
"""

magic_item_cloak_of_arachnida = """
# 节肢斗篷 Cloak of Arachnida
奇物，极珍稀（需同调）
这件精美的服饰由黑色丝绸制成，其上用银色丝线绘成网状花纹。着装此斗篷后，你获得以下增益：
• 你获得对毒素伤害的抗性。
• 你获得和步行速度相同的攀爬速度。
• 你可以沿着垂直平面上下移动，甚至可以双手松开倒挂在天花板上。
• 你不会被任何种类的蛛网困住，在移动穿过蛛网时你将其视为等同于困难地形。
• 你可以用一个动作施展出法术蛛网术 web（豁免 DC 13）。
如此创造的蛛网覆盖范围是普通蛛网术的两倍。直到次日黎明前，斗篷的这项属性都无法再次使用。
"""

magic_item_cloak_of_displacement = """
# 移位斗篷 Cloak of Displacement
奇物，珍稀（需同调）
着装此斗篷后，它将投射出你的幻影，使你看起来像是站在一个和你实际位置稍有偏差的地方。任何生物对你发动攻击时都将承受劣势。你受到伤害时斗篷会暂时失效，直至你的下一回合开始恢复效应。当你陷入失能、束缚状态或因其他原因而无法行动时，斗篷的效应也随之被压制。
"""

magic_item_cloak_of_elvenkind = """
# 精灵斗篷 Cloak of Elvenkind
奇物，非普通（需同调）
着装此斗篷并拉起兜帽后，它将变换颜色为你提供伪装。
任何试图看到你的感知（觉察）检定都将承受劣势，且你在使用敏捷（隐匿）检定进行躲藏时具有优势。褪下或拉起兜帽需要一个动作。
"""

magic_item_cloak_of_the_bat = """
# 蝙蝠斗篷 Cloak of the Bat
奇物，珍稀（需同调）
着装此斗篷后，你的敏捷（隐匿）检定具有优势。在微光光照或黑暗环境中，你可以用双手抓住斗篷边沿，利用它以40 尺的速度飞行。如果你没能抓住斗篷边沿或不再处于微光光照或黑暗环境中，则你失去此飞行速度。
着装此斗篷且身处微光光照或黑暗环境时，你可以用一个动作对自己施展出法术变形术 polymorph，并以此变成一只蝙蝠 bat。你在变成蝙蝠时保留自身的智力、感知和魅力属性。
直到次日黎明前，斗篷都无法再以该方式使用
。
"""

magic_item_cloak_of_the_manta_ray = """
# 蝠鲼斗篷 Cloak of the Manta Ray
奇物，非普通
着装此斗篷并拉起兜帽后，你获得 60 尺游泳速度，并能在水下呼吸。褪下或拉起兜帽需要一个动作。
"""

magic_item_cloak_of_invisibility = """
# 隐身斗篷 Cloak of Invisibility
奇物，传说（需同调）着装此斗篷后，你可以把兜帽拉到头上以使自己隐形。你身上着装和携带的所有东西也会随你隐形。褪下兜帽会使你显形。褪下或拉起兜帽需要一个动作。
隐身斗篷的效应至多能持续 2 小时，持续时间以 1 分钟为单位扣除。使用 2 小时后，斗篷将暂时失效。停止使用斗篷达 12 小时可以为它恢复 1 小时的使用时间。
"""

magic_item_cloak_of_protection = """
# 防护斗篷 Cloak of Protection
奇物，非普通（需同调）
着装此斗篷后，你的 AC 和豁免获得+1 加值。
"""

magic_item_crystal_ball = """
# 水晶球 Crystal Ball
奇物，极珍稀或传说（需同调）
水晶球通常直径 6 寸，是一种非常稀有的魔法物品。接触水晶球时，你可以用它施展出法术探知 scrying（豁免 DC17）。
下列水晶球的变体是传说级物品，具有额外的属性。
读心水晶球 Crystal Ball of Minf Reading。使用此水晶球施展法术探知 scrying 时，你可以用一个动作指定该法术传感器周围 30 尺内你能看到的生物，并对其施展法术侦测思想detect thoughts。该侦测思想持续期间你无需为其保持专注，但如果探知 法术终止它也将随之终止。
心灵感应水晶球 Crystal Ball of Telepathy。使用此水晶球施展法术探知 scrying 时，你可以与该法术传感器周围 30尺内你能看到的生物以心灵感应的方式交流。你还可以用一个 动 作 ， 通 过 传 感 器 对 这 些 生 物 中 的 某 一 个 施 展暗 示 术suggestion（豁免 DC 17）。该暗示术 持续期间内你无需为它保持专注，但如果探知 终止它也将随之终止。使用后，水晶球的探知 能力直到次日黎明前都无法再次启动。
真知水晶球 Crystal Ball of True Seeing。使用此水晶球施展法术探知 scrying 时，你对该法术传感器周围半径 120 尺范围拥有真实视觉感官。
"""

magic_item_cube_of_force = """
# 力场魔方 Cube of Force
奇物，珍稀（需同调）
这个立方体棱长约 1 寸，每个面上都有一个可以按压的独特标记。它共有 36 发充能，每天黎明时会恢复 1d20 发已消耗的充能次数。
立方体每一面都可以产生不同的效应。你可以用一个动作按下立方体某一面，并消耗如下表所示的充能。如果立方体充能不足，则什么也不会发生。否则，按下后将产生一股无形力场构成的障壁，形成一个棱长 15 尺的立方区域。障壁持续1 分钟，并以你为中心移动，直至你用一个动作按下立方体的第六个面或立方体耗尽了充能。你可以按下不同的面来改变障壁的效应，但这会消耗相应的充能而其效应的持续时间也将重新开始计算。
如果由于你的移动使障壁与不能穿过它的固定物件接触，那么你在障壁持续时间内将无法更加靠近该固定物件。
当障壁成为某些特定法术目标，或是与某些特定法术、魔法物品效应接触时，立方体将失去一部分充能，如下表所示。

# table 力场魔方各面效果 Cube of Force Faces
面 充能 效应
1 1 气体、风和雾无法穿过障壁。
2 2 非活体物质无法穿过障壁。你还可以决定是否让墙壁、地板和天花板穿过障壁。
3 3 活体物质无法穿过障壁。
4 4 法术效应无法穿过障壁。
5 5 任何东西都无法穿过障壁。你还可以决定是否让墙壁、地板和天花板穿过障壁。
6 0 解除障壁。

# table 
法术或物品 充能损失
解离术 disintegrate 1d12
音爆号角 horn of blasting 1d10
穿墙术 passwall 1d6
虹光喷射 prismatic spray 1d20
火墙术 wall of fire 1d4
"""

magic_item_cubic_gate = """
# 异界之门魔方 Cubic Gate
奇物，传说
这个棱长 3 寸的立方体散发着明显的魔法能量。立方体的六个面分别对应六个位面，其中之一是物质位面其他则由DM 决定。
你可以用一个动作按下立方体的某个面以施展法术异界之门 gate，并打开连接对应位面的传送门。或者，你可以用一个动作按两次立方体的某个面来施展法术异界传送plane shift（豁免 DC 17），以将你的目标传送到对应位面。
立方体有 3 发充能，每次使用都会消耗 1 发充能。它可以在每天黎明时恢复 1d3 发充能。
如果由于你的移动使障壁与不能穿过它的固定物件接触，那么你在障壁持续时间内将无法更加靠近该固定物件。
立方体每一面都可以产生不同的效应。你可以用一个动作按下立方体某一面，并消耗如下表所示的充能。如果立方体充能不足，则什么也不会发生。否则，按下后将产生一股无形力场构成的障壁，形成一个棱长 15 尺的立方区域。障壁持续1 分钟，并以你为中心移动，直至你用一个动作按下立方体的第六个面或立方体耗尽了充能。你可以按下不同的面来改变障壁的效应，但这会消耗相应的充能而其效应的持续时间也将重新开始计算。 迪恩的折叠要塞 Daern's Instant Fortress奇物，珍稀如果你用一个动作把这个棱长 1 寸的金属立方体放在地上并说出命令语，它将迅速变成一座要塞。要塞内空无一人时，你可以用一个动作说出命令语让它恢复折叠状态。
这个要塞是一座方形的高塔，长宽各 20 尺，高 30 尺。
要塞各面墙上都有箭孔，顶端则为城垛。它的内部被分为两层，其间由楼梯连通。楼梯向上最终可以达到要塞顶部的活板门。
要塞被激活时，它面向你的一面上会出现一扇小门。小门只会因你的命令而开启。说出开门的命令语需要一个附赠动作。这扇门不会受到敲击术 knock 和类似魔法效应的影响（比如开门钟琴 chime of opening 的效应）。
要塞展开时，它即将占据空间位置里的每个生物必须进行一次 DC 15 的敏捷豁免，豁免失败者将受到 10d10 的钝击伤害，豁免成功则伤害减半。无论通过与否，这些生物都会被推到要塞旁边未被占据的空间里。未被着装或携带的物件将直接受到伤害并被推到要塞旁边未被占据的空间里。
要塞由精金打造，魔法力量保护它不会被推倒。要塞的顶部、门和每面墙都有 100 点生命值，免疫除攻城武器外任何非魔法武器造成的伤害，且对其他所有伤害具有抗性。只有法术许愿术 wish 可以修复要塞（这种用法视为复制一个 8 环或更低环的法术）。每一道许愿术 wish可以为要塞顶部、大门或一面墙恢复 50 点生命值。
"""

magic_item_dagger_of_venom = """
# 淬毒匕首 Dagger of Venom
武器（匕首），珍稀
使用此魔法武器进行攻击检定和伤害掷骰时获得+1 加值。
你可以用一个动作使匕首涂上毒液。毒液存在 1 分钟，或直至你用这把武器成功命中某名生物。被击中生物必须进行一次 DC 15 的体质豁免，豁免失败则受 2d10 的毒素伤害并中毒 1 分钟。直到次日黎明前，该匕首都无法再以该方式进行使用。
"""

magic_item_dancing_sword = """
# 舞空剑 Dancing Sword
武器（任意剑），极珍稀（需同调）
你可以用附赠动作将这把魔法剑抛到空中并说出命令语。
此时，魔剑将悬浮在空中，然后飞行至多 30 尺并攻击距离它5 尺以内的一名生物。剑使用你的攻击检定，其伤害掷骰也使用你的属性调整值。
剑在空中悬浮时，你可以用附赠动作令它在你周围 30 尺范围内飞行至多 30 尺，还可以令它攻击距离它 5 尺以内的一名生物（同一个附赠动作）。
剑在浮空状态下攻击四次后，它将飞行至多 30 尺试图回到你手上。如果你没有空着的手，那么它会落在你脚边。如果你和剑之间的路径被阻塞，则它会尽可能的落在离你最近的位置。如果你抓住悬浮的剑或者主动离开它超过 30 尺，那它也将停止悬浮。
"""

magic_item_decanter_of_endless_water = """
# 无尽水瓶 Decanter of Endless Water
奇物，非普通
这个 2 磅重，带瓶塞的瓶子在摇晃时会发出液体晃动的声音，仿佛其中有水一般。
你可以用一个动作拔出瓶塞并说出三个命令语中之一，使瓶子流出淡水或是咸水（由你选择）。水将在你的下一回合开始时停止涌出。瓶子的命令语有以下三种：
• “溪流 Stream”产生 1 加仑的水。
• “泉源 Fountain”产生 5 加仑的水。
• “井喷 Geyser”如同间歇泉般喷出一道高 30 尺，宽 1 尺的水柱，共产生 30 加仑水。如果你握持此瓶，则可以用一个附赠动作将瓶口对准 30 尺范围内一名你能看到的生物。该生物必须进行一次 DC 13 的力量豁免，豁免失败则受到 1d4的钝击伤害并陷入倒地。另外，你也可以用瓶口瞄准一个不超过 200 磅，且未被着装或携带的物件。而该物件将随之被打翻或被你推开 15 尺。
"""

magic_item_deck_of_illusions = """
# 幻象牌组 Deck of Illusions
奇物，非普通
这个匣子里装着一套羊皮纸制的卡牌。一套完整的牌组有 34 张卡，但作为宝藏获得牌组时通常会缺少 1d20-1 张卡。
只有在随机抽取时，卡牌的魔法才会生效（你可以使用扑克牌模拟牌组）。你可以用一个动作从牌组中随机抽出一张牌并扔到 30 尺内的地面上。
一名或多名幻象生物将在扔出的卡牌上形成，并一直持续到幻象被解除。幻象生物看起来活灵活现，和真实生物体型相仿，行为模式也相同（详见《怪物图鉴》）但无法造成伤害。
如果你在幻象生物周围 120 尺内且能看到它，则你就可以用一个动作命令它移动到卡牌周围 30 尺内的任何地方。由于物件可以穿透幻象，因此与幻象生物的任何物理互动都将揭示其幻象本质。以视觉观察幻象生物时，成功通过一次 DC 15 的智力（调查）检定即可发现幻象的本质。检定成功后幻象在该生物眼中即为半透明状态。
幻象将一直持续到被解除或直至它的卡牌被移动。当幻象终止时，它卡牌上的图像也随之消失，该卡牌也从此失去效应。

# table
扑克牌 幻象
红心 A 红龙 red dragon
红心 K 骑士 knight 和四个卫兵 guards
红心 Q 魅魔 succubus 或梦魔 incubus
红心 J 德鲁伊 druid
红心 10 云巨人 cloud giant
红心 9 双头巨人 ettin
红心 8 熊地精 bugbear
红心 2 地精 goblin
方块 A 眼魔 beholder
方块 K 大法师 archemage 和法师学徒 mage apprentice
方块 Q 夜鬼婆 night hag
方块 J 刺客 assassin
方块 10 火巨人 fire giant
方块 9 食人魔巫师 ogre mage
方块 8 豺狼人 gnoll
方块 2 狗头人 kobold
黑桃 A 巫妖 lich
黑桃 K 祭司 priest 和两名侍僧 acolytes
黑桃 Q 美杜莎 medusa
黑桃 J 老兵 veteran
黑桃 10 霜巨人 frost giant
黑桃 9 巨魔 troll
黑桃 8 大地精 hobgoblin
黑桃 2 地精 goblin
梅花 A 铁魔像 iron golem
梅花 K 强盗头目 bandit captain 和三名强盗 bandits
梅花 Q 欲魔 erinyes
梅花 J 狂战士 berserker
梅花 10 山丘巨人 hill giant
梅花 9 食人魔 ogre
梅花 8 兽人 orc
梅花 2 狗头人 kobold
王牌（2 张） 你（牌组的持有者）
"""

magic_item_deck_of_many_things = """
# 万象无常牌 Deck of Many Things
奇物，传说
这种由象牙或羊皮纸制成的卡牌通常存放在盒子或袋子里。一套牌大多数时候（75%）只有 13 张卡，但有时也会有22 张。
抽卡之前，你必须先声明要抽多少张卡牌，然后随机抽取（你可以使用扑克牌模拟牌组）。继续抽取声明数量之外更多的卡牌将不会产生任何效应。按正常方法抽出的卡牌其魔法效应在抽出时立即生效。你抽取两张卡牌之间的间隔不能超过 1 小时。如果你未能抽够声明数量的卡牌，声明了但是未抽取的那部分卡牌将从牌组中自行飞出并同时生效。
被抽出的卡牌其本身的存在将随之消散。除非你抽到的是愚者 Fool 或小丑 Jester，否则抽出的卡型将重新出现在牌组里，使得你可能再次抽到该卡。平衡 Balance。你的心灵经历了剧烈的变化，甚至改变了你的阵营。守序将变为混乱，善良则变为邪恶，反之亦然。如果你的阵营为绝对中立或无阵营，则此卡对你没有影响。彗星 Comet。如果你独自战胜接下来所遭遇的一只或一群敌对怪物，你将获得足够使你提升到下一级的经验值。否则，此卡对你没有影响。
城堡 Donjon。你凭空消失并以静滞状态被禁锢在某个球形异次元空间里。消失时，你着装和携带的所有物品都将落在你之前占据的空间里。你将一直被禁锢，直至被发现并从异次元空间中被解放出来。你无法被任何预言系魔法定位，但法术许愿术 wish 可以获悉你的位置。抽到此卡后你不再抽取其他卡片。
蛇发女妖 Euryale。卡片上与美杜莎相似的画像诅咒了你。
受到此诅咒的影响，你的豁免承受-2 减值。只有某个神灵或卡牌“命运三女神”可以终止这种诅咒。
命运三女神 The Fates。现实本身的存在被拆散而又重新编就，并以此让你得以避免或抹除某件已经发生的事件，如同它从未发生一般。你可以在抽到此卡后，直至自己死前的任何时间使用这张卡的效果。
火焰 Flames。一名强大的魔鬼视你为仇敌。它会试图摧毁你的意志和你的生活，品尝你的痛苦并最终杀了你。这名魔鬼的敌意将持续到它和你中的一方死去为止。
愚者 Fool。你失去 10,000 点经验值。弃掉这张牌并另抽一张牌，把这两次抽牌计为你声明的抽牌次数中的一次。如果失去这些经验值会使你的等级降低，则保留当前等级所需的最低经验值。
宝石 Gem。二十五枚各价值 2,000 gp 的宝石，或五十枚各价值 1,000 gp 的宝石出现在你脚边。
白痴 Idiot。你的智力永久降低 1d4+1（最低为 1）。你在声明的抽卡数量外再抽取一张卡牌。
小丑 Jester。你获得 10,000 经验值，或者你在声明的抽卡数量外再抽取两张卡牌。
钥匙 Key。由 DM 选择一把你拥有熟练项且稀有度为珍稀或更高的武器出现在你手中。
骑士 Knight。一名 4 级战士出现在你身边 30 尺内由你指定的位置并为你服务。战士和你种族相同，并相信命运安排与你相遇且表示至死效忠于你。这名战士将由你控制。
月亮 Moon。你获得 1d3 次施展祈愿术 wish 的能力。
浪人 Rogue。由 DM 选择一名非玩家角色视你为仇敌。你不知道这名新敌人的身份，直到他自己或其他人揭穿真相。只有法术 许愿术 wish 或神灵干涉程度的力量才能终止该非玩家角色对你的敌意。
废墟 Ruin。你失去魔法物品以外一切你持有或拥有的财产。可动产将直接消失；在最低限度修改现实的前提下，你还将失去你拥有的所有生意、建筑物和土地。任何证明你拥有任何财产的文件也将因此卡而消失。
头骨 Skull。你召唤出一名死亡化身 avatar of death——身穿破烂黑袍，手持幽灵镰刀，幽魂般的一个类人生物骷髅。它将在你周围 10 尺内一处 DM 指定的位置出现并对你发动攻击，同时警告其他人你必须要独自面对这场战斗。化身在将你杀死或自身生命值降至 0 后消失。如果有人试图在这场战斗中帮你，则该人物将因此召唤出自己的死亡化身。被死亡化身杀死的生物无法被复活。
星辰 Star。你的一项属性提升 2。由此被提升的属性可以超过 20 但不能超过 24。
太阳 Sun。你获得 50,000 经验值，且某件奇物（DM 决定）出现在你手中。
利爪 Talons。你着装或携带的魔法物品被解离。神器不会被摧毁但会因此消失。
王座 Throne。你获得魅力（说服）技能的熟练项，并在进行该技能检定时加上双倍的熟练加值。此外，你获得世界上某个地方的一座小城堡的所有权。然而这座城堡被怪物所占据，你必须清理其中的怪物以获得城堡的控制权。
大臣 Vizier。抽到此卡后一年内任何时候，你可以在冥想中提出一个问题并获得诚实的回答。这个答案不止会给你提供信息，还会帮助你解决一个困境。换句话说，答案包括了如何实施答案的方法。
虚空 The Void。这张黑色的卡片将带来灾难。你的灵魂从躯体抽离，并囚禁在某个 DM 指定地点的某个物件里。一名或多名强大的存在守护着这个地点。灵魂被囚禁期间，你的躯体处于失能状态。
许愿术 wish 无法唤回你的灵魂，但可以揭示囚禁它的物件所在的方位。抽到此卡后你不再抽取其他卡片。
死亡化身 Avatar of Death中型不死⽣物，中⽴邪恶AC：20HP：召唤者生命值的一半速度：60 尺，飞行 30 尺（悬浮）力量 16（+3） 敏捷 16（+3） 体质 16（+3）智力 16（+3） 感知 16（+3） 魅力 16（+3）伤害免疫：黯蚀，毒素状态免疫：魅惑，恐慌，麻痹，石化，中毒，昏迷感官：黑暗视觉 60 尺，真实视觉 60 尺，被动觉察 13语言：召唤者所知的所有语言挑战等级：--（0 XP）虚体移动 Incorporeal Movement。死亡化身可以移动穿过生物和物件，并视为等同于穿过困难地形。如果它在自己回合结束时身处物件内部，则受到 5（1d10）的力场伤害。
免疫驱散 Turning Immuntiy。死亡化身免疫驱散不死生物特性。
动作收割之镰 Reaping Scythe。死亡化身用幽魂镰刀贯穿 5 尺内的一名生物，造成 7（1d8+3）的挥砍伤害，外加 4（1d8）的黯蚀伤害。

# table
扑克牌 对应卡牌
方块 A 大臣 Vizier*
方块 K 太阳 Sun
方块 Q 月亮 Moon
方块 J 星辰 Star
方块 2 彗星 Comet*
红心 A 命运三女神 The Fates*
红心 K 王座 Throne
红心 Q 钥匙 Key
红心 J 骑士 Knight
红心 2 宝石 Gem*
梅花 A 利爪 Talons*
梅花 K 虚空 The Void
梅花 Q 火焰 Flames
梅花 J 头骨 Skull
梅花 2 白痴 Idiot*
黑桃 A 城堡 Donjon*
黑桃 K 废墟 Ruin
黑桃 Q 蛇发女妖 Euryale
黑桃 J 浪人 Rogue
黑桃 2 平衡 Balance*
小王 愚者 Fool*
大王 小丑 Jester
*只存在于 22 张卡的牌组里

# 关于树敌 A Question of Enmity
万象无常牌中有两张卡牌可能会使某个存在对抽卡的角色产生敌意。“火焰”卡牌导致的敌意是显而易见的，角色会因此多次遭遇魔鬼的恶毒算计。但找到这名魔鬼却并不容易。在最终对抗魔鬼之前，角色可能会多次与它的盟友和手下发生冲突。
“浪人”卡牌导致的敌意来源于抽卡的角色以为是朋友或盟友的角色，因此不易察觉。作为 DM，你应该等待最有戏剧效果的时刻展示这种敌意，让玩家们不断猜测背叛者是谁。
"""

creature_avatar_of_death = """
# 死亡化身 Avatar of Death
中型不死⽣物，中⽴邪恶
AC：20
HP：召唤者生命值的一半
速度：60 尺，飞行 30 尺（悬浮）
力量 16（+3） 敏捷 16（+3） 体质 16（+3）智力 16（+3） 感知 16（+3） 魅力 16（+3）
伤害免疫：黯蚀，毒素
状态免疫：魅惑，恐慌，麻痹，石化，中毒，昏迷
感官：黑暗视觉 60 尺，真实视觉 60 尺，被动觉察 13
语言：召唤者所知的所有语言
挑战等级：--（0 XP）
虚体移动 Incorporeal Movement。死亡化身可以移动穿过生物和物件，并视为等同于穿过困难地形。如果它在自己回合结束时身处物件内部，则受到 5（1d10）的力场伤害。
免疫驱散 Turning Immuntiy。死亡化身免疫驱散不死生物特性。
动作收割之镰 Reaping Scythe。死亡化身用幽魂镰刀贯穿 5 尺内的一名生物，造成 7（1d8+3）的挥砍伤害，外加 4（1d8）的黯蚀伤害。
"""

magic_item_defender = """
# 防御者 Defender
武器（任意剑），传说（需同调）
使用此魔法武器发动的攻击检定和伤害掷骰获得+3 加值。
你在每个自己回合里第一次使用此剑攻击时，可以选择将此剑的加值全部或部分转移到你的护甲等级中，而非用于本回合的任何攻击。例如，你可以将攻击检定和伤害掷骰的加值降低到+1 而在 AC 上获得+2 加值。加值改变持续到你的下一回合开始。你必须握持此剑才能获得它提供的 AC 加值。
"""

magic_item_demon_armor = """
# 恶魔护甲 Demon Armor
护甲（板甲），极珍稀（需同调）
着装该护甲后你的 AC 获得+2 加值，且可以理解和说出深渊语。另外，护甲附带利爪般的铁护手可以令你用手进行徒手打击时视为魔法武器并造成挥砍伤害，你以此发动的攻击检定和伤害掷骰获得+1 加值。
诅咒 Curse。着装这件被诅咒的护甲后，除非你被施予法术移除诅咒 remove curse 或类似的魔法效应，否则你无法将其卸下。着装该护甲后，你对恶魔进行的攻击检定，以及对抗恶魔法术和特殊能力时进行的豁免检定均具有劣势。
"""

magic_item_dimensional_shackles = """
# 次元镣铐 Dimensional Shackles
奇物，珍稀
你可以用一个动作来以此镣铐束缚一个失能的生物。镣铐可以自行调整适应从小型到大型体型的生物。除普通镣铐的作用之外，次元镣铐还能阻止被其束缚生物进行异次元移动，包括传送和异位面旅行。但是，镣铐不会阻止生物穿过一道连接异位面的传送门。
你和你指定的任何生物能用一个动作解除此镣铐。每隔30 日，被束缚的生物可以进行一次 DC 30 的力量（运动）检定，成功则破坏镣铐重获自由。
"""

magic_item_dragon_scale_mail = """
# 龙鳞甲 Dragon Scale Mail
护甲（鳞甲），极珍稀（需同调）
龙鳞甲是以某一种龙的鳞片制成的护甲。有时候是龙把自己褪下的鳞片送给类人生物，有时候则是猎人们小心的剥下死去龙类的鳞片并仔细保存起来。无论如何，龙鳞甲都是非常珍贵的物品。
着装该护甲时，你的 AC 获得+1 加值，且为对抗“骇人威仪 Frightful Presence”和龙的吐息武器时所作豁免具有优势。根据龙鳞甲使用的龙鳞种类，你还会获得对一种伤害类型的抗性（见下表）。
另外，你还可以用一个动作集中精神感知距你最近，且与龙鳞甲的鳞片提供者类型相同的龙类，并得知其相对于你的方向与距离。这条龙必须在你周边 30 里以内且与你处于同一位面。此后直到次日黎明前，该特殊动作都无法再次使用。
"""

magic_item_dragon_slayer = """
# 屠龙者 Dragon Slayer
武器（任意剑），珍稀
你用该魔法武器发动的攻击检定和伤害掷骰获得+1 加值。
你以该武器命中龙类时，它将受到与剑的伤害类型相同的额外 3d6 伤害。此处的“龙”指任何生物类型为龙类的生物，包括龙龟 dragon turtle 和飞龙 wyvern 等。

# table
龙种 抗性
黑龙 强酸
蓝龙 闪电
黄铜龙 火焰
青铜龙 闪电
赤铜龙 强酸
金龙 火焰
绿龙 毒素
红龙 火焰
银龙 寒冷
白龙 寒冷
"""

magic_item_driftglobe = """
# 漂浮之球 Driftglobe
奇物，非普通
这个厚玻璃制成的小球重 1 磅。在它周围 60 尺内，你可以说出命令语以使它施展出光亮术 light 或日光术 daylight。
使用一次后直至次日黎明前，其日光术 daylight 效应将无法再次使用。
你可以用一个动作来说出另一个命令语，以让发光球体飞到空中，漂浮在离地面不超过 5 尺的地方。球体将持续漂浮在空中，直到你或另一生物将它抓住。如果你离开球体周围60 尺范围，则它将沿最短路径跟随你移动直到距离你 60 尺为止。如果它的移动遭到妨碍，它将闪烁着落回地面并回到启动前的状态。
"""

magic_item_dust_of_disappearance = """
# 无踪粉 Dust of Disappearance
奇物，非普通
这是一些装在小包里的细沙般的粉末，其分量足够使用一次。你可以用一个动作将粉末洒向空中，使得你和你周围10 尺内的生物和物件隐身 2d4 分钟（持续时间对所有受影响的对象一致）。粉末一经使用即被消耗。如果一名受影响的生物发动攻击或者施展法术，则该生物的隐形效应也随之终止。
"""

magic_item_dust_of_dryness = """
# 干燥粉 Dust of Dryness
奇物，非普通
这个小包里共装着 1d6+4 把粉末。你可以用一个动作将一把粉末洒到水面上。粉末将把 15 尺立方区域的水变成一个弹珠大小的小球，漂浮或停止在粉末被洒下的位置附近。小球的重量可以忽略不计。
任一生物可以用一个动作将小球摔在某个结实表面，以令小球破碎并释放其中的水分。同时使小球失去其魔力。
身体大部分由水组成的元素生物在接触到一把干燥粉时必须进行一次 DC 13 的体质豁免，失败则受到 10d6 的黯蚀伤害，成功则伤害减半。
"""

magic_item_dust_of_sneezing_and_choking = """
# 喷嚏粉 Dust of Sneezing and Choking
奇物，非普通
这种细沙般的粉末通常被装在小盒子里，其分量足够使用一次。这种粉末看起来像是无踪粉 dust of disappearance，对其施展鉴定术 identify 也会给出这样的结果。你可以用一个动作把这种粉末洒向空中。此时，你和你周围 30 尺内任何需要呼吸的生物必须进行一次 DC 15 的体质豁免，失败者将因不停打喷嚏而无法呼吸。受此影响的生物将陷入失能并窒息。
只要受影响的生物依然清醒，它就能在每次自己的回合结束时再次进行该豁免。一旦豁免成功，其自己身上的效应也将随之终止。法术次级复原术 lesser restoration 也可以终止一名生物身上的该效应。
"""

magic_item_dwarven_plate = """
# 矮人板甲 Dwarven Plate
护甲（板甲），极珍稀
着装该护甲时，你的 AC 获得+2 加值。此外，当某种效应将要在违背你意愿的情况下使你在地面上移动时，你可以用一个反应来减少你被移动的距离至多 10 尺。
"""

magic_item_dwarven_thrower = """
# 矮人飞锤 Dwarven Thrower
武器（战锤），极珍稀（需矮人同调）
你用该魔法武器发动的攻击检定和伤害掷骰获得+3 加值。
它具有投掷属性，常规射程为 20 尺，最大射程为 60 尺。当你用此武器发动远程攻击命中时，它将造成 1d8 的额外伤害。
如果命中的目标是一名巨人，则额外伤害提升为 2d8。攻击后，此武器将立即飞回你的手中。
"""

magic_item_efreeti_bottle = """
# 火巨灵囚瓶 Efreeti Bottle
奇物，极珍稀
这个彩绘的黄铜瓶子重 1 磅。如果你用一个动作拔出瓶塞，一团浓烟将从瓶内溢出。在你的回合结束时，该浓烟会随着一股无害的火焰消失，同时一名火巨灵 efreeti 将出现在你周边 30 尺内一个未被占据的空间位置。火巨灵的资料详见《怪物图鉴》。
瓶子第一次被打开时，DM 掷骰决定效应。

# d-100
d100 效应
01~10 火巨灵攻击你。战斗进行 5 轮后，火巨灵将消失，同时瓶子失去魔力。
11~90 火巨灵为你服务 1 小时，然后回到瓶中。一个新的瓶塞将显现并再次将其封印，且新瓶塞在 24 小时内将无法被拔出。之后两次瓶子被打开时会产生同样的效应。瓶子被打开第四次时火巨灵将逃走并消失，同时瓶子失去魔力。
91~00 火巨灵可以为你施展三次祈愿术 wish。它将在 1 小时后或施展完第三次祈愿术 时消失，而瓶子也随之失去魔力。
"""

magic_item_efreeti_chain = """
# 火巨灵链甲 Efreeti Chain
护甲（链甲），传说（需同调）
着装该护甲时，你的 AC 获得+3 加值，且免疫火焰伤害，还可以说和理解原初语 Primordial。此外，你还可以像在坚实地面上一样行走于熔岩上。
"""

magic_item_elemental_gem = """
# 元素宝石 Elemental Gem
奇物，非普通
这种宝石蕴藏着操纵元素的能量。你可以用一个动作来打碎宝石，其效应如同你施展法术召唤元素生物 conjureelemental 一样召唤出一个元素。被打碎的宝石也将失去魔力。
宝石的种类决定了法术所召唤的元素。

# table 
宝石 召唤的元素
蓝色蓝宝石 blue sapphire 气元素
黄钻石 yellow diamond 土元素
红刚玉 red corundum 火元素
翡翠 emerald 水元素
"""

magic_item_elixir_of_health = """
# 健康灵药 Elixir of Health
魔药，珍稀
饮用此药水将治愈你身上的所有疾病，并移除目盲、耳聋、麻痹、中毒等状态。这种清澈的红色液体中有发光的小气泡。
"""

magic_item_elfven_chain = """
# 精灵链甲 Elven Chain
护甲（链甲衫），珍稀
着装该护甲时，你的 AC 获得+1 加值。即使没有中型护甲的熟练项，你依然视为拥有该护甲的熟练项。
"""

magic_item_eversmoking_bottle = """
# 无尽烟壶 Eversmoking Bottle
奇物，非普通
这个重 1 磅，带铅塞的黄铜瓶子会渗出烟雾。如果你用一个动作拔掉瓶塞，一团浓重的云雾将从瓶中涌出，并扩散到瓶子周围 60 尺半径范围。被云雾笼罩的区域视处于重度遮蔽。
只要瓶子保持开启，每 1 分钟云雾的半径会扩大 10 尺，直至达到 120 尺。
只要瓶子保持开启，该云雾就会持续存在。用一个动作说出命令语可以使瓶子关闭。瓶子关闭后，云雾将在 10 分钟后消散。一阵和风 moderate wind（11 至 20 里每小时）可以用1 分钟吹散云雾，而强风 strong wind（11 至 20 里每小时）则可以用 1 轮吹散云雾。
"""

magic_item_eyes_of_charming = """
# 魅惑镜片 Eyes of Charming
奇物，非普通（需同调）
这种水晶镜片可以着装到眼睛上。魅惑镜片有 3 发充能。
着装该镜片时，如果你和你周围 30 尺内的一名类人生物能够互相看见对方，则你可以用一个动作并消耗 1 发充能来对它施展法术魅惑人类 charm person（DC 13）。镜片消耗掉的充能将在每天黎明时恢复。
"""

magic_item_eyes_of_minute_seeing = """
# 微视镜片 Eyes of Minute Seeing
奇物，非普通
这种水晶镜片可以着装到眼睛上。着装该镜片时，可以更清晰的观察周边 1 尺以内的东西。在此范围内，你为搜索区域或研究物件所作，依赖视力的智力（调查）检定具有优势。
"""

magic_item_eyes_of_the_eagle = """
# 鹰眼镜片 Eyes of the Eagle
奇物，非普通（需同调）
这种水晶镜片可以着装到眼睛上。着装该镜片时，你依赖视力进行的感知（察觉）检定具有优势。在视野清晰的情况下，你可以在很远的地方看清小至 2 尺的生物或物件的细节。
"""

magic_item_figurine_of_wondrous_power = """
# 异能塑像 Figurine of Wondrous Power
奇物，稀有度依塑像种类而不同
异能塑像是小到可以装在口袋里的野兽雕像。当你用一个动作说出命令语并把雕像扔到你周围 60 尺以内的某处时，它将变成一只活体生物。如果雕像被扔到的地方被其他生物或物件占据，或者周围的空间不足以容纳该雕像变成的生物，则它将不会变成生物。
雕像变成的生物对你和你的同伴态度友善。它能听懂你的语言并会按你的口头命令行事。如果你不下达任何命令，则该生物会保护自己而不作其他动作。除巨苍蝇 giant fly 外，其他生物的资料详见《怪物图鉴》。
• 旅行山羊 goat of traveling 可以变为一只资料和乘用马 riding horse 相同的大型山羊。它有 24 发充能，处于野兽形态下时每小时（不足 1 小时按 1 小时计）将消耗 1 发充能。只要雕像还有充能，你就能随意使用它。当充能耗尽时，它将变回雕像且需要等到 7 日后充能恢复时才能再次启动。
• 苦工山羊 goat of travail 可以变为一只巨山羊 giant goat，其存在至多维持 3 小时。使用后，此雕像需要经过 30 日才能再次启动。
• 惊骇山羊 goat of terror 可以变为一只巨山羊 giant goat并至多维持 3 小时。它无法发动攻击，但你可以卸下它的角作为武器。其中一只角变为+1骑枪 lance，而另一只角则变为+2长剑 longsword。卸下一只角视为一个动作。当山羊变回雕像时，角变成的武器也将随之消失，而山羊的角会恢复原状。另外，当你骑乘这头巨大山羊时，它将散发出 30尺半径的恐惧灵光。任何在灵光范围内开始其自己回合的敌对生物，必须进行一次 DC 15 的感知豁免，失败则恐慌1分钟或直到山羊变回雕像。该受恐慌生物可以在每个它自己的回合结束时再次进行该豁免，成功则终止其自己身上的该效应。生物豁免成功时，它将在随后的 24 小时里免疫该山羊的恐惧灵光。使用后，此雕像需要经过 15 日才能再次启动。
大理石象 Marble Elephant（珍稀）。这是一尊长和高约为 4 寸的大理石雕像。它可以变为一头象 elephant，存在至多维持 24 小时。使用后，雕像需要经过 7 日才能再次启动。
黑曜石驹 Obsidian Steed（极珍稀）。这个打磨过的黑曜石驹雕像可以变为一只梦魇 nightmare，其存在至多维持 24小时。梦魇只会为了保护自己而战斗。使用后，此雕像需要经过 5 日才能再次启动。如果你属于善良阵营，则每次你使用此雕像时它有 10%的概率会无视你的命令，包括让它变回雕像的命令。如果你在梦魇无视你命令时骑上它，则你和梦魇会一起立刻被传送到哈迪斯 Hades 位面的随机地点。之后梦魇将变回雕像。玛瑙犬 Onyx Dog（珍稀）。这个玛瑙犬雕像可以变为一只獒犬 mastiff，其存在至多维持 6 小时。这只獒智力为 8 并且会说通用语。它具有 60 尺黑暗视觉并且可以看到 60 尺范围内的隐形生物和物件。使用后，此雕像需要经过 7 日才能再次启动。蛇纹石猫头鹰 Serpentine Owl（珍稀）。这个蛇纹石猫头鹰雕像可以变为一只巨猫头鹰 giant owl，而其存在至多维持8 小时。只要你和该猫头鹰在同一位面，它就可以和你通过心灵感应进行沟通。使用后，此雕像需要经过 2 日才能再次启动。白银渡鸦 Silver Raven（非普通）。这个银制渡鸦雕像可以变为一只渡鸦 raven，其存在至多维持 12 小时。你可以对渡鸦形态的此雕像随意施展动物信使 animal messager。使用后，此雕像需要经过 2 日才能再次启动。
"""

creature_giant_fly = """
# 巨苍蝇 Giant Fly
大型野兽，无阵营
AC：11
HP：19（3d10+3）
速度：30 尺，飞行 60 尺
力量 14（+2） 敏捷 13（+1） 体质 13（+1）智力 2（-4） 感知 10（+0） 魅力 3（-4）
感官：黑暗视觉 60 尺、被动察觉 10
语言：—
"""

magic_item_flame_tongue = """
# 焰舌 Flame Tongue
武器（任意剑），珍稀（需同调）
你可以用一个附赠动作说出命令语，以让这把剑的锋刃吐出烈焰。剑身的火焰为周围 40 尺范围提供明亮光照，以及额外 40 尺的微光光照。剑身燃烧时将对其命中的目标造成额外 2d6 的火焰伤害。火焰将持续燃烧到你把剑放下、收入鞘内或再次用一个附赠动作说出命令语为止。
"""

magic_item_folding_boat = """
# 折叠船 Folding Boat
奇物，珍稀
该物件外观看起来是个长 12 寸，宽 6 寸，深 6 寸的木盒。它重 4 磅且能在水面上漂浮，也可以像普通木盒一样装东西。该物品有三个命令语，说出一个命令语需要一个动作。
第一个命令语能使盒子展开成一条长 10 尺，宽 4 尺，深2 尺的小船 boat。小船有一对桨、一个锚、一根桅杆和一面三角帆。它最多可以搭乘四名中型体型的生物。
第二个命令语能使盒子展开成一条长 24 尺，宽 8 尺，深6 尺的船 ship。这艘船有一块甲板、划桨座、五对桨、一个舵桨、一个锚、一个甲板舱以及一根装有横帆的桅杆。它最多可以搭乘 15 名中型体型的生物。
木盒展开成船只时，它的重量也变为对应船只应有的重量。原本存放在木盒中的东西将留在船内。
当没有生物在折叠船上时，第三个命令语能使展开的船只变回木盒。船内无法装入木盒中的物件会在折叠时留在外面，可以装入木盒的物件则会留在盒内。
"""

magic_item_frost_brand = """
# 霜铭 Frost Brand
武器（任意剑），极珍稀（需同调）
当你用此魔法剑命中目标时，目标将受额外 1d6 的冷冻伤害。另外，握持此剑时你对火焰伤害具有抗性。
在严寒环境中，此剑的剑刃会发光，为周围 10 尺范围提供明亮光照，以及其外 10 尺的微光光照。
拔出此剑时，你可以选择让周围 30 尺内的所有非魔法火焰熄灭。该属性可以每小时使用一次。
"""

magic_item_gauntlets_of_ogre_power = """
# 食人魔力量护手 Gauntlets of Ogre Power
奇物，非普通（需同调）
着装该护手时，你的力量值变为 19。如果未着装该护手时你的力量值已经大于或等于 19，则该护手无效。
"""

magic_item_gem_of_brightness = """
# 光彩夺目宝石 Gem of Brightness
奇物，非普通
这块棱形宝石有 50 发充能。持握该宝石时，你可以用一个动作说出宝石的三个命令语之一并造成如下效应：
• 第一个命令语令宝石发出亮光，提供 30 尺的明亮光照和其外 30 尺的微光光照。此效应将持续到你用一个附赠动作再次说出该命令语，或你使用宝石的另一能力为止。这种用法不会消耗充能。
• 第二个命令语消耗 1 发充能，令宝石向 60 尺内你能看见的一个生物发出一道耀眼的光束。该生物必须成功通过一次DC 15 的体质豁免否则目盲 1 分钟。该生物在每次它自己的回合结束时可以再次进行该豁免，成功则目盲状态终止。
• 第三个命令语消耗 5 发充能，令宝石以自身为原点对 30 尺锥状范围放出刺眼的光芒。范围内的每个生物必须成功通过与第二项功能相同作用的豁免。
耗尽充能后，此宝石变为价值 50gp 的普通宝石。
"""

magic_item_gem_of_seeing = """
# 真视宝石 Gem of Seeing
奇物，珍稀（需同调）
这块宝石有 3 发充能。你可以用一个动作说出宝石的命令语并消耗 1 发充能。接下来的 10 分钟内，你在透过宝石观察周围时具有 120 尺的真实视觉。该宝石在每天黎明时恢复1d3 发充能。
"""

magic_item_giant_slayer = """
# 巨人屠杀者 Giant Slayer
武器（任意斧或剑），珍稀
你用此魔法武器发动的攻击检定和伤害掷骰获得+1 加值。
当你以此武器命中巨人 giant 时，它将额外受与武器伤害类型相同的 2d6 点伤害，并且必须成功通过一次 DC 15 的力量豁免否则应击倒地。此处的“巨人”指任何生物类型为巨人的生物，包括双头巨人 ettin 和巨魔 troll 等。
"""

magic_item_glamoured_studded_leather = """
# 幻惑镶钉皮甲 Glamoured Studded Leather
护甲（镶钉皮甲），珍稀
着装该护甲时，你的 AC 获得+1 加值。你可以用一个附赠动作说出该护甲的命令语，使护甲的外观幻化为任何普通衣物或其他种类护甲。护甲的颜色，样式和配件都由你自己决定，但它的体积和重量不会改变。幻化外观的效应持续到你脱掉此护甲或再次改变护甲外观。
"""

magic_item_gloves_of_missile_snaring = """
# 辟矢夺箭手套 Gloves of Missile Snaring
奇物，非普通（需同调）
着装这双手套时，它几乎和你的手融为一体。着装该手套且至少空着一只手时，如果远程武器攻击命中你，则你可以用反应来减少 1d10＋你的敏捷调整值的伤害。如果你把伤害减少到 0，则你可以选择抓住击中你的抛掷物（前提是它的尺寸足够让你用手抓住）。
"""

magic_item_gloves_of_swimming_and_climbing = """
# 运动健将手套 Gloves of Swimming and Climbing
奇物，非普通（需同调）
着装该手套时，攀爬和游泳不会消耗额外移动力。你进行攀爬与游泳相关的力量（运动）检定时获得+5 加值。
"""

magic_item_gloves_of_thievery = """
# 窃贼手套 Gloves of Thievery
奇物，非普通
这双手套着装到手上时是隐形的。着装该手套时，你进行的敏捷（巧手）检定，以及为开锁进行的敏捷检定具有+5 加值。
"""

magic_item_goggles_of_night = """
# 夜视镜 Goggles of Night
奇物，非普通
着装这副暗色护目镜时，你具有 60 尺黑暗视觉。如果你已经有黑暗视觉，则其范围再扩大 60 尺。
"""

magic_item_hammer_of_thunderbolts = """
# 雷神之锤 Hammer of Thunderbolts
武器（巨锤），传说
你用此魔法武器发动的攻击检定和伤害掷骰获得+1 加值。
巨人杀手 Giant’s Bane（需同调）。要同调此物品，你必须同时着装巨人之力腰带 belt of giant strength（任意一种）和食人魔力量护手 gauntlets of orge power。如果你卸下其中任何一件，雷神之锤的同调也将立刻终止。持握该武器且与之同调时，你的力量值提升 4 且可以超过 20 但不能超过 30。
当你用这把武器攻击巨人且投出 20 时，该巨人必须进行一次DC 17 的体质豁免，失败则立即死亡。
雷神之锤有 5 发充能。与它完成同调后，你可以消耗 1发充能并用它发动一次远程武器攻击，此时它将视为常规射程 20 尺，最大射程 60 尺的投掷武器。攻击命中时，锤子将产生 300 尺内都可听清的雷鸣。目标生物和它周围 30 尺内的生物必须成功通过一次 DC 17 的体质豁免，否则被震慑到你的下一回合结束。雷神之锤每天在黎明时恢复 1d4 发用掉的充能。
"""

magic_item_hat_of_disguise = """
# 易容帽 Hat of Disguise
奇物，非普通（需同调）
着装这顶帽子时，你可以用一个动作随意施展易容术disguise，其效应持续至帽子被摘下为止。
"""

magic_item_headband_of_intellect = """
# 智力头带 Headband of Intellect
奇物，非普通（需同调）
着装此头带时，你的智力值变为 19。如果未着装该头带时你的智力值已经大于或等于 19，则此头带无效。
"""

magic_item_helm_of_brilliance = """
# 光辉头盔 Helm of Brilliance
奇物，极珍稀（需同调）
这顶耀眼的头盔上镶嵌着 1d10 颗钻石 diamonds、2d10颗红宝石 rubies、3d10 颗火蛋白石 fire opals 和 4d10 颗蛋白石 opals。从头盔上摘下的宝石将化为尘埃。所有宝石都被摘下或摧毁后，此头盔将失去魔力。
着装这顶头盔时，你获得以下增益：
• 你可以用一个动作并使用一颗相应的宝石施展下列法术之一（豁免 DC 18）：
昼明术 daylight（蛋白石 opal）、火球术fireball（火蛋白石 fire opal）、虹光喷射 prismatic spray（钻石 diamond）、火墙术 wall of fire（红宝石 ruby）。施展法术后宝石被摧毁并消失。
• 只要头盔上还有至少一颗钻石，当周围 30 尺内有不死生物存在时，头盔就会发出 30 尺半径范围的微光光照。在此范围内开始其回合的不死生物将受到 1d6 的光耀伤害。
• 只要头盔上还有至少一颗红宝石，你就对火焰伤害有抗性。
• 只要头盔上还有至少一颗火蛋白石，你就可以用一个动作说出命令语，使你手中的一把武器燃起火焰，并提供 10 尺的明亮光照和额外 10 尺的微光光照。火焰对你和武器本身无害，但当你用该武器命中一次攻击时，受攻击的目标将额外受 1d6 的火焰伤害。火焰将持续到你收起、扔掉武器或用一个附赠动作再次说出该命令语。
着装头盔时，如果你因为对一个法术豁免失败而受到火焰伤害，则骰一次 d20。如果骰值为 1，则头盔上剩余的宝石将迸射出光束。60 尺范围内的每个生物都必须成功通过一次DC 17 的敏捷豁免否则将被光束击中，并受到与头盔上剩余宝石数量相等的光耀伤害。此后光辉头盔和所有宝石都被摧毁。
"""

magic_item_helm_of_comprehending_languages = """
# 通晓语言头盔 Helm of Comprehending Languages
奇物，非普通
着装这顶头盔时，你可以用一个动作随意施展通晓语言comprehend language。
"""

magic_item_helm_of_telepathy = """
# 心灵感应头盔 Helm of Telepathy
奇物，非普通（需同调）
着装这顶头盔时，你可以用一个动作施展侦测思想 detectthoughts（豁免 DC 13）。保持法术专注期间，你可以用一个附赠动作向你聚焦的生物发送心灵通信。只要你依然聚焦于该生物，则它也可以用一个附赠动作回复你的信息。
使用侦测思想 detect thoughts 并聚焦于某生物期间，你还可以用一个动作对该生物施展暗示术 suggestion（豁免 DC13）。此后直到次日黎明前，其暗示术属性都无法再次启动。
"""

magic_item_helm_of_teleportation = """
# 传送头盔 Helm of Teleportation
奇物，珍稀（需同调）
这顶头盔有 3 发充能。着装这顶头盔时，你可以用一个动作并消耗 1 发充能施展传送术 teleport。每天黎明时头盔将恢复 1d3 发已消耗的充能。
"""

magic_item_heward_s_handy_haversack = """
# 霍华德的便利袋 Heward's Handy Haversack
奇物，珍稀
这个背包有三个袋子：中间一个侧面两个。每个袋都是一个异次元空间。每个侧袋可以容纳重量不超过 20 磅，体积不超过 2 立方尺的物体。中间的大袋则可以容纳重量不超过 80磅，体积不超过 8 立方尺的物质。无论装了多少东西，背包总是重 5 磅。
向背包内放物件时使用与物体互动的规则。从背包内取出物品时需要一个动作。当你在背包里寻找某件特定物品时，该物品会被魔法放到最上面。
使用背包时有一些需要注意的事项。如果背包里装的东西超过了容量，或是背包被戳破、撕裂，则它被毁灭。背包毁灭时它所装载的东西将永远消失，但神器总会被送到其他什么地方。如果背包被内外翻转，它所装载的东西也将安全的掉落出来，但再次使用背包之前必须将它恢复原状。一名需要呼吸的生物被装入背包后，在开始窒息前还可以存活 10 分钟。
将该便利袋放入次元袋 bag of holding、次元洞 portablehole 或其他类似物品时，其产生的异次元空间将立即摧毁这两件物品并打开一扇通往星界的门扉。门产生在被放入另一件物品的前一物件所在的空间位置。任何在该门周围 10 尺内的生物将被吸入门内并送到星界位面的随机位置，随后该门关闭。这扇门只能单向通过且不能被再次打开。
"""

magic_item_holy_avenger = """
# 神圣复仇者 Holy Avenger
武器（任意剑），传说（需圣武士同调）
你用此魔法武器发动的攻击检定和伤害掷骰获得+3 加值。
当你用此剑命中邪魔或不死生物时，该生物将受额外 2d10 的光耀伤害。
持握此剑时，它在你周围产生 10 尺半径的灵光。你和灵光范围内其他友方生物为对抗法术和其他魔法效应而作的豁免检定具有优势。如果你的圣武士等级达到或超过 17 级，则灵光的半径增加到 30 尺。
"""

magic_item_horn_of_blinging = """
# 音爆号角 Horn of Blasting
奇物，珍稀
你可以用一个动作说出号角的命令语然后吹响号角。号角将产生 30 尺锥状范围的音爆，其声音可传播远达 600 尺。
锥状范围内的每个生物必须进行一次 DC 15 的体质豁免。豁免失败的生物将受 5d6 的雷鸣伤害并耳聋 1 分钟，成功则伤害减半且不会耳聋。由玻璃或晶体构成的生物或物件进行该豁免时具有劣势，且会受到 10d6 而非 5d6 的伤害。每次使用号角的效应都有 20%的概率导致它爆炸，号角也将因此被摧毁且对吹响它的人造成 10d6 的火焰伤害。
"""

magic_item_horn_of_valhalla = """
# 瓦尔哈拉号角 Horn of Valhalla
奇物，珍稀（白银或黄铜）、极珍稀（青铜）、传说（黑铁）
你可以用一个动作吹响号角。作为回应，约瑟园 Ysgard的战士英灵们将在你周围 60 尺内出现。这些英灵使用《怪物图鉴》上狂战士 berserker 的资料。生命值降至 0，或者 1 小时之后英灵们将返回约瑟园。使用后，号角需要经过 7 日才能再次启动。
已知共有四种类型的瓦尔哈拉号角，分别由不同的金属制成。号角的类型决定了使用它的前提条件，以及回应你呼唤的狂战士数量。号角的类型由 DM 决定或随机决定。
如果你在不满足前提条件的情况下吹响了号角，则召唤出的英灵们将对你发动攻击。如果你满足前提条件，他们将对你和你的同伴态度友善，并听从你的命令。

# d-100
d100 号角类型 狂战士数量 前提条件
01~40 ⽩银 Silver 2d4+2 无
41~75 ⻩铜 Brass 3d4+3 所有简易武器熟练项
76~90 ⻘铜 Bronze 4d4+4 所有中型护甲熟练项
91~00 ⿊铁 Iron 5d4+5 所有军用武器熟练项
"""

magic_item_horseshoes_of_a_zephyr = """
# 西风马蹄铁 Horseshoes of a Zephyr
奇物，极珍稀
这些马蹄铁四个为一套。当一匹马或类似的生物同时着装四个马蹄铁时，它将悬浮在离地面 4 尺的高度，并如同在平地上一样移动。这使得该生物可以穿过或站在非固体或非稳定的平面上，例如水或岩浆。它无视困难地形并且不会留下足迹。另外，它也可以以正常速度连续移动 12 小时而不会因为强行军 dorced march 而疲乏。
"""

magic_item_horseshoes_of_speed = """
# 加速马蹄铁 Horseshoes of Speed
奇物，珍稀
这些马蹄铁四个为一套。当一匹马或类似的生物同时着装四个马蹄铁时，它的步行速度将增加 30 尺。
"""

magic_item_immovable_rod = """
# 不动权杖 Immovable Rod
权杖，非普通
这根铁制权杖的一端设有一按钮。如果你用一个动作按下按钮，权杖的魔法将把它固定在原地。权杖将保持不动（即使这违反重力）直到你或另一名生物用一个动作再次按下按钮。权杖最多能负载 8,000 磅的重量，超过则权杖的效应自动关闭并掉落。任一生物可以用一个动作进行一次 DC 30 的力量检定，成功则可以将权杖移动至多 10 尺。
"""

magic_item_instrument_of_the_bards = """
# 吟游诗人乐器 Instrument of the Bards
奇物，多种稀有度（需吟游诗人同调）
吟游诗人乐器是乐器中的精品，在各方面都优于普通乐器。这类乐器共有七种，每种都以一个传奇吟游诗人学院的名字命名。下表列出了每种乐器的稀有度、乐器间共通的法术以及每种乐器独有的法术。未与一件吟游诗人乐器同调的生物在尝试弹奏它时必须成功通过一次 DC 15 的感知豁免否则将受 2d4 的心灵伤害。
你可以用一个动作演奏乐器并施展它的一个法术。一旦乐器被用来施展了某一法术，直到次日黎明前它都无法再被用来施展该法术。用乐器施展的法术使用你的法术豁免 DC 和施法关键属性。
当你用乐器施展目标豁免失败则陷入魅惑的法术时，该目标的豁免具有劣势。你使用乐器施展的法术和以乐器为法器施展的法术都可以享受这个效果。

# table
乐器 稀有度 法术
全部 — 飞行术 fly,隐形术 invisibility,浮空术 levitate,防护善恶 protection from evil and good 外加下表中的相应法术
安斯翠瑟竖琴 Anstruth harp 极珍稀 操控天气 control weather,疗伤术 cure wounds (5 环), 荆棘之墙 wall of thorns
藤蔓曼陀林 Canaith mandolin 珍稀 疗伤术 cure wounds (3 环),解除魔法 dispel magic,防护能量 protection from energy (仅闪电)
聆听者七弦琴 Cli lyre 珍稀 塑石术 stone shape, 火墙术 wall of fire, 风墙术 wind wall
安眠鲁特琴 Doss lute 非普通 化兽为友 animal friendship,防护能量 protection from energy (仅火焰), 防护毒素 protection from poison
佛克路坎三弦琴 Fochlucan bandore 非普通 纠缠术 entangle,妖火 faerie fire,橡棍术 shillelagh, 动物交谈 speak with animals 
麦克-弗瑞米西特琴 Mac-Fuimidh cittern 非普通 树肤术 barkskin, 疗伤术 cure wounds, 云雾术 fog cloud
奥莱姆竖琴 Oiiamh harp 传说 困惑术 confusion,操控天气 control weather,火焰风暴 fire storm
"""

magic_item_ioun_stone = """
# 艾恩石 Ioun Stone
奇物，多种稀有度（需同调）
艾恩 Ioun 在许多世界被尊为知识和预言之神，而其名字则被用来命名这种石头。
艾恩石 有许多种，每一种都有与众不同的形状和颜色。
如果你用一个动作将一块艾恩石抛到空中，则它将环绕你的头部，与你的头部距离 1d3 尺移动，并为你带来一些增益。另一名生物必须用一个动作抓住或用网网住艾恩石，才能将它与你分开。上述方法需要成功通过一次对抗 AC 24 的攻击检定，或一次对抗 DC 24 的敏捷（体操）检定。你自己则可以用一个动作抓住并收起石头，终止它的效应。
每颗石头拥有 AC 24，生命值为 10，具有所有伤害类型的抗性。即使只是环绕你的头部移动，它依然视为由你着装。
吸收 Absorption（极珍稀）。该淡紫色椭圆艾恩石环绕着你时，你可以用你的反应使一个法术无效，该法术必须由你能看到的生物所施展，只以你为目标且不超过 4 环。
吸收合计 20 环的法术后，此艾恩石将耗尽力量，并失去其魔法而变为暗灰色。如果一个法术的环阶超出该艾恩石剩余的吸收环数，则石头无法将其吸收。
机敏 Agility（极珍稀）。该深红色球形艾恩石环绕你时，你的敏捷属性提升 2，但无法超过 20。
警觉 Awareness（珍稀）。该深蓝色菱形艾恩石环绕你时，你不会被突袭。
坚韧 Fortitude（极珍稀）。该粉色菱形艾恩石环绕你时，你的体质属性提升 2，但无法超过 20。
高等吸收 Greater Absorption（传说）：该淡紫色和绿色相间大理石纹彩的椭圆艾恩石环绕你时，你可以用你的反应使一个法术无效，该法术必须由你能看到的生物施展，只以你为目标且不超过 8 环。
吸收合计 50 环的法术后，此艾恩石将耗尽力量，失去魔法并变为暗灰色。如果一个法术的环阶超出了此艾恩石剩余的吸收环数，则石头无法将其吸收。
洞悉 Insight（极珍稀）。该荧蓝球形艾恩石环绕你时，你的感知属性提升 2，但无法超过 20。
才智 Intellect（极珍稀）。该绯红和蓝色相间大理石纹彩的球形艾恩石环绕着你时，你的智力属性提升 2，但无法超过20。统御 Leadership（极珍稀）。该粉色和绿色相间大理石纹彩的球形艾恩石环绕你时，你的魅力属性提升 2，但无法超过20。精通 Mastery（传说）。该淡绿色棱晶艾恩石环绕你时，你的熟练加值增加 1。
防护 Protection（珍稀）。该灰玫瑰色棱晶艾恩石环绕你时，你的 AC 获得+1 加值。再生 Regeneration（传说）。该珍珠白纺锤形艾恩石环绕你时，在每经过一小时只要你尚有 1 点生命值，就可以恢复15 点生命值。储法 Reserve（珍稀）。你可以向这个亮紫色棱晶艾恩石施展法术，随后该法术将被保存到你决定使用它们时。它同时只能储存共计不超过 3 环的法术。新发现的储法艾恩石中储存着由 DM 选定的 1d4-1 环法术。
任何生物都可以在施展一个 1 环到 3 环的法术时触碰该艾恩石以将该法术储存在石头中。此时法术将被储存，而非直接产生效应。如果石头无法储存该法术，则它不生效且被消耗。
被储存的法术以其所耗用的法术位环阶来决定其在石头中占用的空间。
该艾恩石环绕你时，你可以施展任何储存在其中的法术。
该法术使用原施法者的法术位、法术豁免 DC、法术攻击加值和施法关键属性，但其他方面则视为由你施展。法术施展后，它将从艾恩石内消失，并清空其占用的空间。
力量 Strength（极珍稀）。该浅蓝色菱形艾恩石环绕你时，你的力量属性提升 2，但无法超过 20。
维生 Sustenance（珍稀）。该透明的纺锤形艾恩石环绕你时，你无需饮食也能生存。
"""

magic_item_iron_bands_of_bilarro = """
# 比拉罗的铁索 Iron Bands of Bilarro
奇物，稀有
这个锈迹斑斑的铁球重 1 磅，直径 3 寸。你可以用一个动作说出命令语并把铁球扔向一个 60 尺内你能看到的巨型或更小体型生物。球在空中飞行时会张开成为一张铁网。
用你的敏捷调整值加上熟练加值进行一次远程攻击检定。
如果攻击命中，则目标被束缚，直到你用一个附赠动作再次说出命令语释放它。如果你决定释放目标，或是攻击检定没能命中，那么铁网将重新变回铁球。
任一生物（包括被束缚的生物）都可以尝试用一个动作进行 DC 20 的力量检定以试图破网而出。一旦检定成功，铁索即被破坏，被束缚的生物亦重获自由。如果检定失败，则该生物在接下来 24 小时中再次尝试破网时总会直接失败。
铁索使用后，直到次日黎明前都无法再次启动。
"""

magic_item_iron_flask = """
# 收妖瓶 Iron Flask
奇物，传说
这是一个带黄铜瓶塞的铁瓶。你可以选择一个 60 尺内你能看见的生物作为目标，并用一个动作说出瓶子的命令语。如果目标并非你所处位面的生物，则它必须成功通过一次 DC 17的感知豁免否则将被困入瓶中。如果目标曾经被瓶子囚禁过，则它进行的豁免具有优势。一旦被瓶子吸入，该生物将被困在瓶中直到被释放。收妖瓶最多只能同时容纳一名生物。被困在瓶中的生物无需呼吸和饮食，也不会衰老。
你可以用一个动作拔掉瓶塞释放瓶中的生物。该生物将在 1 小时内对你和你的同伴态度友善并服从你的命令。如果你没有下达命令或你的命令可能导致该生物死亡，则它会保护自己且不执行任何动作。持续时间结束后，该生物将按自己的意愿和阵营行动。
鉴定术 identify 可以辨别瓶中是囚禁有生物，但只有打开瓶塞才能确定其中的生物具体是什么。一个新发现的收妖瓶可能已经囚禁了一名由 DM 决定或随机决定的生物。

# d-100
D100 瓶中生物
01~50 无
51 奥登罗斯魔 Arcanaloth
52 魔裔 Cambion
53~54 土巨灵 Dao
55~57 恶魔（类型 1）
58~60 恶魔（类型 2）
61~62 恶魔（类型 3）
63~64 恶魔（类型 4）
65 恶魔（类型 5）
66 恶魔（类型 6）
67 梵天神侍 Deva
68~69 魔鬼（高等）
70~72 魔鬼（次等）
73~74 气巨灵 Djinni
75~76 火巨灵 Efreeti
77~78 元素 Elemental（任意）
79 吉斯扬基骑士 Githyanki knight
80 吉斯扬基泽斯修士 Githyanki zerth
81~82 隐形追猎者 Invisible stalker
83~84 水巨灵 Marid
85~86 麦泽罗斯魔 Mezzoloth
87~88 夜鬼婆 Night hag
89~90 尼卡罗斯魔 Nycaloth
91 异界神使 Planetar
92~93 火蜥蜴 Salamander
94~95 史拉蟾 Slaad（任意）
96 炽天神使 Solar
97~98 魅魔 succubus／梦魔 incubus
99 乌特罗斯魔 Ultroloth
00 索尔石怪 Xorn
"""

magic_item_javelin_of_lighting = """
# 闪电标枪 Javelin of Lighting
武器（标枪），非普通
这把标枪是魔法武器。当你投掷它并说出命令语时，它将转变为一道 5 尺宽的闪电束，向 120 尺内的某个目标飞去。
闪电经过的直线上除你和目标之外的每个生物必须进行一次DC 13 的敏捷豁免，失败则受 4d6 的闪电伤害，成功则伤害减半。闪电束到达目标时变回标枪并对目标发动一次远程攻击。如果攻击命中，则目标将受标枪的伤害外加 4d6 的闪电伤害。
标枪的这个属性直到次日黎明前都无法再次启动，但你仍然可以把它当做普通魔法武器使用。
"""

magic_item_keoghtoms_ointment = """
# 卡夫统灵药 Keoghtom's Ointment
奇物，非普通
这个直径 3 寸的玻璃瓶中装着 1d4+1 剂闻起来隐约有芦荟气味的混合剂。瓶子和混合剂共重 1/2 磅。
用一个动作可以吞下或外敷一剂软膏。软膏将为使用它的生物恢复 2d8+2 的生命值，并解除毒素和治愈任何疾病。
"""

magic_item_lantern_of_revealing = """
# 显像提灯 Lantern of Revealing
奇物，非普通
这盏带罩提灯点燃时提供 30 尺的明亮光照和其外 30 尺的微光光照。1 品脱油可以供提灯燃烧 6 小时。处于提灯明亮光照范围内的隐形生物或物件将被其显形。你可以用一个动作降下灯罩，让提灯仅在 5 尺内提供微光光照。
"""

magic_item_luck_blade = """
# 吉兆之刃 Luck Blade
武器（任意剑），传说（需同调）
你用该魔法武器发动的攻击检定和伤害掷骰获得+1 加值。
只要带着这把剑，你进行豁免时还获得+1 加值。
幸运 Luck。只要带着这把剑，它就会为你带来好运，使你可以重骰一次攻击检定、属性检定或豁免检定（无需动作）。
而你必须接受重投后的结果。此后直到次日黎明前，该属性都无法再次启动。
许愿 Wish。这把剑有 1d4-1 发充能。持握它时，你可以用一个动作并消耗一发充能施展许愿术 wish。此后直到次日黎明前，该属性都无法再次启动。充能耗尽后，吉兆之刃也将失去这项属性。
"""

magic_item_mace_of_disruption = """
# 瓦解之锤 Mace of Disruption
武器（硬头锤），珍稀（需同调）
当你用这把魔法武器命中一名邪魔或不死生物时，该目标将额外受 2d6 的光耀伤害。受此伤害后该生物的生命如果小于等于 25，则它必须成功通过一次 DC 15 的感知豁免否则被摧毁。如果豁免成功，则直到你的下一回合结束，该生物对你恐慌。
你握持此武器时，它将向 20 尺范围散发出明亮光照以及其外 20 尺的微光光照。
"""

magic_item_mace_of_smiting = """
# 打击之锤 Mace of Smiting
武器（硬头锤），珍稀
你在用此魔法武器发动的攻击检定和伤害掷骰获得+1 加值。如果你使用此武器攻击构装体，则加值变为+3。
当你使用这把武器攻击并投出 20 时，目标将额外受 7 点钝击伤害。如果目标是构装体，则额外伤害为 14。如果受到此伤害后该构装体的生命值小于等于 25，则目标被摧毁。
"""

magic_item_mace_of_terror = """
# 恐惧之锤 Mace of Terror
武器（硬头槌），珍稀（需同调）
这把魔法武器有 3 发充能。持握它时，你可以用一个动作并消耗一发充能来释放一股恐惧波动。你周围 30 尺半径内每个被你指定的生物必须成功通过一次 DC 15 的感知豁免否则对你恐慌 1 分钟。受该恐慌影响的生物必须在自己的回合尽全力向远离你的方向移动，且无法主动进入你周围 30 尺范围内也无法执行反应。它的只能选择疾走 Dash 动作或是试图脱离阻止它移动的效果。如果无处可逃，则它可以使用闪避Dodge 动作。每个该生物的回合结束时，它都可以再次进行该豁免，成功则终止其自己身上的该效应。
每天黎明时恐惧之锤将恢复 1d3 发充能。
"""

magic_item_mantle_of_spell_resistance = """
# 法术抗性斗篷 Mantle of Spell Resistance
奇物，珍稀（需同调）
穿着这件斗篷时，你对法术的豁免具有优势。
"""

magic_item_manual_of_bodily_health = """
# 强身手册 Manual of Bodily Health
奇物，极珍稀
这本手册记载了保健与饮食的秘诀，其文字蕴含魔力。如果你在 6 日或更少的时间内花费 48 小时研读这本书并实践其中的方针，你的体质属性和体质属性上限均增加 2。之后这本手册将失去魔力，直到一个世纪后才能恢复。
"""

magic_item_manual_of_gainful_exercise = """
# 健体手册 Manual of Gainful Exercise
奇物，极珍稀
这本手册记载了健身与运动的秘诀，其文字蕴含魔力。如果你在 6 日或更少的时间内花费 48 小时研读这本书并实践其中的方针，你的力量属性和力量属性上限均增加 2。之后这本手册失去魔力，直到一个世纪后才能恢复。
"""

magic_item_manual_of_golems = """
# 魔像手册 Manual of Golems
奇物，极珍稀
这本手册记载了制造某种魔像所必须的知识和符咒，魔像的类型由 DM 选择或随机决定。只有拥有至少 2 个 5 环法术位的施法者才能解读并使用这本书。无法解读这本书的生物在阅读它时将受到 6d6 的心灵伤害。
制造魔像时，你需要花费表格中所标注的时间，每天休息不超过 8 小时。工作时你必须把魔像手册放在手边随时参考，并且不能受到打扰。此外，你还要付出表格中标注的金钱用以购买材料。
魔像完工后，魔像手册将被魔焰吞噬。当你把手册的灰烬洒在魔像上时，它将获得生命。它服从你的控制，理解并听从你的口头命令。魔像的资料见《怪物图鉴》。

# d-20
d20 魔像 时间 花费
1~5 粘土魔像 30 日 65,000 金币
6~17 肉身魔像 60 日 50,000 金币
18 钢铁魔像 120 日 100,000 金币
19~20 石魔像 90 日 80,000 金币
"""

magic_item_manual_of_quickness_of_action = """
# 灵巧手册 Manual of Quickness of Action
奇物，极珍稀
这本手册记载了平衡与协调的秘诀，其文字蕴含魔力。如果你在 6 日或更少的时间内花费 48 小时研读这本书并实践其中的方针，你的敏捷属性和敏捷属性上限均提升 2。之后这本手册失去魔力，直到一个世纪后才能恢复。
"""

magic_item_mariner_s_armor = """
# 水手护甲 Mariner's Armor
护甲（轻型，中型或重型），非普通
着装该护甲时，你获得等同于你步行速度的游泳速度。另外，当你在水下以 0 生命值开始你的回合时，护甲将使你向水面上升 60 尺。护甲表面带着鱼贝的纹饰。
"""

magic_item_medallion_of_thoughts = """
# 读心勋章 Medallion of Thoughts
奇物，非普通（需同调）
这枚勋章有 3 发充能。着装勋章时，你可以用一个动作并消耗 1 发充能使用侦测思想 detect thoughts（DC 13）。勋章每天黎明时恢复 1d3 发充能。
"""

magic_item_mirror_of_life_trapping = """
# 摄心镜 Mirror of Life Trapping
奇物，极珍稀
以非直接的方式看向这面镜子时，其中映着生物模糊的影像。镜子重 50 磅，拥有 AC11，生命值为 10，钝击易伤。
生命值降至 0 时，镜子将粉碎并被摧毁。
镜子被挂在垂直平面上时，你可以在 5 尺内用一个动作说出命令语激活它。它将一直保持激活状态直到你再次用一个动作说出该命令语。
除你之外，任何在一面激活的摄心镜 周围 30 尺内从镜中看到自己影像的生物必须成功通过一次 DC 15 的魅力豁免，否则会连同其着装或携带的东西一起被困入镜中的十二个异次元空间之一。如果该生物了解镜子的本质，则它进行的豁免具有优势。构装生物进行该豁免时直接成功。
异次元空间中充满了浓雾，能见度只有 10 尺。被囚禁的生物不会衰老，也无需饮食和睡眠。使用位面旅行魔法可以逃脱该空间，但除此之外被囚禁的生物只能等待被释放。
如果镜子的十二个异次元空间已被占满而镜子又困住了新的生物，则它将随机释放一名之前被囚禁的生物以容纳新囚犯。被释放的生物在镜子前未被占据的空间背对镜子出现。
如果镜子被打碎，它囚禁的生物将全部被释放，出现在它周围未被占据的空间里。
你可以在镜子周边 5 尺内用一个动作说出一名被囚禁生物的名字或是一个异次元空间的号码。该生物或是被囚禁于该号码空间里的生物的影像将出现在镜子里，使你得以和该生物进行正常交流。
以类似的方式，你可以用一个动作说出另一个命令语以释放一名被囚禁的生物。被释放的生物连带其所有物将背对镜子出现在离镜子最近的未被占据的空间里。
"""

magic_item_mithral_armor = """
# 秘银甲 Mithral Armor
护甲（中型或重型，非兽皮甲），非普通
秘银是一种轻盈柔韧的金属。秘银链甲衫或胸甲可以穿在普通衣物下面。一些护甲会使着装者的敏捷（隐匿）检定具有劣势，或是对穿着者的力量属性有要求，但它的秘银版本则没有这些特性。
"""

magic_item_necklace_of_adaptation = """
# 适应项链 Necklace of Adaptation
奇物，非普通（需同调）
卓专该项链时，你可以在任何环境中正常呼吸，并且其对抗有害气体（如死云术 cloudkill、臭云术 stinking cloud、吸入式毒药和某些龙的吐息武器）时进行的豁免具有优势。
"""

magic_item_necklace_of_fireballs = """
# 火球项链 Necklace of Fireballs
奇物，珍稀
这条项链上挂着 1d6+3 颗珠子。你可以用一个动作取下一颗珠子并投掷到至多 60 尺远的地方。它将在移动轨迹的终点爆炸，效果等同于 3 环的火球术 fireball（豁免 DC 15）。
你可以一次投掷多个珠子甚至整条项链。同时投掷的珠子数量每增加 1，火球术的环阶也增加 1。
"""

magic_item_necklace_of_prayer_beads = """
# 念珠项链 Necklace of Prayer Beads
奇物，珍稀（需牧师、德鲁伊或圣武士同调）
这条项链上挂着蓝晶 aquamarine、黑珍珠 black pearl 以及黄玉 topaz 制成的 1d4+2 颗魔法珠子。另外也有许多非魔法的珠子挂在项链上，例如琥珀 amber、血石 bloodstone、黄水晶 citrine、珊瑚 coral、翡翠 jade、珍珠 pearl 和石英 quartz。
如果从项链上把魔法珠摘下，则相应的枚珠子将失去魔力。
项链上共有六种魔法珠子。随机或由 DM 决定一条项链上每颗珠子的类型，同类型的珠子可能出现在一条项链上。要使用珠子，你必须佩带此项链。
每枚珠子保存着一个法术。使用一枚珠子中的法术将作为一项附赠动作（如果珠子中保存的法术允许豁免，则使用你的法术豁免 DC）。一旦你使用了某枚珠子中的法术，则相应珠子的法术直到次日黎明前都无法再次使用。

# d-20
d20 珠子类型 法术
1~6 祝福 祝福术 Bless
7~12 疗愈 疗伤术 Cure wound (2 环) 或 次级复原术 lesser restoration
13~16 恩赐 高等复原术 Greater restoration
17~18 打击 印记斩 Branding smite
19 召唤 异界盟友 Planar ally
20 风行 御风而行 Wind walk
"""

magic_item_nine_lives_stealer = """
# 九转夺命剑 Nine Lives Stealer
武器（任意剑），极珍稀（需同调）
你用此魔法武器发动的攻击检定和伤害掷骰获得+2 加值。
九转夺命剑有 1d8+1 发充能。当你用此剑对一名生命值不足 100 的生物造成重击时，它必须成功通过一次 DC 15 的体质豁免否则立刻因生命力被剑吸干而死（不死生物和构装生物免疫）。如果该生物因此被杀，剑将消耗 1 发充能。用尽充能后，剑将失去该属性。
"""

magic_item_nolzur_s_marvelous_pigments = """
# 诺泽尔的惊奇颜料 Nolzur's Marvelous Pigments
奇物, 极珍稀
这种颜料通常 1d4 罐一组和画笔一起装在精美的木盒里（共重 1 磅）。它可以把你在二维平面上画出的东西变为三维实体。当你用心画下图案时，它将从笔尖跃动而出，形成你想要的形状。
每一罐颜料可以涂满 1000 平方尺的面积，创造出至多10000 立方尺的无生命物件或地形特征（比如一扇门、一个坑、鲜花、大树、小房间、大房间或是武器）。每绘制 100 平方尺需要花费 10 分钟。
你绘制完成的物件或地形将变为真实的非魔法物件。因此，画在墙上的门可以正常打开并通过，画在地上的坑也会变成真正的坑，其内部区域计入你创造的物件总体积。
颜料不能创造出比 25 金币更贵重的东西。如果你试图制造更贵重的东西（例如钻石或金块），产生的物件仅仅看上去像是真的，但仔细检查就会发现它是由浆糊、骨头或其他不值钱的材料拼成。
如果你画出某种形式的能量（例如火焰或闪电），则该能量在你完成绘制的一瞬间就会消散，不会造成任何伤害。
"""

magic_item_oathbow = """
# 誓仇弓 Oathbow
武器（长弓），极珍稀（需同调）
当你弯弓搭箭时，誓仇弓会用精灵语悄声念出“速歼敌”。
当你用此武器发动远程攻击时，你可以说出命令“负我者死”，而这次攻击的目标将成为你的仇敌，直到它死亡或直到七日后的黎明之时。你同时只能指明一名这样的仇敌。仇敌死后，你可以在次日黎明后重新选择仇敌。
使用此弓对仇敌发动远程攻击时，你的攻击检定具有优势。另外，目标不会从非全身掩护的掩护状态中受益，你也不会因为超出常规射程而承受劣势。如果攻击命中，你的仇敌将额外受 3d6 的穿刺伤害。
只要你的仇敌还活着，你使用其他武器发动的攻击检定将承受劣势。
"""

magic_item_oil_of_etherealness = """
# 以太化之油 Oil of Etherealness
魔药，珍稀
这种浑浊的灰色油膏在容器外会变成珠状并迅速蒸发。
一瓶油膏可以涂抹一个中型或更小体型的生物及其着装和携带的装备上。生物的体型每比中型大一级就需要多使用一瓶。
使用以太化之油耗时 10 分钟，此后受油膏影响的生物将获得法术以太化 etheralness 的效应，并持续 1 小时。
"""

magic_item_oil_of_sharpness = """
# 锐锋之油 Oil of Sharpness
魔药，极珍稀
这种透明的胶状油膏中掺杂着极纤细的银色碎片。它可以涂抹于一把挥砍或穿刺武器，或是 5 发造成挥砍或穿刺伤害的弹药上。使用锐锋之油耗时 1 分钟，此后受油膏影响的武器或弹药所发动的攻击检定和伤害掷骰获得+3 加值。
"""

magic_item_oil_of_slipperiness = """
# 滑溜之油 Oil of Slipperiness
魔药，非普通
这种粘稠的黑色油膏装在容器中时看起来十分浓重，但倒出来时却可以迅速流动。油膏可以涂抹于一个中型或更小体型的生物及其着装和携带的装备上。生物的体型每比中型大一级就需要多使用一瓶。使用滑溜之油耗时 10 分钟，此后受油膏影响的生物获得自由行动 freedom of movement 的效应，并持续 8 小时。
你也可以用一个动作把这瓶油膏泼在 10 平方尺的地面上。该区域将如同被施展了法术油腻术 grease，并持续 8 小时。
"""

magic_item_pegasus_boost = """
# 法力再生珍珠 Pearl of Power
奇物，非普通（需施法者同调）
该珍珠在你身上时，你可以用一个动作说出珍珠的命令语以恢复一个已消耗的法术位。如果已消耗的法术位为 4 环或更高环阶，则所恢复的法术位为 3 环。使用后直到次日黎明前，珍珠都无法再次启动。
"""

magic_item_periapt_of_health = """
# 保健护符 Periapt of Health
奇物，非普通
着装此护符时，你免疫所有疾病。如果你在此前已经感染了疾病，则疾病的效应在你着装此护符期间被压制。
"""

magic_item_periapt_of_proof_against_poison = """
# 辟毒护符 Periapt of Proof Against Poison
奇物，珍稀
这条精巧的银链上挂着一颗切割闪亮的黑宝石吊坠。着装它时，毒素无法影响你。你免疫中毒状态和毒素伤害。
"""

magic_item_periapt_of_wound_closure = """
# 愈合护符 Periapt of Wound Closure
奇物，非普通（需同调）
着装此护符时，如果你在自己的回合开始时处于濒死状态，则你将直接转为伤势稳定。此外，你掷生命骰恢复生命值时，其恢复的数值加倍。
"""

magic_item_philter_of_love = """
# 迷情媚药 Philter of Love
魔药，非普通
饮用此药水后 10 分钟内，你将被你看见的第一名生物魅惑。魅惑效应持续 1 小时。如果该生物的物种和性别符合你的取向，被魅惑期间你将把它视为自己的真爱。不仔细观察的话，很难发现这种漂浮着气泡的玫瑰色液体中有一个气泡是心形的。
"""

magic_item_pipes_of_haunting = """
# 颤栗乐笙 Pipes of Haunting
奇物，非普通
你必须拥有乐器的熟练项才能使用该乐笙。该乐笙有 3发充能。你可以用一个动作吹奏它并消耗 1 发充能，以发出一阵含有魔法的怪异音调。你周围 30 尺内的每名生物都必须成功通过一次 DC 15 的感知豁免否则对你恐慌 1 分钟。你可以选择让范围内所有对你没有敌意的生物豁免自动成功。豁免失败的生物可以在每次它的回合结束时再次进行该豁免，成功则终止其自己身上的恐慌效应。豁免成功的生物在 24 小时内免疫该乐笙的效应。该乐笙在每天黎明时恢复 1d3 发充能。
"""

magic_item_pipes_of_the_sewers = """
# 唤鼠乐笙 Pipes of the Sewers
奇物，非普通（需同调）
你必须拥有乐器的熟练项才能使用该乐笙。与唤鼠乐笙同调时，普通老鼠和巨鼠对你的态度变为冷漠。除非你威胁或伤害它们，否则它们不会主动攻击你。
唤鼠乐笙有 3 发充能。你可以用一个动作吹奏它，然后用一个附赠动作消耗 1 到 3 发充能。如果你周围半里内有足够可供召唤的老鼠（由 DM 决定），那么每消耗 1 发充能就能召唤 1 个鼠群 swarm of rats（资料见《怪物图鉴》）。如果范围内老鼠的数量不足以形成集群，则该次充能被耗用。被召唤的集群以最短路线靠近唤鼠乐笙被吹响的地方，但并不受你控制。唤鼠乐笙在每天黎明时恢复 1d3 发充能。
吹奏唤鼠乐笙时，你可以对你周围 30 尺内一个未被他人控制的鼠群进行魅力检定，对抗集群的感知检定。如果你在对抗中落败，则集群会按通常的行为模式行动，并且在 24 小时内不会再被唤鼠乐笙影响。如果你在对抗中获胜，那么集群会被乐笙的音乐控制。你在每个自己的回合以一个动作吹奏唤鼠乐笙期间，该鼠群对你和你的同伴态度友善。你没下达命令时，它会尽力保护自己，但不会执行其他动作。如果一个友善的鼠群在其自己的回合开始时无法听到唤鼠乐笙的声音，则该集群会按通常的行动模式行动，并且在 24 小时内不再被乐笙的音乐影响。
"""

magic_item_plate_armor_of_etherealness = """
# 以太化板甲 Plate Armor of Etherealness
护甲（板甲），传说（需同调）
着装该护甲时，你可以用一个动作说出命令语以获得法术以太化 etherealness 的效应，并持续 10 分钟，或直到你用一个动作再次说出命令语，亦或持续至你脱下此护甲。此后直到次日黎明前，该属性都无法再次启动。
"""

magic_item_portable_hole = """
# 次元洞 Portable Hole
奇物，珍稀
这块丝绸般顺滑的黑色布料展开时为直径 6 寸的圆形，也可以被折叠成手帕大小。
你可以用一个动作展开次元洞并把它放在某个坚实的表面上。次元洞随即打开一个 10 尺深的异次元孔洞。次元洞内的圆柱形空间存在于异位面，因此不能被用来打开通道。次元洞打开时，其内部的生物可以攀爬而出。
你可以用一个动作抓住布料的边缘把它折叠起来以关闭次元洞。次元洞关闭后，任何留在其内部的生物和物件仍留存在异次元空间中。无论内部装了什么，次元洞的重量都可以忽略不计。
次元洞关闭后，洞中的生物可以用一个动作进行 DC 10的力量检定。如果检定成功，则该生物从洞中钻出，出现在次元洞或携带它的人周围 5 尺内某处。在关闭的次元洞中，一名需要呼吸的生物在开始窒息之前可以存活 10 分钟。
将次元洞放入次元袋 bag of holding、霍华德的便利袋Heward’s handy haversack 或其他类似物品产生的异次元空间时，将立即摧毁这两件物品并打开一扇通往星界之门。门产生在被放入另一件物品的前一物件所在的空间位置。任何在该门周围 10 尺内的生物将被吸入门内并送到星界位面的随机位置，随后该门关闭。这扇门只能单向通过且不能被再次打开。
"""

magic_item_potion_of_animal_friendship = """
# 化兽为友药水 Potion of Animal Friendship
魔药，非普通
饮用此药水后 1 小时，你可以任意施展化兽为友 animal friendship（DC 13）。搅动这种浑浊的液体可以看到一些残渣：
鱼鳞、蜂鸟的舌头、猫爪或松鼠毛。
"""

magic_item_potion_of_clairvoyance = """
# 鹰眼术药水 Potion of Clairvoyance
魔药，珍稀
饮用此药水后，你获得鹰眼术 clairvoyance 的效应。这种泛黄的液体中漂浮着一个眼球，但会在你打开瓶盖时消失。
"""

magic_item_potion_of_climbing = """
# 攀爬药水 Potion of Climbing
魔药，普通
饮用此药水后，你获得等同于你步行速度的攀爬速度，持续 1 小时。在此期间，你攀爬时进行的力量（运动）检定具有优势。药水分离成类似于岩层的褐色、银色和灰色三层，即使摇晃也不会让三种颜色混合到一起。
"""

magic_item_potion_of_diminution = """
# 缩小药水 Potion of Diminution
魔药，珍稀
饮用此药水后，你获得变巨/缩小术 enlarge/reduce 的“缩小”效应，并持续 1d4 小时（无需专注）。药水中的红色成分不断聚合成一个小球，然后又散开将周围的液体染成红色。摇晃药水也不会打断这个过程。
"""

magic_item_potion_of_fire_breath = """
# 火焰吐息药水 Potion of Fire Breath
魔药，非普通
饮用此药水后，你可以用一个附赠动作向你周边 30 尺内的一个目标喷出火焰。目标必须进行一次 DC 13 的敏捷豁免，失败受到 4d6 的火焰伤害，成功则伤害减半。药水的效应在你喷出三次火焰或 1 小时后终止。
这瓶橙色的药水不停闪烁着，瓶中没有药水的部分则充满了烟雾。打开容器时烟雾将飘出。
"""

magic_item_potion_of_flying = """
# 飞行药水 Potion of Flying
魔药，极珍稀
饮用此药水后，你获得等同于你步行速度的飞行速度并可以悬浮，效应持续 1 小时。如果药水效应终止时你仍在空中，并且也没有其他飞行手段，那么你将坠落。这种透明的液体漂浮在容器顶部，其中含有些许云雾状的白色杂质。
"""

magic_item_potion_of_gaseous_form = """
# 气化形体药水 Potion of Gaseous Form
魔药，珍稀
饮用此药水后，你获得气化形体 gaseous form 的效应，持续一小时或直到你用一个附赠动作将其终止（无需专注）。
这种药水装在瓶中若云雾，倒出来则似水流。
"""

magic_item_potion_of_giant_strength = """
# 巨人之力药水 Potion of Giant Strength
魔药，多种稀有度
饮用此药水后，你的力量值将变为药水所赋予的数值（由巨人类型决定，见下表），持续 1 小时。如果你的力量值已经大于或等于药水所能赋予的数值，则药水无效。
巨人之力药水透明的药液中漂着一点对应类型巨人的指甲碎片。
霜巨人之力药水和石巨人之力药水效果相同。

# table
巨人类型 力量 稀有度
山丘巨人 21 非普通
霜巨人/石巨人 23 珍稀
火巨人 25 珍稀
云巨人 27 极珍稀
风暴巨人 29 传说
"""

magic_item_potion_of_growth = """
# 成长药水 Potion of Growth
魔药，非普通
饮用此药水后，你获得变巨/缩小术 enlarge/reduce 的“变巨”效应，持续 1d4 小时（无需专注）。药水中的红色成分不断从一个小球散开将周围的液体染成红色，然后又聚合。摇晃药水也不会打断这个过程。
"""

magic_item_potion_of_healing = """
# 治疗药水 Potion of Healing
魔药，多种稀有度
饮用此药水后，根据药水稀有度不同（见下表），你将恢
复一定数值的生命值。无论效果如何，这种红色药水在摇晃时
都会微微发亮。

# table 治疗药水 Potions of Healing
药水类型 稀有度 生命值恢复
治疗药水 普通 2d4+2
高等治疗药水 greater 非普通 4d4+4
强效治疗药水 superior 珍稀 8d4+8
极效治疗药水 supreme 极珍稀 10d4+20
"""

magic_item_potion_of_heroism = """
# 英雄气概药水 Potion of Heroism
魔药，珍稀
饮用此药水后，你获得 10 点临时生命值和祝福术 Bless的效应（无需专注），持续 1 小时。这种蓝色的药水如同沸腾搬冒出气泡和蒸汽。
"""

magic_item_potion_of_invisibility = """
# 隐身药水 Potion of Invisibility
魔药，极珍稀
装着这种药水的容器看起来是空的，但你仍能感觉到其中保存着液体。饮用此药水后，你隐形 1 小时。你着装或携带的东西也将和你一起隐形。如果你攻击或施法，则隐形效应提前终止。
"""

magic_item_potion_of_invulnerability = """
# 坚不可摧药水 Potion of Invulnerability
魔药，珍稀
饮用此药水后，你获得对所有伤害的抗性，持续 1 分钟。
这种粘稠的药水看起来就像液化的钢铁。
"""

magic_item_potion_of_longevity = """
# 延寿药水 Potion of Longevity
魔药，极珍稀
饮用此药水后，你的生理年龄减少 1d6+6 岁，但不能小于 13 岁。此后每当你再次饮这种药水时，都会累加 10%的概率令你增加而非减少 1d6+6 岁。这种琥珀色药水中悬浮着一条蝎子的尾巴，一颗蝰蛇的牙，一只死蜘蛛，以及一颗违反常理地跳动着的小心脏。药水被打开时，这些成分便随之消失。
"""

magic_item_potion_of_mind_reading = """
# 读心药水 Potion of Mind Reading
魔药，珍稀
饮用此药水后，你获得侦测思想 detect thoughts（DC 13）的效应。这种粘稠的紫色药水中漂浮着一团粉色的卵形云雾。
"""

magic_item_potion_of_poison = """
# 剧毒药水 Potion of Poison
魔药，非普通
这种药水看起来、闻起来和尝起来都和治疗药水 potion of healing 或其他增益药水差不多。但实际上，它是用幻术伪装过的毒药。
鉴定术 identify 可以发现它的本质。
饮用此药水后，你受到 3d6 的毒素伤害并且必须成功通过一次 DC 13 的体质豁免否则中毒。中毒期间每次你的回合开始时，你受到 3d6 的毒素伤害。每次你的回合结束时你可以再次尝试豁免。如果豁免成功，则你在接下来的回合中受的毒素伤害减少 1d6。当毒素伤害降低至 0 时，毒药效应终止。
"""

magic_item_potion_of_resistance = """
# 抗性药水 Potion of Resistance
魔药，非普通
饮用此药水时，你获得对某种伤害类型的抗性，持续 1 小时。DM 可以自行选定伤害类型，或从下表中随机选择。

# d-10
d10 伤害类型
1 强酸
2 冷冻
3 火焰
4 力场
5 闪电
6 黯蚀
7 毒素
8 心灵
9 光耀
10 雷鸣
"""

magic_item_potion_of_speed = """
# 加速药水 Potion of Speed
魔药，极珍稀
饮用此药水后，你获得加速术 haste 的效应，持续 1 分钟（无需专注）。这瓶黄色的药水中混杂着黑色杂质，并有一个漩涡不断自行旋转。
"""

magic_item_potion_of_vitality = """
# 活力药水 Potion of Vitality
魔药，极珍稀
饮用此药水将消除你所有的力竭状态，并治愈影响你的任何疾病或毒素。此后 24 小时内，你使用生命骰时所恢复的生命值都为生命骰的最大值。这种深红色药水有节奏的发出微光，让人联想到心脏的跳动。
"""

magic_item_potion_of_water_breathing = """
# 水下呼吸药水 Potion of Water Breathing
魔药，非普通
饮用此药水后，你可以在水下呼吸，持续 1 小时。这种浑浊的绿色药水闻起来有海水的味道，其中漂浮着一个水母形状的气泡。
"""

magic_item_quaals_feather_token = """
# 夸尔羽符 Quaal's Feather Token
奇物，珍稀
这是一件外观类似羽毛的小物品。夸尔羽符有很多种，每种都有一个一次性效应。羽符的类型由 DM 选取或参照下表随机决定。
锚 Anchor。你可以用一个动作以这枚羽符碰触一艘船。接下来的 24 小时中，无论采取何种方式，该船都无法被移动。用羽符再次碰触该船将终止该效应。效应终止时，羽符也将随之消失。
鸟 Bird。你可以用一个动作将这枚羽符抛到 5 尺高的空中。羽符将消失，取而代之的是一只五彩斑斓的大鸟。这只鸟使用大鹏 roc 的资料（详见《怪物图鉴》）。它服从你的简单命令但无法攻击。负载不超过 500 磅时，它能以全速飞行（16里每小时，每飞行 3 小时休息 1 小时，每天至多飞行 144 里）。而负重不超过 1000 磅时则以半速飞行。大鸟飞过 144 里或生命值降至 0 后消失。你可以用一个动作解消羽符的效应。
扇 Fan。如果你正乘坐一艘船，你可以用一个动作将这枚羽符抛到 10 尺高的空中。羽符将消失，取而代之的是一把巨大的扇子。这把扇子会悬浮在空中，并扇起一阵足以推动一艘船的风，使船的速度增加 5 里每小时，持续 8 小时。你可以用一个动作解消羽符的效应。
天鹅船 Swan Boat。你可以用一个动作以这枚羽符碰触一个至少直径 60 尺的水体。羽符将消失，取而代之的是一艘50 尺长，20 尺宽的天鹅形小船。这艘小船可以自行在水面上以 6 里每小时的速度前进。乘坐这艘小船时，你可以用一个动作命令它前进或在不超过 90 度的范围内转向。小船可以搭载至多三十二名中型或更小体型的生物。一名大型体型生物计为四名中型生物，一名巨型生物计为九名中型生物。小船将在 24 小时后消失。你可以用一个动作解消羽符的效应。
树 Tree。这枚羽符只能在室外使用。你可以用一个动作以这枚羽符碰触一片未被占据的地面。羽符将消失，一棵巨大的非魔法橡树将在羽符消失的地方长出。橡树高 60 尺，其树干直径 5 尺，树冠半径 20 尺。
鞭 Whip。你可以用一个动作将这枚羽符扔出至多 10 尺。
羽符将消失，取而代之的是一条悬浮在空中的长鞭。你可以用一个附赠动作让长鞭对它周围 10 尺内的一名生物发动近战法术攻击，攻击加值+9。如果攻击命中，目标将受到 1d6+5的力场伤害。
你可以在自己的回合里用一个附赠动作命令长鞭飞行至多 20 尺并攻击它周围 10 尺内的一名生物。长鞭将在 1 小时后消失，你陷入失能或你死亡时鞭子也会消失。你可以用一个动作解消羽符的效应。

# d-100
d100 羽符
01~20 锚 anchor
21~35 鸟 bird
36~50 扇 fan
51~65 天鹅船 swan boat
66~90 树 tree
91~100 鞭 whip
"""

magic_item_quiver_of_ehlonna = """
# 艾罗娜的箭袋 Quiver of Ehlonna
奇物，非普通
这个箭袋有三个口袋，每一个都连接着一个异次元空间。
无论其中存放了多少东西，箭袋的重量永远不会超过 2 磅。
三个口袋中最小的可以容纳 60 支箭，弩矢或类似的物件；中等大小的口袋可以容纳 18 支标枪或类似物件；最大的口袋可以容纳六件长条型物件（比如弓、法杖、矛等）。
你可以像从普通箭袋或剑鞘中取出物品一样从艾罗娜箭袋中拿取物品。
鞭 Whip。你可以用一个动作将这枚羽符扔出至多 10 尺。
羽符将消失，取而代之的是一条悬浮在空中的长鞭。你可以用一个附赠动作让长鞭对它周围 10 尺内的一名生物发动近战法术攻击，攻击加值+9。如果攻击命中，目标将受到 1d6+5的力场伤害。
你可以在自己的回合里用一个附赠动作命令长鞭飞行至多 20 尺并攻击它周围 10 尺内的一名生物。长鞭将在 1 小时后消失，你陷入失能或你死亡时鞭子也会消失。你可以用一个动作解消羽符的效应。
"""

magic_item_ring_of_animal_influence = """
# 支配动物戒指 Ring of Animal Influence
戒指，珍稀
这枚戒指有 3 发充能，且每天黎明时恢复 1d3 发已消耗的充能。着装这枚戒指时，你可以用一个动作并消耗 1 发充能以施展下列法术其一：
•化兽为友 animal friendship（DC 13）•恐惧术 Fear（DC 13），目标只能是智力为 3 或更低的野兽•动物交谈 speak with animal召唤气巨灵戒指 Ring of Djinni Summoning戒指，传说（需同调）着装这枚戒指时，你可以用一个动作说出它的命令语以从气元素位面召唤一名特定的气巨灵 djinni。该气巨灵将出现在你周围 120 尺内你指定的某个未被占据的位置。你必须专注以维持气巨灵的存在（如同专注法术），持续时间至多 1 小时，或直到其生命值降至 0。随后它将回到自己的位面。
被召唤的气巨灵对你和你的伙伴态度友善。无论你使用何种语言，它都会服从你的命令。如果你没有下达命令，它便只会保护自己且不执行任何动作。
气巨灵被遣返后，你必须等待 24 小时才能再次召唤它。
如果该气巨灵死去，则这枚戒指将变为非魔法物品。
"""

magic_item_ring_of_elemental_command = """
# 命令元素戒指 Ring of Elemental Command
戒指，传说（需同调）
这枚戒指连接着四个元素位面之一，由 DM 决定或随机选择。
着装这枚戒指时，你对来自戒指连接位面的元素发动攻击检定时具有优势，且它们对你发动的攻击检定具有劣势。另外，视戒指连接的位面不同，你还获得相应的属性（见下）。
戒指有 5 发充能，每天黎明时恢复 1d4+1 发已消耗的充能。利用戒指施展的法术 DC 为 17。
命令气元素戒指 Ring of Air Elemental Command。你可以消耗 2 发充能对一名气元素施展法术支配怪物 dominatemonster。另外，坠落时你每回合只会下降 60 尺，也不会受到坠落伤害。你可以说和理解风族语 Auran。
如果你维持与戒指同调期间参与杀死了一名气元素，则你额外获得以下属性：
• 你获得对闪电伤害的抗性。
• 你获得等同于步行速度的飞行速度并且可以悬浮。
• 你可以利用戒指施展以下法术（消耗充能数在括号中注明）：连环闪电 chain lightning（3 充能）、造风术 gust of wind（2充能）、风墙术 wind wall（1 充能）。命令土元素戒指 Ring of Earth Elemental Command。你可以消耗 2 发充能对一名土元素施展法术支配怪物 dominatemonster。另外，你可以在瓦砾、岩石或泥泞造成的困难地形中如常移动。你可以说和理解土族语 Terran。
如果你维持与戒指同调期间参与杀死了一名土元素，则你额外获得以下属性：
• 你获得对强酸伤害的抗性。
• 你可以移动穿过坚实的地面或岩石内，其规则等同于穿过困难地形。如果你在穿行途中结束自己的回合，则你将被推至你最后占据过的未被占据的空间。
• 你可以利用戒指施展以下法术（消耗充能数在括号中注明）：塑石术 stone shape（2 充能）、石肤术 stoneskin（3 充能）、石墙术 wall of stone（3 充能）。
命令火元素戒指 Ring of Fire Elemental Command。你可以消耗 2 发充能对一名火元素施展支配怪物 dominatemonster。另外，你获得对火焰伤害的抗性。你可以说和理解火族语 Ignan 。
如果你维持与戒指同调期间参与杀死了一名火元素，则你额外获得以下属性：
• 你对火焰伤害免疫。
• 你可以利用戒指施展以下法术（消耗充能数在括号中注明）：
燃烧之手 burning hands（1 充能）、火球术 fireball（2 充能）、火墙术 wall of fire（3 充能）。
命令水元素戒指 Ring of WaterElemental Command。你可以消耗 2 发充能对一名水元素施展法术支配怪物 dominatemonster。另外，你可以在液体表面移动或站立，如同在坚实的地面上一般。你可以说和理解水族语 Aquan。
如果你维持与戒指同调期间参与杀死了一名水元素，则你额外获得以下属性：
• 你可以在水下呼吸，并获得等同于步行速度的游泳速度。
• 你可以利用戒指施展以下法术（消耗充能数在括号中注明）：
造水术/枯水术 create or destory water（1 充能）、冰风暴ice storm（2 充能）、冰墙术 wall of ice（3 充能）、操纵水体control water（3 充能）。
"""

magic_item_ring_of_evasion = """
# 反射闪避戒指 Ring of Evasion
戒指，珍稀（需同调）
这枚戒指有 3 发充能，且每天黎明时恢复 1d3 发已消耗的充能。着装这枚戒指时，如果你进行敏捷豁免失败，则你可以用你的反应消耗 1 发充能使该豁免成功。
"""

magic_item_ring_of_feather_falling = """
# 羽落戒指 Ring of Feather Falling
戒指，珍稀（需同调）
着装这枚戒指时，你在坠落中每回合只会下降 60 尺，并且不会受到坠落伤害。
"""

magic_item_ring_of_free_action = """
# 自由行动戒指 Ring of Free Action
戒指，珍稀（需同调）
着装这枚戒指时，你通过困难地形时无需消耗额外的移动力。另外，魔法无法降低你的速度，也无法令你陷入麻痹或束缚状态。
"""

magic_item_ring_of_invisibility = """
# 隐身戒指 Ring of Invisibility
戒指，传说（需同调）
着装这枚戒指时，你可以用一个动作进入隐形。任何你着装或携带的东西也将随你隐形。你保持隐形直到发动攻击、施展法术，或是戒指被摘下。你也可以用一个附赠动作解除隐形。
"""

magic_item_ring_of_jumping = """
# 跳跃戒指 Ring of Jumping
戒指，非普通（需同调）
着装这枚戒指时，你可以随意以一个附赠动作施展跳跃术 jump，但只能以自身为目标。
"""

magic_item_ring_of_mind_shielding = """
# 心灵护盾戒指 Ring of Mind Shielding
戒指，非普通（需同调）
着装这枚戒指时，你免疫其他生物对你使用的以下魔法效应：读心、测谎、侦测阵营、侦测生物类型。只有在你同意时，其他生物才能和你建立心灵感应。
你可以用一个动作将戒指隐形，也可以用一个动作令它显形。当你把戒指摘下或你死亡时，戒指也将显形。
如果你死亡时戴着戒指，你的灵魂将注入戒指中，除非其中已经寄居了一个灵魂。你可以选择留在戒指中或是离开它而往生。只要你的灵魂还寄居在戒指里，你就可以通过心灵感应和着装戒指的生物交流。着装戒指的生物无法拒绝寄居灵魂的心灵感应。
"""

magic_item_ring_of_protection = """
# 防御戒指 Ring of Protection
戒指，珍稀（需同调）
着装这枚戒指时，你的 AC 和豁免获得+1 加值。
"""

magic_item_ring_of_regeneration = """
# 再生戒指 Ring of Regeneration
戒指，极珍稀（需同调）
着装这枚戒指时，只要你尚有至少 1 点生命值，你就能每 10 分钟恢复 1d6 的生命值。即使你失去了一部分肢体，只要你能在 1d6+1 日内保持至少有 1 点生命值，则失去的肢体也会重新长出并恢复功能。
"""

magic_item_ring_of_resistance = """
# 抗性戒指 Ring of Resistance
戒指，珍稀（需同调）
着装该戒指时，你获得对某种类型伤害的抗性。戒指上镶嵌的宝石种类决定抗性的种类，具体由 DM 决定或随机选择。

# d-10
d10 伤害类型 宝石
1 强酸 珍珠 pearl
2 冷冻 电气石 tourmaline
3 火焰 石榴石 garnet
4 力场 蓝宝石 sapphire
5 闪电 黄水晶 citrine
6 黯蚀 黑玉 jet
7 毒素 紫晶 amethyst
8 心灵 翡翠 jade
9 光耀 黄玉 topaz
10 雷鸣 尖晶石 spinel
"""

magic_item_ring_of_shooting_stars = """
# 流星戒指 Ring of Shooting Stars
戒指，极珍稀（需在夜晚的户外同调）
着装这枚戒指且在黑暗或微光光照环境下时，你可以随意施展舞光术 dancing light 和光亮术 light。利用戒指施法需要一个动作。
戒指有 6 发充能，每天黎明时恢复 1d6 发已消耗的充能。
妖火 Faerie Fire。你可以用一个动作并消耗 1 发充能施展妖火 Faerie Fire。
球形闪电 Ball Lightning。你可以用一个动作并消耗 2 发充能以创造一到四个 3 尺直径的闪电球。你创造的闪电球越多，单个闪电球的威力就越小。
每个闪电球将会出现在你周围 120 尺内未被占据的空间。
它们将在你专注（如同专注于法术）期间持续存在，但至多不能超过 1 分钟。每个闪电球都为其周围 30 尺提供微光光照。
作为一个附赠动作，你可以将每个闪电球移动至多 30 尺，但不能离开你周围 120 尺范围。当闪电球和某名除你以外的生物间距离不足 5 尺时，它将向该生物释放闪电然后消失。
该生物必须进行一次 DC 15 的敏捷豁免，失败则受到相应闪电伤害。单个闪电球的伤害如下表所示：
流星 Shooting Stars。你可以用一个动作并消耗 1 到 3 发充能。每 1 发充能将转化为一点光屑，从戒指中射出到 60 尺内你能看到的地点。光屑落点周围 15 尺范围内的每名生物都必须进行一次 DC 15 的敏捷豁免，豁免失败者将受到 5d4 的火焰伤害，成功则伤害减半。

# table 球形闪电
闪电球数量 单个闪电球伤害
4 2d4
3 2d6
2 5d4
1 4d12
"""

magic_item_ring_of_spell_storing = """
# 储法戒指 Ring of Spell Storing
戒指，珍稀（需同调）
这枚戒指可以储存对它施展的法术，保存直到与它同调的生物使用这些法术。戒指中可以储存的法术环数之和不能超过 5。新发现的储法戒指可能已经储存了由 DM 选定 1d6-1个环阶的法术。
任何生物都可以在施展一个 1 环到 5 环法术时接触戒指以将该法术储存在戒指中。如此被施展的法术将被储存，而不会立即生效。如果法术无法储存在戒指中，则它将被浪费而不产生任何效应。施展法术所使用的法术位环阶决定该法术在戒指中占据的空间。
着装此戒指时，你可以施展其中储存的任何法术。使用原施法者的资料决定法术的环阶、豁免 DC、法术攻击加值和施法关键属性。但除这些之外，该法术仍视为由你施展。戒指中的法术一经施展即消失，释放其原本占据的空间。
"""

magic_item_ring_of_spell_turning = """
# 法术反转戒指 Ring of Spell Turning
戒指，传说（需同调）
着装这枚戒指时，你在对任何仅以你为目标（而非影响你所在区域）的法术进行豁免时具有优势。另外，该法术为 7 环或更低环阶且你的豁免骰出 20 时，该法术对你无效且目标变为原施法者。使用原施法者的资料决定法术位环阶、豁免 DC、攻击加值和施法关键属性属性。
"""

magic_item_ring_of_swimming = """
# 善泳戒指 Ring of Swimming
戒指，非普通
着装这枚戒指时，你获得 40 尺游泳速度。
"""

magic_item_ring_of_telekinesis = """
# 心灵遥控戒指 Ring of Telekinesis
戒指，极珍稀（需同调）
着装这枚戒指时，你可以随意施展心灵遥控 telekinesis，但只能以未被着装或携带的物件为目标。
"""

magic_item_ring_of_the_ram = """
# 公羊戒指 Ring of the Ram
戒指，珍稀（需同调）
这枚戒指有 3 发充能，且每天黎明时恢复 1d3 发已消耗的充能。着装这枚戒指时，你可以用一个动作并消耗 1 到 3发充能以攻击你周围 60 尺内一名你能看见的生物。戒指产生一个山羊头的幻影冲向目标，其攻击加值为+7。如果攻击命中，每消耗 1 发充能，目标就受到 2d10 的力场伤害并被向远离你的方向推开 5 尺。
此外，你还可以用一个动作并消耗 1 到 3 发充能以破坏周围 60 尺内一件你能看到，且未被着装或携带的物件。每消耗 1 发充能，戒指就在力量检定时获得一个+5 加值。
"""

magic_item_ring_of_three_wishes = """
# 三愿戒指 Ring of Three Wishes
戒指，传说
这枚戒指有 3 发充能。着装这枚戒指时，你可以用一个动作并消耗 1 发充能施展祈愿术 wish。充能用尽后，这枚戒指将变为非魔法物品。
"""

magic_item_ring_of_warmth = """
# 温暖戒指 Ring of Warmth
戒指，非普通（需同调）
着装这枚戒指时，你对寒冷伤害具有抗性。另外，你自身及你着装或携带的物件都可不受最低华氏-50 度的低温影响。
"""

magic_item_ring_of_water_walking = """
# 水行戒指 Ring of Water Walking
戒指，非普通
着装这枚戒指时，你可以在液体表面站立和行走，如同在坚实地面上一般。
"""

magic_item_ring_of_x_ray_vision = """
# X 射线戒指 Ring of X-Ray Vision
戒指，珍稀（需同调）
着装此戒指时，你可以用一个动作说出命令语启动戒指的效应。启动后，你获得可以看到实体物件内部或穿透它看到后方的特殊视觉，其半径为 30 尺，持续 1 分钟。对你而言，此视觉范围内的实体均为透明状态，并且不会阻碍光线通过。
此视觉可以穿透 1 尺厚的石头、1 寸厚的普通金属、或是至多3 尺厚的木头或泥土。更厚的物件，或是一层铅片，将阻碍这种视觉。
如果你在一次长休前尝试再次启动这枚戒指，则必须成功通过一次 DC 15 的体质豁免否则将提升一级力竭。
"""

magic_item_robe_of_eyes = """
# 百眼法袍 Robe of Eyes
奇物，珍稀（需同调）
这件长袍上绘满了眼睛的图案。着装这件长袍时，你获得以下好处：
• 你可以看到所有的方向，并且你在依赖视觉进行的感知（察觉）检定具有优势。
• 你获得 120 尺黑暗视觉。
• 在 120 尺的范围内，你可以看到隐形的生物、物件以及以太位面的事物。
长袍上的眼睛图案无法闭合或是转移视线。即使你闭上你自己的眼睛或移开视线，法袍依然会让你看到四周，如同你并未闭上眼睛或移开视线一般。
对法袍施展光亮术 light 或在你周围 5 尺内施展昼明术daylight 将使你目盲 1 分钟。在你的每回合结束时，你可以进行一次体质豁免（对光亮术 light 时 DC 为 11，对昼明术daylight 时 DC 为 15），成功则终止你身上的相应效应。
"""

magic_item_robe_of_scintillating_colors = """
# 虹光法袍 Robe of Scintillating Colors
奇物，极珍稀（需同调）
这件长袍有 3 发充能，且每天黎明时恢复 1d3 发已消耗的充能。
着装这件长袍时，你可以用一个动作并消耗 1 发充能让长袍显现不断变幻的耀眼图像，直到你的下回合结束。这段时间内，长袍提供 30 尺的明亮光照和额外 30 尺的微光光照。
能看到你的生物对你发动的攻击检定具有劣势。另外，在长袍效应启动期间，任何处于长袍产生的明亮光照区域内，且可以看到你的生物必须成功通过一次 DC 15 的感知豁免否则被震慑直到长袍的效应终止。
"""

magic_item_robe_of_stars = """
# 星辰法袍 Robe of Stars
奇物，极珍稀（需同调）
这件黑色和深蓝为底色的长袍上点缀着白色或银色的星星。着装这件长袍时，你的豁免具有+1 加值。
长袍的前襟附近有六枚较大的星。着装这件长袍时，你可以用一个动作取下其中一颗并以之施展 5 环效应的魔法飞弹magic missile。每天黎明时，1d6 颗已消耗的星将重新出现在法袍上。
着装这件长袍时，你可以用一个动作使你和你身上着装或携带的物件一起进入星界。直到你再用一个动作回到你原本所在的位面，此时你出现在之前占据的空间。如果该空间已被占据，则你出现在最近的未被占据空间。
"""

magic_item_robe_of_the_archmagi = """
# 大法师法袍 Robe of the Archmagi
奇物，传说（需术士、邪术师或法师同调）
这件典雅的长袍由白色、灰色或黑色的精制布料制成，并饰有银色的符文。每一件大法师法袍都为某个阵营所定制，其颜色与阵营对应。白色代表善良、灰色代表中立，而黑色代表邪恶。你无法和与你阵营不符的法袍同调。
着装这件长袍时，你获得以下好处：
• 不着装护甲时，你的基础 AC 为 15＋你的敏捷调整值。
• 你对抗法术和其他魔法效果时作的豁免检定具有优势。
• 你的法术豁免 DC 和法术攻击加提升 2。
"""

magic_item_robe_of_useful_items = """
# 杂货法袍 Robe of Useful Items
奇物，非普通
这件长袍上打着各种颜色和形状的补丁。穿着这件长袍时，你可以用一个动作撕下一块补丁，令它变成它象征的物件。
所有补丁都被撕下后，这件长袍将变为普通衣物。
杂货法袍有以下补丁各 2 个：
• 匕首• 牛眼提灯（装满燃料且点燃）• 钢镜• 10 尺长杆• 麻绳（长 50 尺，盘绕状态）• 麻布袋另外，杂货法袍还有 4d4 个其他补丁。补丁对应的物品由 DM 选择或随机决定。

# d-100
d100 补丁
01~08 装有 100 金币的钱袋
09~15 价值 500 金币的银柜（高 1 尺，宽、深各 6 寸）
16~22 至多 10 尺长宽，一面有门闩的铁门。你可以选择一处你可触及的空当安放铁门，它将自动改变形状贴合空当并设置铰链。
23~30 10 枚宝石。每枚价值 100 金币。
31~44 24 尺长的木梯
45~51 1 只乘用马 riding horse（资料详见《怪物图鉴》）及鞍囊
52~59 每边 10 尺的立方陷坑。你可以将其布置在你周围 10尺内的地面上。
60~68 4 瓶治疗药水 potion of healing
69~75 12 尺长的划艇 rowboat
76~83 写有 1 个 1 环到 3 环法术的法术卷轴 spell scroll
84~90 2 只獒犬 mastiff（资料详见《怪物图鉴》）
91~96 2 尺 x 4 尺的窗户，最多 2 尺深。你可以将它布置在你能触及的竖直平面上。
97~00 便携式攻城锤 portable ram
"""

magic_item_rod_of_absorption = """
# 吸收权杖 Rod of Absorption
权杖，极珍稀（需同调）
持握这把权杖时，你可以用反应来吸收一个仅以你为目标（而非影响你所在的区域）的法术。被吸收的法术不产生效应，但其能量（而非法术本身）被权杖吸收。这股能量的环阶与该法术被施展时的环阶相同。吸收权杖从制成到毁灭只能储存共 50 环的能量。吸收满 50 环能量后，它将无法再吸收法术。如果权杖无法吸收某个以你为目标的法术，则该法术不受权杖影响。
与吸收权杖同调时，你将了解到权杖已经吸收过多少能量，以及它现时储存了多少能量。
如果你是一名施法者，当你持握吸收权杖时，你可以将权杖中储存的能量转化为法术位并用以施展你自己准备或知晓的法术。你可以转化至高 5 环的法术位，但不能高于你拥有的最高环法术位。你仍如通常一般施法，只是消耗权杖储存的能量代替自身法术位。例如，你可以用权杖储存的 3 环能量代替自身的一个 3 环法术位。
新发现的吸收权杖 通常已经储存了 1d10 环能量。无法继续吸收能量且储存的能量已经用尽的吸收权杖将变为普通物品。
"""

magic_item_rod_of_alertness = """
# 警示权杖 Rod of Alertness
权杖，极珍稀（需同调）
这把权杖顶端有尖刺状凸起。权杖具有以下属性：
警觉 Alertness。持握这把权杖时，你进行的感知（察觉）检定和先攻检定具有优势。
法术 Spells。持握这把权杖时，你可以用一个动作施展以下法术之一：
侦测善恶 detect evil and good、侦测魔法 detectmagic、侦测毒性和疾病 detect poison and disease、识破隐形see invisibility。
防护灵光 Protective Aura。你可以用一个动作将这把权杖的柄插入地面。权杖顶部将放出光芒，提供 60 尺的明亮光照和额外 60 尺的微光光照。处于明亮光照区域时，你和任何对你友善的生物其 AC 和豁免获得+1 加值，且可以感知区域内有敌意的隐形生物的位置。此效应持续十分钟或直到一名生物用一个动作将权杖拔起。此后直到次日黎明前，该属性都无法再次启动。
"""

magic_item_rod_of_lordly_might = """
# 王者权杖 Rod of Lordly Might
权杖，传说（需同调）
这把权杖顶端有尖刺状凸起。它还是一把魔法硬头锤。你用它发动的攻击检定和伤害掷骰获得+3 加值。
王者权杖 的杖柄上排列着六个不同的按钮，用来启动权杖的相应属性。权杖还有其他三种属性，其细节如下。
六个按钮 Six Buttons。你可以用一个附赠动作按下权杖六个按钮之一。某个按钮的效应将一直生效，直到你按下另一个按钮，或再次按下同一个按钮为止。再次按下同一按钮将使权杖变回通常形态。
如果你按下按钮 1，权杖将变为一把焰舌 flame tongue。
被烈焰覆盖的刀刃从权杖没有凸起的一端伸出。
如果你按下按钮 2，权杖顶端的凸起折下，并伸展出两片新月般的斧刃，将权杖变为一把魔法战斧 battleaxe。你用它发动的攻击检定和伤害掷骰获得+3 加值。
如果你按下按钮 3，权杖顶端的凸起折下，顶端伸出矛尖，柄伸长至 6 尺，将权杖变为一把魔法矛 spear。你用它发动的攻击检定和伤害掷骰获得+3 加值。
如果你按下按钮 4，权杖将变为一根爬杆，长度由你设定但不能超过 50 尺。在花岗岩一般坚硬的表面上，爬杆尾部的岩钉和顶部的三个爪钩可以固定住爬杆。爬杆上每隔 1 尺向两侧伸展出一根 3 寸长的把手，构成一架梯子。爬杆最多可以承受 4000 磅的重量。如果超重或是失去固定点，则爬杆将会变回权杖。
如果你按下按钮 5，权杖将变为一把手持式战斗攻城锤ram。使用它的角色在破坏门、路障或其他障碍时所在的力量检定获得+10 加值。
如果你按下按钮 6，权杖将变回或维持通常形态，并指出地磁北极。如果权杖所在的地点并没有地磁北极的概念，则此属性无效。权杖还会让你了解到自己在地下的深度或在地上的高度。
吸取生命 Drain Life。用权杖发动近战攻击命中一生物时，你可以迫使目标进行一次 DC 17 的体质豁免。如果豁免失败，则目标将受额外 4d6 的黯蚀伤害，而你获得等于伤害值一半的生命值。此后直到次日黎明前，该属性都无法再次启动。
麻痹 Paralyze。用权杖发动近战攻击命中一名生物时，你可以迫使目标进行一次 DC 17 的力量豁免。如果豁免失败，目标将麻痹 1 分钟。目标可以在它的每轮结束时再次尝试该豁免，成功则终止其身上的相应效应。直到次日黎明前，此后这个属性都无法再次启动。
惊惧 Terrify。持握此权杖时，你可以用一个动作迫使 30尺内一名你能看见的生物进行一次 DC 17 的感知豁免。如果豁免失败，目标将受你恐慌 1 分钟。目标可以在它的每回合结束时再次进行该豁免，成功则终止自己身上的相应效应。直到次日黎明前，该属性都无法再次启动。
"""

magic_item_rod_of_the_pact_keeper = """
# 契约掌控者权杖 Rod of the Pact Keeper
权杖，非普通（+1），珍稀（+2），极珍稀（+3）（需邪术师同调）
持握这把权杖时，你施展邪术师法术时法术攻击检定与豁免 DC 获得由权杖稀有度决定的加值。
此外，持握这把权杖时，你可以用一个动作恢复 1 个邪术师法术位。你必须完成一次长休才能再次使用权杖的这个属性。
"""

magic_item_rod_of_resurrection = """
# 复活权杖 Rod of Resurrection
权杖，传说（需牧师、德鲁伊或圣武士同调）
这把权杖有 5 发充能。持握权杖时，你可以用一个动作施 展 以 下 法 术 ：
医疗术 heal （消耗 1 充能） 或复活术resurrection（消耗 5 充能）。
权杖每天黎明时恢复 1 发已消耗的充能。当权杖充能耗尽时，骰一次 d20。如果掷骰结果为 1，则权杖在一阵强光中消失。
"""

magic_item_rod_of_rulership = """
# 支配权杖 Rod of Rulership
权杖，珍稀（需同调）
你可以用一个动作展示权杖，并指定周边 120 尺内若干能看见的生物使其服从于你。每个目标必须成功通过一次 DC15 的感知豁免否则被你魅惑 8 小时。豁免失败的生物将视你为可以信赖的领袖。如果你或你的同伴伤害了被支配者，或是命令被支配者进行违反其天性的行为，魅惑将立即终止。此后直到次日黎明前，该权杖都无法再次启动。
"""

magic_item_rod_of_security = """
# 庇护权杖 Rod of Security
权杖，极珍
稀持握这把权杖时，你可以用一个动作启动它。权杖立刻将你和你能看到的至多 199 名自愿的其他生物传送到存在于异位面的一处乐园福地。你可以自行定义乐园的景观。它可以是宁静的花园、迷人的林间空地、热闹的酒馆、宽阔的宫殿、热带的海岛、奇妙的嘉年华会，或是任何你能想象到的美景。无论环境如何，乐园都有足够的食物和水供访客享用。除食水之外，乐园内的任何东西都只能在乐园的异位面空间中存在。例如，在乐园的花园中采的花在被带出异位面空间时将消失。
在乐园中每度过 1 小时，每名访问者将如使用了 1 枚生命骰一般恢复生命值。虽然时间正常流动，但乐园中的生物并不会老化。访问者可以在乐园停留的时间为 200 天除以生物数量（向下取整）。
当到达时限或你用一个动作解除权杖效应时，所有访客将被送回你权杖启动前的位置或是该位置最近的未被占据空间。此后经过 10 日庇护权杖才能再次启动。
"""

magic_item_rope_of_climbing = """
# 攀爬绳 Rope of Climbing
奇物，非普通
这条 60 尺长的丝质绳索重 3 磅，可以承受 3000 磅的重量。你可以握住绳索的一端并用一个动作说出命令语以使绳索活化。以一个附赠动作，你可以命令绳索的另一端向你指定的目的地移动。从你下达命令的回合开始，绳索的另一端在你的每个回合移动 10 尺，直到到达目的地、长度不足或你命令它停止。你也可以命令绳索牢牢绑在一个指定物体上，或是松绑、打结、解结、卷起。
如果你命令攀爬绳打结，它将每隔 1 尺打一个大结。打结将使绳索长度缩短为 50 尺，但你在使用绳索进行攀爬时具有优势。
绳索拥有 AC 20 和 20 点生命值。只要还剩至少 1 点生命值，绳索就能每 5 分钟恢复 1 点生命值。如果绳索的生命值降至 0，则它被摧毁。
"""

magic_item_rope_of_entanglement = """
# 纠缠绳 Rope of Entanglement
奇物，珍稀
这条绳索长 30 尺，重 3 磅。你可以握住绳索的一端并用一个动作说出命令语，绳索的另一端将疾速飞出困住你周围20 尺内一名你能看见的生物。该生物必须成功通过一次 DC15 的敏捷豁免否则被束缚。
你可以用一个附赠动作说出另一命令语以释放被束缚的生物。被束缚的生物也可以用一个动作进行一次 DC 15 的力量检定或敏捷检定（由该生物选择），检定成功则挣脱束缚。
绳索拥有 AC 20 和 20 点生命值。只要还剩至少 1 点生命值，绳索就能每 5 分钟恢复 1 点生命值。如果绳索的生命值降至 0，则它被摧毁。
"""

magic_item_saddle_of_the_cavalier = """
# 铁骑马鞍 Saddle of The Cavalier
奇物，非普通
骑乘配有这副马鞍的坐骑时，只要你保持清醒，你就不会在非自愿的情况下解除骑乘状态。同时，所有对你坐骑发动的攻击检定具有劣势。
"""

magic_item_scarab_of_protection = """
# 防护圣甲虫 Scarab of Protection
奇物，传说（需同调）
如果你用手握住这个甲虫形徽章 1 轮，它表面上将浮现出铭文，揭示其魔法本质。当你携带圣甲虫时，它为你提供两项增益：
• 你在对法术进行的豁免具有优势。
• 圣甲虫有 12 发充能。如果你在对抗一个死灵系法术或由不死生物造成的有害效应时豁免失败，则你可以使用反应并消耗 1 发充能以使该豁免成功。充能耗尽后，防护圣甲虫将化为灰烬。
"""

magic_item_scimitar_of_speed = """
# 急速弯刀 Scimitar of Speed
武器（弯刀），极珍稀（需同调）
你用此魔法武器发动的攻击检定和伤害掷骰获得+2 加值。
另外，你在自己的每一回合里可以用一个附赠动作以该弯刀发动一次攻击。
"""

magic_item_scroll_of_protection = """
# 守护卷轴 Scroll of Protection
卷轴，珍稀
每张守护卷轴 仅针对一种特定类型的生物起效。生物类型由 DM 指定或按下表随机决定。
用一个动作阅读这张卷轴后，一道半径 5 尺，高 10 尺的圆柱形隐形屏障将在你周围展开。在屏障持续的 5 分钟内，屏障会阻止指定类型生物进入屏障范围或影响屏障内的任何事物。
屏障以你为中心移动。如果你主动移动使指定类型的生物进入屏障范围，则屏障的效应立即终止。
一名指定类型的生物可以用一个动作进行一次 DC 15 的魅力检定以尝试突破屏障，成功则终止该效应对它的影响。
"""

magic_item_sending_stones = """
# 传讯石 Sending Stones
奇物，非普通
传讯石由两块经过雕刻相互可以匹配的光滑石头组成，外形非常容易辨认。当你碰触其中一块传讯石时，你可以用一个动作施展短讯术 sending，目标为另一块传讯石的携带者。
如果另一块传讯石没有被任何生物携带，则你在使用石头时将会得知这一信息，而该短讯术 不会被浪费。
使用短讯术 后，直到次日黎明前传讯石都无法再次启动。
如果一块传讯石被摧毁，则与它配对的另一块石头也将失去其魔法。
"""

magic_item_sentinel_shield = """
# 警戒之盾 Sentinel Shield
护甲（盾牌），非普通
持握此盾牌时，你所进行的先攻检定和感知（察觉）检定具有优势。这面盾牌上绘制一个眼睛的图案。
盾牌 Shield，+1、+2 或+3护甲（盾牌），非普通（+1），珍稀（+2），极珍稀（+3）持握此盾牌时，你将依据盾牌本身的 AC 加值基础上获得额外的加值。加值的数值取决于该盾牌的稀有度。
"""

magic_item_shield_of_missile_attraction = """
# 引弹盾 Shield of Missile Attraction
护甲（盾牌），珍稀（需同调）
持握此盾牌时，你对远程武器造成的伤害具有抗性。诅咒 Curse。与这面受诅咒的盾牌同调的生物将受到其诅咒影响。摘下盾牌不会终止诅咒，只有对你施展移除诅咒remove curse 或类似的魔法才能移除。受诅咒影响时，任何瞄准你周围 10 尺内目标的远程武器攻击都将转为攻击你。
"""

magic_item_slippers_of_spider_climbing = """
# 蛛行便鞋 Slippers of Spider Climbing
奇物，非普通（需同调）
着装这双便鞋时，你可以在垂直平面上移动，也可以在松开双手的情况下倒挂在天花板上。你获得等于你步行速度的攀爬速度。不过，这双鞋不能让你在滑溜的平面，如冰、油覆盖的平面上行走。
"""

magic_item_sovereign_glue = """
# 至尊胶 Sovereign Glue
奇物，传说
这种白浊粘稠的物质可以把任何两件物体永久性的粘在一起。至尊胶必须被储存在一个内壁涂满了滑溜之油 oil ofslipperiness 的瓶子或罐子中。新发现的这类容器中通常装有1d6+1 盎司的至尊胶。
每盎司至尊胶可以覆盖 1 平方尺的表面，并在 1 分钟后凝固。一旦至尊胶凝固，被粘在一起东西就只能用万溶剂universal solvent、滑溜之油 oil of slipperiness 或祈愿术 wish分开。
"""

magic_item_spell_scroll = """
# 法术卷轴 Spell Scroll
卷轴，多种稀有度
每张法术卷轴都以神秘暗语记录了一道法术。如果该法术属于你的职业法术列表，则你可以阅读该卷轴并施展其法术且无需提供任何材料构材。否则你将无法理解该卷轴。通过阅读卷轴施展的法术同样需要遵循相应法术正常的施法时间。
法术施展过后，卷轴上的文字将随之消散，卷轴本身也将化作尘土。施法被打断时，卷轴并不会因此消失。
假如卷轴记载的法术在你职业的法术列表内，但其环阶超过了你目前能施展的水平，则你必须以你的施法关键属性通过一次 DC 为 10＋法术环阶的属性检定。如果检定失败，则卷轴上记载的法术将消失而不生效。
卷轴上的法术一经施展即消失。卷轴本身则化为尘埃。
卷轴的稀有度、其法术的豁免 DC 和攻击加值由它所记载的法术环阶决定，如下表所示：
法术可以如同抄录法术书上的法术一般抄录法术卷轴上的法师法术。抄录卷轴上的法术时，抄录者必须成功通过一次DC 为 10＋法术环阶的智力（奥秘）检定以成功抄录。无论检定成功与否，法术卷轴 都将被摧毁。

# table 法术卷轴 Spell Scroll
法术环阶 稀有度 豁免 DC 攻击加值
戏法 普通 13 +5
1 环 普通 13 +5
2 环 非普通 13 +5
3 环 非普通 15 +7
4 环 珍稀 15 +7
5 环 珍稀 17 +9
6 环 极珍稀 17 +9
7 环 极珍稀 18 +10
8 环 极珍稀 18 +10
9 环 传说 19 +11
"""

magic_item_spellguard_shield = """
# 抗法盾 Spellguard Shield
护甲（盾牌），极珍稀（需同调）
持握此盾牌时，你对抗法术和其他魔法效应所作的豁免检定具有优势，而对你发动的法术攻击简单具有劣势。
"""

magic_item_sphere_of_annihilation = """
# 湮灭法球 Sphere of Annihilation
奇物，传说
这个 2 尺直径的黑色球体是多元宇宙中的一个空洞，由一个围绕在它周围的魔法场维持稳定。
湮灭法球会毁灭任何穿过它或被它穿过的物质。而神器除非标注了易受湮灭法球影响，否则可以不受影响的穿过法球。其它接触到法球但未被完全毁灭或吞噬的东西都将受到4d10 的力场伤害。
除非被人控制，湮灭法球总是保持静止。如果你在一个未被控制的湮灭法球周围 60 尺内，你可以用一个动作进行一次DC 25 的智力（奥秘）检定。如果检定成功，你可以让法球向一个你选择的方向移动尺数等于 5×你的智力调整值的距离（至少 5 尺）。如果检定失败，则湮灭法球向你移动 10 尺。
如果法球进入某名生物占据的空间，则该生物必须成功通过一次 DC 13 的敏捷豁免以避开法球，失败则受 4d10 的力场伤害。
你可以尝试从另一名生物处夺取湮灭法球的控制权。你和该生物进行智力（奥秘）对抗，胜者将获得法球的控制权并可以如常的操纵它移动。
如果湮灭法球与位面传送门（如异界之门 gate 制造的传送门）或是异位面空间（如次元洞 portable hole 内部）接触，则 DM 按下表决定发生的事件：

# d-100
d100 结果
01~50 法球被摧毁
51~85 法球穿过位面传送门或进入异位面空间
86~00 一个空间裂缝出现，将湮灭法球和其周围 180 尺范内的生物和物件送到一个随机存在位面。
"""

magic_item_charming_staff = """
# 魅惑法杖 Staff of Charming
法杖，珍稀（需诗人、牧师、德鲁伊、术士、邪术师或法师同调）
法杖有 10 发充能。持握法杖时，你可以用一个动作并消耗 1 发充能施展魅惑人类 charm person、命令术 command 或通晓语言 comprehend language（使用你自身的法术豁免 DC）。
魅惑法杖也可以用作一把魔法长棍 quarterstaff。
持握法杖时，如果你对一个仅以你为目标的附魔法术豁免失败，则你可以将这次失败变为成功。此后该属性直到次日黎明前都无法再次启动。如果你在对一个仅以你为目标的附魔法术豁免成功（无论是否受益于法杖属性），则你可以用反应并消耗 1 发充能将该法术反射回原施法者，而你则视为该反射法术的施法者。
法杖每天黎明时恢复 1d8+2 发已消耗的充能。当充能耗尽时，骰一次 d20。若骰值为 1，则法杖将变为一把无魔法的长棍。
"""

magic_item_fire_staff = """
# 火焰法杖 Staff of Fire
法杖，极珍稀（需德鲁伊、术士、邪术师或法师同调）
持握这把法杖时，你对火焰伤害具有抗性。
这把法杖有 10 发充能。持握法杖时，你可以用一个动作并消耗 1 发或更多充能以施展以下法术之一（使用你自身的法术豁免 DC）：
燃烧之手 burning hand（1 充能）、火球术fireball（3 充能）、火墙术 wall of fire（4 充能）。
法杖每天黎明时恢复 1d6+4 发已消耗的充能。当充能耗尽时，骰一次 d20。如果骰值为 1，则法杖将化为灰烬而毁灭。
"""

magic_item_frost_staff = """
# 冰霜法杖 Staff of Frost
法杖，极珍稀（需德鲁伊、术士、邪术师或法师同调）
持握这把法杖时，你对冰冻伤害具有抗性。
这把法杖有 10 发充能。持握法杖时，你可以用一个动作并消耗 1 发或更多充能以施展以下法术之一（使用你自身的法术豁免 DC）：
云雾术 fog cloud（1 充能）、冰风暴 ice storm（4 充能）、冰墙术 wall of ice（4 充能）、寒冰锥 cone of cold（5 充能）。
法杖每天黎明时恢复 1d6+4 发已消耗的充能。当充能耗尽时，骰一次 d20。如果骰值为 1，则法杖将被摧毁且化为一滩水。
"""

magic_item_healing_staff = """
# 治愈法杖 Staff of Healing
法杖，珍稀（需诗人、牧师、或德鲁伊同调）
这把法杖有 10 发充能。持握法杖时，你可以用一个动作并消耗 1 发或更多充能以施展以下法术之一（使用你自身的法术豁免 DC）：
疗伤术 cure wounds（每环 1 发充能，至多 4充能）、次级复原术 lesser restoration（2 充能）、群体疗伤术mass cure wounds（5 充能）。
法杖每天黎明时恢复 1d6+4 发已消耗的充能。当充能耗尽时，骰一次 d20。若骰值为 1 则法杖将在一阵闪光中消失。
"""

magic_item_power_staff = """
# 威力法杖 Staff of Power
法杖，极珍稀（需术士、邪术师或法师同调）
该法杖是一把魔法长棍，你在用它发动的攻击检定和伤害掷骰获得+2 加值。持握法杖时，你的 AC、豁免检定和法术攻击检定获得+2 加值。
这把法杖有 20 发充能，且每天黎明时恢复 2d8+4 发已消耗的充能。当充能耗尽时，骰一次 d20。如果骰值为 1，法杖将失去除攻击检定和伤害掷骰的+2 加值外的所有属性。如果骰值为 20，则法杖恢复 1d8+2 发充能。
威力打击 Power Strike。用这把法杖发动近战攻击并命中时，你可以消耗 1 发充能以对目标造成额外 1d6 的力场伤害。
法术 Spells。持握这把法杖时，你可以用一个动作并消耗1 发或更多充能以施展以下法术之一（使用你自身的法术攻击加值和豁免 DC）：
魔法飞弹 magic missile（1 充能）、衰弱射线 ray of enfeeblement（1 充能）、浮空术 levitate（2 充能）、寒冰锥 cone of cold（5 充能）、火球术 fireball（5 环版本，5充能）、怪物定身术 hold monster（5 充能）、闪电束 lightningbolt（5 环版本，5 充能）、力场墙 wall of force（5 充能）、法术无效结界 globe of invulnerability（6 充能）。
复仇打击 Retributive Strike。你可以用一个动作在自己的膝盖上或坚固的表面上折断这把法杖，释放复仇性的打击。
法杖将毁灭并产生一场以其为中心半径 30 尺的爆炸，释放其剩余的所有魔力。
你有 50%的概率被传送到某个随机位面以避开爆炸。如果你未被传送，则你将受 16×法杖剩余充能数的力场伤害。
爆炸范围内的其他生物必须进行一次 DC 17 的敏捷豁免。豁免失败的生物根据它距离爆炸中心的距离承受伤害，如下表所示。豁免成功的生物伤害减半。

# table
与爆炸中心的距离 伤害
10 尺或更近 8×法杖剩余充能数
11~20 尺 6×法杖剩余充能数
21~30 尺 4×法杖剩余充能数
"""

magic_item_striking_staff = """
# 强袭法杖 Staff of Striking
法杖，极珍稀（需同调）
该法杖可以用作一把魔法长棍，你在用它发动的攻击检定和伤害掷骰获得+3 加值。
法杖有 10 发充能。用它发动近战攻击并命中时，你可以消耗至多 3 发充能。每消耗 1 发充能，目标将受额外 1d6 的力场伤害。法杖每天黎明时恢复 1d6+4 发已消耗的充能。当充能耗尽时，骰一次 d20。如果骰值为 1，法杖将变为一把非魔法的长棍。
"""

magic_item_swarm_staff = """
# 虫群法杖 Staff of Swarming Insects
法杖，珍稀（需诗人、牧师、德鲁伊、术士、邪术师或法师同调）
虫群法杖有 10 发充能，且每天黎明时恢复 1d6+4 发已消耗的充能。当充能耗尽时，骰一次 d20。如果骰值为 1，一群昆虫将吞噬法杖，将其摧毁。
法术 Spells。持握法杖时，你可以用一个动作并消耗若干充能以施展以下法术（使用你自身的法术豁免 DC）：
巨虫术 giant insect（4 充能）、疫病虫群 insect plague（5 充能）。
虫云 Insect Cloud。握持法杖时，你可以用一个动作并消耗 1 发充能令一群无害的昆虫布满你周围 30 尺半径的空间，效应持续 10 分钟。持续时间内，这片区域被除你以外的生物视为重度遮蔽。虫群以你为中心随你移动。一阵时速超过 10里每小时的风可以驱散虫群，终止虫云的效应。
"""

magic_item_adder_staff = """
# 蝰蛇法杖 Staff of The Adder
法杖，非普通（需牧师、德鲁伊或邪术师同调）
你可以用一个附赠动作说出法杖的命令语，并将法杖的头部活化为一条毒蛇，效应持续 1 分钟。你可以用另一个附赠动作再次说出该命令语使法杖还原。
你视为拥有法杖变成的蛇头攻击的熟练项，并能以之发动近战攻击（触及 5 尺）。如果攻击命中，则目标受到 1d6 的穿刺伤害并且必须成功通过一次 DC 15 的体质豁免否则受3d6 的毒素伤害。
法杖头部活化为蛇头时可以被指定为攻击目标。它具有AC 15 和 20 点生命值。当蛇头的生命值降至 0 时，法杖将被摧毁。只要法杖未被摧毁，它就会在恢复非活化状态时恢复所有失去的生命值。
"""

magic_item_magi_staff = """
# 贤者法杖 Staff of The Magi
法杖，传说（需术士、邪术师或法师同调）
该法杖可以用作一把魔法长棍，你用它发动的攻击检定和伤害掷骰获得+3 加值。持握它时，你所发动的法术攻击检定获得+2 加值。
法杖有 50 发充能，且每天黎明时恢复 4d6+2 发已消耗的充能。当充能耗尽时，骰一次 d20。如果骰值为 20，则法杖恢复 1d12+1 发充能。
法术吸收 Spell Absorption。持握这把法杖时，你对抗法术时所作的豁免检定具有优势。当另一名生物施展仅以你为目标的法术时，你可以用反应以法杖吸收该法术。在消除法术的同时，法杖还会获得等同于该法术环阶的充能数。但如果吸收法术后法杖的充能数超过 50，则它将随之爆炸，视为启动了复仇打击（见下）。
法术 Spells。持握这把法杖时，你可以用一个动作并消耗若干充能从法杖施展下列法术之一（使用你自身的施法关键属性和豁免 DC）：
炽焰法球 flaming sphere（2 充能）、隐形术invisibility（2 充能）、敲击术 knock（2 充能）、蛛网术 web（2充能）、解除魔法 dispel magic（3 充能）、冰风暴 ice storm（4充能）、火墙术 wall of fire（4 充能）、穿墙术 passwall（5 充能）、心灵遥控 telekinesis（5 充能）、召唤元素生物 conjureelemental（7 充能）、火球术 fireball（7 环版本，7 充能）、闪电束 lightning bolt（7 环版本，7 充能）、异界传送 plane shift（7 充能）。
你还可以用一个动作从法杖随意施展下列法术：
秘法锁 arcane lock 、侦测魔法 detect magic 、变巨/缩小术enlarge/reduce、光亮术 light、法师之手 mage hand、防护善恶 pretection from evil and good。
复仇打击 Restributive Strike。你可以用一个动作在自己的膝盖上或坚固的表面上折断这把法杖，并释放复仇性的打击。法杖将毁灭并产生一场以其为中心半径 30 尺的爆炸，释放其剩余的所有魔力。
你有 50%的概率被传送到某个随机位面以避开爆炸。如果你未被传送，你将受到 16×法杖剩余充能数的力场伤害。
爆炸范围内的其他生物必须进行一次 DC 17 的敏捷豁免。豁免失败的生物将根据它距离爆炸中心的距离承受伤害，如下表所示。豁免成功的生物则伤害减半。

与爆炸中心的距离 伤害
10 尺或更近 8×法杖剩余充能数
11~20 尺 6×法杖剩余充能数
21~30 尺 4×法杖剩余充能数
"""

magic_item_python_staff = """
# 巨蟒法杖 Staff of The Python
法杖，非普通（需牧师、德鲁伊或邪术师同调）
你可以用一个动作说出该法杖的命令语并把它扔到你周边 10 尺范围内的地面上。随后，法杖将变为一条巨蟒 giantconstrictor snake（资料详见《怪物图鉴》）。巨蟒听从你指挥，并以其自身的先攻行动。用一个附赠动作再次说出命令语可将巨蟒变回法杖形态。
在你的回合内，只要巨蟒在你周围 60 尺内且你并未失能，你就可以通过精神命令控制巨蟒。你可以决定巨蟒下一轮的动作和移动，或是下达宽泛的命令，如“攻击敌人”或“保护某地点”。
巨蟒在生命值降至 0 时死亡，法杖也会随之被摧毁。只要巨蟒的生命没有降至 0，它就会在恢复法杖形态时恢复所有失去的生命值。
"""

magic_item_woodlands_staff = """
# 丛林法杖 Staff of The Woodlands
法杖，珍稀（需德鲁伊同调）
该法杖可以用作一把魔法长棍被持用，你用它发动的攻击检定和伤害掷骰获得+2 加值。持握它时，你在发动的法术攻击检定获得+2 加值。
丛林法杖有 10 发充能，且每天黎明时恢复 1d6+4 发已消耗的充能。当充能耗尽时，骰一次 d20。如果结果为 1，法杖将变为一把无魔法的长棍。
法术 Spells。你可以用一个动作消耗 1 发或更多充能从法杖施展以下法术之一（使用你自身的法术豁免 DC）：
化兽为友 animal friendship（1 充能）、动物交谈术 speak with animals（1 充能）、树肤术 barkskin（2 充能）、动植物定位术 locateanimals or plants（2 充能）、植物交谈术 speak with plants（3充能）、启蒙术 awaken（5 充能）、荆棘之墙 wall of thorns（6充能）。
你也可以用一个动作从法杖施展行踪无迹 pass withouttrace 而无需消耗充能。
树形态 Tree Form。你可以用一个动作并消耗 1 发充能把法杖的一端插入肥沃的土地，将它变为一颗健壮的树。树高60 尺、树干直径 5 尺、树冠半径 20 尺。这棵树看起来和普通的树没有区别，但在侦测魔法 detect magic 的效应下会放出微弱的变化系灵光。你可以在接触树时用一个动作说出命令语，将它变回法杖形态。树变回法杖时，树上的生物都将掉下来。
雷霆法杖 Staff of Thunder And Lightning法杖，极珍稀（需同调）该法杖可以用作一把魔法长棍持用，你用它发动的攻击检定和伤害掷骰获得+2 加值。法杖具有以下属性。使用法杖的某一属性后，直到第二天黎明前其该属性都无法再次启动。
电闪 Lightning。当你用这把法杖以近战攻击命中目标时，你可以令目标受额外 2d6 的闪电伤害。
雷鸣 Thunder。当你用这把法杖以近战攻击命中目标时，你可以使法杖爆出一阵 300 尺内都清晰可闻的雷鸣。目标必须进行一次 DC 17 的敏捷豁免，失败则被震慑到你的下一回合结束。
闪电击 Lightning Strike。你可以用一个动作从法杖尖端射出一束宽 5 尺、长 120 尺的闪电。在闪电束路径上的生物必须进行一次 DC 17 的敏捷豁免，失败则受 9d6 的闪电伤害，成功则伤害减半。
雷霆 Thinderclap。你可以用一个动作使法杖发出在 600尺内都清晰可闻的刺耳雷鸣。你周围 60 尺除你以外的生物必须进行一次 DC 17 的体质豁免，失败则受 2d6 的雷鸣伤害并耳聋 1 分钟。豁免成功的生物只受一半伤害且不会耳聋。
雷电 Thinder and Lightning。你可以用一个动作同时启动闪电击和雷霆两个特性。这样做不会消耗闪电击或雷霆的使用次数，只会消耗雷电的使用次数。
"""

magic_item_withering_staff = """
# 凋零法杖 Staff of Withering
法杖，珍稀（需牧师、德鲁伊或邪术师同调）
凋零法杖有 3 发充能，且每天黎明时恢复 1d3 发已消耗的充能。
该法杖可以用作一把魔法长棍持用。当你用这把法杖命中目标时，除了造成普通长棍的伤害外，你还可以消耗 1 发充能以对目标造成额外 2d10 的黯蚀伤害。此外，目标必须成功通过一次 DC 15 的体质豁免否则它基于力量或体质的属性检定或豁免检定将具有劣势，其效应持续 1 小时。
"""

magic_item_earth_elementals_stone = """
# 命令元素石核 Stone of Controlling EarthElementals
奇物，珍稀
只要这块石头与地面接触，你就可以用一个动作说出它的命令语并召唤一个土元素 earth elemental，如同你施展了召唤元素生物 conjure elemental 法术。直到次日黎明前石头无法再次启动。命令元素石核重 5 磅。
幸运石 Stone of Good Luck (Luckstone)奇物，非普通（需同调）把这块光亮的玛瑙 agate 带在身上时，你在属性检定和豁免获得+1 加值。
"""

magic_item_sun_blade = """
# 阳炎剑 Sun Blade
武器（长剑），珍稀（需同调）
这件物品看起来像是一把长剑的剑柄。持握剑柄时，你可以用一个附赠动作展开或是解消这把剑完全由光构成的剑刃。
展开剑刃的阳炎剑是一把具有灵巧属性的魔法长剑。如果你拥有长剑或短剑的熟练项，则你也能熟练使用阳炎剑。
你在使用阳炎剑发动的攻击检定和伤害掷骰获得+2 加值，但它造成光耀伤害而非挥砍伤害。被这把剑命中的不死生物将额外受 1d8 的光耀伤害。
阳炎剑剑刃放出的光视为阳光，并提供 15 尺明亮光照和额外 15 尺微光光照。剑刃展开时，你可以用一个动作使明亮与微光光照半径各扩大或缩小 5 尺。光照范围上限为明亮和微光区域各扩大 30 尺，下限为各缩小 10 尺。
"""

magic_item_answering_sword = """
# 应答之剑 Sword of Answering
武器（长剑），传说（需阵营与剑相同的生物同调）
在灰鹰世界中，已知存在的这种剑仅有九把。这些剑都是传说中被称为“最终遗言 Final Word”的宝剑弗拉格拉克Fragarach 的仿制品。九把剑的名字和阵营各不相同，且把手末端镶有不同宝石。
你在使用此剑发动的攻击检定和伤害掷骰获得+3 加值。
此外，持握该剑时，你可以用反应对你触及范围内任何一个对你造成伤害的生物发动一次攻击。这次攻击的攻击检定具有优势，且这次攻击造成的伤害忽略目标任何伤害免疫或抗性。

# table
名称 阵营 宝石
解答者 Answer 混乱善良 翡翠 emerald
还击者 Back Talker 混乱邪恶 黑玉 jet
定论者 Concluder 守序中立 紫晶 amethyst
讥讽者 Last Quip 混乱中立 电气石 tourmaline
驳斥者 Rebutter 中立善良 黄玉 topaz
答复者 Replier 绝对中立 橄榄石 peridot
反驳者 Retorter 守序善良 蓝晶 aquamarine
潜伏者 Scather 守序邪恶 石榴石 gatnet
毁灭者 Squelcher 中立邪恶 尖晶石 spinel
"""

magic_item_life_stealing_sword = """
# 窃命剑 Sword of Life Stealing
武器（任意剑），珍稀（需同调）
当你用这把魔法武器攻击一名非构装非不死的生物并骰出 20 时，目标额外受 10 点黯蚀伤害，且你获得 10 点临时生命值。
"""

magic_item_sharpness_sword = """
# 锋锐之剑 Sword of Sharpness
武器（任意造成挥砍伤害的剑），极珍稀（需同调）
用这把魔法剑命中物件时，武器的伤害掷骰将直接取满。
用这把武器攻击生物并投出 20 时，该目标额外受 14 点挥砍伤害。并再骰一次 d20，如果结果依然为 20，则你可以切掉目标一条肢体。对于没有肢体的生物，你可以切掉它躯体的一部分。由 DM 判断这种损伤的效应。
另外，你可以说出剑的命令语使剑身放出亮光，提供 10尺的明亮光照和额外 10 尺的微光光照。要熄灭亮光时，你可以再次说出命令语或是收起武器。
"""

magic_item_vengeance_sword = """
# 复仇之剑 Sword of Vengeance
武器（任意剑），非普通（需同调）
你在用该魔法武器发动攻击检定和伤害掷骰时获得+1 加值。
诅咒 Curse。这把剑被寄宿其中一个渴望复仇的精魂所诅咒，与之同调的生物将受到其诅咒影响。只要诅咒还在生效，你总是会把剑带在身边，不愿与它分开。与这把剑的同调持续期间，你在用其他武器进行的攻击检定和伤害掷骰具有劣势。
持握该剑时，每当你在战斗中受到伤害，你就必须进行一次 DC 15 的感知豁免。如果豁免失败，则你必须持续攻击对你造成伤害的生物，直到你的生命值降至 0 或你的无法到达近战攻击距离以对该发动近战攻击为止。
你可以用常见方式解除剑上的诅咒，也可以对剑施展放逐术 banishment 以驱逐其中寄宿的复仇精魂。此后，这把剑将变为一把普通的+1 武器。
"""

magic_item_wounding_sword = """
# 血光剑 Sword of Wounding
武器（任意剑），珍稀（需同调）
这把武器造成的伤害只能通过短休或长休恢复。再生、魔法或其他任何手段都无法治愈这种伤害。
你每回合有一次机会，在用该剑命中一名生物时对它造成流血效应。在目标的每回合开始时，它将因每层流血效应受1d4 的黯蚀伤害。之后，它可以进行一次 DC 15 的体质豁免，成功则终止自己承受的所有流血效应。另外，流血的生物或是它周围 5 尺内的其他生物可以用一个动作进行一次 DC 15 的感知（医药）检定，成功则终止该生物承受的所有流血效应。
"""

magic_item_pure_good_talisman = """
# 纯善护符 Talisman of Pure Good
奇物，传说（需善良阵营生物同调）
这枚护符是至善的象征。接触到护符的非善良非邪恶生物受 6d6 的光耀伤害，邪恶生物则受到 8d6 的光耀伤害。如果这两类生物在自己回合结束时仍握持或携带该护符，则会再次受到等量伤害。
善良的牧师或圣武士可以将纯善护符当作圣徽使用，持握或佩戴它时其法术攻击检定获得+2 加值。
该护符有 7 发充能。持握或佩戴它时，你可以用一个动作消耗 1 发充能并指定你周围 120 尺内地面上一个你能看见的生物。如果目标属于邪恶，则一道冒着火焰的裂隙将在它脚下打开。目标必须成功通过一次 DC 20 的敏捷豁免否则坠入裂隙，尸骨无存。裂隙随后将不留痕迹地关闭。充能耗尽后，护符将被摧毁，并化为闪着金光的尘埃。
"""

magic_item_sphere_talisman = """
# 法球护符 Talisman of The Sphere
奇物，传说（需同调）
持握此护符时，你要操控湮灭法球 sphere of annihilation而作的智力（奥秘）检定可以加上双倍熟练加值。另外，如果在你回合开始时你操纵着一个湮灭法球，则你可以用一个动作将法球升起 10 尺外加 10×智力调整值的尺数。
"""

magic_item_ultimate_evil_talisman = """
# 至恶护符 Talisman of Ultimate Evil
奇物，传说（需邪恶阵营生物同调）
这枚护符是至恶的象征。接触到护符的非善良非邪恶生物受 6d6 的黯蚀伤害，善良生物则受 8d6 的黯蚀伤害。如果这两类生物在自己回合结束时仍握持或携带着护符，则会再次受到等量伤害。
邪恶的牧师或圣武士可以将至恶护符当作圣徽使用，持握或佩戴它时进行的法术攻击检定获得+2 加值。
至恶护符有 7 发充能。持握或佩戴它时，你可以用一个动作，消耗 1 发充能并选择你周围 120 尺内地面上一个你能看见的生物。如果目标属于善良，则一道冒着火焰的裂隙将在它脚下打开。目标必须成功通过一次 DC 20 的敏捷豁免否则坠入裂隙，尸骨无存。裂隙随后将不留痕迹地关闭。充能耗尽后，护符将被摧毁，化为散发着恶臭的粘液。
"""

magic_item_tentacle_rod = """
# 触须权杖 Tentacle Rod
权杖，珍稀（需同调）
这把卓尔制造的权杖属于魔法武器，末端是三条有弹性的触手。持握权杖时，你可以用一个动作令三条触手各对 15尺内的一个目标发动一次攻击。触手的近战攻击加值为+9，命中时造成 1d6 的钝击伤害。如果三条触手都命中了同一个目标，则目标必须进行一次 DC 15 的体质豁免，失败则速度减半，其敏捷豁免将承受劣势，且在 1 分钟内无法执行反应。
另外，在目标的回合内它只能执行一个动作或执行一个附赠动作。目标在自己的每个回合结束时可以重新尝试豁免，成功则终止其相应的效应。
"""

magic_item_clear_thought_tome = """
# 静思卷册 Tome of Clear Thought
奇物，极珍稀
这本书的文字蕴含魔力，记载了训练记忆力和逻辑思维的方法。如果你在至多 6 日内花费累计 48 小时研究这本书的内容并按其中的方法训练，你的智力和智力上限将提高 2。此后静思卷册将失去魔力，直到一个世纪后才会恢复。
"""

magic_item_leadership_influence_tome = """
# 统御卷册 Tome of Leadership And Influence
奇物，极珍稀
这本书的文字蕴含魔力，记载了影响和吸引他人的方法。
如果你在至多 6 日内花费累计 48 小时研究这本书的内容并按其中的方法训练，你的魅力和魅力上限将提高 2。此后统驭卷册失去魔力，直到一个世纪后才会恢复。
"""

magic_item_stilled_tongue_tome = """
# 静语卷册 Tome of The Stilled Tongue
奇物，传说（需法师同调）
这本厚重皮革包覆的卷册封面上钉着一条风干的舌头。
共存在 5 本这样的卷册，但无人知晓哪本才是原版。巫妖神，守秘者维克 Vecna 那将一名背叛他的仆人的舌头割下，制作了原版静语卷册封面的可怕装饰。其它四本复制品封面的舌头则来自于冒犯了维克那的施法者。卷册的前几页充满了无法理解的草稿，剩余的页则空白如新。
同调此卷册的人可以用它作为法术书和法器。持握此书时，你可以用一个附赠动作施展一个记录在书中的法术，而无需提供言语和姿势构材，也无需消耗法术位。此后该属性直到次日黎明前都无法再次启动。
与卷册同调时，你可以移除书封面的舌头，这将永久抹消书中记录的所有法术。
维克那留意着任何使用卷册的人。他可以向书内写入密文。这些密文会在午夜出现，在被人阅读后即消失不见。
"""

magic_item_understanding_tome = """
# 通晓卷册 Tome of Understanding
奇物，极珍稀
这本书的文字蕴含魔力，记载了训练直觉和洞察力的方法。如果你在至多 6 日内花费累计 48 小时研究这本书的内容并按其中的方法训练，你的感知和感知上限将提高 2。此后通晓卷册失去魔力，直到一个世纪后才会恢复。
"""

magic_item_fish_command_trident = """
# 唤鱼三叉戟 Trident of Fish Command
武器（三叉戟），非普通（需同调）
该三叉戟是一把魔法武器。它有 3 发充能。持握它时，你可以用一个动作并消耗 1 发充能以对一只有天生游泳速度的野兽施展支配野兽 dominate beast（DC 15）。该三叉戟每天黎明时恢复 1d3 发已消耗的充能。
"""

magic_item_universal_solvent = """
# 万溶剂 Universal Solvent
奇物，传说
这管乳白色的液体散发着浓烈的酒精气味。你可以用一个动作将管中液体倒在触及范围内的某表面上。万溶剂将立刻溶解它接触到的至多 1 立方尺的粘合剂（包括至尊胶sovereign glue）。
"""

magic_item_vicious_weapon = """
# 恶毒武器 Vicious Weapon
武器（任意），珍稀
当你用这把魔法武器发动攻击并骰出 20 时，目标额外受到与武器伤害类型相同的 7 点伤害。
"""

magic_item_vorpal_sword = """
# 斩首剑 Vorpal Sword
武器（任意造成挥砍伤害的剑），传说（需同调）
你在使用此魔法武器发动的攻击检定和伤害掷骰获得+3加值，并忽略挥砍抗性。
当你命中一名有头生物并投出 20 时，你砍下该生物的一颗头。如果该生物无法在失去头的情况下生存，则它将随之死亡。免疫挥砍伤害、没有头、不需要头、有传奇动作或 DM 认为体型太大无法被斩首的生物免疫斩首效应，但额外受到 6d8的挥砍伤害。
"""

magic_item_binding_wand = """
# 定身魔杖 Wand of Binding
魔杖，珍稀（需施法者同调）
这把魔杖有 7 发充能，且每天黎明时恢复 1d6+1 发已消耗的充能。当充能耗尽时，骰一次 d20。如果骰值为 1，魔杖将化为灰烬而毁灭。
法术 Spells。持握此魔杖时，你可以用一个动作并消耗若干充能以施展下列法术之一（豁免 DC 17）：
人类定身术 holdperson（2 充能）、怪物定身术 hold monster（5 充能）援助脱离 Assisted Escape。持握此魔杖时，你可以用反应并消耗 1 发充能，使你在进行一次避免麻痹或束缚的豁免时获得优势。你也可以使用反应并消耗 1 发充能在一次脱离擒抱的检定中获得优势。
"""

magic_item_enemy_detection_wand = """
# 搜敌魔杖 Wand of Enemy Detection
魔杖，珍稀（需施法者同调）
这把魔杖有 7 发充能。持握此魔杖时，你可以用一个动作说出命令语并消耗 1 发充能。你以此获知 60 尺内离你最近对你有敌意的生物所在方向，但不知道距离，效应持续 1 分钟。魔杖可以感知可见的、隐形的、灵体的、伪装的以及躲藏的生物。你不再持握魔杖时，其效应也随之终止。
该魔杖每天黎明时恢复 1d6+1 发已消耗的充能。当充能耗尽时，骰一次 d20。如果骰值为 1，魔杖将化为灰烬而毁灭。
"""

magic_item_fear_wand = """
# 恐惧魔杖 Wand of Fear
魔杖，珍稀（需同调）
该魔杖有 7 发充能，且每天黎明时恢复 1d6+1 发已消耗的充能。当充能耗尽时，骰一次 d20。如果骰值为 1，魔杖将化为灰烬而毁灭。
命令 Command。持握此魔杖时，你可以用一个动作并消耗 1 发充能以命令一名生物逃跑或趴下（如同命令术command，豁免 DC 15）。
恐惧力场 Cone of Fear。持握此魔杖时，你可以用一个动作并消耗 2 发充能，令魔杖尖端发出 60 尺锥状的橙光。锥状区域内的每名生物必须成功通过一次 DC 15 的感知豁免否则对你恐慌 1 分钟。因此效应恐慌的生物每轮必须以其移动力尽可能远离你且无法自愿进入你周围 30 尺范围内。使用自己的动作时，它只能执行疾走 Dash 动作或是尝试逃离某种阻止它移动的效应。它无法执行反应。如果无处可逃，则它会可以执行闪避 Dodge 动作。受此效应影响的生物在其每轮结束时可以再次尝试豁免，成功则终止自己身上的相关效应。
"""

magic_item_fireball_wand = """
# 火球魔杖 Wand of Fireballs
魔杖，珍稀（需施法者同调）
这把魔杖有 7 发充能。持握此魔杖时，你可以用一个动作并消耗 1 发或更多充能以施展火球术 fireball（豁免 DC 15）。
施展 3 环火球术 消耗 1 发充能，每多消耗 1 发充能法术环阶也提升一阶。
该魔杖每天黎明时恢复 1d6+1 发已消耗充能。当充能耗尽时，骰一次 d20。如果骰值为 1，魔杖将化为灰烬而毁灭。
"""

magic_item_lightning_bolts_wand = """
# 闪电束魔杖 Wand of Lightning Bolts
魔杖，珍稀（需施法者同调）
这把魔杖有 7 发充能。持握此魔杖时，你可以用一个动作并消耗 1 发或更多充能以施展闪电束 lightning bolt（豁免DC 15）。施展 3 环闪电束 消耗 1 发充能，每多消耗 1 发充能法术环数也增加一阶。
该魔杖每天黎明时恢复 1d6+1 发已消耗的充能。当充能耗尽时，骰一次 d20。如果骰值为 1，魔杖将化为灰烬而毁灭。
"""

magic_item_magic_detection_wand = """
# 搜魔魔杖 Wand of Magic Detection
魔杖，非普通
这把魔杖有 3 发充能，且每天黎明时恢复 1d3 发已消耗的充能。持握此魔杖时，你可以用一个动作并消耗 1 发充能以施展侦测魔法 detect magic。
"""

magic_item_magic_missiles_wand = """
# 魔法飞弹魔杖 Wand of Magic Missiles
魔杖，非普通
这把魔杖有 7 发充能，且每天黎明时恢复 1d6+1 发已消耗的充能。当充能耗尽时，骰一次 d20。如果骰值为 1，魔杖将化为灰烬而毁灭。
持握此魔杖时，你可以用一个动作并消耗 1 发或更多充能以施展魔法飞弹 magic missile。施展 1 环魔法飞弹 消耗 1发充能，每多消耗 1 发充能法术环数也增加一阶。
"""

magic_item_paralysis_wand = """
# 麻痹魔杖 Wand of Paralysis
魔杖，珍稀（需施法者同调）
这把魔杖有 7 发充能。持握此魔杖时，你可以用一个动作并消耗 1 发充能从魔杖尖端向 60 尺内一名你能看到的生物射出一道纤细的蓝色光线。目标必须成功通过一次 DC 15的体质豁免否则麻痹 1 分钟。目标可以在它的每回合结束时再次尝试豁免，成功则不再麻痹。
魔杖每天黎明时恢复 1d6+1 发已消耗的充能。当充能耗尽时，骰一次 d20。如果骰值为 1，魔杖将化为灰烬而毁灭。
"""

magic_item_polymorph_wand = """
# 变形魔杖 Wand of Polymorph
魔杖，极珍稀（需施法者同调）
这把魔杖有 7 发充能，且每天黎明时恢复 1d6+1 发已消耗的充能。当充能耗尽时，骰一次 d20。如果骰值为 1，魔杖将化为灰烬而毁灭。
持握此魔杖时，你可以用一个动作并消耗 1 发充能以施展变形术 polymorph（豁免 DC 15）。
"""

magic_item_secret_wand = """
# 探秘魔杖 Wand of Secrets
魔杖，非普通
这把魔杖有 3 发充能，且每天黎明时恢复 1d3 发已消耗的充能。持握此魔杖时，你可以用一个动作并消耗 1 发充能以侦测你周围 30 尺内的密门或陷阱。如果范围内有密门或陷阱，魔杖将跳动着指向离你最近的一个。
"""

magic_item_war_mage_wand = """
# 战法师魔杖 Wand of The War Mage，+1、+2 或+3
魔杖，非普通（+1），珍稀（+2），极珍稀（+3）（需施法者同调）
持握此魔杖时，你的法术攻击检定获得加值。加值的数值取决于魔杖的稀有度。另外，你在使用法术攻击时忽略半身掩蔽状态。
"""

magic_item_web_wand = """
# 蛛网魔杖 Wand of Web
魔杖，非普通（需施法者同调）
这把魔杖有 7 发充能，且每天黎明时恢复 1d6+1 发已消耗的充能。当充能耗尽时，骰一次 d20。如果骰值为 1，魔杖将化为灰烬而毁灭。
持握此魔杖时，你可以用一个动作并消耗 1 发充能以施展蛛网术 web（豁免 DC 15）。
"""

magic_item_wonder_wand = """
# 惊异魔杖 Wand of Wonder
魔杖，珍稀（需施法者同调）
这把魔杖有 7 发充能。持握此魔杖时，你可以用一个动作消耗 1 发充能并选择你周围 120 尺内的一名生物、一个物件或空间中的一点为目标。骰 d100 然后参考下表决定效应。
如果魔杖的效应为让你施展一个法术，则该法术豁免 DC为 15。如果该法术的施法范围以尺计算，则其施法范围变为120 尺。
如果魔杖的效应覆盖一个范围区域，则你必须以目标为中心并包括它在内。如果魔杖的效应影响多个单位，由 DM 随机决定哪些单位受到影响。
该魔杖每天黎明时恢复 1d6+1 发已消耗的充能。当充能耗尽时，骰一次 d20。如果骰值为 1，魔杖将化为灰烬而毁灭。
"""

magic_item_weapon = """
武器 Weapon，+1、+2 或+3
武器（任意），非普通（+1），珍稀（+2），极珍稀（+3）你
在用此魔法武器发动的攻击检定和伤害掷骰获得加值。
加值的数值取决于武器的稀有度。
"""

magic_item_warning_weapon = """
# 警戒武器 Weapon of Warning
武器（任意），非普通（需同调）
这把魔法武器能在危险时给你警告。持有此武器时，你进行先攻检定时具有优势。除非因非魔法睡眠以外的原因陷入失能，否则你和你周围 30 尺内的同伴不会被突袭。如果战斗开始时你或范围内你的同伴处于自然睡眠状态，则该武器的魔法也会将你们唤醒。
"""

magic_item_many_worlds_well = """
# 诸界之井 Well of Many Worlds
奇物，传说
这块丝绸般柔软的精致黑色布料折叠起来有手帕大小，展开时则为半径 6 尺的圆形。
你可以用一个动作展开诸世界之井并把它放在坚实表面上，产生一扇通向另一个位面的双向传送门。每次诸界之井展开时，由 DM 决定它所连接的位面。你可以用一个动作抓住布料的边缘把它折叠起来，将传送门关闭。使用后，诸界之井在 1d8 小时内将无法再次启动。

# d-100
d100 效应
01~05 你施展缓慢术 slow。
06~10 你施展妖火 faerie fire。
11~15 你感觉刚刚发生了什么令人惊叹的事，因此被震慑到你的下一回合开始。
16~20 你施展造风术 gust of wind。
21~25 你对目标施展侦测思想 detect thoughts。如果你选择的目标不是生物，则你受到 1d6 的心灵伤害。
26~30 你施展臭云术 stinking cloud。
31~33 以目标为中心半径 60 尺的范围内落下大雨，使该区域变为轻度遮蔽。大雨持续到你的下一回合开始。
34~36 目标附近最近的未被占据空间内出现一只动物。该动物不受你控制而按其天性行动。投 d100 决定具体出现的动物。骰值为 01~25 为一只犀牛 rhinoceros,骰值为 26~50 为一头象 elephant，骰值为 51~100 为一只老鼠 rat。动物的资料详见《怪物图鉴》。
37~46 你施展闪电箭 lightning bolt。
47~49 以目标为中心半径 30 尺的范围内出现 600 只巨大的蝴蝶，使该区域变为重度遮蔽。蝴蝶将存在 10 分钟。
50~53 你对目标施展变巨/缩小术 enlarge/reduce 并选取变巨效应。如果目标无法被该法术影响，则你变为法术的目标。
54~58 你施展黑暗术 darkness。
59~62 以目标为中心半径 60 尺的范围内长出草。如果该区域原本就生长着草，则草长至原本的十倍长短并保持 1 分钟。
63~65 由 DM 选择，目标周围 120 尺内一件在任一方向都不超过 10 尺且未被着装或携带的物件消失并进入以太位面。
66~69 你对自己施展变巨/缩小术 enlarge/reduce 并选取缩小效应。
70~79 你施展火球术 fireball。
80~84 你对自己施展隐形术 invisibility。
85~87 目标长出树叶。如果你选择的目标为空间中的一点，则距该点最近的生物身上长出树叶。除非树叶被摘下，否则它们将在 24 小时后变黄并凋落。
88~90 一股宝石的激流（1d4 x 10 颗宝石，每颗价值 1gp）从魔杖尖端喷出，影响 30 尺长、5 尺宽的线状区域。每颗宝石造成 1 点钝击伤害，伤害由范围内的生物均分。
91~95 你发出一阵多彩的闪光。你和你周围 30 尺半径范围内的每名生物必须成功通过一次 DC 15 的体质豁免否则目盲 1 分钟。受影响的生物在自己的每个回合结束时可以重新尝试豁免，成功则终止效应对自己的影响。
96~97 目标的皮肤变成蓝色 1d10 日。如果你选择的目标为空间中的一点，则距该点最近的生物受此影响。
98~00 如果你选择的目标是生物，则它必须进行一次 DC 15的体质豁免。如果你选择的目标不是生物，则你变作为目标且必须进行一次体质豁免。如果目标的豁免结果比 DC 低出 5 或低，则它将立即被石化。其他失败的情况下，目标将被束缚并渐渐变为石头。目标在自己的下一回合结束时，必须再次进行体质豁免，失败则被石化，成功则终止效应。此石化效应将一直持续，直到被高等复原术 greater restoration 或类似魔法效应解除。
"""

magic_item_wind_fan = """
# 造风之扇 Wind Fan
奇物，非普通
持握这把扇子时，你可以用一个动作施展造风术 gust ofwind（豁免 DC 13）。使用扇子后，在次日黎明前每次再次启动它都会累加 20%的失败概率。失败时，扇子也将被撕裂成无魔法的废纸。
"""

magic_item_winged_boots = """
# 飞翼之靴 Winged Boots
奇物，非普通（需同调）
着装这双靴子时，你获得等同于你步行速度的飞行速度。
你可以使用飞翼之靴连续或间断的飞行 4 小时，并以分钟为单位计算使用时间。如果你在飞行期间耗尽其使用时间，则你将以每轮 30 尺的速度下落，直到着陆。
停止使用靴子达 12 小时将为它恢复 2 小时的使用时间。
"""

magic_item_wings_of_flying = """
# 飞翼斗篷 Wings of Flying
奇物，珍稀（需同调）
着装这件斗篷时，你可以用一个动作说出它的命令语，并将斗篷转变为你背上的一对蝙蝠翅膀或鸟类翅膀。这种转变持续 1 小时或直到你再次用一个动作说出命令语。这对翅膀赋予你 60 尺的飞行速度。斗篷使用完毕后，你必须再等待1d12 小时才能再次启动它。
"""

article_sentient_magic_items = """
# 智能魔法物品 Sentient Magic Items
一些魔法物品拥有感情和人格。这样的物品可能因为被之前所有者的精神影响，或者是创造时的魔法让他们产生意识，无论如何，这些物品就像角色一样，他们会有怪癖，理想，牵绊或某些缺点。智能魔法物品可能是持有者珍贵的盟友，也可能是他们暗地里不断的烦扰。
绝大多数的智能物品是武器，而其他类型的这种物品可能能够操控心灵，但是消耗性物品如魔药或者卷轴等绝不会是智能物品。
智能魔法物品就像 NPC 一样受 DM 控制。物品的任何特殊属性都被物品自身掌控，而非其持有者。如果持有者和物品保持良好的关系，持有者则能够正常的使用物品的特殊能力。
否则，物品会压制自己的特殊能力，甚至于伤害持有者。

# 创作智能魔法物品 Creating Sentient Magic Items
当你要创造一个智能魔法物品时，你要像创造 NPC 一样赋予物品人格，外加下述内容。

# 属性值 Abilities
智能魔法物品有智力、感知、魅力属性。你可以自己决定物品的属性或者随机分配其属性。如果随机决定的话，为每个属性骰一次 4d6 来随机决定物品的属性。

# 交流方式 Communication
智能魔法物品有一定的交流能力，它们会表达自己的情绪，心灵感应传递思想，或是直接大声的说出来。你可以按照下表决定物品的交流方式感官 Senses随着其智能觉醒。智能魔法物品能够有限的感知它周围的环境。你可以按照下表决定物品感知周围环境的能力。

# d-100
d100 交流方式
01~60 物品向持有者或持握者传递情绪进行交流。
61~90 物品能够听、说、读一门或多门语言。
91~100 物品能够听、说、读一门或多门语言，并且还能与
持有者通过心灵感应进行交流。

# 感官 Senses
随着其智能觉醒。智能魔法物品能够有限的感知它周围的环境。你可以按照下表决定物品感知周围环境的能力。

# d-4
d4 感官
１ 听力与正常视觉 30 尺
２ 听力与正常视觉 60 尺
３ 听力与正常视觉 120 尺
４ 听力与黑暗视觉 120 尺

# 阵营 Alignment
智能魔法物品有阵营。它的创造者或其本性会使其倾向某个阵营。如果没有被赋予，则你可以赋予它一个阵营，或者按照下表决定其阵营。

# d-100
d100 阵营
01~15 守序善良
16~35 中立善良
36~50 混乱善良
51~63 守序中立
64~73 绝对中立
74~85 混乱中立
86~89 守序邪恶
90~96 中立邪恶
97~00 混乱邪恶

# 性格 Characteristics
用第 4 章关于设定 NPC 的信息决定智能魔法武器的行为态度、个性特点、理想、牵绊与缺点。你也可以按本章前文“专有特征”一节的信息进行确定。
如果你想随机选择物品的性格，可以尝试忽视或者调整那些不适用于无生机物件的性格。你可以重掷这些性格，直到得到一个你满意的结果为止。

# 目标 Special Purpose
你可以给智能魔法物品设定一个追随的目标，甚至让其排斥除目标外的其他事物。只要持有者的使用方式与物品的目标一致，物品便会愿意和持有者合作。与物品目标违背有可能导致物品与持有者发生分歧，甚至导致物品压制自身的特殊属性。你可以选择一个目标或者按照下表决定目标

# d-10
d10 目标
1 阵营 Aligned：打败或摧毁对立阵营（这样的物品通常都不是绝对中立阵营）。
2 祸害 Bane：打败或摧毁特殊生物类型（比如邪魔，变形生物，巨魔或法师）。
3 守护者 Protector：守护特殊种族或生物种类（比如精灵，德鲁伊）。
4 十字军 Crusader：打败、削弱或摧毁特定神祇的信徒。
5 圣殿骑士 Templar：守护特定神祇的信徒。
6 破坏者 Destoryer：渴望破坏且催促其使用者战斗。
7 荣誉追寻者 Glory Seeker：希望通过帮助使用者成为声名远扬或是臭名昭著的形象，使自己成为世上最伟大的魔法物品。
8 学识追寻者 Lore Seeker：渴望知识或者致力于解决谜题，知晓秘密，通晓晦涩的预言。
9 命运追寻者 Destiny Seeker：认为自己和持用者在将来会成为重要人物。
10 根源追寻者 Creator Seeker：寻找它的创造者，希望知道自己被创造的原因。

# 对抗 Conflict
一个智能魔法物品有自己的意愿，并受其性格和阵营影响。如果它的持用者其行为与物品的阵营和目标不符，则物品可能会奋起反抗。这种反抗发生时，该物品需要进行一个检定和持有者的检定进行对抗（该检定基于魅力），如果物品在对抗中获胜，则物品会对持有者有下列一项或多项的要求：
• 物品要求持有者一直携带或着装自己。
• 物品要求持有者丢弃所有它反感的物品。
• 物品要求持有者专心地追求物品的目标。
• 物品要求持有者将它送给别人。
如果持有者拒绝物品的要求，则物品会做下列一项或多项的事情：
• 让持用者不能与其同调。
• 压制自己一项或多项特殊属性。
• 尝试控制其持用者。
如果智能魔法物品尝试操控其持用者，则持用者必须进行一次魅力检定，其 DC 为 12＋该物品的魅力调整值。如果检定失败，则持有者被魅惑 1d12 小时。在被魅惑的时候，持用者必须尽其所能听从物品的命令。如果持用者受到伤害，则它可以再次进行豁免，成功则终止该魅惑效应。不论这次魅惑尝试是否成功，该物品直至第二天黎明前都无法再次尝试。

# 智能魔法物品范例 Sample Sentient Items
以下描述的一些智能武器都带着悠久的历史。
"""

sentient_item_blackrazor = """
# 黑刃 Blackrazor
武器（巨剑），传说（需非守序阵营同调）
黑刃 藏在白羽山 White Plume Mountain 的地下城中，它像夜空中的繁星一样闪耀，黑色的剑鞘上镶满了切割好的黑曜石。
使用该魔法武器发动攻击检定和伤害掷骰时具有+3 加值。
它还具有以下额外属性。
吞噬灵魂 Devour Soul。当你用它将一个生物的生命值降到 0 时，这把剑会杀死这个生物并且吞噬它的灵魂。不死生物和构装生物不受影响。被暗黑刃 吞噬灵魂的生物只能通过祈愿术 wish 复活。
每当黑刃吞噬一个灵魂时，它会赐予你被杀死生物的最大生命值作为你的临时生命值。该临时生命值持续存在 24 小时。只要这些临时生命值存在且你正手握黑刃，那么你的攻击检定、豁免检定和属性检定均带有优势。
当你用这把武器击中不死生物时，你将受 1d10 的黯蚀伤害，目标恢复 1d10 生命值。如果黯蚀伤害将你的生命值降至0，则黑刃将会吞噬你的灵魂。
灵魂猎手 Soul Hunter。你手持这把武器时，能够意识到60 尺内超小型或更大体型的非构装体非不死生物类型的其他生物。你陷入魅惑或者恐慌时，这项属性失效。
黑刃 每天可以对你使用一次加速术 haste。它会自己决定什么时候施展该法术并维持专注，所以你在法术生效时不必维持专注。
智能 Sentience。
黑刃 是一把混乱中立的智能魔法武器。
它的智力为 17，感知 10，魅力 19。它的听觉和黑暗视觉的感官范围为 120 尺。
这把武器能够说、读和理解通用语，同时也能够与持有者通过心灵感应进行交流。它的声音低沉且带有回声。当你与之完成同调后，黑刃 也能听懂你掌握的所有语言。
个性 Personality。黑刃的语气带着傲慢，好像习惯别人服从于它。
这把剑的目标是吞噬灵魂，它并不在乎吞噬谁的灵魂，哪怕是其持用者。这把剑相信所有的物质与能量都来源于负能量的虚无之中，且终将有一日一切都将回归其中。
黑刃 则希望能够加快这个过程。
除它信仰的虚无主义以外，黑刃 对波涛 Wave 和征服Whelm 这两把也被封印在白羽山中的剑有着莫名的亲近感。
它希望这三把剑能够重聚并一起战斗，尽管它十分不同意征服 的看法也觉得波涛 很无聊。
黑刃 对灵魂的渴望必须经常得到满足。如果这把剑三日或更长时间没吞噬灵魂，那它就会在次日黄昏时与其持用者进行对抗。
"""

sentient_item_moonblade = """
# 月刃 Moonblade
武器（长剑），传说（需中立善良的精灵或半精灵同调）
在所有精灵制造的魔法物品当中，最有价值也最受严格保护的就是月刃。在远古时期，几乎每个精灵贵族家族都有这样一柄长剑。几个世纪以来，一些月刃 已经销声匿迹，其魔法也随着家族一起消失。还有一些则伴随其持有者消失在执行伟大任务的路上。因此，只有很少月刃 被保留下来。
月刃 在家族中随着辈分传递。它会自己选择其持有者并且会一直忠于其持有者。持有者死亡时，其继承权将传递给其后代。如果没有一个足够强大的后代，则月刃会自行休眠。它平时会像普通长剑一样，直到一个足够强大的灵魂找到它，并需求它的力量。
一柄月刃 同一时间只会侍奉一个主人。它的同调时需要在精灵统治者的王宫中，或在精灵神的神殿中执行一项特殊仪式才能完成。
月刃 不会侍奉他认为懦弱、古怪、堕落或不想护卫精灵族的主人。如果一柄月刃 拒绝了你，那你在接下来的 24 小时内所进行的属性检定、攻击检定和豁免检定均具有劣势。如果一柄月刃 接受你，你与其同调后其剑刃上将出现一个新的符文。你将一直与它保持同调直至死亡或该武器被摧毁。
月刃 每侍奉一个主人，剑刃上就多出一个符文（通常是1d6+1 个）第一个符文通常是让该魔法武器发动的攻击检定和伤害掷骰获得+1 加值。从第二个符文开始，每个符文会给月刃一项额外的属性。DM 可以自行决定每项属性或按照下表随机决定。
智能 Sentience。
月刃 是一把中立善良的智能魔法武器。它的智力是 12，感知 10，魅力 12。它的听觉和黑暗视觉的感官范围为 120 尺。
月刃 想要交流一些自己的感受时，会通过传递情绪以及向持用者手上传递刺痛来进行交流。它会在持用者进行出神trance 或睡梦时以梦境和影像进行更细致的交流。
个性 Personality。每一柄月刃 追求精灵族的进步并且致力于达成精灵族的梦想。勇气、忠诚、美丽、音乐以及生命是它全部的目标。
月刃 与其决心服侍的家族联系在一起。而一旦它与一位和自己理想相通的拥有者建立联系，便会绝对忠诚于对方。
如果月刃 有缺点，那一定是它的自负。它一旦决定了自己的持有者，就会认定只有对方能够持用自己。哪怕其拥有者随后背离了精灵的理想，它也绝不改变。

# d-100 月刃属性 Moonblade Properties
d100 属性
01~40 其攻击检定和伤害掷骰的加值提升 1，最高到+3，如果月刃 已经有了+3 的加值则重骰。
41~80 月刃 随机获得一项小增益（见前文“专有特征”）。
81~82 月刃 获得灵巧 finesse 属性。
83~84 月刃 获得投掷 thrown 属性（射程 20/60 尺）。
85~86 月刃 获得与防御者 defender 一样的功能。
87~90 月刃 的重击范围变为 19~20
91~92 你用 月刃 击中对手时，可以额外造成 1d6 的挥砍伤害。
93~94 你用 月刃 击中特定类型的生物时（例如龙类、邪魔或不死生物），你可以造成 1d6 的额外伤害，伤害类型为强酸、冷冻、火焰、闪电或者雷鸣其中之一。
95~96 你可以用附赠动作让月刃 闪光。每个在你身边 30 尺且能看到你的生物必须成功通过一次 DC 15 的体质豁免，否则将会目盲 1 分钟。每个生物在其自己的回合结束时重掷该豁免直到它豁免成功。该特殊属性只能在短休前使用一次，你也必须先与该武器同调。
97~98 月刃 获得与储法戒指 ring of spell storing 一样的功能
99 你可以用一个动作召唤一个幽影精灵 elfshadow，你在同一时间里只呢拥有一个幽影精灵。影精灵将随机出现在你周围 120 尺一处未被占用空间。他使用《怪物图鉴》中幽影 shadow 的资料，只是其阵营为绝对中立，且免疫驱散亡灵以及不能创造新的幽影。你可以控制幽灵精灵，决定它的行动方式。它会一直存在直到生命值降至 0 或直至你用一个动作将其解散。
00 月刃 获得与斩首剑 vorpal sword 一样的功能
"""

sentient_item_wave = """
# 波涛 Wave
武器（三叉戟），传说（需海之神的信徒同调）波涛 藏在白羽山的地下城中，这把精致的三叉戟上面雕有波浪、贝壳和海洋生物。尽管你必须是海神的信徒才能与其同调，但波涛 本身也会欣然接受某些新的改变。
你用这把武器发动的攻击检定和伤害掷骰获得+3 的加值。
如果你用它造成重击，目标会额外受相当于其最大生命值一半的黯蚀伤害。
波涛 还有跟唤鱼三叉戟 trident of fish command，以及警戒武器 weapon of warning 一样的功能。你在持握它时，还可以获得如同水下呼吸帽 cap of water breathing 一样的增益。
你还可以用它实现力场魔方 cube of force 的功能，且可以直接选择其效应而无需按压魔方的各面。
智能 Sentience。
波涛 是一把绝对中立的智能魔法武器。
它的智力是 14，感知 10，魅力 18。它的听觉和黑暗视觉的感官范围为 120 尺。
这把武器能够说、读和理解水族语 Aquan，同时也能够与其持用者通过心灵感应进行交流。它可以与水生动物进行交流，如同使用了法术动物交谈 speak with animals，此时还可以用心灵感应让其持用者加入对话。
个性 Personality。
波涛 不安时它会哼唱小曲，曲子可能是船夫曲也有可能是神圣的海神赞歌。
波涛 渴望将凡人转变为信奉诸海神的信徒，或者一直保持无信直到死亡。如果其持用者不能秉持其目标传遍世界，它就会进行对抗。
波涛 对一个叫做雷铸 Thunderforge 的荒凉小岛有所眷恋，因为那正是它的锻造之地。一位海神曾将一个风暴巨人家族监禁在那个小岛中。这些风暴巨人便锻造出这把武器奉献给海神，或是反叛海神。
波涛 一直隐藏着一个关于它天性和目标的秘密。除去它对海神的忠诚，波涛 害怕自己的真正意图是杀死一名海神。而这一命运或许自己终究无法避免。
"""

sentient_item_whelm = """
# 征服 Whelm
武器（战锤），传说（需矮人同调）征服藏在白羽山的地下城中，它是一把由矮人锻造，极具威力的战锤。
你使用这把武器发动的攻击检定和伤害掷骰获得+3 加值。
只要你维持与它同调，从你第一次以征服 掷攻击检定的次日黎明开始，你便会对室外产生恐惧。在白天可以看到天空时，你的攻击检定、豁免检定和属性检定均具有劣势。
投掷武器 Thrown Weapon。
征服 带有投掷属性，常规射程为 20 尺，最大射程 60 尺。当你以远程攻击命中目标时，你对目标造成额外 1d8 的钝击伤害（如果目标是巨人，额外伤害变为 2d8）。你每次掷出该武器后，它会自动飞回你手里。
如果你没有空着的手，则该武器会落在你的脚边。
震荡波 Shock Wave。你可以用一个动作以征服 重击地面，从一点发出震荡波。在你周围 60 尺的所有生物必须进行一次 DC 15 的体质豁免，失败则被震慑 1 分钟。每个生物在自己回合结束时可以重骰该豁免，豁免成功者可以终止自己身上的震慑效应。此后该属性直到次日黎明前都不能再使用。
超然警觉 Supernatural Awareness。持握该武器时，它能让你发现周边 30 尺内的密门。此外，你还可以用一个动作以征服 施展法术侦测善恶 detect evil and good 或物件定位术locate object。施展任一项法术后，直至次日黎明你都无法再用该武器的施法能力。
智能 Sentience。
征服 是一把守序中立的智能魔法武器。
它的智力是 15，感知 12，魅力 15。它听觉与黑暗视觉的感官范围为 120 尺。
这把武器会与持有者通过心灵感应进行交流，它也能说、读和理解矮人语、巨人语和地精语。在战斗时征服 会发出矮人语的呐喊。
个性 Personality。
征服 的目标是杀戮巨人和地精。它也会与所有敌人战斗来保卫矮人。如果持有者不能秉持摧毁巨人与地精或不能秉持守卫矮人时，它便会做出对抗。
征服 与创造它的矮人氏族紧密的联系在一起，该氏族有各种称呼，如丹吉尔 Dankil 或称强锤 Mightyhammer 氏族。征服 渴望回到氏族中。并且会倾其所能来保护矮人一族免受侵害。
征服 也有自己的不能开口的秘密。若干世纪前，一个叫契丹米尔 Ctenmiir 的英勇矮人曾短暂的持用着它。但契丹米尔最后却被变成了一只吸血鬼。他以自己强大的意志强迫征服 为自己的邪恶意图服务，甚至用其杀死了自己部落的成员。
"""

article_artifacts = """
# 神器 Artifacts
神器是极之强大且独一无二的魔法物品，而且各自还有着独特的历史与起源。神器可能创自众神或某些能力卓越的凡人，其创作时机往往是历史上的危难之时。彼时，其存在可能对某个王国，乃至整个世界构成威胁，甚至于影响整个多元宇宙。而正是那关键时期，其存在起着至关重要的作用。
有些神器会在被需要时挺身而出，另一些则长年与世隔绝。而当这些隐世神器被发现时，往往连世界也会为之颤栗不已。为战役做准备设定时，你可以按自己的需求把合适的神器加入其中。该神器可能是敌对势力一直想弄到手的强大物品，也可以是在关键时刻出现并帮助冒险者们克服难关的关键物。
冒险角色不能通过常规的手段获得神器。事实上，神器最好是在你的精心安排下，作为剧情要素兼魔法物品出现在战役中。一般情况下可以在战役中设计寻找并修复神器的冒险，然后让角色们四处打听流言，历经重要试炼，并以身犯险进入危险的偏僻之地寻找神器的踪迹。又或者，让一名大反派持用一件强大的神器，而角色们则设法前去抢夺并摧毁它，以免其力量继续危害世人。

# 神器属性 Artifact Properties
每件神器都拥有独特的魔法属性，与其他普通魔法物品不同的是，其属性通常强大无比。神器的属性往往同时具有增益和减益的效果。你可以从本节的表格里自主或随机的选取神器的属性，并将这些增减益加入你要使用的神器当中。毕竟每件神器重现世间时，这些属性都会发生改变。
一件神器可以拥有最多四项弱效增益属性以及两项强效增益属性，它同时具有最多四项弱效减益属性以及两项强效减益属性。

# 破坏神器 Destroying Artifacts
神器只会在特殊的情况下遭到破坏，其他情况下神器将无视对其造成的任何伤害。
每件神器在创造时都会产生一个可能使之受到破坏的弱点。为了揭示神器的弱点，你必须经过大量的研究或完成某个特定任务。而具体如何才能破坏特定的神器，则由 DM 作最终决定。以下是一些供参考的建议：
• 该神器必须在创造其本身的场所，即某座火山、某个熔炉或某个坩锅中熔化。
• 该神器必须被丢进冥河 River Styx。
• 该神器必须被一只泰拉斯奎巨兽 tarrasque 或其他远古生物吞噬并消化。
• 该神器必须浸涤在一名神灵或一名天使 angel 的血泊中。
• 该神器必须被一件特定的武器无效化，并被其打碎。该武器本身也正是为此而创。
• 该神器必须在一个机械境 Mechanus 的设备内碾碎。
• 该神器必须归还给它的创造者，其创造者的触碰即可使之消灭。

# 神器范例 Sample Artifacts
以下列出的神器曾经出现在 D&D 的世界中。你可以将其作为参考自创新的神器，也可以对其作适当修改后直接使用。
"""

dice_table_minor_beneficial_properties = """
# d-100 弱效增益属性 Minor Beneficial Properties
d100 属性
01~20 与神器同调后，你的某项技能成为熟练项，具体哪项技能则由 DM 选出。
21~30 与神器同调后，你免疫疾病状态。
31~40 与神器同调后，你不再受魅惑或恐慌状态影响。
41~50 与神器同调后，你对某个伤害类型拥有抗性，具体哪种伤害类型由 DM 选出。
51~60 与神器同调后，你能够以一个动作施展一个戏法，具体哪个戏法由 DM 选出。
61~70 与神器同调后，你能够以一个动作施战一个 1 环法术，具体哪个法术由 DM 选出。完成施法后，你可以骰一次 d6。骰值为 1~5 时，则直至第二天黎明前你无法再以该方式施法。
71~80 与 61~70 相同，并把法术替换为一个 2 环法术。
81~90 与 61~70 相同，并把法术替换为一个 3 环法术。
91~00 与神器同调后，你的护甲等级获得＋1 加值。
"""

dice_table_major_beneficial_properties = """
# d-100 强效增益属性 Major Beneficial Properties
d100 属性
01~20 与神器同调后，你的一项属性值提升 2，其总值最高不能超过 24。具体哪项属性由 DM 选出。
21~30 与神器同调后，你将在你的回合开始时恢复 1d6 的生命值，前提是你必须至少还有 1 点生命值。
31~40 与神器同调后，你以武器攻击命中敌人时，将额外造成 1d6 的伤害，其伤害类型与所使用的武器相同。
41~50 与神器同调后，你的步行速度增加 10 尺。
51~60 与神器同调后，你可以用一个动作施放一个 4 环法术，具体哪个法术由 DM 选出。完成施法后，你可以骰一次 d6。骰值为 1~5 是，则直至第二天黎明前你无法再以该方式施法。
61~70 与 61~60 相同，并把法术替换为一个 5 环法术。
71~80 与 61~60 相同，并把法术替换为一个 6 环法术。
81~90 与 61~60 相同，并把法术替换为一个 7 环法术。
91~00 与神器同调后，你不再受目盲、耳聋、石化或震慑状态影响。
"""

dice_table_minor_detrimental_properties = """
# d-100 弱效减益属性 Minor Detrimental Properties
d100 属性
01~05 与神器同调后，你进行抵抗法术的豁免检定时具有劣势。
06~10 与神器同调后，你首次触碰某个宝石或珠宝时，其价值将变为一半。
11~15 与神器同调后，当你离开神器 10 尺范围外时，将进入目盲状态。
16~20 与神器同调后，你进行抵抗中毒的豁免检定时具有劣势。
21~30 与神器同调后，你散发着一阵酸腐的恶臭，该气味在10 尺范围可以被轻易察觉到。
31~35 与神器同调后，靠近你身边 10 尺范围内的圣水都将被自动摧毁。
36~40 与神器同调后，你的身体变的病弱，并且在进行基于力量或体质属性的属性检定或豁免检定时具有劣势。
41~45 与神器同调后，你的体重增加 1d4 x 10 磅。
46~50 与神器同调后，你的外貌发生变化，具体变的怎样由DM 决定。
51~55 与神器同调后，当你离开神器 10 尺范围外时，将进入耳聋状态。
56~60 与神器同调后，你的体重减少 1d4 x 5 磅。
61~65 与神器同调后，你失去嗅觉。
66~70 与神器同调后，你身边 30 尺范围内的非魔法火焰都将自动熄灭。
71~80 与神器同调后，你身边 300 尺范围内的其他生物无法进行短休或长休。
81~85 与神器同调后，你触碰任何非生物的植物时对其造成1d6 的黯蚀伤害。
86~90 与神器同调后，你身边 30 尺范围内的动物都会进入对你敌对的状态。
91~95 与神器同调后，你每天必须进食六次。
96~00 与神器同调后，你的缺点以某种形式恶化，具体的变化由 DM 决定。
"""

dice_table_major_detrimental_properties = """
# d-100 强效减益属性 Major Detrimental Properties
d100 属性
01~05 与神器同调后，你的身体会在四天内逐渐腐坏。第 1 天结束时你的头发脱落，第 2 天结束时轮到手指尖和脚趾尖，第 3 天结束时轮到鼻子嘴唇，第 4 天结束时轮到耳朵。你可以对自身施展再生术 regenerate 以恢复因此失去的身体器官。
06~10 与神器同调后，你的阵营将每天都发生变化。在每天的黎明时分骰两次 d6 并依此作出选择。第一次骰值为 1~2 时为守序，3~4 为中立，5~6 为混乱。第二次骰值为 1~2 时为善良，3~4 为中立，5~6 为邪恶。当你与该神器首次同调时，必须让 DM 为你先进行一次上述的掷骰。
11~15 你必须完成一个任务，该任务等同于你被施展了指使术 geas 的效应。一旦你完成该任务，就不再受该属性的效应所影响。
16~20 神器中寄宿着一个没有肉身的生命体。该生命体与你敌对，并且每当你以执行动作的形式使用神器属性时，它将有 50%的几率离开神器进入你的身体。这时你必须进行一次 DC 20 的魅力豁免。豁免失败时，你将变成一个由 DM 控制的 NPC，直到入侵的生命体被魔法力量所驱逐。法术如反制善恶 dispel evil and good 可以实现驱逐该生命体的效应。
21~25 在神器周围 10 尺范围内的生物，如果其挑战等级为0（比如非生物的植物）其生命值也将降为 0。
26~30 神器中关押着一个史拉亡蟾 death slaad（详见《怪物图鉴》）。每当你执行动作的形式使用神器属性时，该史拉亡蟾有 10%的几率成功逃跑。而当他出现在你的 15 尺范围内时，将立即对你发动攻击。
31~35 与神器同调后，某个特定种类的生物（比如人类）会始终与你敌对，具体哪一种类则由 DM 作出选择。
36~40 在神器周围 10 尺范围内的魔法药水将被该神器所弱化，并失去其魔法效应。
41~45 在神器周围 10 尺范围内的魔法卷轴将被该神器所弱化，并失去其魔法效应。
46~50 当你以执行动作的形式使用神器属性时，你必须先执行一个放血的附赠动作。该动作的目标可以是你自身，也可以是可触及范围内任何自愿或处于乏力状态的其他人。该动作必须使用一把穿刺或劈砍近战武器，而其目标则受 1d4 的相应类型伤害。
51~60 与神器同调后，你获得一项长期性的疯狂效应（见第8 章“运作游戏”）。
61~65 与神器同调后，你受到 4d10 的心灵伤害。
66~70 与神器同调后，你受到 8d10 的心灵伤害。
71~75 在你完成与神器的同调前，必须先杀死一个与你同一阵营的生物。
76~80 与神器同调后，你随机选择一项属性值并使其数值降低 2。法术高等复原术 greater restoration 可以使属性值的变化得以恢复。
81~85 每次与神器同调后，你的年龄将增加 3d10 岁。你必须成功通过一次 DC 10 的体质豁免，否则将因此死亡。如果你以这种方式死去，则会立即转变为一只由 DM控制的尸妖 wight（详见《怪物图鉴》），并立誓守护该神器。
86~90 与神器同调后，你失去说话的能力。
91~95 与神器同调后，你将具有对所有伤害类型的易伤。
96~00 与神器同调后，你有 10%的几率引起一位神灵的注意。该神灵将委派一名化身前来从你手中抢夺该神器。该化身拥有与其创造者同样的阵营，其资料可以参考生物至高天 empyrean（详见《怪物图鉴》）。该化身会在夺得神器之后自行消失。
"""

artifacts_axe_of_the_dwarvish_lords = """
# 矮人王圣斧 Axe of The Dwarvish Lords
武器（战斧），神器（需要同调）
曾经有一位年轻的矮人王子，在见证民众面对危困时产生了一个念头：矮人一族需要某种东西促使他们凝聚在一起。
此后，矮人王子决心立即起行，寻找方法铸造一把武器作为联合的象征。
年轻的王子从山地之下进行了深入的探索，开拓了其他矮人都未触及到的地域。最后，他进入一座巨型火山炽燃的中心地带，并在矮人的造物神 莫拉丁 Moradin 的帮助下制作了四件强大的工具：粗暴之镐 Brutal Pick、地心锻炉 EarthheartForge、歌之铁砧 Anvil of Songs 和塑形之锤 Shaping Hammer。
四件工具完成后，王子再以它们铸造出强大的矮人王圣斧。
完成铸造后，王子手持神器回归氏族，打算以此为同胞争得和平。王子与圣斧最后成功结束了同伴们的猜忌与磨擦，使各氏族联成同盟，击退仇敌开始了矮人的繁荣时代。此后这名矮人王子被纪念为“始王 First King”，这把传奇的武器也在他年老后传给了他的继任者，并从此成为了矮人之王的官方象征，其传承也一直持续了数个世代。
后来，在一个记录为反叛与阴谋的黑暗时期，一群觊觎圣斧力量和它地位象征的人发动了一场血腥内战，圣斧也因此遗失。随后的几个世纪里，矮人们不断寻找圣斧的下落，而众多的冒险者也不停的寻求坊间传说，并四处挖掘古老的宝库以期寻得其踪迹。
魔法武器 Magic Weapon。
矮人王圣斧 是一把魔法武器，以其发动攻击检定和伤害掷骰时具有+3 加值。圣斧使用时，还可以视为等同于一条矮人腰带 belt of dwarvenkind，一把矮人飞锤 dwarven thrower 和一把锐锋之剑 sword of sharpness。
随机属性 Random Properties。圣斧具有下列已知的随机属性：
• 2 项弱效增益属性• 1 项强效增益属性• 2 项弱效减益属性莫拉丁的祝福 Blessings of Moradin。当你作为一名矮人与圣斧完成同调后，将获得以下增益：
• 你免疫毒素伤害。• 你的黑暗视觉增加 60 尺。
• 你获得铁匠、酿造和石匠的工匠工具熟练项。
召唤土元素 Conjure Earth Elemental。持握圣斧时，你可以用一个动作从中施展召唤元素生物 conjure elemental。该法术将固定召唤一个土元素 earth elemental，此后该属性直到第二天黎明前不可以再次使用。
地深漫游 Travel the Depths。你可以用一个动作触碰圣斧上一个特定的矮人石刻，并以此从圣斧施战一个传送术teleport。如果你的目标地点在地下，则你的传送不会出现意外事故或地点错误状况。该属性使用后必需经过 3 日才可以再次使用。
诅咒 Curse。圣斧携带一个有针对性的诅咒，任何与之同调的非矮人种族都将受该诅咒影响，且诅咒效应在同调切断后依然持续。受诅咒的生物身体外貌和状况会逐渐变得跟矮人相仿。七日之后，该生物将完全变成一个矮人，不过并不会失去其原本的种族特质，也不会因此获得任何的矮人的种族特质。因圣斧发生的身体变化其本质并非魔法（因此无法按魔法来解除），但其依然受任何移除诅咒的效应影响，比如高等复原术 greater restoration 或移除诅咒 remove curse 都可以移除该诅咒的效应。
破坏圣斧 Destroying the Axe。破坏圣斧的唯一办法是在创造它的地心熔炉 Earthheart Forge 里把它熔毁。它必须在熔炉的火焰里持续燃烧五十年，直至其最终屈服于火焰并被燃烧殆尽。
"""

artifacts_book_of_exalted_deeds = """
# 圣洁之书 Book of Exalted Deeds
奇物，神器（需要由善良阵营生物同调）
圣洁之书 是囊括了多元宇宙中所有善良的最终著作，其中凝练的箴言在多个宗教中都有着重要的影响力。圣书不单是为特定信仰贡献的圣经典籍，为其编作的众多作者更在书页之间注入了美德的真实影像，帮助指引众生击退邪恶。
圣洁之书 很少在某地长留。它会在被阅读完毕时自行消失，并在多元宇宙的另一角落重现，然后为该处所充盈的黑暗作道德的引路明灯。曾经有人尝试复制这本巨著，但都无法成功捕捉到其魔法本质，也无法转移其对纯粹心灵和坚定信念的神奇增益。
一把天使之翼样式的坚固锁扣守护着圣书的内页。只有与圣书成功同调的善良阵营生物才能将其打开。圣书一旦开启，与之同调的生物必须花费 80 小时对其进行研习，以理解其内容并从中获得增益。这时其他生物也可以阅读书页内的文章，只是无法得知其深层的含义，也无法从中获得增益。试图阅读圣书的邪恶生物将受到 24d6 的光耀伤害，该伤害无视生物的抗性和免疫，并且不能以任何形式实现减免。受到该伤害的生物如果因此生命值降为 0，则会被一片眩目的闪光消灭殆尽，只留下其原来的所有物。
圣洁之书 的增益只会协助你为善良作斗争。一旦你在 10日内没有执行任何善意或慷慨的行为，又或者主动实行一项邪恶行为时，圣书所提供的所有增益也将即时消散。
随机属性 Random Properties。圣洁之书 具有下列已知的随机属性:• 2 项弱效增益属性• 2 项强效增益属性提高感知 Increased Wisdom。花费时间对圣书研习完毕后，你的感知值提升 2，其总值最高不能超过 24。你不能超过一次的从圣书中获得这项增益。
魔法启迪 Enlightened Magic。花费时间对圣书研习完毕后，你所有施放牧师或圣武士法术的法术位均视为高一环的法术位。
光环 Halo。花费时间对圣书研习完毕后，你获得一个护身光环。光环使身边半径 10 尺半径范围笼罩在明亮光照中，其外再延伸 10 尺的微光光照。你可以用一个附赠动作显现或解散光环。光环存在时，你与善良生物互动时进行的魅力（游说）检定，以及与邪恶生物互动时进行的魅力（威吓）检定均具有优势。另外邪魔与不死生物在光环的明亮光照中对你发动攻击时，其攻击检定具有劣势。
破坏圣书 Destroying the Book。传说只要多元宇宙中还存在着善良，圣洁之书 就无法被破坏。然而，把圣书丢进冥河 River Styx 后，其内文和图像将会消失殆尽，且在 1d100 年里失去其魔力。
"""

artifacts_book_of_wile_darkness = """
# 秽暗之书 Book of Vile Darkness
奇物，神器（需要同调）
秽暗之书 是一本肮脏的手抄原稿，其内容包含着难以言喻的恶念，却被受邪恶蛊惑者视为美酒佳肴。凡人本不该知晓其内的秘密，而在这些记载着可怕内容的潦草书页中，简单一瞥所传递的信息就足以引发内心的疯狂。
很多人认为秽暗之书 出自巫妖神祇 维克那 Vecna 的手笔。他在该书中记录了自己每种病态的主张，每种失常的想法，乃至每个他亲身经历或计划的最黑暗最邪恶的魔法。维克那在书中尽情叙述了所能涉及的每一个邪秽话题，让该书成为了包含凡间所有坏事的骇人大全书。
其他曾持有该书的邪恶践行者，都为这本邪秽知识大全添加了新的内容。这些后续的作者添加内容的方式各不相同，有人把自己书写的内容精心缝入这本巨著中，又或者直接在已有的内容上进行注解或续写。书本的书页之间偶有破陋，有些书页被弄丢，被撕毁，或是被墨迹、血迹以及划痕完全覆盖导致无法分辨其内容。
自然界无法容忍该书的存在。普通植物在该书面前迅速枯萎，连动物们也不愿意靠它太近。该书会渐渐破坏任何其触及之物，连与该书接触过久的石头也会逐渐化作粉末。
与该书同调的生物必须花费 80 小时对其进行研习，以理解其内容并从中获得增益。此后该生物可以随意修改该书的内容，而这些修改都将使其本来包含的邪恶知识得以拓展。
任何与秽暗之书 同调的非邪恶生物都必须进行一次 DC17 的魅力豁免。豁免失败时，该生物的阵营将变为中立邪恶。
秽暗之书 的增益只会支持你为邪恶事业而奋斗。一旦你在 10 日内没有执行任何邪恶的行为，又或者主动施行一个善良行为时，该书将即时消失不见。与该书同调后，如果你在同调切断前死去，则会出现一个巨恶的存在前来索取你的灵魂，而你在灵魂被关押时也无法复活。
随机属性 Random Properties。秽暗之书 具有下列已知的随机属性:• 3 项弱效增益属性• 1 项强效增益属性• 3 项弱效减益属性• 2 项强效减益属性属性值调整 Adjusted Ability Scores。花费时间对该书研习完毕后，你一项自选的属性值提升 2，其总值最高不能超过24。选定项之外的属性值均降低 2，期总值最低不能低于 3。
此后该书无法再次对你的属性值进行调整。
黑暗印记 Mark of Darkness。花费时间对该书研习完毕后，你的外观容貌将受到损毁。你将出现一些骇人的外貌特征以此象征你为秽暗之力作出的献身决心。你的脸上可能会出现一个邪恶符文，可能是眼珠变成全黑，或者可能开始从前额长出魔角。你可能变得干枯丑陋，失去所有貌美的特质，并长出分叉的舌尖或是其他由 DM 选择作为替换的外观特征。拥有黑暗印记时，你与邪恶生物互动时进行的魅力（游说）检定，以及与非邪恶生物互动时进行的魅力（威吓）检定均具有优势。
命令邪恶 Command Evil。与秽暗之书 同调后，当你手持该书时可以用一个动作对一个邪恶目标施展法术支配怪物dominate monster（豁免 DC 18）。此后该属性直到第二天黎明之前都不可以再次使用。
暗秘学识 Dark Lore。你可以引用秽暗之书 的内容进行相关的智力检定。当该检定的内容与邪恶相关时（比如恶魔的相关轶闻），你的熟练加值在检定时可以翻倍使用。
暗秘灵言 Dark Speech。与秽暗之书 同调后，你可以在手持该书时用一个动作演说书中的内容，演说时你将使用一种名为暗秘灵言 Dark Speech 的污秽语言。每次演说时，你将受到 1d12 的心灵伤害，而你身边 15 尺范围内的每个非邪恶生物将受到 3d6 的心灵伤害。
破坏书典 Destroying the Book。
秽暗之书 的书页可以从书中撕下来，但其内包含的所有邪恶学识都会自行寻找方法回到书中，通常是通过新作者加入书页的方式回归。
一名炽天神使 solar 将该书撕成两半后，可以暂时将其摧毁。但经过 1d100 年后它会在多元宇宙的某个黑暗角落重新成型。
与本书同调超过一百年的生物，可以发现藏在其平常文字下的隐语。当这段隐语被翻译为天界语高声诵读时，其诵读者和书本将同时被一道眩目的光耀摧毁。然而只要多元宇宙中还存在邪恶，本书就能够在 1d10 x 100 年后重现人间。
如果多元宇宙中的所有邪恶被清除，则本书也将化为灰烬而被彻底消灭。
邪秽学识 Vile Lore秽暗之书 与宇宙中的所有邪恶紧密相连。角色可以使用书中的学识揭示凡人无从知晓的秘密。在书的内容中角色可能发现以下信息，你也可以自行补充其他内容。
• 邪秽升格 Vile Apotheosis。该书可以举行一个仪式，使得角色成为一个巫妖 lich 或死亡骑士 death knight。
• 真名 True Names。任何邪魔的真名都可能在书中有所记载。
• 黑暗魔法 Dark Magic。DM 可以设计或者选择若干骇人的邪恶法术加入书中。这些法术的内容可以施加痛苦的诅咒，可以让人毁容，或是需要献祭活人，用极端的痛苦折磨其他生物，散播邪秽的瘟疫，诸如此类。
"""

artifacts_eye_and_hand_of_vecna = """
# 维克那法眼和魔掌 Eye and Hand of Vecna
奇物，神器（需要同调）
维克那 Vecna 之名即为不语之代表，偶有提及也只能示以静默之音。在其在世的年代，维克那是世上最强大的法师之一。他行驶黑暗魔法之力南征北讨，建立了一个恐怖的大帝国。
其时，拥有强大力量的维克那依然无法逃脱凡人终要面对的死亡终结。然后他开始惧怕死亡，并着手阻止自己的末日。
直至不死魔君 奥喀斯 Orcus 出现，并向维克那传授了转化为巫妖的邪恶仪式，此后他就以巫妖的形式继续存活。即使成为了巫妖，超越死亡的维克那也是所有巫妖中最强大的一个。转化后的维克那在身体逐渐枯萎腐烂之时，依然不忘扩张其邪恶的统治。他异常乖戾而阴险的脾性，使其臣民都敬而远之，甚至不敢提及他的名号。他被称为耳语者 Whispered One，蜘蛛王座之主 Master of the Spider Throne，不死之王 UndyingKing 以及腐塔领主 Lord of the Rotted Tower。
传闻维克那的副官 凯斯 Kas 曾觊觎其蜘蛛王座，又有说是主君为其制作的宝剑曾对他不停的煽动挑拨。不管原因为何，凯斯最终发动了叛乱，并在一场骇人的战争中结束了维克那的统治，甚至让维克那的法师塔回归尘土。而维克那本身则只留下一只手掌和一只眼睛，并化作力量惊人的神器继续在世上贯彻耳语者的意志。
维克那法眼 Eye of Vecna 和维克那魔掌 Hand of Vecna 不一定会同时出现。法眼布满血丝，有如刚刚直接从眼眶中抽出。
魔掌则是一副风干萎缩断肢的样子。
与法眼同调前，你必须先挖出自身的一颗眼珠，再把神器放入挖空的眼眶内。法眼会自行嫁接入你的脑袋并留在其位置直至你死亡。一旦就位，法眼会变为一只有着狭长瞳孔的金色的猫眼。此后法眼一旦被取下，你将立即死亡。
与魔掌同调前，你必须先将左手手腕以下砍断，再把神器接入断手的截面。魔掌会自行嫁接入你的手臂并成为一副正常运作的前肢。此后魔掌一旦被取下，你将立即死亡。
随机属性 Random Properties。
维克那法眼 和维克那魔掌 具有下列已知的随机属性：
• 1 项弱效增益属性• 1 项强效增益属性• 1 项弱效减益属性法眼属性 Properties of the Eye。你的阵营变为中立邪恶，并且获得以下增益：
• 你获得真实视觉。• 你可以使用一个动作来视物，并视为等同于带着 X射线戒指 ring of X-ray vision。你可以用一附赠动作终止该效应。
• 法眼拥有 8 发充能。你可以用一个动作并花费 1 发或更多充能，然后从法眼施展以下法术（豁免 DC 18）之一：
鹰眼术 clairvoyance（2 充能），疯狂冠冕 crown of madness（1充能），解离术 disintegrate（4 充能），支配怪物 dominatemonster（5 充能）或摄心目光 eyebite（4 充能）。法眼在每天黎明时恢复 1d4+4 发已消耗的充能。每次使用法眼的法术时，你有 5%的几率被维克那抽取灵魂并吞噬殆尽，而你的身体则变为受其控制的傀儡。该情况下你将成为 DM 控制的 NPC。
魔掌属性 Properties of the Hand。你的阵营变为中立邪恶，并获得以下增益：
• 你的力量值变为 20，除非其数值已经是 20 或者更高。
• 使用魔掌进行的任何近战法术攻击，以及使用魔掌持用近战武器发动的近战武器攻击，命中时将加上额外的 2d8 冷冻伤害。
• 魔掌拥有 8 发充能。你可以使用一个动作并花费 1 发或更多充能，然后从魔掌施放以下法术（豁免 DC 18）之一：
死亡一指 finger of death（5 充能），睡眠术 sleep（1 充能），缓慢术 slow（2 充能），或传送术 teleport（3 充能）。魔掌在每天黎明时恢复 1d4+4 发已消耗的充能。每次使用魔掌的法术时，它将对你施展暗示术 suggestion（豁免 DC 18），并敦促你施行邪恶行为。魔掌可能对此有具体的指示或是随你自行决定。
法眼加魔掌属性 Properties of the Eye and Hand。与魔掌和法眼都进行同调后，你将获得以下的额外增益：
• 你免疫疾病和中毒。
• 使用法眼的 X 射线时不再承受力竭状态。
• 你对危险拥有预感，除非你处于失能状态，否则无法被偷袭。
• 在你的回合开始时，如果你的生命值至少还剩 1，则恢复1d10 的生命值。
• 你可以用维克那魔掌 对有骨架的生物进行一次触碰，并使其骨头变为凝胶。发动该属性时，你需要使用一个动作对一个可触及的生物发动一次近战攻击，攻击时你可以选择使用你可选的近战武器或法术攻击加值。一旦命中，则目标必须成功通过一次 DC 18 的体质豁免否则其生命值降至 0。
• 你可以使用一个动作施放祈愿术 wish。该属性使用后必需经过 30 日才可再次使用。
破坏法眼和魔掌 Destroying the Eye and Hand。如果维克那法眼 和维克那魔掌 与同一生物同调，并且该生物被凯斯之剑 Sword of Kas 所斩杀，则法眼和魔掌即时迸出火焰烧成灰烬，并且被彻底摧毁。任何其他行为似乎也可以破坏法眼和魔掌，但这些神器会在维克那其中一个隐藏宝库中重现，并在此等待重现人间。
"""

artifacts_orb_of_dragonkind = """
# 龙珠 Orb of Dragonkind
奇物，神器（需要同调）
很久以前，在一个叫克莱恩 Krynn 的世界，精灵与人类对邪恶巨龙发动了一场惨烈的战争。在最后世界接近崩溃之际，大法师诸塔 Towers of High Sorcery 的法师们齐聚一堂，运用其最强大的魔法制作了五颗龙珠 Orb of Dragonkind（或称龙族宝珠 Dragon Orbs），希望以此击败巨龙。制作完成后，五颗龙珠 分给了五座法师塔，手持龙珠 法师们使用神器的力量引诱巨龙们前来，然后用强大的魔法对其进行轰杀。此后，人类联盟凭借龙珠 的力量开始加速通往胜利的步伐。
随着历史的变迁，大法师诸塔也走向没落。其持有的五颗龙珠 也相继被破坏或遗失在传奇之中。相传仍然有三颗保存完好的龙珠 流传在世，虽然它们的魔法随着岁月的变迁而扭曲变换，但其呼唤巨龙的原始功能却依然健全，还能在一定程度上控制巨龙。
每颗龙珠 内包含着一只邪恶巨龙的精华，其存在让龙珠愤恨被人用以施展诱惑魔法。这些个性情绪不断释出，有时会使被奴役者有所察觉，并发现自身正被龙珠 控制的事实。
龙珠 的主体是一枚装饰着蚀刻的水晶球。它直径 10 寸，而在使用时则会增长为 20 寸直径，并且在内部萦绕着盘旋的迷雾。
与龙珠 同调后，你可以用一个动作深入窥视龙珠 深处并说出其命令语。你必须进行一次 DC 15 的魅力检定。检定成功时，你将成功控制龙珠 直至同调中断。检定失败时，你将被龙珠 魅惑，并持续至同调中断。
被龙珠 迷惑时，你不能自行中断同调，而龙珠 可以随意对你施展暗示术 suggestion（豁免 DC 18），并敦促你施行邪恶行径以满足其欲望。
龙珠 里的巨龙精华有着各种需求：歼灭某个特定人物；从龙珠 里获得解放；四处折磨世人；为塔克西丝 Takhisis（即提亚玛特 Tiamat 在克莱恩的称呼）传诵信仰，或是其他由 DM 决定的事情。
随机属性 Random Properties。
龙珠 具有下列已知的随机属性：
• 2 项弱效增益属性• 1 项弱效减益属性• 1 项强效减益属性法术 Spells。
龙珠 拥有 7 发充能，并且每天黎明时分可以恢复 1d4+3 发已消耗的充能。你可以使用一个动作并花费1 发或更多充能，然后从龙珠 中施展以下法术（豁免 DC 18）之一：
疗伤术 cure wounds（5 环版本，3 充能），昼明术 daylight（1 充能），防死结界 death ward（2 充能），或探知 scrying（3 充能）。
你还可以从龙珠 中随意施展侦测魔法 detect magic 且不需花费任何充能。
呼唤巨龙 Call Dragons。控制龙珠 时，你可以使用一个动作让神器向所有方向释放 40 里远的心灵呼唤。在影响范围内的邪恶巨龙将感受到龙珠 的呼唤，并被强制以最快的方式来到龙珠 身边。只有龙神提亚玛特可以无视龙珠 的呼唤。由于被迫违背自己的意志，龙珠 唤来的巨龙可能对你抱有敌意。
使用该属性后，你不能在接下来的 1 小时内再次使用。
破坏龙珠 Destroying an Orb。
龙珠 表面上十分脆弱，却可以抵挡大多数伤害，其中就包括巨龙的吐息武器和各种攻击。尽管如此，法术解离术 disintegrate 以及+3 魔法武器的攻击伤害都可以直接摧毁龙珠。
"""

artifacts_sword_of_kas = """
# 凯斯之剑 Sword of Kas
奇物，神器（需要同调）
维克那在其力量增长时期曾经任命一名无情的邪恶副官，其名为血手凯斯 Kas the Bloody Handed。除了作维克那的保镖及心腹，这名邪恶反派还担任顾问、军官以及刺客的工作。
他的成功赢得了维克那的钦佩与奖赏，并给予他一把如其持用者一样臭名昭著的宝剑。
凯斯为巫妖忠心服务了一段相当长的时间，但随着其力量的日渐增长，其野心也随之膨胀。他的佩剑力劝他推翻维克那，并取代其地位统治巫妖建立的整个帝国。传说维克那殒落自凯斯的双手，但反叛的副官也遭到处决。最后一切烟消云散，从此世界一片光明。而凯斯的佩剑却继续流传于世。
凯斯之剑 是一把具有智能的魔法长剑。以其发动的攻击检定和伤害掷骰具有+3 加值，在投得 19 或 20 时它即可造成重击，并且可以对不死生物造成额外的 2d10 的劈砍伤害。
魔剑一旦出鞘，如果无法在 1 分钟之内浸染鲜血，则其持用者必须成功通过一次 DC 15 的魅力豁免。豁免成功，则该持用者受 3d6 的心灵伤害。豁免失败时，持用者将被魔剑支配，其效应视为等同于法术支配怪物 dominate monster。魔剑会继续渴求浸染鲜血，而法术的支配效应则一直持续到满足其渴求之后结束。
随机属性 Random Properties。
凯斯之剑 具有下列已知的随机属性:• 1 项弱效增益属性• 1 项强效减益属性• 1 项弱效减益属性• 1 项强效减益属性凯斯之灵 Spirit of Kas。魔剑在身边时，你每场战斗开始时，先攻可以加入一个 d10。另外，使用魔剑执行攻击动作时，你可以将其攻击加值全部或者部分转移至你的 AC。加值的调整效应将保持至你的下一回合开始时结束。
法术 Spells。魔剑在身边时，你可以使用一个动作从中施展以下法术之一（豁免 DC 18）：
召雷术 call lightning，圣言术 divine word，或死亡一指 finger of dead。使用魔剑的某个法术后，你在第二天黎明之前无法再使用魔剑施展该法术。
智能 Sentience。
凯斯之剑 是一把混乱邪恶阵营的智能武器，它的智力为 15，感知 13，魅力 16，它听觉和黑暗视觉的感官范围为 120 尺。
魔剑还可以通过心灵感应与其持用者交流，且能够说、读和理解通用语。
个性 Personality。魔剑的最终目标是摧毁维克那。杀死维克那的信徒，破坏他的巫妖造物，以及阻挠他的计划都是完成其最终目标的手段。
凯斯之剑 四处追杀受维克那法眼和魔掌腐化的人。魔剑对这两件神器的执着最终也会传染其持用者。
破坏魔剑 Destroying the Sword。
维克那法眼 和维克那魔掌 与同一个生物同调后，该生物可以使用其外加的联合属性祈愿术 wish，并以此撤销凯斯之剑 被创造的事实。该生物必须先施展祈愿术，然后进行一次魅力检定，并与凯斯之剑的魅力检定作对抗。魔剑必须在该生物 30 尺范围之内，否则法术失效。如果最终魔剑赢得对抗，则祈愿失效，所有事物保持原状。如果魔剑输掉比试则直接被摧毁。
"""

artifacts_wand_of_orcus = """
# 奥喀斯之杖 Wand of Orcus
魔杖，神器（需要同调）
阴森恐怖的奥喀斯之杖 总是陪伴在 奥喀斯 Orcus 的身边。它继承了其恶魔领主创造者的邪恶意志与终极目标，想方设法消灭所有生命，然后使物质位面沦为不死的停滞空间。奥喀斯有时会故意让魔杖流落远方，密谋实现某个堕落的目的。
彼时魔杖仍与奥喀斯保持联系，让不死主君时刻掌握其动向。
魔杖主体的骨头坚硬如铁，其顶端一个由魔法巨大化的骷髅头装饰曾属于一个被奥喀斯残杀的人类英雄。另外，魔杖的魔法还可以改变自身大小以适合其持用者的身形。
奥喀斯之杖 充满邪恶，其所到之处寸草不生，水源与肉食迅速变质腐坏，强盗暴徒横行无忌导致四处混乱不堪。
除奥喀斯外，任何生物与魔杖同调后，必须进行一次 DC17 的体质豁免。豁免成功，则生物受 10d6 的黯蚀伤害。豁免失败，则该生物死亡并复活为一只僵尸 zombie。
与魔杖同调后，你可以将该魔杖用作一把魔法硬头锤。其发动的攻击检定和伤害掷骰具有+3 加值，使用魔杖每击命中时可额外造成 2d12 的黯蚀伤害。
随机属性 Random Properties。
奥喀斯之杖 具有下列已知的随机属性：
• 2 项弱效增益属性• 1 项强效减益属性• 2 项弱效减益属性• 1 项强效减益属性奥喀斯本人与奥喀斯之杖 同调后，魔杖的减益属性将受到抑制而无法生效。
防护 Protection。持握魔杖时，你的护甲等级获得+3 加值。
法术 Spells。魔杖拥有 7 发充能。你可以用一个动作花费1 发或更多充能，然后从魔杖施展以下法术之一（豁免 DC 18）：
操纵死尸 animate dead（1 充能），枯萎术 blight（2 充能），死亡法阵 circle of death（3 充能），死亡一指 finger of death（3 充能），律令死亡 power word kill（4 充能），或死者交谈speak with dead（1 充能）。魔杖在每天黎明时分恢复 1d4+3的已消耗充能。
与魔杖同调后，如果同调者为奥喀斯或受其祝福的追随者，则使用魔杖法术时每项法术需要消耗的充能降低 2（最低为 0）。
呼唤不死生物 Call Undead。持握魔杖时，你可以用一个动作召唤骷髅 skeleton 或僵尸 zombie，所召唤生物的生命值总值不能超过 500，每只不死生物拥有等于平均数值的生命值（相关的资料见《怪物图鉴》）。召唤的不死生物出现在你身边 300 尺范围内为被占据的空间位置，它们由魔法从地下唤起，或是在未被占据的空间中凭空成形。这些不死生物服从你的命令，直至被摧毁或直至第二天黎明时分自行毁灭。该属性被使用后，你必须在第二天黎明时分后才能再次使用。
与魔杖同调后，奥喀斯可以召唤任意种类的不死生物而不仅仅是骷髅和僵尸。并且其召唤出来的不死生物不会在第二天黎明时腐朽或消失，并一直存在至奥喀斯主动将其解散。
智能 Sentience。奥喀斯之杖 是一件混乱邪恶阵营的智能物品，它的智力为 16，感知 12，魅力 16，它的听觉和黑暗视觉的感官范围是 120 尺。
该魔杖还可以通过心灵感应与其持用者交流，且能够说、读和理解深渊语和通用语。
个性 Personality。魔杖的目标是满足奥喀斯杀戮多元宇宙所有生物的欲望。魔杖冷酷残暴，行为无法无天，而且毫无幽默感。
为了完成起真正主人的目标，魔杖会假装屈服于其现任使用者，甚至给对方许下根本不打算应允的承诺，比如帮助对方推翻奥喀斯本尊。
破坏魔杖 Destroying the Wand。要破坏奥喀斯之杖 ，必需由一位远古英雄把它带到正能量位面 Positive EnergyPlane。这位英雄必需是魔杖上骷髅头的本尊，因此，要完成这个任务必须先让这位故去已久的英雄重新复活。由于奥喀斯将其灵魂藏在一个守备森严的秘密地点，因此你必需先排除万难解救这位英雄的灵魂，再进行之后的操作。
将魔杖浸没在正能量中可以让其迅速崩坏炸裂，但如果无法满足上述的前提条件，破坏的魔杖将立即在奥喀斯所控制的深渊层级中成型再现。
"""

article_other_rewards = """
# 其他奖励 Other Rewards
冒险家们渴望财富，但有时也会接受其他形式的奖励。本节展示了众神、君主和其他强大存在给予角色的成就，包括一些赋予角色新能力的超自然赠礼；头衔、土地和其他威望加持；
以及一些只有达到 20 级的冒险者才能使用的恩惠。

# 超自然赠礼 Supernatural Gifts
超自然赠礼是由强大魔力存在或原力赋予的特殊奖励。
这类超自然赠礼有两种形式：祝福和护咒。祝福通常由神灵或类神存在所赐。而护咒则通常是某强大精魂，某远古魔法区域，或某个传奇生物的作用。与魔法物品不同，超自然赠礼不是物品，也不需要同调。它可以赋予角色可以单次或多次使用的非凡能力。

# 祝福 Blessings
角色施行某意义重大之事时——即某件能同时引起众神和凡人注意的成就时，便会获得神祇的祝福。杀死横行的豺狼人群，或者在提亚玛特 Tiamat 的高阶祭司意图召唤龙之女王是将其杀死，都会罕见的获得这样的祝福。
一项祝福是对下列成就之一的适当奖励：
• 修复某神灵最神圣的圣地• 挫败某神灵敌人的惊天阴谋• 帮助某神灵青睐的侍奉者完成其神圣任务冒险者也会在前去执行危险任务前得到祝福。例如，一位圣武士在出发前去追杀某个向大陆散布魔法瘟疫的可怕巫妖前，便可获得一项祝福。
一名角色理应只接受对自己有用的祝福，而某些祝福还伴随着其施予者的期望。神灵通常会为某特定目的而赐福，比如回收某圣人的遗体或推翻某暴政帝国。如果角色没能贯彻该目标，或者违背了神灵的旨意，那该神灵也可能会收回祝福。
角色可以永久保留祝福的增益，或直至该祝福被赋予的神灵回收。与魔法物品不同，这样的祝福不会被反魔法力场antimagic field 或类似的效应所压制。
大多冒险者终其一生都无法受惠于一份这样的祝福。角色能接受的祝福数量没有限制，一名角色获得多于一份的祝福应该是极为罕见的情况。此外，一名角色不能同时复数的同样祝福中获益。例如，一名角色无法同时从两份“健康祝福”中获得增益。
下面给出一些祝福的范例。每项祝福的文本均指向其使用者。如果你想要创作更多的祝福，则可以参考模仿一件奇物的属性。
祝福健康 Blessing of Health。你的体质值提升 2，上限为 22。
保护祝福 Blessing of Protection。你在 AC 和豁免获得+1加值。
魔抗祝福 Blessing of Magic Resistance。你为抵抗法术和其他魔法效应而作的豁免检定具有优势。
理解祝福 Blessing of Understanding。你的感知值提升2，上限为 22。
瓦尔哈拉祝福 Blessing of Valhalla。该祝福使你获得召唤精魂武士的力量，其效应等同于你吹响一件白银级的瓦尔哈拉号角 horn of Valhalla。你使用一次该祝福后，必须经过 7日之后才能再次启用其效应。
武器增强祝福 Blessing of Weapon Enhancement。你所拥有的一把非魔法武器在你持用时变为一把+1武器。
愈合祝福 Blessing of Wound Closure。该祝福为你带来愈合护符 periapt of wound closure 所提供的增益。

# 护咒 Charms
护咒是一种获取渠道更为广泛的弱效超自然赠礼。例如，一个法师在某去世大法师的法术书中发现了一个关于魔能的秘密，并利用其作为魔法护咒灌注到自己身上。相似的情况里，解开翔狮兽谜题或从魔法喷泉中饮水的角色，也可以以此获取护咒。传奇生物如远古金龙和独角兽，有时也会给盟友们施加护咒，某些探险家有在发现某个受魔法浸淫而失落久远的地点时，也会受该地影响而获得一份魔法护咒。
一些护咒只可以使用一次，而其他的护咒可以在消失前使用特定的次数。护咒赋予的施法能力，可以让你不消耗法术位也不提供任何构材（言语、姿势或材料）的实现施法。任何情况下，护咒都无法在反魔法力场 antimagic field 或类似的效应中生效，护咒的效应也会受解除魔法 dispel magic 等类似效应影响。但是护咒本身无法从某生物身上移除，除非受神能干涉或受法术祈愿术 wish 影响。
下面给出一些护咒的范例。每项护咒的文本均指向其使用者。护咒的效应通常是模仿魔药或法术，因此你也可以简单随意的自创更多的护咒。
召唤动物护咒 Charm of Animal Conjuring。该护咒可以让你得以用一个动作施展法术召唤动物 conjure animals（3 环版本）。使用三次后，该护咒将随即从你身上消失。
黑暗视觉护咒 Charm of Darkvision。该护咒可以让得以用一个动作施展法术黑暗视觉 darkvision，且无需任何构材。使用三次后，该护咒将随即从你身上消失。
羽落护咒 Charm of Feather Falling。该护咒可以让你获得羽落戒指 ring of feather falling 的增益。该增益可以持续 10日，随后该护符便会从你身上消失。
英雄气概护咒 Charm of Heroism。该护咒可以让你用一个动作获得一剂英雄气概药水 potion of heroism 的增益。使用一次该增益后，该护咒便会从你身上消失。
复原护咒 Charm of Restoration。该护咒有 6 发充能。你可以用一个动作消耗定量的充能来施展下列法术：
高等复原术 greater restoration（4 充能），次级复原术 lesser restoration（2 充能）。所有充能耗尽后，该护咒便会从你身上消失。
杀戮护咒 Charm of the Slayer。你拥有的一把剑在随后的 9 日里变为一把屠龙者 dragon slayer 或巨人屠杀者 giantslayer（由 DM 选择）。时效过后，该武器恢复正常而该护咒也随之从你身上消失。
活力护咒 Charm of Vitality。该护咒可以让你得以用一个动作获得活力药水 potion of vitality 的增益。使用一次该增益后，该护咒便会从你身上消失。

# 威望加持 Masks of Prestige
有时候冒险者接受的最响亮的奖赏便在获取通行整个国度的威望。各种冒险会为他们带来名誉与权力、盟友和敌人，以及可以传承给后代的头衔。一些领主和女领主曾经也是从平民起步，再随着踏进危险世界中一步步通过勇武行为塑造起自己的名声。
本节详细介绍一些战役冒险中通常能够获得的威望加持。
这些加持通常与宝藏一同获取，但有时也可能会独立出现。

# 推荐信 Letters of Recommendation
黄金供不应求时，冒险者的恩人可能会给他们提供一封推荐信，而非支付钱财。这样的信件通常封在漂亮的开本、盒子或卷轴中以保证安全便携，而且通常都带有书写该信任务的签名和印章。
一封来自于某极高声誉者的推荐信可以让冒险者们得以绕开许多麻烦直接拜访某些 NPC，如公爵、总督或女王。此外，带着某人的推荐，可以帮助消除与当地政府相关的“误解”，并以此让地方当局不敢对角色们的任何言论采取某些措施。
一封推荐信的价值只能相当于其书写者的的价值，在作者不具备影响力的地方信件本身也无法带来任何好处。

# 勋章 Medals
勋章通常由黄金和其他贵金属精制而成，但其本身意义并不如授勋行为本身的象征意义那样重大。
勋章一般是由权威政治人物为英雄行为而颁发奖赏，就佩戴勋章这一形象本身就足以让某些理解其重要意义的人予以尊敬。
不同的英雄行为可以赢得不同种类的勋章。不列兰德王King of Breland（艾伯伦 Eberron 战役设定）会授予皇家英勇奖章 Royal Badge of Valor（形状像一面由红宝石和银金制成的盾牌）给保护不列里斯 Brelish 公民的冒险者，而不列兰德金熊 Golden Bear of Breland（一枚由黄金制成，带着宝石眼睛的熊头形勋章）则用以证明冒险者们对不列里斯王权的效忠，并展示其挫败试图终止王座条约 Treaty of Thronehold 并重燃终末之战 the Last War 阴谋的功绩。
一枚勋章并不会给其佩戴者带来任何游戏内的特定增益，但却可以影响与 NPC 的互动。例如，一名骄傲地展示不列兰德金熊的角色在不列兰德王国境内将被人们奉为英雄。但离开不列兰德境后，除非在不列兰德王的盟友面前，否则勋章的分量也会大打折扣。

# 封地 Parcels of Land
封地简单直接，通常还会附带一封皇家信件以确定土地作为某种服务的回报而授予。这样的土地通常仍作为当地统治者或统治机构的财产，之算作转租给他人，获赠者必须明白其真正所有人随时可回收土地，特别是当获赠者的忠诚受质疑时更是如此。
足够大片的封地可以让人在其中建造一个或多个农场或村庄。此时，受赠者会被宣告为该地的领主或女领主，且有权征收税款，或行使其他任何职责。
获得封地的角色可以随意在其中事实建造工程，并被期望为该地提供庇护。该角色可以声明该封地作为其遗产的一部分，但未经当地统治者或统治主体的许可不得买卖或交易。
固定的土地作为奖励时，可以授予那些想要寻找某处定居的角色。角色组建了家庭或在当地周边区域作某些个人投资时，也很适合接受这种奖励。

# 人情 Special Favors
有些奖励会以暂欠人情的方式保留，以让角色们在未来某日需要时索取回报。施予的个体值得信赖时，人情的运作会向好的方向发展。守序善良或守序中立的 NPC 会尽一切努力来履行曾经的承诺，但不会因此违反律法。手续邪恶的 NPC也会履行诺言，但其自身只将其当做一笔交易。中立善良或绝对中立的 NPC 也会为维护自己的名誉而实现承诺。混乱善良的 NPC 更关心为冒险者们做正确的事，他们会履行任何义务而不担心是否要冒个人风险或是否会违反律法。

# 特权 Special Rights
政治当权者可以给角色们授予特权作为奖励，此时通常会以某种官方文件的形式表达。例如，角色们可能被授予的特权包括：在公共场所携带武器，杀死国王的敌人或与公爵的代表进行谈判。角色们可能有权要求获得免费的休息室，聚集社群公布消息，或是有权安排当地的民兵为自己提供协助。
特权只在法律文件规定的情况下才能持续，如果冒险者滥用这些权里，则这些权利也可能会被撤销。

# 要塞 Strongholds
一所要塞通常是给经验丰富的冒险者们授予的奖励，以彰显其精诚效忠某权威政治人物或统治主体，如国王、骑士会或法师议会。要塞的形式多样，它可以是城市中心的加固塔楼，也可以是边境的省区堡垒。虽然要塞可以让角色们按照自己的想法来施行统治，但它所处的地产仍属于国王或当地统治者。如果角色被证实为不忠或配不上该赠礼，那他们也可以被要求或被迫放弃对要塞的监护权。
作为额外的奖励，作为遗赠的要塞可以免除一个月或几个月的维护费用，此后该角色才开始承担其维护职责。见第 6章关于要塞维护的相关信息。

# 头衔 Titles
一位政治上的权威人物有权给他人分配头衔。头衔通常附带有封地（见前文）。例如，授封为“风暴流河伯爵 Earl ofStormriver”或“顿峡湾女伯爵 Countess of Dun Fjord”时还附带有一块封地，其中包括一个同名的聚居地或地区。
角色可以拥有一个以上的头衔，在封建社会中，这些头衔可以传承（或分封）给所有者的孩子。拥有某头衔的角色可能会以适合该头衔的方式行事。依据法令，如果当地统治者或统治主体有理由质疑该角色的忠诚或能力时，其头衔也可以就此被剥夺。

# 训练 Training
角色可以接受特殊训练来代替金钱奖励。这种培训并不常见因而存在一定价值。训练设定有一位经验丰富的训练员（也许是一位退休的冒险者或冠军勇士）愿意出任导师。教练可能是一个为清还女王的人情而前来帮忙的隐居法师或傲慢术士，或是国王卫队的骑士指挥官，强大的德鲁伊结社领袖，住在某偏僻山顶宝塔修道院的古怪武僧，野蛮人酋长，生活在游牧民中作为占卜者的邪术师，或一位所作诗词歌剧家喻户晓人人皆知却时常漫不经心的吟游诗人。
同意接受训练作为奖励的角色在自己的休整期时间里必须与培训师一起度过（参阅第 6 章以获得更多关于休整期活动的相关信息）作为交换，该角色可以确保获得一项特殊增益。
可能的训练收益包括以下内容：
• 该角色在每天的黎明时分获得可持续 1d4+6 日的激励。
• 该角色获得一项技能作为其熟练项。
• 该角色获得一项专长。
"""

article_epic_boons = """
# 传奇恩惠 Epic Boons
传奇恩惠，是一种只有 20 级以上的角色才能获得的独特能力。即使达到该等级，角色们也只能随你的意愿，并由你选择合适的时机赋予传奇恩惠。传奇恩惠是角色完成一项重大任务，或完成其他某些可圈可点的事迹后，可获取的绝佳奖励。
角色也许可以在摧毁一件邪恶神器，击败一头远古龙或终止一场来自外层位面的入侵后，获得一项传奇恩惠。
传奇恩惠也可以作为一种特殊的提升方式，为无法再升级的角色提供更强大的力量。按照该方式，你可在角色超过355,000 XP 后每再获取 30,000 XP 时授予角色一项传奇恩惠。
你来决定角色该获得哪项传奇恩惠。理想情况下，你授予角色的传奇恩惠应该为他们在随后的冒险中有提供助益。你也可以随自己意愿让玩家自己选择获取某项传奇恩惠。
无论人物最终获得怎样的恩惠，请将之视作你的故事和世界的一部分。传奇恩惠中许多都远超凡俗，以表明角色逐步扬升为一个半神般存在的过程。获得一个传奇恩惠，也许会使角色的外貌产生肉眼可见的改变。例如，一个获得了真实视觉之恩惠的角色，当他激起强烈情感时可能会双眼发光；而一个获得了高等魔法之恩惠的角色，可能会有闪耀着微光的光点在其上头闪烁。你还要负责决定这项恩惠如何出现。这项恩惠是神秘的主动出现吗？或者一种驾驭着宇宙力量的存在亲自显现，赐予角色该力量？赋予角色一项传奇恩惠，这本身就可能是冒险中动人心魄的一幕。

# 英勇战斗之恩惠 Boon of Combat Prowess
你一次近战武器攻击未命中时，可以选择使之命中。使用该恩惠后，你需要完成一次短休才能再次使用它。
# 次元旅行之恩惠 Boon of Dimensional Travel
作为一个动作，你可以施展法术迷踪步 misty step，且不消耗法术位也不需要任何构材。使用该恩惠后，你需要完成一次短休才能再次使用它。
# 扭曲命运之恩惠 Boon of Fate
你周边 60 尺内除你自身外一个你能看见的生物进行一次属性检定、攻击检定或豁免检定时，你可以骰一次 d10，再将掷骰结果作为加值或减值附加到对方的检定结果中。使用该恩惠后，你需要完成一次短休才能再次使用它。
# 超凡强韧之恩惠 Boon of Fortitude
你的生命值上限提升 40。
# 高等魔法之恩惠 Boon of High Magic
如果你拥有 9 环法术位，则可再获得一个 9 环法术位。
# 不朽不灭之恩惠 Boon of Immortality
你停止衰老。你免疫任何会使你衰老的效应，并且不会因衰老而死。
# 金身不坏之恩惠 Boon of Invincibility
你受到任何来源的伤害时可以将其伤害量减为 0。使用该恩惠后，你需要完成一次短休才能再次使用它。
# 无敌攻势之恩惠 Boon of Irresistible Offense
你可以击穿任何生物的伤害抗性。
# 操弄幸运之恩惠 Boon of Luck
你进行一次属性检定、攻击检定或豁免检定时，可以在该检定结果上增加一次 d10 骰值。使用该恩惠后，你需要完成一次短休才能再次使用它。
# 魔法抗性之恩惠 Boon of Magic Resistance
你为抵抗法术和魔法效应而作的豁免检定具有优势。
# 无双狙杀之恩惠 Boon of Peerless Aim
你可以让自己发动的一次远程攻击检定获得+20 加值。使用该恩惠后，你需要完成一次短休才能再次使用它。
# 完美健康之恩惠 Boon of Perfect Health
你免疫所有毒素和疾病，且你的体质豁免具有优势。
# 位面旅者之恩惠 Boon of Planar Travel
你在获得该恩惠时，先指定一个除物质位面外的存在位面。此后你可以用一个动作施展法术异界传送 plane shift（无需法术位和任何法术构材），法术目标限定为你本身且只能传送到你指定的位面，或者从该位面回到物质位面。使用该恩惠后，你需要完成一次短休后才能再次使用它。
# 迅捷施法之恩惠 Boon of Quick Casting
指定一个你可以施展的 1 至 3 环法术，该法术的施法时间必须是 1 动作。此后你可以用 1 附赠动作施展该法术。
# 恢复能力之恩惠 Boon of Recovery
你可以用一个附赠动作，恢复等于你生命值上限一半的生命值。使用该恩惠后，你需要完成一次短休才能再次使用它。
# 动能反弹之恩惠 Boon of Resilience
你对非魔法武器的钝击、穿刺和挥砍伤害具有抗性。
# 技能熟练之恩惠 Boon of Skill Proficiency
你获得所有技能的熟练项。速度爆发之恩惠 Boon of Speed你的步行速度提升 30 尺。此外，你可以用一个附赠动作执行疾走或撤离动作。使用该恩惠后，你需要完成一次短休才能再次使用它。
# 法术掌控之恩惠 Boon of Spell Mastery
指定一个你可施展的 1 环术士、邪术师或法师法术。此后你可以随意施展该法术的最低环版本且无需消耗法术位。
# 法术召返之恩惠 Boon of the Recall
你可以施展任何你已知或已准备的法术且无需消耗法术位。使用该恩惠后，你需要完成一次短休才能再次使用它。
# 炽焰魂魄之恩惠 Boon of Fire Soul
你免疫火焰伤害。你还可以随意施展发生燃烧之手burning hands（豁免 DC 15），且无需消耗法术位也无需使用任何法术构材。
# 暗夜精魂之恩惠 Boon of the Night Spirit
你完全身处微光光照或黑暗环境时，可以用一个动作进入隐形，隐形持续到你执行一个动作或一个反应为止。
# 暴风降生之恩惠 Boon of Stormborn 
你免疫闪电和雷鸣伤害。你可以随意施展法术雷鸣波thunderwave（豁免 DC 15），且无需消耗法术位或使用任何法术构材。
# 无拘无束之恩惠 Boon of the Unfettered
你为抵抗被擒抱而进行的属性检定具有优势。此外，你可以用一个动作直接挣脱擒抱或从任何形式的束缚状态中脱身。
# 真实视觉之恩惠 Boon of Truesight
你获得 60 尺真实视觉感官。
# 无形无迹之恩惠 Boon of Undetectability
你的敏捷（隐匿）检定获得+10 加值，且你无法被预言魔法指定或侦测到，即使是探知的传感器也不行。

# 传奇恩惠替代品 Alternatives to Epic Boons
也许你会选择给一位 20 级的角色赋予以下某项奖励而不是给其奖励传奇恩惠。这两个选项可被多次赋予同一角色。
# 属性值加成 Ability Score Improvement。
该角色可以自选一项属性提升 2，或选择两项属性各自提升 1。现在你可以将属性提升到 20 以上，上限为 30。
# 新专长 New Feat。
角色获得一项自选的新专长，但需要得到你的许可。
"""