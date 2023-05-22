#!/usr/bin/env python3
# coding=utf-8
#
import pathlib
import os

if __name__ == '__main__':
    workdir = pathlib.Path(__file__).parent.parent.resolve() 
    print(f'Working directory: {workdir}')
    with open(os.path.join(workdir, 'flypy.dict.yaml'), 'r', encoding='utf-8') as f:
        buffer_in = f.readlines()
    len_in = len(buffer_in)

    i = 0
    for i in range(len_in):
        if buffer_in[i].startswith('...'):
            break
    i += 2

    data = []
    with open(os.path.join(workdir, 'flypy.dict.yaml'), 'w', encoding='utf-8') as f:
        f.writelines(buffer_in[:i])
        data = buffer_in[i:]

        data = list(filter(lambda x: x.strip() != '', data))
        data = sorted(data, key=lambda x: x.split('\t')[1][:-1])
        f.writelines(data)

