#coding:utf-8


import os, os.path


for f in os.listdir(r'.'):
    if f.endswith(r'.py'): continue

    if r'java' in f:
        new_f = '2012-02'+f[7:]
        os.rename(f, new_f)
    elif r'python' in f:
        new_f = '2012-03'+f[7:]
        os.rename(f, new_f)
