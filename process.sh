#!/usr/bin/env sh
# This script converts the cifar data into leveldb format.
set -e

echo "Creating $DBTYPE..."
convert_cifar_data.bin data/ data/ lmdb

echo "Computing image mean..."
./build/tools/compute_image_mean -backend=lmdb data/cifar10_train_lmdb model/mean.binaryproto

echo "Done."