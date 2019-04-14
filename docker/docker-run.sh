#!/bin/bash

docker run --rm -it \
--security-opt seccomp=unconfined \
-e LOCAL_USER_ID=`id -u` \
--env-file .env \
-p 8887:8888 \
-v `pwd`/../:/ws hello_caffe /bin/bash