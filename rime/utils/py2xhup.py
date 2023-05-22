YUMMU_1 = list('aoeiuv')
SHENGMU_1 = list('bpmfdtnlgkhjqxrzcsyw')
SHENGMU_MAP = {
        'zh': 'v',
        'ch': 'i',
        'sh': 'u',
        }
YUNMU_MAP = {
        'a': 'a',
        'o': 'o',
        'e': 'e',
        'i': 'i',
        'u': 'u',
        'v': 'v',
        'iu': 'q',
        'ei': 'w',
        'uan': 'r',
        'ue': 't',
        've': 't',
        'un': 'y',
        'uo': 'o',
        'ie': 'p',
        'ong': 's',
        'iong': 's',
        'ai': 'd',
        'en': 'f',
        'eng': 'g',
        'ang': 'h',
        'an': 'j',
        'uai': 'k',
        'ing': 'k',
        'uang': 'l',
        'iang': 'l',
        'ou': 'z',
        'ua': 'x',
        'ia': 'x',
        'ao': 'c',
        'ui': 'v',
        'in': 'b',
        'iao': 'n',
        'ian': 'm',
        }

def py2xhup(py: str):
    py = py.strip()
    if len(py) == 1:
        if py in ['a', 'o', 'e']:
            return py+py
        else:
            raise Exception(f'Invalid pinyin {py}')

    if py == 'er':
        return py

    if py[0] in SHENGMU_1:
        # 有声母
        if py[:2] in SHENGMU_MAP.keys():
            return SHENGMU_MAP[py[:2]] + YUNMU_MAP[py[2:]]
        else:
            return py[0] + YUNMU_MAP[py[1:]]

    else:
        return py[0] + YUNMU_MAP[py]
