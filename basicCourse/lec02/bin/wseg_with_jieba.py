#!/usr/bin/env python
# coding=utf-8
"""
2017  3,22 , huangpingping
Brief: word segment for sentences from stdin and print ret to stdout
"""

import sys
import jieba

def seg_pos_sen(sen):
    """
    args:
        sen: input sentence for word segment using jieba 
    return:
        a string of segmented words with spaces
    """
    ret = []
    if sen != None and len(sen.strip()) > 0:
        try:
            ret = jieba.cut(sen, cut_all = False)
            ret = [x.encode(gcs) for x in ret]
        except Exception as e:
            sys.stderr.write(str(e) + "\n")
    return " ".join(ret)


if __name__== "__main__":
    gcs = "gb18030"
    for line in sys.stdin:
        line = line.strip()
        segs = line.strip().split("\t")
        NF = len(segs)
        if NF >= 3:  
            out_str = ""
            for i in range(2, NF):
                out_str += "\t" + seg_pos_sen(segs[i])
            out_str = out_str.strip()
            print "%s\t%s\t%s" % (segs[0], segs[1], out_str)
