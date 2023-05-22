#!/usr/bin/env python3
# coding=utf-8

import pathlib
import os

DICT = {}
def add(k, v):
    if k not in DICT:
        DICT[k]= []
    DICT[k].append(v)

if __name__ == "__main__":
    workdir = pathlib.Path(__file__).parent.parent.resolve() 
    print(f'Working directory: {workdir}')

    # Read flypy dict
    with open(os.path.join(workdir, 'flypy.dict.yaml'), 'r', encoding='utf-8') as f:
        dict_flypy = f.readlines()
    len_dict = len(dict_flypy)
    i = 0
    # skip dict header
    for i in range(len_dict):
        if dict_flypy[i].startswith('...'):
            break
    i += 2

    for j in range(i, len_dict):
        try:
            parts = dict_flypy[j][:-1].split('\t')
            add(parts[1], f'dict:{j} : ' + parts[0])
        finally:
            pass

    def parse_txt(lines, source):
        for line in lines:
            line = line.strip()

            # ignore comments
            if line.startswith('#'):
                continue
            # ignore white lines
            if len(line) == 0:
                continue

            try:
                parts = line.split('\t')
                if parts[1].startswith('o'):
                    continue
                add(parts[1], f'{source}:{j} : ' + parts[0])
            finally:
                pass

    with open(os.path.join(workdir, 'flypy_sys.txt'), 'r', encoding='utf-8') as f:
        dict_sys = f.readlines()
    parse_txt(dict_sys, 'sys')

    with open(os.path.join(workdir, 'flypy_top.txt'), 'r', encoding='utf-8') as f:
        dict_top = f.readlines()
    parse_txt(dict_top, 'top')
    
    with open(os.path.join(workdir, 'flypy_user.txt'), 'r', encoding='utf-8') as f:
        dict_user = f.readlines()
    parse_txt(dict_user, 'user')

    for k, v in DICT.items():
        if len(v) > 2:
            print(f'{k} has {len(v)} items:', end='\n\t')
            print('\n\t'.join(v))



