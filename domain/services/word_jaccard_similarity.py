
def word_similarity(text1: str, text2: str) -> float:
    words1 = set(text1.split())
    words2 = set(text2.split())

    intersection = words1.intersection(words2)
    union = words1.union(words2)

    return len(intersection) / len(union)
