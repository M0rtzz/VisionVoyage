#!/bin/env bash

LOCKFILE=/tmp/VisionVoyage.lock

# 尝试获取锁，如果获取失败则退出
exec 200>"${LOCKFILE}"
flock -n 200 || {
    echo "已经有一个实例在运行了！"
    exit 1
}

# NOTE: fix BUG: ImportError: /lib/x86_64-linux-gnu/libgobject-2.0.so.0: undefined symbol: ffi_type_uint32, version LIBFFI_BASE_7.0
export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libffi.so.7

# NOTE: fix BUG: qt.qpa.input.events: scroll event from unregistered device 22
export QT_LOGGING_RULES="qt.qpa.input.events=false"

# 获取脚本所在路径
run_path=$(dirname "$0")
main_py_path="${run_path}/main.py"
cd "${run_path}" || exit
"${main_py_path}"
exit
