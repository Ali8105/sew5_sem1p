import unicodedata


def remove_accent(txt):
    norm_txt = unicodedata.normalize('NFD',txt)
    
