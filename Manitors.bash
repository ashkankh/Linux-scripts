#! /bin/bash

# for config screen use this software => apt-get install arandr 
xrandr --output DVI-I-0 --off --output DVI-I-1 --mode 1920x1200 --pos 0x0 --rotate normal --output HDMI-0 --off --output DP-0 --off --output DP-1 --primary --mode 1920x1080 --pos 1920x120 --rotate normal --output DP-2 --off --output DP-3 --off --output DP-4 --off --output DP-5 --off

audio_ID=$(wpctl status | grep "Built-in Audio Analog Stereo" | sed 's@^[^0-9]*\([0-9]\+\).*@\1@') &&
wpctl set-default $audio_ID
