#!/bin/bash
# 获取脚本所在路径
run_path=$(dirname "$0")
main_py_path="$run_path/main.py"
cd "$run_path"
"$main_py_path"
exit
