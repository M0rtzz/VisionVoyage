#!/bin/env bash

UE4_TRUE_SCRIPT_NAME=$(echo \"$0\" | xargs readlink -f)
# UE4_PROJECT_ROOT=$(dirname "$UE4_TRUE_SCRIPT_NAME")
UE4_PROJECT_ROOT="/home/m0rtzz/Program_Files/VisionVoyage_Server"
# gnome-terminal -- bash -c 'sleep 5s && wmctrl -r "CarlaUE4" -T "VisionVoyage Server"; exec bash'
# gnome-terminal -- bash -c 'while true; do wmctrl -r "CarlaUE4" -T "VisionVoyage Server"; done'
# gnome-terminal -- bash -c 'while true; do wmctrl -r "CarlaUE4" -T "VisionVoyage Server"; echo $?; done'
# gnome-terminal -- bash -c 'while true; do wmctrl -r "CarlaUE4" -T "VisionVoyage Server"; code=$?; echo $code; if [ $code -eq 0 ]; then break; fi; done'
# gnome-terminal -- bash -c 'while true; do wmctrl -r "CarlaUE4" -T "VisionVoyage Server"; code=$?; if [ $code -eq 0 ]; then break; fi; done; read -p "Press any key to exit..."'
gnome-terminal -- bash -c 'while true; do wmctrl -r "CarlaUE4" -T "VisionVoyage Server"; code=$?; if [ $code -eq 0 ]; then break; fi; done'
chmod +x "$UE4_PROJECT_ROOT/VisionVoyage-Server-UE4/Binaries/Linux/VisionVoyage-UE4-Shipping"
"$UE4_PROJECT_ROOT/VisionVoyage-Server-UE4/Binaries/Linux/VisionVoyage-UE4-Shipping" CarlaUE4 "$@" 

