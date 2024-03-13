#!/bin/bash

# NOTE: fix BUG: ImportError: /lib/x86_64-linux-gnu/libgobject-2.0.so.0: undefined symbol: ffi_type_uint32, version LIBFFI_BASE_7.0
export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libffi.so.7

# 获取脚本所在路径
run_path=$(dirname "$0")
main_py_path="$run_path/main.py"
cd "$run_path"
"$main_py_path"
exit
