import numpy as np
import string
import json
import csv

lines = []
analytics = {}
frequencies = {}

# Provide a table that indicates descriptive statistics (minimum, maximum, mean,
# median, standard deviation) for each of the measures as applied to the texts in each
# forum and language in the corpus.

# Read in the lines
with open('../data/dail_utterances.txt', newline='') as file:
    lines = file.readlines()
    # Strip new line characters + trailing/leading whitespace
    lines = [line.strip() for line in lines]

# Read in the frequency table
with open("../data/archive/unigram_freq.csv", newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        word = row['word']
        count = int(row['count'])
        frequencies[word] = count


# Calculate the minimum, maximum, mean, median and, standard deviation for each of the measures
def stats_of_array(arr):
    if len(arr) == 0:
        return "Array is empty"

    arr_min = np.min(arr)
    arr_max = np.max(arr)
    arr_mean = np.mean(arr)
    arr_median = np.median(arr)
    arr_std = np.std(arr)

    return {
        'Minimum': arr_min,
        'Maximum': arr_max,
        'Mean': arr_mean,
        'Median': arr_median,
        'Standard Deviation': arr_std
    }


# Calculate the lexical density of an array of sentences
def lexical_density(text):
    # Removing punctuation and converting text to lowercase
    text = text.translate(str.maketrans('', '', string.punctuation)).lower()
    words = text.split()
    unique_words = set(words)
    return len(unique_words) / len(words) if words else 0


def calculate_lexical_complexity(frequency_dict, sentences, rarity_threshold=10000):
    complexity_scores = []

    frequency_dict = {word.lower(): count for word, count in frequency_dict.items()}

    for sentence in sentences:
        rare_word_count = 0

        words = sentence.lower().split()

        for word in words:
            if word not in frequency_dict or frequency_dict[word] < rarity_threshold:
                rare_word_count += 1

        complexity_scores.append(rare_word_count)

    return complexity_scores


# Calculates the average length of words in an array of sentences
def average_word_length(sentences):
    averages = []
    for sentence in sentences:
        words = sentence.split()
        if len(words) == 0:  # Handle empty sentences to avoid division by zero
            averages.append(0)
            continue
        total_length = sum(len(word) for word in words)
        avg_length = total_length / len(words)
        averages.append(avg_length)
    return averages


analytics["lexical_density"] = stats_of_array([lexical_density(line) for line in lines])
analytics["avg_word_length"] = stats_of_array([average_word_length(lines)])
analytics["unlikely_word_frequency"] = stats_of_array(calculate_lexical_complexity(frequencies, lines))

with open('../data/archive/analytics.json', 'w') as file:
    for key, value in analytics.items():
        analytics[key] = {k: (v.item() if isinstance(v, np.generic) else v) for k, v in value.items()}
    json.dump(analytics, file, indent=4)

