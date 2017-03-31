#!/bin/bash

set -e
set -u
set -o pipefail

train_fp="../IT_train_1vsR"
test_fp="../IT_test_1vsR"
valid_fp="../IT_validate"

#one-vs-rest data: score around 0.96 without gridsearch
#one-vs-sameNPos data: score around 0.93 without gridsearch
python ./lr_biclass_with_sklearn.py "IT" $train_fp $test_fp "gb18030"
