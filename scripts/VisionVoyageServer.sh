#!/usr/bin/env bash

REPO_ROOT_DIR=$(git rev-parse --show-toplevel)
UE4_PROJECT_ROOT="${REPO_ROOT_DIR}/server/VisionVoyageServer"
gnome-terminal -- bash -c "while true; do wmctrl -r 'CarlaUE4' -T 'VisionVoyage Server'; code=\$?; if [ \$code -eq 0 ]; then break; fi; done"
chmod +x "${UE4_PROJECT_ROOT}/VisionVoyageServer-UE4/Binaries/Linux/VisionVoyageServer"
"${UE4_PROJECT_ROOT}/VisionVoyageServer-UE4/Binaries/Linux/VisionVoyageServer" CarlaUE4 "$@"
