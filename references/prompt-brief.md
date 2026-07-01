# Prompt Brief

这个文件不是最终生图提示词。它用于在生图前把创意判断清楚，避免把所有规则一股脑塞进 image model。

最终喂给生图工具的内容，应从本 brief 中提取到 `runtime-prompt.md`，只保留当前命题真正相关的部分。

## 使用时机

- 直接生图：快速填写已知字段；缺失字段用保守假设补齐，不要长篇讨论。
- 辅助表达：先用 `idea-expansion.md` 把抽象主题转成动作，再填写 brief。
- 回归测试：记录本案例使用了哪些空间、硬件、人物和载体约束。

## 1. Creative Summary

- User idea:
- One-sentence gameplay:
- Target audience:
- Main diagram archetype:
- Aspect ratio:
- Output goal:
  - 一张清晰能看懂玩法的展项装置交互图。
  - 没参与过讨论的人应能在 3 秒内理解：人怎么参与、触发了什么、反馈在哪里发生。

## 2. Interaction Chain

- Participant:
- Core action:
- Trigger:
- Feedback area:
- Result:
- The visual link that must be readable:
  - 人的动作 -> 触发点/感应范围 -> 反馈区域 -> 内容变化。

如果这条链路无法一句话说清，先不要进入生图。

## 3. Information Content

- Theme/content:
- Feedback content:
  - 屏幕、投影、灯光、声音或机械反馈中具体出现什么。
- Content change:
  - 互动前后内容如何变化。
- Content-carrier pairing:
  - 为什么这个内容适合当前载体。
- Specificity boundary:
  - 用户没有指定真实城市、建筑、品牌、地点、人物或车辆品牌时，使用泛化轮廓、编号对象和抽象信息。
  - 不要自行生成真实地标、品牌标识、可识别专属建筑或具体车型品牌。

媒体反馈不能是固定蓝色 UI、空白投影或无意义发光效果。它必须服务当前主题和玩法。

## 4. Spatial And Hardware Grounding

- Space condition:
  - 尺寸、亮度、人流、通道属性、儿童空间、黑场/半暗/明亮等。
- Carrier suitability:
  - 当前载体为什么适合这个空间。
- Device form:
  - 独立轻量 / 家具化 / 局部安装 / 大型结构。
  - 普通互动默认优先独立轻量、家具化或局部安装。
  - 顶天立地轨道、龙门架、全高立柱、天花吊架、大型桁架只在明确需要时使用。
- Device working distance:
  - 设备到墙面、地面、物体、屏幕或感应目标之间的合理距离。
  - 投影、探照灯、扫描灯、定向声源、体感感应必须画出源头、路径或检测范围。
- Human reach envelope:
  - 人站在哪里，手、脚、视线是否自然够得到。
  - 儿童展项要检查儿童手高、眼高、步幅和成人陪伴关系。
  - 如果设备需要在高处或远处移动，必须有可触达的把手、滑块、拉绳、手轮、平衡臂或低位控制件。
- Hardware category:
  - 投影机 / 短焦投影 / 背投 / LCD 商显 / 拼接屏 / LED 点阵 / 透明 LED / 地踩 LED / 触摸屏 / 红外框 / 激光雷达 / Kinect / 编码器 / 音响 / 机柜 / 自定义硬件。
- Installation method:
  - 吊装 / 壁挂 / 落地支架 / 桌内嵌入 / 墙后 / 屏幕后 / 地面嵌入 / 设备机身集成 / 其他。
- Physical cues:
  - 边框、拼缝、箱体厚度、支架、吊点、维护门、散热、机柜、传感器视场、投影锥、声场方向。

## 5. Visual References

- Required human atomic reference:
  - 每次必须选 1 张 `assets/visual-system/atomic/human/` 下的人物资产。
  - 人物资产优先级高于 examples、主题内容和设备造型。
- Optional action reference:
- Optional carrier reference:
- Optional result reference:
- Optional finished example:
  - 最多选 1 张 `assets/examples/`，只用于图面密度和完整度校准。
  - 不复制构图、设备造型、标注位置或主题内容。
- Reference budget:
  - 通常 1 张人物 + 0-2 张相关 atomic 资产。
  - 不使用组图、contact sheet、退稿图或整套资产。

## 6. Rules To Inject

只选择当前命题相关规则，不要全量复制。

- Human lock:
  - 所有人物必须沿用选中人物资产的统一 IP。
  - 只能改变身高、姿态、朝向和数量。
- Carrier rules:
  - 屏幕：有清晰显示面、厚度或边框，内容服务主题。
  - 投影：有投影源、路径、目标面，亮度和空间成立。
  - 灯光：有灯具、照射范围、被照亮的内容变化。
  - 感应：有识别区域、传感器位置、身体进入方式。
  - 声音：有声源、听音位置、声场方向。
  - 机械：有可操作件、运动方向、反馈结果。
- Spatial rules:
  - 小空间避免大型展台和沉浸式投影。
  - 明亮空间避免普通投影作为主反馈。
  - 普通手动交互避免重型全高结构。
- Content rules:
  - 反馈画面必须有主题信息。
  - 不把小屏幕改成独立大屏、浮动说明卡或底部说明条，除非用户明确要求。

## 7. Runtime Prompt Assembly

进入 `runtime-prompt.md` 时只带入这些内容：

- 一句话玩法。
- 人 - 触发 - 反馈 - 结果链路。
- 反馈中的具体信息内容。
- 当前空间和硬件约束。
- 选中的人物资产。
- 0-2 个必要载体或结果参考。
- 2-5 条当前载体最关键的规则。
- 6-10 条硬约束。

不要把本文件整段复制进最终提示词。最终提示词应该短、准、可执行。

## Pre-generation Gate

生图前快速检查：

- 玩法是否能在 3 秒内看懂。
- 人物是否真的参与核心动作。
- 反馈内容是否具体，不是通用 UI 或空白效果。
- 空间亮度、尺寸、观看距离是否支撑载体选择。
- 设备工作距离是否成立。
- 成人或儿童是否自然够得到操作点。
- 是否只选择了必要资产。
- 是否避免了无理由的大型结构。
- 是否避免了用户未指定的真实品牌、地标和专属建筑。
