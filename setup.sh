#!/bin/env bash

function _echoInfo() {
    echo -e "\e[1;33m[Info]: ${1}\e[0m"
}

function _echoError() {
    echo -e "\e[1;31m[Error]: ${1} \e[0m"
}

function _echoSuccess() {
    echo -e "\e[1;32m[Success]: ${1} \e[0m"
}

function onCtrlC() {
    _echoError "[Warning]: stopped by user."
    exit
}

function modifyUE4Path() {
    local file="./scripts/VisionVoyageServer.sh"
    local new_path

    # 提示用户输入新的路径
    echo "请输入您的 \`VisionVoyage_Server/文件夹的\` 路径（例如：/home/m0rtzz/Program_Files/VisionVoyage_Server）："
    read new_path

    new_path=$(realpath "${new_path}")

    # 使用 sed 进行替换，注意使用双引号以正确处理包含空格的路径
    sed -i "s|^UE4_PROJECT_ROOT=.*|UE4_PROJECT_ROOT=\"${new_path}\"|" "${file}" || {
        _echoError "替换失败，请手动修改文件 ${file} 中的路径"
        exit 1
    }

    _echoSuccess "已替换文件 '${file}' 的 \`UE4_PROJECT_ROOT\`为 '${new_path}'"
}

function modifyInterpreterPath() {
    local file_paths=("$@") # 将参数作为文件路径数组

    # env_path=$(python3 -c 'import os, sys; print(os.path.join(sys.prefix, "bin/python3"))')
    env_path=$(python3 -c 'import sys; print(sys.executable)')

    local replacement="#!${env_path}" # 替换为的新内容

    for file in "${file_paths[@]}"; do
        if [ -f "${file}" ]; then     # 检查文件是否存在
            if [ -s "${file}" ]; then # 检查文件是否非空
                # 临时保存第一行以外的内容
                old_first_line=$(head -n 1 "${file}")
                rest_of_file=$(tail -n +2 "${file}")

                # 将新的第一行内容和剩余内容重定向回原文件
                echo "${replacement}" >"${file}"
                echo "${rest_of_file}" >>"${file}"
                _echoSuccess "已替换文件 '${file}' 的SheBang为 '${replacement}'"
            else
                _echoError "文件 '${file}' 为空，跳过替换操作"
            fi
        else
            _echoError "文件 '${file}' 不存在"
        fi
    done
}

trap 'onCtrlC' INT

_echoInfo "执行此脚本前请先使用 \`conda activate your-env\` 切换到您的虚拟环境"
echo "脚本将完成以下两件事："
echo "    1. 修改\`scripts/VisionVoyage.sh中的路径\`"
echo "    2. 修改Python文件的SheBang中的解释器路径"

file_paths=(
    "./main.py"
    "./scripts/automatic_control.py"
    "./scripts/cubemap2fisheye.py"
    "./scripts/dataset_main.py"
    "./scripts/fisheye_utils.py"
    "./scripts/generate_traffic.py"
    "./scripts/get_fisheye_dataset.py"
    "./scripts/manual_control_gbuffer.py"
    "./scripts/manual_control.py"
    "./scripts/PT2fisheye.py"
    "./scripts/sem_seg_image.py"
    "./scripts/sem_seg_video.py"
    "./scripts/agents/navigation/basic_agent.py"
    "./scripts/agents/navigation/behavior_agent.py"
    "./scripts/agents/navigation/behavior_types.py"
    "./scripts/agents/navigation/constant_velocity_agent.py"
    "./scripts/agents/navigation/controller.py"
    "./scripts/agents/navigation/global_route_planner.py"
    "./scripts/agents/navigation/local_planner.py"
    "./scripts/agents/tools/misc.py"
)

modifyUE4Path
modifyInterpreterPath "${file_paths[@]}"
