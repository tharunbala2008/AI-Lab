import string
def analyze_text(text):
    cleaned = text.translate(str.maketrans("", "", string.punctuation)).lower()
    words = cleaned.split()
    return {"total_words": len(words), "unique_words": len(set(words))}
