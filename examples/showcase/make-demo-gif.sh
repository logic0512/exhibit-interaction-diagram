#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")"

ffmpeg -y \
  -loop 1 -t 2 -i yangtze-fishing-ban-table.png \
  -loop 1 -t 2 -i spiral-stair-city-timeline.png \
  -filter_complex "[0:v]scale=1280:720:force_original_aspect_ratio=decrease,pad=1280:720:(ow-iw)/2:(oh-ih)/2:white,setsar=1[v0];[1:v]scale=1280:720:force_original_aspect_ratio=decrease,pad=1280:720:(ow-iw)/2:(oh-ih)/2:white,setsar=1[v1];[v0][v1]concat=n=2:v=1:a=0,fps=12,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" \
  demo.gif

