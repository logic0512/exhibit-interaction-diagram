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
- Gameplay evidence: {number of objects, selectable items, positions, layers, states, or timeline nodes needed to make the gameplay readable}
- Specificity boundary: if the user did not specify real cities, landmarks, brands, named buildings, people, or vehicle brands, use generic silhouettes, numbered objects, abstract labels, and non-branded forms.
- Color strategy: {main feedback color, secondary accent color, and how cyan/blue is limited to screen/projection/sensing/digital feedback only}

Spatial and hardware grounding:
- Space condition: {size, brightness, viewing distance, circulation, child scale, dark/bright assumption}
- Carrier and device form: {independent lightweight / furniture-like / local installation / large structure only if necessary}
- Projection type if used: {front projection / short-throw / ultra-short-throw / rear projection / table projection / model mapping / hidden source / projection blending / none}
- Projection target fit if used: {why the target medium is best: object surface / tabletop / model / device body / floor path / scrim / translucent screen / rear projection / wall or freestanding screen only when justified}
- Projection optical axis if used: source position {where}; lens direction {where it points}; target medium {wall/screen/tabletop/model/scrim/object/rear projection}; target position {in front of the lens}; throw distance {approximate}
- Working distance: {reasonable distance or path between device, sensing area, projection/light/sound source, and target; show source-to-target direction along the lens axis}
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
- Projection feasibility: the light path starts at the projection source, not at the user's hand, button, or annotation arrow. A normal front projector needs visible throw distance; a near-wall source must read as short-throw, rear projection, or embedded projection with correct angle and support.
- Projection optical-axis rule: first decide where the lens points, then place the target surface in front of that lens. Do not default to a right-side wall or distant wall just to show projection content. The lens direction, beam centerline, target surface, and projected image must align.
- Projection diversity rule: projection is not automatically an external wall or freestanding screen. Prefer projecting onto the object, model, tabletop, floor path, device surface, translucent layer, or rear-projection surface when that better expresses the gameplay. Use an external screen only when the content needs a separate readable display.
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
Cyan/blue only for local screen glow, projection, sensing, or digital feedback; do not make the whole image blue-dominant.
Use theme-appropriate restrained secondary colors when helpful, such as soft green for ecology, amber for history or memory, warm gray for mechanical layers, red-orange for warning or selection, black-white photo tone for archives, or pale violet for special zones.
Keep lots of empty space. Make the image a concept sketch, not a polished 3D render.

Chinese handwritten labels:
{4-6 short labels, such as 互动把手 / 感应区域 / 投影内容 / 信息层显现 / 滑动屏 / 儿童视角}

Hard constraints:
- One image explains one core gameplay idea.
- The main participant must perform the core action.
- Feedback must contain theme-specific information, not generic UI, empty projection, or meaningless glow.
- If the gameplay depends on selection, comparison, scanning, recognition, reconstruction, layered reveal, disassembly, or timeline progress, show enough visual evidence: 2-4 objects, states, layers, positions, or nodes. Do not use a single static object unless it visibly changes.
- Use only devices needed for this interaction; do not create a hardware inventory.
- Do not invent real landmarks, brands, logos, named buildings, specific locations, people, or vehicle brands unless the user specified them.
- Match carrier scale to the space; avoid large projection, oversized tables, or immersive setups in small or bright spaces unless justified.
- Prefer independent lightweight, furniture-like, or local installation forms. Avoid floor-to-ceiling rails, gantries, full-height columns, ceiling-to-floor frames, trusses, or architectural-scale structures unless functionally necessary.
- Device working distance must be believable. Projection, spotlight, scanning, sensing, and directional sound need a visible gap, path, or detection volume.
- Projection distance and direction must be believable. Show the source, beam direction, target surface, and landing content. Keep interaction-control arrows visually separate from projection beams.
- Projection target placement must follow the lens optical axis. The projected image cannot appear on a side wall, right wall, or rear wall unless the projector lens clearly points at that surface and the surface faces the beam.
- If a physically aligned projection target cannot be shown clearly, switch the feedback carrier to a built-in screen, transparent display, lightbox, model surface, or physical reveal instead of forcing wall projection.
- Avoid projection composition sameness. Do not make every projection concept into a left-side device plus a right-side freestanding screen. Choose the target medium and composition from the idea: object-mapped, tabletop/model-mapped, floor/path, translucent/rear projection, wall/screen, or embedded display.
- If the interaction object itself can carry the projected feedback, keep the feedback on that object or its immediate surface instead of adding a separate screen.
- Human reach must be believable. Do not stretch arms, place controls outside natural reach, or let children use adult-height controls without a reachable interface.
- Avoid blue overuse. Do not turn every screen, projection, label, glow, information layer, and feedback object into the same cyan/blue.
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

玩法证据不足：

```text
Regenerate the image with the same installation idea, but add enough visual evidence for the gameplay. If the interaction depends on selection, recognition, reconstruction, comparison, layered reveal, disassembly, or timeline progress, show 2-4 objects, states, layers, positions, or nodes. Do not rely on one static object and long labels.
```

投影不可实现：

```text
Regenerate the image so the projection is physically plausible. First lock the lens optical axis: source position, lens direction, target medium, target position, and throw distance. Place the projection target directly in front of the lens along the beam centerline; do not default to a right-side wall. Show source, beam direction, target surface, and landing content aligned. Separate interaction arrows from the projection beam.
```

投影构图同质化：

```text
Regenerate the image with a projection target medium that fits the concept instead of defaulting to a separate right-side screen. Consider object mapping, tabletop/model mapping, floor/path projection, translucent/rear projection, or feedback embedded into the device body. Keep the optical axis physically plausible, but vary the target surface and spatial composition.
```

蓝色过量：

```text
Regenerate the image with restrained color. Keep cyan/blue only for local screen, projection, sensing, or digital feedback. Use theme-appropriate secondary colors for content layers, such as soft green, amber, warm gray, red-orange, black-white photo tone, or pale violet. Do not make the whole image blue-dominant.
```

组件太多：

```text
Regenerate the image and remove irrelevant carrier components. Keep only the devices needed to explain this specific interaction. The image should feel like a clear exhibit interaction sketch, not a hardware inventory.
```
