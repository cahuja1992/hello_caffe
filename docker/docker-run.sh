#!/bin/bash

docker run --rm -it\
-p 8887:8888 \
-v `pwd`:/ws \
-d hello_caffe