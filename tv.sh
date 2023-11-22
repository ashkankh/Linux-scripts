#!/bin/sh
xrandr --output DVI-I-0 --off --output DVI-I-1 --off --output HDMI-0 --primary --mode 3840x2160 --scale 0.6x0.6 --pos 1920x0  --rotate normal --output DP-0 --off --output DP-1 --off --output DP-2 --off --output DP-3 --off --output DP-4 --off --output DP-5 --off && hdmi_ID=$(wpctl status | grep "HDMI" | sed 's@^[^0-9]*\([0-9]\+\).*@\1@') &&
wpctl set-default $hdmi_ID
