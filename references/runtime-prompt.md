# Runtime Prompt

这个文件是最终生图提示词母版。使用前先完成 `prompt-brief.md`，再把当前命题真正需要的信息压缩进这里。

目标：短、准、可执行。不要把 brief、QA 或全部载体规则整段塞进来。

```text
Generate one standalone concept image for an exhibition interactive installation.
Choose the aspect ratio that best explains the gameplay; do not force a horizontal layout.

Goal:
The image must clearly show how the installation is played. A viewer who did not join the discussion should understand within 3 seconds:
who interacts, what action triggers the system, where the feedback appears, and what information changes.

Creative idea:
{one-sentence gameplay}

Interaction chain:
- Participant: {adult / child / family / group}
- Action: {the core physical action}
- Trigger: {button / prop / gesture / sensing volume / rail movement / light beam / floor step / mechanical control}
- Feedback area: {screen / projection target / wall / tabletop / floor / object / sound zone / mechanical object}
- Result: {what the participant sees, hears, or changes}

Interactive information content:
- Theme: {knowledge, story, relationship, state, comparison, timeline, ecology, city development, structure, etc.}
- Feedback content: {specific images, layers, labels, model states, map paths, timeline fragments, data changes, biological distribution, structural parts, etc.}
- Content change: {before/after or action-driven change}
- Specificity boundary: if the user did not specify real cities, landmarks, brands, named buildings, people, or vehicle brands, use generic silhouettes, numbered objects, abstract labels, and non-branded forms.

Spatial and hardware grounding:
- Space condition: {size, brightness, viewing distance, circulation, child scale, dark/bright assumption}
- Carrier and device form: {independent lightweight / furniture-like / local installation / large structure only if necessary}
- Working distance: {reasonable distance or path between device, sensing area, projection/light/sound source, and target}
- Human reach: {where the person stands and how hand/foot/gaze naturally reaches the control}
- Hardware cues: {frames, thickness, seams, support, sensing volume, projection cone, lighting beam, sound direction, maintenance door, hidden controller if needed}

Visual lock references:
- Required human atomic reference: {asset path from assets/visual-system/atomic/human/}
- Optional references: {0-2 directly relevant atomic assets or one finished example; otherwise none}

Required human component:
All people must follow the selected human atomic reference as the strict style anchor:
simplified gray-black hand-drawn figures, blank oval heads, no hair, no facial features, simple long-sleeve top, simple pants, simple shoes, light pencil shading.
People may only vary in height, pose, orientation, and quantity.
One main participant must perform the core interaction. Hands, feet, gaze, and body direction must connect visibly to the trigger and feedback.
If the exhibit is for children or families, show child height, eye level, reach range, and adult-child scale clearly.

Carrier-specific rules:
{insert only 2-5 rules relevant to this concept}

Examples:
- Projection: show source, path, and target; do not place projector/spotlight flush against the target unless it is explicitly embedded.
- Built-in screen: keep the information on the small built-in screen; do not replace it with a detached large screen or floating UI card.
- Sliding screen: show track length, handle position, screen movement direction, and changing content behind or on the screen.
- Hand recognition: show an open sensing bay, recess, frame, or transparent detection volume; the hand enters it naturally.
- Lighting/spotlight: show the lamp body, beam, illuminated zone, and content revealed by the beam; use reachable controls for manual movement.
- Sound: show source, listening position, and sound direction.
- Mechanical operation: show handle, crank, wheel, slider, pivot, or prop plus visible movement result.

Composition:
{one main diagram archetype and the specific spatial arrangement}

Visual DNA:
Clean professional exhibit concept sketch on white or light gray background.
Gray-black hand-drawn line art with slight sketch wobble and clear device scale.
Sparse yellow/orange handwritten Chinese annotations for hotspots and arrows.
Cyan/blue only for screen glow, projection, sensing, or digital feedback.
Keep lots of empty space. Make the image a concept sketch, not a polished 3D render.

Chinese handwritten labels:
{4-6 short labels, such as 互动把手 / 感应区域 / 投影内容 / 信息层显现 / 滑动屏 / 儿童视角}

Hard constraints:
- One image explains one core gameplay idea.
- The main participant must perform the core action.
- Feedback must contain theme-specific information, not generic UI, empty projection, or meaningless glow.
- Use only devices needed for this interaction; do not create a hardware inventory.
- Do not invent real landmarks, brands, logos, named buildings, specific locations, people, or vehicle brands unless the user specified them.
- Match carrier scale to the space; avoid large projection, oversized tables, or immersive setups in small or bright spaces unless justified.
- Prefer independent lightweight, furniture-like, or local installation forms. Avoid floor-to-ceiling rails, gantries, full-height columns, ceiling-to-floor frames, trusses, or architectural-scale structures unless functionally necessary.
- Device working distance must be believable. Projection, spotlight, scanning, sensing, and directional sound need a visible gap, path, or detection volume.
- Human reach must be believable. Do not stretch arms, place controls outside natural reach, or let children use adult-height controls without a reachable interface.
- Do not copy reference assets or examples literally. Use them only to stabilize character style, carrier readability, and diagram language.
- Do not make a poster, advertisement, PPT infographic, UI mockup, wiring diagram, children's illustration, game concept art, or polished product render.
```

## 局部编辑提示

人物没有参与核心动作：

```text
Edit or regenerate the image so the main human participant clearly performs the core interaction action. Connect the participant's hands, feet, gaze, and body orientation to the trigger point and feedback area. Keep the installation concept, sketch style, composition, and sparse labels.
```

玩法看不清：

```text
Regenerate the image with the same installation idea, but make the gameplay legible in 3 seconds. Simplify unnecessary components, clarify the participant action, show the trigger point or sensing area, and make the feedback area visibly connected to the action.
```

组件太多：

```text
Regenerate the image and remove irrelevant carrier components. Keep only the devices needed to explain this specific interaction. The image should feel like a clear exhibit interaction sketch, not a hardware inventory.
```
