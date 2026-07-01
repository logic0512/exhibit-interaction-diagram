# 完成图 Examples

## 作用

`assets/examples/` 是完成图校准层，不是组件库。

它回答的问题是：一张合格的展项装置交互图整体应该长什么样。它不负责提供可复制的设备造型、主题内容或构图模板。

使用 examples 时，只看这些维度：

- 画面密度。
- 留白比例。
- 人物与装置的尺度关系。
- 人物动作、触发点、反馈区域的连接方式。
- 中文标注数量和位置。
- 设备类型如何被一眼识别。
- 最终图如何保持“一张完整玩法图”，而不是组件图。

## 使用规则

- 默认不要一次打开全部 examples。
- 只在当前创意涉及相应设备类型，或上一次生成风格漂移时，查看 1 张最接近的 example。
- examples 只做低频视觉校准，不进入默认提示词堆叠。
- 不要照抄 example 的构图、设备形状、标注位置或内容效果。
- 如果生成图和 example 太像，需要换构图、换装置形态或换人物动作。
- 如果用户给了明确参考图，以用户参考图为主，examples 只负责保持本 skill 的图面语言。

## Example Index

### 01 Wall Screen Interaction

文件：`assets/examples/01-wall-screen-interaction.png`

校准：

- 墙面屏幕反馈。
- 站位或手势触发。
- 屏幕内容用抽象反馈块表达，不画真实 UI。

不要复制：

- 墙面屏幕数量。
- 具体图标和数据图形。
- 人物站位角度。

### 02 Projection Mapping

文件：`assets/examples/02-projection-mapping.png`

校准：

- 投影源、投影路径、投影落点三者必须同时可读。
- 人物触发和投影光路要分开表达。
- 实体模型表面可以承载投影反馈。

不要复制：

- 桌面模型造型。
- 投影机位置。
- 等高线式内容效果。

### 03 Lighting Feedback

文件：`assets/examples/03-lighting-feedback.png`

校准：

- 儿童触发和成人陪伴的身高关系。
- 灯具、光束、被照亮区域之间的反馈关系。
- 黄色/橙色作为灯光反馈的主色。

不要复制：

- 墙面浮雕造型。
- 灯具数量。
- 操作柱外形。

### 04 Sound Listening Point

文件：`assets/examples/04-sound-listening-point.png`

校准：

- 声源位置。
- 人物站入点位并朝向声源。
- 声波方向和小反馈屏的关系。

不要复制：

- 声柱外形。
- 站位圆形大小。
- 右侧反馈屏布局。

### 05 Floor Trigger Path

文件：`assets/examples/05-floor-trigger-path.png`

校准：

- 儿童踩踏触发。
- 地面点位和路径点亮。
- 低位反馈适配儿童视角。

不要复制：

- 低位长屏造型。
- 地面点位数量。
- 植物或装饰物。

### 06 Tangible Operation Table

文件：`assets/examples/06-tangible-operation-table.png`

校准：

- 手部放置道具。
- 操作台触发区域。
- 屏幕反馈与道具输入的连接。

不要复制：

- 操作台比例。
- 控件组合。
- 屏幕图形内容。

### 07 Mechanical Response

文件：`assets/examples/07-mechanical-response.png`

校准：

- 手动输入和机械联动。
- 结构打开、旋转、升起等实体动作。
- 局部放大框的使用边界。

不要复制：

- 花瓣式开合结构。
- 底座比例。
- 放大框位置。

### 08 Multi Person Collaboration

文件：`assets/examples/08-multi-person-collaboration.png`

校准：

- 2-3 人协作输入。
- 多个输入汇总到一个共享结果。
- 成人与儿童同一人物系统下的身高差。

不要复制：

- 圆桌形式。
- 参与者数量和站位。
- 中央屏幕图形。

### 09 Specimen Reconstruction

文件：`assets/examples/09-specimen-reconstruction.png`

校准：

- 选择、识别、复原类玩法需要多个对象或多个状态支撑。
- 标本入口、识别托盘和复原反馈之间要形成清晰链路。
- 反馈内容可以分成骨骼、外形、生态环境等层级。

不要复制：

- 标本数量和具体形态。
- 透明显示柜造型。
- 生物复原题材。

### 10 Globe Surface / Arc Projection

文件：`assets/examples/10-globe-surface-arc-projection.png`

校准：

- 投影反馈可以贴合到装置本体、球面或半透明信息弧上。
- 投影目标介质要服务内容，而不是默认外接幕布。
- 短焦投影源、球面落点和弧形信息层要保持物理关系。

不要复制：

- 地球仪外形。
- 透明弧的具体角度和尺寸。
- 地理/生态内容。

### 11 Film Embedded Rear Projection

文件：`assets/examples/11-film-embedded-rear-projection.png`

校准：

- 胶片、档案、记忆类内容可以使用内嵌背投窗、光箱或半透明片窗。
- 机械输入、选中胶片帧和反馈窗口要在同一装置里形成闭环。
- 不必为了表达投影而外接独立幕布。

不要复制：

- 胶片环造型。
- 台座比例。
- 具体城市记忆画面。

## 失败信号

如果使用 examples 后出现以下情况，说明 examples 被误用了：

- 画面和 example 构图过于相似。
- 设备造型被直接复制。
- 主题内容被带入当前创意。
- 图变成 example 的变体，而不是用户创意的表达。
- 为了凑齐某个 example 里的元素，加入了当前玩法不需要的设备。

正确用法是：借图面质量和设备表达逻辑，不借具体方案。
