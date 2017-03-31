#!/bin/bash
# Brief: text preprocess functions for data prepare
 
set -e
set -u
set -o pipefail
#######################

# origianl data dir
readonly DATADIR=".."
# data with POSLAB are positive samples in biclass, others are negative samples
readonly POSLAB="IT"

test_fp="$DATADIR/test"
train_fp="$DATADIR/train"
valid_fp="$DATADIR/validate"
biclass_train_fp="$DATADIR/${POSLAB}_train_1vsR"
biclass_test_fp="$DATADIR/${POSLAB}_test_1vsR"
biclass_valid_fp="$DATADIR/${POSLAB}_validate_1vsR"

sample_bin="./sample_Nline_withseed.py"
wseg_bin="./wseg_with_jieba.py"
#######################

function gen_biclassData() {
    tmp_pos_fp="./_tmp_pos_fp"
    tmp_neg_fp="./_tmp_neg_fp"

    #step1, grep data with POSLAB from full data
    cat $1 | egrep "^${POSLAB}\t" > $tmp_pos_fp
    pos_sample_cnt=`wc -l < $tmp_pos_fp`

    #step2, grep data not with POSLAB from full data
    #the number of positive and negative samples are the same
    cat $1| egrep -v "^${POSLAB}\t" > $tmp_neg_fp

    #TODO(@huangpingping): text normalization preprocess step

    #step3, wordsegs for combined pos and neg data
    cat $tmp_pos_fp $tmp_neg_fp | python $wseg_bin > $2

    #step4, remove tmp files
    rm -rf $tmp_pos_fp
    rm -rf $tmp_neg_fp
}

#######################
gen_biclassData $train_fp $biclass_train_fp
#gen_biclassData $valid_fp $biclass_valid_fp
#gen_biclassData $test_fp $biclass_test_fp
