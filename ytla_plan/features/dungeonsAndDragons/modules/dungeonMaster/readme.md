<p>
  语言
 <a href="./docs/readme/zh-CN/readme.md"> 简体中文 </a>
 <a href="./docs/readme/en-US/readme.md"> English </a>
</p>


# dungeonsAndDragons - dungeonMaster

### YTLA特性

### Tsukuyomi Alice

version 1.0

后端语言及开发框架: Python-Flask  
适用YTLA core版本: **classic**  
文件更新日期: 2026-03-23

## 概念

dungeonMaster 是 Dungeons & Dragons 5e 地下城主辅助模块，提供规则数据集、AI 提示词、骰子处理等功能

## 特性包目录

```
dungeonMaster/
├── __init__.py
├── ai_tools/
│   └── __init__.py
├── api/
│   └── __init__.py
├── caller/
│   └── __init__.py
├── const/
│   └── __init__.py
├── dao/
│   └── __init__.py
├── dataset/
│   ├── __init__.py
│   ├── datasetJsonPicker.py
│   ├── datasetPyToJson.py
│   ├── dnd_5e_dmguide_000_introduction.json
│   ├── dnd_5e_dmguide_000_introduction.py
│   ├── dnd_5e_dmguide_001_a_world_of_your_own.json
│   ├── dnd_5e_dmguide_001_a_world_of_your_own.py
│   ├── dnd_5e_dmguide_002_creating_a_multiverse.json
│   ├── dnd_5e_dmguide_002_creating_a_multiverse.py
│   ├── dnd_5e_dmguide_003_creating_adventures.json
│   ├── dnd_5e_dmguide_003_creating_adventures.py
│   ├── dnd_5e_dmguide_004_creating_nonplayer_characters.json
│   ├── dnd_5e_dmguide_004_creating_nonplayer_characters.py
│   ├── dnd_5e_dmguide_005_adventure_environments.json
│   ├── dnd_5e_dmguide_005_adventure_environments.py
│   ├── dnd_5e_dmguide_006_between_adventures.json
│   ├── dnd_5e_dmguide_006_between_adventures.py
│   ├── dnd_5e_dmguide_007_treasure.json
│   ├── dnd_5e_dmguide_007_treasure.py
│   ├── dnd_5e_dmguide_010_random_dungeons.json
│   ├── dnd_5e_dmguide_010_random_dungeons.py
│   ├── dnd_5e_monster_000_introduction.json
│   ├── dnd_5e_monster_000_introduction.py
│   ├── dnd_5e_player_000_preface.json
│   ├── dnd_5e_player_000_preface.py
│   ├── dnd_5e_player_001_step_by_step_characters.json
│   ├── dnd_5e_player_001_step_by_step_characters.py
│   ├── dnd_5e_player_002_races.json
│   ├── dnd_5e_player_002_races.py
│   ├── dnd_5e_player_003_classes.json
│   ├── dnd_5e_player_003_classes.py
│   ├── dnd_5e_player_004_personality_and_background.json
│   ├── dnd_5e_player_004_personality_and_background.py
│   ├── dnd_5e_player_005_equipment.json
│   ├── dnd_5e_player_005_equipment.py
│   ├── dnd_5e_player_006_customization_options.json
│   ├── dnd_5e_player_006_customization_options.py
│   ├── dnd_5e_player_007_using_ability_scores.json
│   ├── dnd_5e_player_007_using_ability_scores.py
│   ├── dnd_5e_player_008_adventuring.json
│   ├── dnd_5e_player_008_adventuring.py
│   ├── dnd_5e_player_009_combat.json
│   ├── dnd_5e_player_009_combat.py
│   ├── dnd_5e_player_010_spellcasting.json
│   ├── dnd_5e_player_010_spellcasting.py
│   ├── dnd_5e_player_011_spells.json
│   ├── dnd_5e_player_011_spells.py
│   ├── dnd_5e_player_012_conditions.json
│   ├── dnd_5e_player_012_conditions.py
│   ├── dnd_5e_player_013_gods_of_multiverse.json
│   ├── dnd_5e_player_013_gods_of_multiverse.py
│   ├── dnd_5e_player_014_planes_of_existence.json
│   ├── dnd_5e_player_014_planes_of_existence.py
│   ├── dnd_5e_player_015_creature_statistics.json
│   ├── dnd_5e_player_015_creature_statistics.py
│   ├── dnd_5e_player_016_inspirational_readings.json
│   └── dnd_5e_player_016_inspirational_readings.py
├── docs/
│   ├── readme/
│   │   ├── en-US/
│   │   │   └── readme.md
│   │   └── zh-CN/
│   │       └── readme.md
│   └── tasks/
├── func/
│   └── __init__.py
├── instance/
│   └── __init__.py
├── process/
│   ├── __init__.py
│   ├── processAgentCore.py
│   ├── processAgentDM.py
│   ├── processAgentPL.py
│   └── processClassicDice.py
├── prompts/
│   ├── __init__.py
│   ├── promptCore.py
│   ├── promptGuideAnswer.py
│   ├── promptGuideKeywordList.py
│   ├── promptGuideKeywordPicker.py
│   ├── promptGuideKeywordTopics.py
│   ├── promptGuideMaskedKeywordTopics.py
│   └── promptGuidePreAnswer.py
├── routes/
│   └── __init__.py
├── schedule/
│   └── __init__.py
├── script/
│   ├── __init__.py
│   ├── scriptDNDEmbedder.py
│   ├── scriptDNDTextTransformer.py
│   ├── scriptDNDtext.py
│   └── scriptDnDQuery.py
└── utils/
    └── __init__.py
```

## 变更记录

### 2026-03-23
填充概念和文件结构部分，更新日期
