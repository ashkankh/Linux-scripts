#! /bin/bash

xrandr --output DP-1 --off  --output HDMI-0 --mode 1920x1080 &&
hdmi_ID=$(wpctl status | grep "HDMI" | sed 's@^[^0-9]*\([0-9]\+\).*@\1@') &&
wpctl set-default $hdmi_ID
