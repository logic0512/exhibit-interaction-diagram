# Runtime Prompt

这个文件是最终生图提示词母版。使用前先完成 `prompt-brief.md`，再从本文件选择：

1. `Base Prompt`：每次必用。
2. `Conditional Blocks`：只选当前命题相关模块。
3. `Repair Prompts`：只在出图失败后用于重生成或局部编辑，不进入首次生图 prompt。

原则：最终提示词应该短、准、可执行。不要把 brief、QA、reference 或本文件全文塞进 image model。

## Base Prompt

每次生图只填入当前命题已经成立的信息。

```text
Generate one standalone concept image for an exhibition interactive installation.
Choose the aspect ratio that best explains the gameplay; do not force a horizontal layout.

Goal:
Make the gameplay legible within 3 seconds: who interacts, what action triggers the system, where feedback appears, what information changes, and why the interaction helps explain the theme.

Creative idea:
{one-sentence gameplay}

Interaction chain:
- Participant: {adult / child / family / group}
- Core action: {physical action}
- Player task: {aim / match / move / block / connect / sort / repair / collect / route / cooperate / reach success target}
- Trigger: {control / prop / gesture / sensing volume / rail movement / light beam / floor step / mechanical action}
- Feedback area: {screen / projection target / tabletop / floor / object / sound zone / mechanical object / space surface}
- Result: {what changes visually, physically, aurally, or spatially}
- Content variable changed by the action: {time / position / selected object / layer / connection / parameter / sequence / disassembly / reconstruction / collaboration state}
- Content-interaction thesis: {what relationship the visitor understands because of this action}

Interactive information:
- Theme: {knowledge, story, relationship, state, comparison, timeline, ecology, city development, structure, etc.}
- Feedback content: {specific simplified images, layers, paths, states, map nodes, timeline fragments, model parts, or result indicators}
- Information obtained through interaction: {what is revealed, changed, compared, verified, advanced, or summarized only because the visitor acts}
- Gameplay evidence: {objects, states, layers, positions, or nodes needed to make the gameplay readable}

Spatial and device grounding:
- Space condition: {size, brightness, circulation, viewing distance, child scale, dark/bright assumption}
- Device form: {independent lightweight / furniture-like / wall-integrated / floor-integrated / showcase-integrated / custom shaped device / handheld / wearable when explicit / large structure only if necessary}
- Working distance and reach: {how the device, target, sensing area, control, and visitor body relate physically}
- Required visual reference: {selected human atomic asset path}
- Optional references: {0-2 directly relevant assets or one finished example; otherwise none}

Visual DNA:
Clean professional exhibit concept sketch on white or light gray background.
Gray-black hand-drawn line art, slight sketch wobble, clear scale, sparse yellow/orange handwritten Chinese annotations.
Use restrained color: cyan/blue only for local screen glow, projection, sensing, or digital feedback; choose one theme-appropriate secondary accent when useful.
Keep the image visually restrained, not crowded with explanations. It should feel like an exhibit design sketch, not a poster, UI mockup, PPT infographic, wiring diagram, children's illustration, or polished product render.

Chinese handwritten labels:
{0-6 short labels, only where they clarify action or feedback}

Always enforce:
- One image explains one core gameplay idea.
- People follow the selected human atomic reference: blank oval heads, no hair, no facial features, simple clothing, gray-black sketch style.
- The main participant must perform the core action.
- Feedback must contain theme-specific information, not generic UI, empty projection, or meaningless glow.
- Information printed or displayed on the installation is not interaction by itself. Visitor action must reveal, change, compare, verify, advance, or summarize the information.
- Use only devices needed for this interaction; do not create a hardware inventory.
- Keep carrier scale, working distance, human reach, and human-device boundary believable.
```

## Conditional Blocks

只把相关模块追加到 Base Prompt。通常每次追加 1-4 个模块即可；不要全量复制。

### Children Or Family

```text
Child/family rules:
- Show child height, eye level, reach range, and adult-child scale clearly.
- Controls must be low, large, graspable, and readable from a child's point of view.
- Children should perform the main task when the exhibit is designed for children; adults may guide but should not take over.
```

### Multi-Person Collaboration

```text
Multi-person rules:
- Each participant needs a meaningful role, reachable control, immediate feedback, and contribution to one shared visible result.
- Avoid one active person with others watching.
- If there are 4-5 people, divide roles by stage, node, parameter, object, or task instead of repeating the same button.
```

### Process Or Evolution Content

```text
Process-content rules:
- For evolution, development, communication, flow, transformation, or system-collaboration topics, show one content object transforming across stages.
- Use the same message, route, artifact, dataset, model, or signal from input to change to result.
- Do not replace the process with unrelated hotspots.
```

### Selection, Comparison, Scanning, Timeline, Reconstruction

```text
Gameplay-evidence rules:
- If the gameplay depends on selection, comparison, scanning, recognition, reconstruction, layered reveal, disassembly, or timeline progress, show enough visual evidence: 2-4 objects, states, layers, positions, or nodes.
- A single object is allowed only if it visibly opens, rotates, splits, changes state, or reveals hidden content.
```

### Spatial Scene Or Immersive Room

```text
Spatial-scene rules:
- If the user asks for a spatial scene, immersive room, blank walls, or no wall media, show true spatial embedding: room boundary, floor area, standing zones, circulation, viewing distance, and how the exhibit occupies the space.
- If room dimensions are provided or the space is immersive, do not collapse the image into a single-wall elevation. Show at least two wall planes or a corner/wraparound layout, floor depth, and participant positions.
- If walls must remain blank, keep main feedback on the installation body, floor path, low freestanding modules, handheld props, or central object.
```

### Lightweight Or Non-Table Installation

```text
Installation-form rules:
- Do not default every installation into a central exhibit table.
- Choose the form from the content and action: wall-integrated, floor-integrated, showcase-integrated, spatial-surface based, custom shaped device, handheld, or wearable when explicit.
- Prefer independent lightweight, furniture-like, wall/floor/showcase-integrated, or local installation forms.
- Avoid floor-to-ceiling rails, gantries, full-height columns, ceiling-to-floor frames, trusses, or architectural-scale structures unless functionally necessary.
```

### Projection

```text
Projection rules:
- Show projection source, one active emitting aperture, beam direction, target surface, and landing content.
- The beam starts from the visible lens, top mirror slot, angled outlet, hidden opening, or rear-projection source; do not make multiple apertures glow on one source.
- Place the target surface in front of the lens along the optical axis. Do not put projection content on a side wall or right wall unless the lens clearly points there and the surface faces the beam.
- Separate interaction arrows from projection beams.
- Prefer the target medium that best expresses the idea: object, model, tabletop, floor path, device surface, translucent layer, rear projection, wall, or screen.
```

### Built-In Or Small Screen

```text
Built-in screen rules:
- Keep feedback on the specified built-in, small, handheld, or device screen.
- Do not replace it with a detached large screen, floating UI card, or bottom explanation bar.
- Screen content should be a simplified result, state, map node, layer, comparison, or next-step cue, not a full app interface.
```

### Sensor Or Gesture Recognition

```text
Sensing rules:
- Show the sensor position and detection zone.
- If the user puts a hand into a recognition device, show an open sensing bay, recess, frame, or transparent detection volume; the hand enters it naturally.
- The detection zone must cover the body, hand, prop, or object being sensed.
```

### IoT Or Many Sensing Devices

```text
IoT/many-device rules:
- Do not place every sensor as a labeled wall box or device catalog.
- Combine wall-mounted sensing points with scene-integrated sensors embedded in props, shelves, plants, bins, lights, doors, appliances, floor pads, or handheld tags.
- Organize devices around application scenarios or event chains, not application names alone.
- Show local feedback on or near the sensed object: light ring, status strip, valve movement, shelf light, bin indicator, floor point, local display, or object state change.
```

### Mechanical Controls Or Physical Props

```text
Mechanical/control rules:
- Show the control's mounting point: pivot plate, base, shaft, track, bracket, tabletop, pedestal face, wall mount, floor base, or prop body.
- The participant may grip or touch the control, but fixed hardware must not grow out of the hand, arm, torso, clothing, or child body.
- A wheel, knob, crank, slider, handle, or prop must visibly control something through an axis, bracket, pointer, linked lamp head, moving receiver, track direction, target ring, or immediate feedback.
```

### Wearable Or Handheld Device

```text
Wearable/handheld rules:
- Wearable or handheld devices are allowed only when the concept explicitly calls for them.
- Show readable straps, handles, controller shells, head straps, wrist straps, shoulder straps, belt, sleeve, clasp, or garment-integrated modules.
- Do not paste unexplained hardware blocks onto the body.
```

### No Real-World Specificity

```text
Specificity rules:
- Do not invent real landmarks, brands, logos, named buildings, specific locations, people, or vehicle brands unless the user specified them.
- Use generic silhouettes, numbered objects, abstract labels, and non-branded forms.
```

### Iterative Revision

```text
Iteration-lock rules:
- Keep the accepted human IP, sketch linework, material feel, spatial brightness, main composition mode, device scale, and color strategy unless the user explicitly asked to change them.
- Only fix the stated failure.
```

## Repair Prompts

以下只在失败后使用，不进入首次生图 prompt。

### 人物没有参与核心动作

```text
Edit or regenerate the image so the main human participant clearly performs the core interaction action. Connect the participant's hands, feet, gaze, and body orientation to the trigger point and feedback area. Keep the installation concept, sketch style, composition, and sparse labels.
```

### 玩法看不清

```text
Regenerate the image with the same installation idea, but make the gameplay legible in 3 seconds. Simplify unnecessary components, clarify the participant action, show the trigger point or sensing area, and make the feedback area visibly connected to the action.
```

### 玩法证据不足

```text
Regenerate the image with the same installation idea, but add enough visual evidence for the gameplay. If the interaction depends on selection, recognition, reconstruction, comparison, layered reveal, disassembly, or timeline progress, show 2-4 objects, states, layers, positions, or nodes. Do not rely on one static object and long labels.
```

### 内容交互意义弱

```text
Regenerate the image with the same installation idea and visual style, but make the content-interaction relationship explicit. Show what content variable the participant changes: time, position, object, layer, connection, parameter, sequence, disassembly, reconstruction, or collaboration state. The feedback must show how the theme-specific content changes because of the action, not just that a screen, projection, light, or wall turns on. For process or evolution topics, keep one content object transforming across stages.
```

### 信息摆放冒充交互

```text
Regenerate with the same topic and visual style, but remove designer-facing information boards, static parameter plaques, diagnostic gauges, or principle labels that are merely placed on the device. Turn the information into visitor-obtained feedback: the participant must perform a clear action that reveals, changes, compares, verifies, advances, or summarizes the theme-specific information. If the information would still be complete after removing the participant, redesign it as a playable task with reachable controls, immediate feedback, and a visible success/failure or before/after result.
```

### 投影不可实现

```text
Regenerate the image so the projection is physically plausible. First lock one active emitting aperture for each source: front lens, top mirror slot, angled outlet, hidden opening, or rear-projection source. The beam must begin at that aperture, not another glowing part of the same device. Then lock the lens optical axis: source position, lens direction, target medium, target position, and throw distance. Place the projection target directly in front of the lens along the beam centerline; do not default to a right-side wall. Show source, beam direction, target surface, and landing content aligned. Separate interaction arrows from the projection beam.
```

### 投影构图同质化

```text
Regenerate the image with a projection target medium that fits the concept instead of defaulting to a separate right-side screen. Consider object mapping, tabletop/model mapping, floor/path projection, translucent/rear projection, or feedback embedded into the device body. Keep the optical axis physically plausible, but vary the target surface and spatial composition.
```

### 蓝色过量

```text
Regenerate the image with restrained color. Keep cyan/blue only for local screen, projection, sensing, or digital feedback. Use theme-appropriate secondary colors for content layers, such as soft green, amber, warm gray, red-orange, black-white photo tone, or pale violet. Do not make the whole image blue-dominant.
```

### 人机边界错误

```text
Regenerate the image so fixed exhibition hardware is physically separate from the human body and visibly mounted to the installation. A participant may hold the knob or touch the control, but the control's pivot, base, shaft, track, bracket, tabletop, pedestal face, wall mount, floor base, or handheld prop body must be readable. Do not let fixed handles, cranks, levers, sliders, buttons, brackets, projectors, screens, sensors, cables, or device shells grow out of the hand, arm, torso, clothing, or child body. If the concept explicitly uses wearable or handheld devices, show readable straps, handles, controller shells, garment modules, or attachment structures instead of treating the body as an unexplained mounting surface.
```

### 组件太多

```text
Regenerate the image and remove irrelevant carrier components. Keep only the devices needed to explain this specific interaction. The image should feel like a clear exhibit interaction sketch, not a hardware inventory.
```

### 装置被固定成展台

```text
Regenerate the image with the same interaction logic, but choose the installation form from the content and spatial relationship instead of defaulting to a central exhibit table. Consider a wall-integrated element, floor path, showcase-integrated device, spatial corner, custom shaped object, handheld prop, or wearable device if it better explains the gameplay. Keep the form lightweight and readable.
```

### 空间置入不足

```text
Regenerate with the same interaction logic, but make it a real spatial exhibit scene rather than a product-style device placed in an empty room. Show blank walls if required, room corners or boundaries, floor circulation, participant standing zones, viewing distance, and multiple low freestanding interaction modules if the gameplay has multiple operations. Keep the walls unused when the user asked for blank walls; all feedback should stay on the installation body, floor path, central object, or low modules.
```

### 空间被压成单面墙

```text
Regenerate with the same wall-panel or device strategy, but show the full room volume. Do not present a single-wall elevation. Use a corner or wraparound perspective with at least two wall planes, floor depth, circulation path, participant positions, and exhibit elements distributed across multiple wall segments or spatial zones.
```

### 多人可玩性不足

```text
Regenerate with the same content principle, but turn the setup into a playable multi-person interaction. Each participant needs a clear role, reachable control, and immediate feedback that affects one shared goal. Replace designer-facing diagnostic modules with visitor-facing tasks: aim the light, move the receiver, insert/remove obstacle cards, reduce interference, route the signal, or make the signal packet reach the target. Show success/failure as a result of the players' actions.
```

### 控件意图不清

```text
Regenerate so every control clearly shows what it controls. A wheel, knob, crank, slider, or handle must be mounted and mechanically or visually linked to the changed element: lamp direction, receiver distance, obstacle position, signal strength, or selected state. Do not show a floating wheel, disconnected turntable, or abstract parameter knob.
```

### 同项目迭代风格漂移

```text
Regenerate with the same accepted visual system as the previous version: unified blank-oval-head human figures, gray-black hand-drawn sketch linework, light concept-sketch background, restrained cyan only for local digital feedback, and the same general material feel and spatial brightness. Only fix the stated issue; do not change the illustration style, character system, composition language, or color strategy unless explicitly requested.
```
