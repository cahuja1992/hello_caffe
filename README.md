# Hello Caffe
Caffe Cifar10 classification example

## System Setup

```
sudo apt-get update && sudo apt-get install -y --no-install-recommends \
        build-essential \
        cmake \
        git \
        wget \
        libatlas-base-dev \
        libboost-all-dev \
        libgflags-dev \
        libgoogle-glog-dev \
        libhdf5-serial-dev \
        libleveldb-dev \
        liblmdb-dev \
        libopencv-dev \
        libprotobuf-dev \
        libsnappy-dev \
        protobuf-compiler \
        python-dev \
        python-numpy \
        python-pip \
        python-setuptools \
        python-scipy && \
    sudo rm -rf /var/lib/apt/lists/*
```

## 1 . Prebuilt
* Download prebuild and model from https://drive.google.com/drive/folders/1rvnPxWUjOkmlKIH0TQMTycN1V_LWOY_b?usp=sharing 
* cd opencv && source ./env.sh && cd ..
* cd prebuilt
* source ./env.sh
* ./bin/hello_caffe ../model/test.prototxt ../model/weights/cifar10_quick_iter_5000.caffemodel.h5 ../model/mean.binaryproto ../model/labels.txt <img_path>

## 2. Build own your own
* git clone @
* cd hello_caffe/caffe
* mkdir build && cd build
* cmake .. && make -j`nproc` && sudo make install
* ./install/bin/hello_caffe ../model/test.prototxt ../model/weights/cifar10_quick_iter_5000.caffemodel.h5 ../model/mean.binaryproto ../model/labels.txt <img_path>