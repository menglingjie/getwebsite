# -*- coding: utf-8 -*-
__author__ = 'meng'
import os
import re

def modifyFile(path, depth):
    print("Transform %s."%path)
    if depth == 0 :
        dst_str = 'href="./'
    else:
        dst_str = 'href="%s' % ("../"*depth)

    with open(path,'r') as f:
        lines = f.readlines()
    with open(path, 'w+') as f:
        for line in lines:
            tmp = re.sub('href="/',dst_str,line)
            # tmp = re.sub('href="http://'+path.split('/')[0],dst_str,tmp)
            f.writelines(tmp)


def changeRef(rootDir, depth=0):
    for dir in os.listdir(rootDir):
        path = os.path.join(rootDir, dir)
        if os.path.isdir(path):
            changeRef(path, depth+1)
        else :
            modifyFile(path, depth)

def trans(args):
    changeRef(args[0])
#changeRef("www.runoob.com")