#!/bin/bish

payload=$1
target=$2
port=$3

# connect with target 
command adb connect $target:$port

adb $(./$payload) shell