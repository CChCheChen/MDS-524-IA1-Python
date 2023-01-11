from collections import Counter
from string import punctuation


def load_text(input_file):
    """_summary_

    Args:
        input_file (_type_): _description_

    Returns:
        _type_: _description_
    """
    with open(input_file, "r") as file:
        text = file.read()
    return text
    
def clean_text(text):
    """Lowercase and remove punctuation from a string."""
    text = text.lower()
    for p in punctuation:
        text = text.replace(p, "")
    return text
    
def count_words(input_file):
    """Count unique words in a string."""
    text = load_text(input_file)
    text = clean_text(text)
    words = text.split()
    return Counter(words)