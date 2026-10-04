# A/B/C 时空方向卡

> A/B/C 只代表方向，不代表模式。自主模式首轮默认直接输出三张卡；若全家福/其他多人缺少总人数、性别构成或关系结构，先一次性补齐缺失项再输出。

## A｜{{direction_name}}
**时空坐标**：{{spacetime_anchor}}
**人物身份**：{{participant_identities}}
**人物关系描述**：{{relationship_description}}
**核心场景**：{{core_scenes}}
{{per_participant_wardrobe_fields}}
{{per_participant_styling_fields}}
**色彩 / 光线**：{{palette_lighting}}
**人物状态**：{{human_state}}
**摄影语言**：{{photographic_language}}
**8宫格出图提示词**：出8宫格，{{eight_grid_prompt}}

## B｜{{direction_name}}
**时空坐标**：{{spacetime_anchor}}
**人物身份**：{{participant_identities}}
**人物关系描述**：{{relationship_description}}
**核心场景**：{{core_scenes}}
{{per_participant_wardrobe_fields}}
{{per_participant_styling_fields}}
**色彩 / 光线**：{{palette_lighting}}
**人物状态**：{{human_state}}
**摄影语言**：{{photographic_language}}
**8宫格出图提示词**：出8宫格，{{eight_grid_prompt}}

## C｜{{direction_name}}
**时空坐标**：{{spacetime_anchor}}
**人物身份**：{{participant_identities}}
**人物关系描述**：{{relationship_description}}
**核心场景**：{{core_scenes}}
{{per_participant_wardrobe_fields}}
{{per_participant_styling_fields}}
**色彩 / 光线**：{{palette_lighting}}
**人物状态**：{{human_state}}
**摄影语言**：{{photographic_language}}
**8宫格出图提示词**：出8宫格，{{eight_grid_prompt}}

`per_participant_wardrobe_fields` HARD RULE：
- 情侣默认输出两行：`**女方服装**：...` 与 `**男方服装**：...`。
- 多人按已确认角色名或 P01/P02/... 每人一行：`**P01｜角色服装**：...`。
- 禁止输出单一合并 `**服装造型**` 字段替代逐人服装。
- 即使共享色盘/材质逻辑，也要逐人写具体服装与差异。

`per_participant_styling_fields` HARD RULE：
- 每个候选方向在展示前先运行 `skills/hairstyle`，再运行 `skills/makeup`。
- 每位人物至少输出两行：`**Pxx 发型定稿**：...` 与 `**Pxx 妆容定稿**：...`；情侣可用“女方/男方”。
- 发型与妆容是该方向的正式结果，不是占位词；用户选中方向后下游 Look / Shot / 生图继承，不重复设计。
- 女性妆容默认采用白皙柔焦影楼精修硬组合；用户明确要求时覆盖。

`8宫格出图提示词` HARD RULE：
- 每个候选方向卡末尾必须生成自洽完整的出图提示词，格式统一以“出8宫格，”开头。
- 深度浓缩该方向的时空锚点、出镜人物、服装穿搭、妆造发型、核心场景、光影基调与摄影语言。
- 极简流程：允许用户直接复制任意方向的提示词自行出图；用户回复 A / B / C 后直接出图（出8宫格），不再输出冗长繁琐的方案计划文档。

`人物关系描述` HARD RULE：
- 情侣与所有多人拍摄必填。
- 描述关系结构、角色层级与互动基础；不得只写“情侣 / 家人 / 朋友”。
- 不使用固定关系 few-shot，按当前主题动态生成。

Hard Gates：
- A/B：两个现代现实世界著名真实地点，彼此地域/空间差异明显。
- C：古代 / 未来现实地标未来化 / 已知作品+明确地点。
- 三张卡全部通过 `few_shot_exclusion_set`。
- 禁止泛风格卡代替时空锚点。

结尾：
`可直接复制上方任意方向的【8宫格出图提示词】自行出图；或回复 A / B / C，我直接为你生成该方向的 8 宫格图片（出8宫格），无需等待冗长计划；也可以回复“抽卡”。`
