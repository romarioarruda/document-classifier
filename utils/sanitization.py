from unicodedata import normalize


def remove_diacritics(txt: str, encode: str = 'ASCII'):
    return normalize('NFKD', txt).encode(encode, 'ignore').decode(encode)

