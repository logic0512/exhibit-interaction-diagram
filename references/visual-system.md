# 视觉 atomic 资产

## 作用

这些资产相当于本 skill 的视觉校准器。它们不负责产生创意，也不是完整展项模板；它们只负责让人物、动作、载体和反馈结果稳定。

active assets 只使用 `assets/visual-system/atomic/` 里的单意图图片。每张图只能对应一个意思。

组图、contact sheet、未筛选资产页、派生过程图和退稿图都不能作为最终生图参考，也不能进入 skill active assets。

完成图 examples 位于 `assets/examples/`，由 `references/example-gallery.md` 管理。examples 和 atomic assets 是两层不同资产：

- atomic assets：校准人物、动作、载体、反馈这些局部关系。
- examples：校准一张完整展项交互图的整体密度、构图和设备交互样式。

不要把 examples 当组件库拆开使用，也不要把 atomic assets 拼成完整方案。

## 约束优先级

不同资产层级的权重不同：

1. 人物 atomic 资产：硬约束。每次生图都必须选择并查看 1 张人物资产。所有人物必须沿用它的人物 IP。
2. 动作 atomic 资产：强参考。用于校准手、脚、身体和触发点的关系。
3. 载体和结果 atomic 资产：中强参考。用于保证载体和反馈可识别，但不复制具体外形。
4. 完成图 examples：低频校准。只看整体图面密度和交互关系，不控制人物画法。

如果人物 atomic 资产和完成图 example 发生冲突，以人物 atomic 资产为准。

## 选择规则

每次根据当前玩法选择少量 atomic 资产，不要一次性加载整套资产：

- 人物：必选 1 张。儿童/亲子/空间尺度优先 `human/01-adult-child-scale.png`；儿童低位操作或桌面互动优先 `human/02-child-low-reach.png`；墙面触摸优先 `human/03-touch-wall.png`。
- 动作：按需要选 0-1 张最接近主参与动作的图。若动作资产与人物资产冲突，优先保持人物 IP，再借用动作关系。
- 载体：只有涉及屏幕、投影、灯光、感应、声音、地面触发、操作面或机械响应时，选 0-1 张。
- 结果反馈：如果反馈结果容易画不清，选 0-1 张。
- 交互链路：不使用步骤条图片，用 `interaction-logic.md` 和提示词控制。

禁止把多个动作资产混合成一个复杂动作。禁止把多个载体资产堆成设备清单。禁止生成分格组件图。

## 资产目录

### 人物尺度与基础姿态

路径：`assets/visual-system/atomic/human/`

用于校准统一人物 IP、成人/儿童/亲子尺度、儿童低位触达和墙面触摸关系。

常用文件：

- `01-adult-child-scale.png`
- `02-child-low-reach.png`
- `03-touch-wall.png`

### 动作姿态

路径：`assets/visual-system/atomic/actions/`

用于校准道具触发、角色任务、声音记忆、选择判断、创造输出或协作任务里的核心动作。

常用文件：

- `01-place-to-trigger.png`
- `02-scan-recognition.png`
- `03-listen-to-sound-point.png`
- `04-vote-choice.png`
- `05-parent-child-collaboration.png`
- `06-record-message.png`
- `07-two-person-collaboration.png`

### 载体识别

路径：`assets/visual-system/atomic/carriers/`

用于校准载体的可识别方式，不固定外形。载体可以根据创意变化，稳定的是识别关系。

常用文件：

- `01-projection-source-path-target.png`
- `02-sensing-range.png`
- `03-floor-trigger.png`
- `04-operation-surface.png`
- `05-display-surface.png`
- `06-sound-direction.png`
- `07-mechanical-response.png`

### 结果反馈

路径：`assets/visual-system/atomic/results/`

用于校准“触发之后发生了什么”，避免只画触发点、看不出结果。

常用文件：

- `01-generated-result.png`
- `02-path-light-up.png`
- `03-work-on-wall.png`
- `04-connected-network.png`
- `05-unlock-reveal.png`
- `06-branching-feedback.png`
- `07-scale-magnification.png`
- `08-saved-record.png`

## 使用规则

- 看资产是为了校准，不是为了复刻。
- 人物资产不是软参考，是风格硬锁。不能让主题、空间或 example 把人物变成新的插画角色。
- 单张最终图只表达一个核心玩法。
- 资产只能提供人物尺度、动作关系、载体识别或反馈表达。
- 如果用户创意需要新造型，允许创造新装置；不要受 atomic 资产外形限制。
- 如果生成结果像组图、组件库、设备清单或分镜说明，说明资产使用失败，要重生成。
