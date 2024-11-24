#!/usr/bin/env bash

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

function modifyInterpreterPath() {
    local file_paths=("$@") # 将参数作为文件路径数组

    # env_path=$(python3 -c 'import os, sys; print(os.path.join(sys.prefix, "bin/python3"))')
    env_path=$(python3 -c 'import sys; print(sys.executable)')

    local replacement="#!${env_path}"

    for file in "${file_paths[@]}"; do
        if [ -f "${file}" ]; then
            if [ -s "${file}" ]; then
                sed -i "1s|^#!.*|${replacement}|" "${file}"
                _echoSuccess "已替换文件 '${file}' 的 SheBang 为 '${replacement}'"
            else
                _echoError "文件 '${file}' 为空，跳过替换操作"
            fi
        else
            _echoError "文件 '${file}' 不存在"
        fi
    done
}

function confirmAndModify() {
    _echoInfo "执行此脚本前请先使用 \`conda activate your-env\` 切换到您的虚拟环境."
    echo "脚本将完成："
    echo "    修改Python文件的SheBang中的解释器路径。"
    echo "请确认是否继续（按回车键继续，按 \`Ctrl+C\` 取消）："
    read -r

    modifyInterpreterPath "${file_paths[@]}"
}

trap 'onCtrlC' INT

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

confirmAndModify
