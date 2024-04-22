import spacy
from math import sqrt

# Load the SpaCy model
nlp = spacy.load("en_core_web_sm")


def lexical_density(text):
    """
    Calculate lexical density of a text.
    Lexical density is the ratio of lexical items (nouns, verbs, adjectives, adverbs) to the total number of words.
    """
    doc = nlp(text)
    lexical_items = 0
    total_words = 0

    for token in doc:
        if not token.is_punct and not token.is_space:
            total_words += 1
            if token.pos_ in ['NOUN', 'VERB', 'ADJ', 'ADV']:
                lexical_items += 1

    return lexical_items / total_words if total_words > 0 else 0


def lexical_diversity(text):
    """
    Calculate lexical diversity of a text.
    Lexical diversity is the ratio of unique words to the total number of words.
    """
    doc = nlp(text)
    words = [token.text.lower() for token in doc if token.is_alpha]
    unique_words = set(words)
    total_words = len(words)

    return len(unique_words) / total_words if total_words > 0 else 0


def calculate_ttr(sentence):
    """Calculate the Type-Token Ratio (TTR) of a given sentence."""
    doc = nlp(sentence)
    tokens = [token.text for token in doc if not token.is_punct and not token.is_space]
    types = set(tokens)
    ttr = len(types) / len(tokens) if tokens else 0
    return ttr


def calculate_cttr(sentence):
    """Calculate the Corrected Type-Token Ratio (CTTR) of a given sentence."""
    doc = nlp(sentence)
    tokens = [token.text for token in doc if not token.is_punct and not token.is_space]
    types = set(tokens)
    cttr = (len(types) / sqrt(2 * len(tokens))) if tokens else 0
    return cttr


corpus = "dail"

with open(f"data/{corpus}_utterances.txt", mode="r") as file:
    sentences = file.readlines()

with open(f"data/presented/linguistic/cttr/{corpus}.txt", mode="w") as file:
    for sentence in sentences:
        file.write(str(calculate_cttr(sentence)) + "\n")

with open(f"data/presented/linguistic/ttr/{corpus}.txt", mode="w") as file:
    for sentence in sentences:
        file.write(str(calculate_ttr(sentence)) + "\n")

with open(f"data/presented/linguistic/density/{corpus}.txt", mode="w") as file:
    for sentence in sentences:
        file.write(str(lexical_density(sentence)) + "\n")

with open(f"data/presented/linguistic/diversity/{corpus}.txt", mode="w") as file:
    for sentence in sentences:
        file.write(str(lexical_diversity(sentence)) + "\n")

# print("\nLexical Density and Diversity:")
# for sentence in sentences:
#     print(f"Sentence: {sentence}")
#     print(f"Lexical Density: {lexical_density(sentence)}")
#     print(f"Lexical Diversity: {lexical_diversity(sentence)}")