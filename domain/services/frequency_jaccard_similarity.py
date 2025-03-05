from collections import Counter

def frequency_similarity(text1: str, text2: str) -> float:
    freq1 = Counter(text1)
    freq2 = Counter(text2)

    intersection = sum((freq1 & freq2).values())
    union = sum((freq1 | freq2).values())

    return intersection / union
