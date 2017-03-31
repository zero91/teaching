#!/usr/bin/env python
# coding=utf-8
"""
2016 Feb,25 , huangpingping
Brief:
"""

import os
import sys
import random
import string

def random_sample(N, f):
    results = []
    i = 0
    ran = random.Random(0)
    for v in f:
        v = v.strip()
        if len(v) == 0:
            continue
        r = ran.randint(0,i)
        if r < N:
            if i < N:
                results.insert(r, v)
            else:
                results[r] = v
        i += 1
    return results

if __name__ == "__main__":
    #usage python sample_Nline.py N [fileP]
    #if N is missing ,read from stdin
    N = string.atoi(sys.argv[1])
    fp = sys.stdin 
    if len(sys.argv) > 2:
        fp = open(sys.argv[2])
    if len(sys.argv) > 3:
        lab = sys.argv[3]
    rets = random_sample(N, fp)
    for line in rets:
        print line
