# Examples

本目录放公开说明用的示例材料。

## showcase

`showcase/` 存放 README 中直接展示的稳定案例图。每张图都应满足：

- 输入 prompt 可追溯。
- 输出能看懂“人 - 触发 - 反馈 - 结果”。
- 反馈内容和主题相关，不是空屏或通用 UI。
- 不含私人路径、客户信息、真实未授权素材。

当前 showcase：

- `showcase/demo.gif`
- `showcase/yangtze-fishing-ban-table.png`
- `showcase/spiral-stair-city-timeline.png`

重新生成 GIF：

```bash
bash examples/showcase/make-demo-gif.sh
```

如果安装了 VHS，也可以录制终端版演示：

```bash
vhs examples/showcase/demo.tape
```

## finished examples

完成图校准层在 `../assets/examples/`：

- `../assets/examples/01-wall-screen-interaction.png`
- `../assets/examples/02-projection-mapping.png`
- `../assets/examples/03-lighting-feedback.png`
- `../assets/examples/04-sound-listening-point.png`
- `../assets/examples/05-floor-trigger-path.png`
- `../assets/examples/06-tangible-operation-table.png`
- `../assets/examples/07-mechanical-response.png`
- `../assets/examples/08-multi-person-collaboration.png`
- `../assets/examples/09-specimen-reconstruction.png`
- `../assets/examples/10-globe-surface-arc-projection.png`
- `../assets/examples/11-film-embedded-rear-projection.png`

使用规则见 `../references/example-gallery.md`。这些 examples 只做整体图面校准，不作为可复制模板。
