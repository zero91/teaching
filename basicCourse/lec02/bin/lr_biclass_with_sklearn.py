#!/usr/bin/env python
# coding=utf-8
"""
2017  3,22 , huangpingping
Brief:
"""

import os
import sys

import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
import time


def _load_corpus_data_fromfile(fp, tar_cat, cs):
    """brief: load corpus data from sogou news segmented data
    args:
        fp, target file path for input data
        tar_cat, target category lable for positive data
        cs, charset for input file
    returns:
        corpus, list of segmentted text string
        labs, target labels
    """
    labs = []
    corpus = [] 
    try:
        for line in open(fp):
            segs = line.strip().decode(cs, "ignore").split("\t")
            lab = 0
            if segs[0] == tar_cat:
                lab = 1
            words = " ".join(segs[2:])
            corpus.append(words)
            labs.append(lab)
    except Exception as e:
        sys.stderr.write(str(e) + "\n")
    return corpus, labs

def train_and_test_with_lr(fp_train, fp_test, tar_cat, cs):

    corpus, labs = _load_corpus_data_fromfile(fp_train, tar_cat, cs)
    vectorizer = TfidfVectorizer(min_df = 5)
    #vectorizer = CountVectorizer(min_df = 5)
    X = vectorizer.fit_transform(corpus)
    Y = np.array(labs) 

    test_cor, test_labs = _load_corpus_data_fromfile(fp_test, tar_cat, cs) 
    test_X = vectorizer.transform(test_cor)
    test_Y = np.array(test_labs)

    sys.stderr.write(">> Begin train at :%s\n" % (time.ctime()))
    clf = LogisticRegression(penalty='l1', C=3.0)
    clf.fit(X, Y)
    sys.stderr.write(">> Finish train at :%s\n" % (time.ctime()))
    s = clf.score(X, Y)
    sys.stderr.write("   Training score : %.3f\n" % (s))

    pred_s = clf.score(test_X, test_Y)
    print(">> Test score : %.3f" % (pred_s))

if __name__ == "__main__":
    usage_str = "Usage: python %s target_label train_filepath \
            test_filepath filecharset" % (sys.argv[0])
    if len(sys.argv) < 4:
        print usage_str
        sys.exit(0)
    else:
        tar_cat = sys.argv[1]
        fp_train = sys.argv[2]
        fp_test = sys.argv[3]
        cs = sys.argv[4]
        train_and_test_with_lr(fp_train,fp_test, tar_cat, cs)
