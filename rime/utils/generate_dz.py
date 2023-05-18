#!/usr/bin/env python3
# encoding: utf-8

import pathlib
import os

DICT_HEADER_DZ = \
'''# Rime dict
# encoding: utf-8
# GENERATED BY generate_dz.py
# DO NOT EDIT

---
name: flypy_dz
version: "2023.05"
sort: original
...

'''

if __name__ == "__main__":
    workdir = pathlib.Path(__file__).parent.parent.resolve() 
    print(f'Working directory: {workdir}')
    with open(os.path.join(workdir, 'flypy.dict.yaml'), 'r', encoding='utf-8') as f:
        buffer_in = f.readlines()
    len_in = len(buffer_in)

    i = 0
    # skip dict header
    for i in range(len_in):
        if buffer_in[i].startswith('...'):
            break
    i += 2

    with open(os.path.join(workdir, 'flypy_dz.dict.yaml'), 'w', encoding='utf-8') as f:
        f.write(DICT_HEADER_DZ)

        for lineno in range(i, len_in):
            try:
                # remove '\n'
                line = buffer_in[lineno][:-1]
                parts = line.split('\t')
                word, keys = parts[0], parts[1]
                if len(word) != 1:
                    continue

                # process char
                len_key = len(keys)
                k = 1 << len_key
                for j in range(k-1):  # ignore full '`'
                    b = []
                    for u in range(len_key):
                        bitmask = 1 << u
                        if (j & bitmask) == 0:
                            b.append(keys[u])  
                        else:
                            b.append('`')

                    f.write(word)
                    f.write('\t')
                    f.write(''.join(b))
                    f.write('\n')
            except Exception:
                print(f'Error in line {lineno}: {buffer_in[lineno][:-1]}')

        f.write('\n')
            
