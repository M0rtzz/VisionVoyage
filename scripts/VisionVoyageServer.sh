#!/usr/bin/env bash

REPO_ROOT_DIR=$(git rev-parse --show-toplevel)
UE4_TRUE_SCRIPT_NAME=$(readlink -f "$0")
UE4_PROJECT_ROOT="${REPO_ROOT_DIR}/server/VisionVoyage_Server"
gnome-terminal -- bash -c "while true; do wmctrl -r 'CarlaUE4' -T 'VisionVoyage Server'; code=\$?; if [ \$code -eq 0 ]; then break; fi; done"
chmod +x "${UE4_PROJECT_ROOT}/VisionVoyage-Server-UE4/Binaries/Linux/VisionVoyage-UE4-Shipping"
"${UE4_PROJECT_ROOT}/VisionVoyage-Server-UE4/Binaries/Linux/VisionVoyage-UE4-Shipping" CarlaUE4 "$@"
