#! /bin/bash

export PYTHONPATH=${PYTHONPATH}:../common-robotics
./line_follower.py -w 400 --bgr "[188, 86, 254]" --display
