import re

def calculate_mls(file_path):
    total_words = 0
    sentence_count = 0

    with open(file_path, 'r') as file:
        # Split the text into sentences using a simple regular expression that looks for punctuation marks followed by white spaces
        sentences = file.readlines()
        sentence_count = len(sentences)

        for sentence in sentences:
            # Split each sentence into words and count them
            words = sentence.split()
            total_words += len(words)

    if sentence_count > 0:
        mls = total_words / sentence_count
    else:
        mls = 0

    return mls


# Example usage
file_path = '../data/formal_utterances.txt'
mean_length_of_sentence = calculate_mls(file_path)
print("Mean Length of Sentence (MLS):", mean_length_of_sentence)