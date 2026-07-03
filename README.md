# Exhibit Interaction Diagram Skill

> 把一句展项创意，变成一张别人 3 秒能看懂怎么玩的装置交互图。

[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-exhibit--interaction--diagram-blueviolet)](SKILL.md)
[![skills.sh](https://skills.sh/b/logic0512/exhibit-interaction-diagram)](https://skills.sh/logic0512/exhibit-interaction-diagram)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**用于生成、扩展和质检展览多媒体互动装置概念图，重点不是漂亮效果图，而是清楚表达“人怎么参与、触发了什么、反馈在哪里、内容表达什么”。**

[效果示例](#效果示例) · [快速开始](#快速开始) · [触发方式](#触发方式) · [工作链路](#工作链路) · [验证与测试](#验证与测试) · [安全边界](#安全边界)

---

<table>
  <tr>
    <td><img src="examples/showcase/cases/01-yangtze-fishing-ban-table.png" alt="长江禁渔互动桌"></td>
    <td><img src="examples/showcase/cases/02-tree-spotlight-interaction.png" alt="树木生态探照灯"></td>
    <td><img src="examples/showcase/cases/03-city-memory-group-wall.png" alt="城市记忆多人互动"></td>
  </tr>
  <tr>
    <td><img src="examples/showcase/cases/04-visible-light-children-interaction.png" alt="可见光通信儿童互动"></td>
    <td><img src="examples/showcase/cases/05-flower-scent-recognition.png" alt="花香与植物识别"></td>
    <td><img src="examples/showcase/cases/06-ar-nature-habitat-viewer.png" alt="AR 自然场景观察"></td>
  </tr>
</table>

<sub>六个真实测试案例：互动桌、探照灯、多人协作、儿童科普、气味识别、AR 自然观察。</sub>

---

## 它解决什么问题

展项装置图很容易变成三种东西：漂亮但看不懂怎么玩的效果图、堆满设备的硬件清单、或者只有屏幕 UI 的概念稿。

这个 skill 把展项创意先拆成“人 - 触发 - 反馈 - 结果”，再结合空间大小、亮度、设备距离、人体可达范围和信息内容，生成一张能沟通玩法的装置交互图。

它也内置了人物、动作、载体、结果反馈的 atomic assets，用来稳定人物风格和载体识别，避免每次生图都漂成不同画风。

---

## 效果示例

### 示例 1：长江禁渔互动桌

输入：

```text
我有一个长5米，宽4米的空间。在空间的中间，我想做一个宽2米，长4米的互动桌。在这个互动桌上，可以进行交互，了解关于长江禁渔的相关保护措施，长江的生态资源面貌。设置不同的道具，跟桌面的屏幕进行结合互动。
```

输出图：

![长江禁渔互动桌](examples/showcase/yangtze-fishing-ban-table.png)

质检结果：

- 人物、儿童身高和桌面尺度能支撑玩法。
- 道具触发区、桌面地图、禁渔区、巡护线、湿地修复、江豚栖息和鱼群恢复都有对应关系。
- 没有额外加入无关大屏、投影或设备清单。

### 示例 2：AR 自然场景观察

输入：

```text
在一个展厅仿真自然场景中，做一个跟AR相关的交互装置，可以通过这个交互装置看到对应这个场景中会生存的相关动物。
```

输出图：

![AR 自然场景观察](examples/showcase/cases/06-ar-nature-habitat-viewer.png)

质检结果：

- 仿真自然场景、AR 观察装置和参与者站位关系清楚。
- AR 信息叠加在场景对应位置，而不是漂浮成普通说明卡。
- 动物、栖息环境和观察动作形成了清晰的内容反馈链路。

### 案例介绍

这些案例用于展示不同主题、空间条件、交互动作和反馈载体下，skill 如何把原始想法转成一张能看懂玩法的装置交互图。

| 展项名字 | 展项的原始 prompt | 图 |
|---|---|---|
| 长江禁渔互动桌 | 我有一个长5米，宽4米的空间。在空间的中间，我想做一个宽2米，长4米的互动桌。在这个互动桌上，可以进行交互，了解关于长江禁渔的相关保护措施，长江的生态资源面貌。设置不同的道具，跟桌面的屏幕进行结合互动。 | <img src="examples/showcase/cases/01-yangtze-fishing-ban-table.png" alt="长江禁渔互动桌" width="260"> |
| 树木生态探照灯 | 做一个探照灯效果的多媒体装置，设计一个垂直的树木线稿图案在墙体，通过互动的探照灯上下移动，灯光印在墙体的位置，探照灯上的小屏幕会展示出来这颗树对应的位置的生物生态分布。 | <img src="examples/showcase/cases/02-tree-spotlight-interaction.png" alt="树木生态探照灯" width="260"> |
| 城市记忆多人互动 | 做一个满足4-5个人一起互动的多媒体装置，放在5米X4米的空间，主题为城市的记忆，可以结合空间的一面墙一起做交互。 | <img src="examples/showcase/cases/03-city-memory-group-wall.png" alt="城市记忆多人互动" width="260"> |
| 可见光通信儿童互动 | 在一个空间里做一个满足3人以内的交互场景，不要利用空间的墙面，墙面留白。主题是关于可见光通信的，通过不同的操作方式，了解影响可见光通行的因素。场景的交互装置要符合儿童可交互的特点。 | <img src="examples/showcase/cases/04-visible-light-children-interaction.png" alt="可见光通信儿童互动" width="260"> |
| 花香与植物识别 | 做一个可以闻花香和识别不同植物的花的类型的装置。 | <img src="examples/showcase/cases/05-flower-scent-recognition.png" alt="花香与植物识别" width="260"> |
| AR 自然场景观察 | 在一个展厅仿真自然场景中，做一个跟AR相关的交互装置，可以通过这个交互装置看到对应这个场景中会生存的相关动物。 | <img src="examples/showcase/cases/06-ar-nature-habitat-viewer.png" alt="AR 自然场景观察" width="260"> |
| 标本复原互动装置 | 做一个标本复原互动装置，孩子选择不同的岩石或化石标本，触发旁边的透明显示面，看到对应古生物从骨骼、外形到生态环境的复原过程。 | <img src="assets/examples/09-specimen-reconstruction.png" alt="标本复原互动装置" width="260"> |
| 地球仪球面投影 | 做一个手摇地球仪互动装置，观众转动地球仪选择区域，投影反馈展示该区域的气候、路线和生态信息，但希望装置不要变成旁边放一块屏幕。 | <img src="assets/examples/10-globe-surface-arc-projection.png" alt="地球仪球面投影" width="260"> |
| 胶片内嵌背投 | 做一个城市记忆胶片互动装置，观众手摇推进胶片，投影或背光反馈放大选中的记忆片段，但不要又变成旁边一块独立幕布。 | <img src="assets/examples/11-film-embedded-rear-projection.png" alt="胶片内嵌背投" width="260"> |

---

## 快速开始

### 方式 1：从 GitHub 安装

仓库公开后可用：

```bash
npx skills add logic0512/exhibit-interaction-diagram
```

装完对 Agent 说：

```text
Use $exhibit-interaction-diagram to 把这个展项创意生成一张清晰能看懂玩法的装置交互图：{你的创意}
```

### 方式 2：手动安装

把本目录复制到你的 skills 目录，例如：

```bash
cp -R exhibit-interaction-diagram ~/.codex/skills/
```

然后用同样的触发句调用。

---

## 触发方式

- “把这个展项创意画成一张能看懂玩法的装置交互图。”
- “我只有一个主题，帮我扩展成可互动、可画出来的方案。”
- “这张装置图看起来不落地，帮我检查设备距离和人能不能操作。”
- “帮我做一个屏幕/投影/灯光/声音/机械互动展项的概念图。”
- “我想做儿童展项，要体现孩子身高和视角。”
- “不要只做效果图，要让客户看懂怎么玩。”

---

## 工作链路

这个 skill 有四种使用路径：

| 路径 | 适合情况 | 交付物 |
|---|---|---|
| 直接生图 | 已经有明确装置、动作、反馈和空间条件 | 一张玩法清楚的装置交互图 |
| 辅助表达 | 只有方向，玩法还没成型 | 1 个补全后的互动方案，再进入生图 |
| 创意扩展 | 只有主题、内容、目标人群或空间诉求 | 2-3 个互动方向，并推荐最适合画图的方案 |
| 失败复盘 | 已有图效果不对 | 按人物、设备距离、可达范围、空间秩序、反馈内容做质检 |

核心生成链路：

```text
用户创意
→ prompt-brief.md 结构化判断
→ 选择人物和必要 atomic assets
→ runtime-prompt.md 组装最终生图提示词
→ image generation
→ qa-checklist.md 质检迭代
```

---

## 它和普通生图提示词有什么不同

| 维度 | 普通提示词 | 本 skill |
|---|---|---|
| 目标 | 生成好看的概念图 | 生成能看懂玩法的装置交互图 |
| 人物 | 可有可无，容易漂移 | 人物强制参与核心动作，并锁定统一视觉层 |
| 设备 | 常被画成抽象发光物 | 要符合常见展陈硬件逻辑、安装方式和工作距离 |
| 空间 | 容易忽略尺度和亮度 | 先判断空间大小、亮度、人流、儿童尺度和载体适配 |
| 反馈内容 | 常见空屏、蓝色 UI、泛光效 | 屏幕/投影/灯光/声音/机械反馈必须承载主题信息 |
| 失败处理 | 靠重新描述 | 内置质检规则，会优先检查玩法、尺度、设备和反馈是否成立 |

---

## 文件结构

```text
SKILL.md                         # 主工作流
README.md                        # GitHub 说明和 showcase
LICENSE                          # MIT license
agents/openai.yaml               # Agent 界面元信息
references/                      # 规则、模板、质检和空间/硬件约束
references/prompt-brief.md       # 生图前的结构化判断母版
references/runtime-prompt.md     # 最终生图短提示词母版
assets/visual-system/atomic/     # 人物、动作、载体、结果的单意图资产
assets/examples/                 # 完成图 examples，只做低频图面校准
examples/showcase/               # 公开 README 使用的稳定案例图
```

`outputs/` 是本地测试输出目录，不进入发布仓库。

---

## 质量控制

这个 skill 会在生成前后关注这些质量点：

- 人物是否真的参与核心动作。
- 设备距离、投影方向、人体可达范围是否成立。
- 屏幕、投影、灯光、声音和机械反馈是否承载主题信息。
- 图面是否像一张能沟通玩法的展项装置图，而不是海报、PPT、设备清单或纯 UI。

---

## 安全边界

- 不自动发布、不上传、不调用外部 API。
- 不把私人素材路径写进提示词。
- 不把本地 `outputs/` 测试图当成 active assets。
- 不把任何未授权材料里的具体案例复制成最终图。
- 不把装置图做成施工图、弱电系统图或可直接制造的工程图。
- 如果用户给出的空间、亮度或硬件条件不足以支撑某个载体，会先补假设或提示限制。

---

## 包含内容

这个 skill 包含：

- 出图工作流
- 人物锁定
- 空间匹配
- 硬件落地
- atomic assets
- finished examples
- showcase 案例图

## License

[MIT](LICENSE)
