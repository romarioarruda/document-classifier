from collections import Counter
from utils.sanitization import remove_diacritics
from utils.pdf_text_extractor import extract_text_from_pdf

def frequency_similarity(text1: str, text2: str) -> float:
    freq1 = Counter(text1)
    freq2 = Counter(text2)

    intersection = sum((freq1 & freq2).values())  # values in both dictionary
    union = sum((freq1 | freq2).values())  # both dictionary values merge

    return intersection / union # jaccard similarity

# Example
text1 = remove_diacritics(extract_text_from_pdf('./pdf_2.pdf')).lower()
text2 = remove_diacritics(extract_text_from_pdf('./pdf_1.pdf')).lower()

similarity = frequency_similarity(text1, text2)
print(f"Similarity: {similarity:.2f}")
