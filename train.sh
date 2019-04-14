#!/usr/bin/env sh
set -e

TOOLS=./build/tools

$TOOLS/caffe train --solver=model/solver.prototxt $@

# reduce learning rate by factor of 10 after 8 epochs
$TOOLS/caffe train --solver=model/solver_lr1.prototxt --snapshot=model/cifar10_quick_iter_4000.solverstate $@