#!/usr/bin/env sh
set -m
vault server -dev &
sleep 1 
vault auth enable -address=http://0.0.0.0:8200 kubernetes
#while sleep 60; do
#  ps aux |grep vault |grep -q -v grep
#  PROCESS_1_STATUS=$?
#  if [ $PROCESS_1_STATUS -ne 0]; then
#    echo "One of the processes has already exited."
#    exit 1
#  fi
#done
vault kv put secret/hello foo=world
fg %1
