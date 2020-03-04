from tuitse import THAU_JI, LIAN_JI, KHIN_SIANN_JI


def pau(jitin):
    kiatko = []
    su = []
    for ji in jitin:
        lui = ji[3]
        if lui == THAU_JI:
            sin = {
                'hanji': ji[0],
                'lomaji': ji[1],
                'si_tioh': ji[3]
            }
        su.append(sin)
    if su:
        kiatko.append(su)
    return kiatko
