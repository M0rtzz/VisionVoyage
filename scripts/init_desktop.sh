#!/bin/bash
#添加桌面文件
# base_path=$(dirname "$0")
base_path=$(pwd)
exec_name="main"
rm -rf "$HOME/Desktop/VisionVoyage.desktop" 2>/dev/null
echo "[Desktop Entry]
Name=VisionVoyage
Exec=$base_path/$exec_name.sh
Icon=$base_path/icon.ico
Terminal=true
Type=Application
StartupNotify=false" >"$HOME/Desktop/VisionVoyage.desktop"
chmod +x "$HOME/Desktop/VisionVoyage.desktop"
exit 0
