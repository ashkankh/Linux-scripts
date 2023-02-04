#! /bin/bash

xrandr --output HDMI-0 --off  --output DP-1 --mode 1920x1080 --output DVI-I-1 --mode 1920X1200
audio_ID=$(wpctl status | grep "Built-in Audio Analog Stereo" | sed 's@^[^0-9]*\([0-9]\+\).*@\1@') &&
wpctl set-default $audio_ID
