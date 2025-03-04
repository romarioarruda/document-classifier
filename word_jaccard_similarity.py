from app.common.sanitization import remove_diacritics
from app.common.pdf_text_extractor import extract_text_from_pdf


def word_similarity(text1: str, text2: str) -> float:
    words1 = set(text1.split())
    words2 = set(text2.split())

    intersection = words1.intersection(words2)  # values in both sets
    union = words1.union(words2) # both set values merge

    return len(intersection) / len(union)  # jaccard similarity


text1 = remove_diacritics(extract_text_from_pdf('./pdf_2.pdf')).lower()
text2 = remove_diacritics(extract_text_from_pdf('./pdf_1.pdf')).lower()

similarity = word_similarity(text1, text2)
print(f"Similarity: {similarity:.2f}")
