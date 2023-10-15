import unicodedata


def remove_accent(txt):
    norm_txt = unicodedata.normalize('NFD',txt)
    shaved = ''.join(c for c in norm_txt
                     if not unicodedata.combining(c))
    erg = unicodedata.normalize('NFC', shaved)
    return erg
