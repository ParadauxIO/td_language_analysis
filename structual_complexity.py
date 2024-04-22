import json
import spacy

# Load the English tokenizer, tagger, parser, NER, and word vectors
nlp = spacy.load("en_core_web_sm")

def average_dependency_length(sentence):
    """Calculate the average length of dependency arcs in a sentence."""
    doc = nlp(sentence)
    distances = []
    for token in doc:
        head = token.head
        # Calculate the distance between the current token and its head
        distance = abs(token.i - head.i)
        distances.append(distance)
    # Return the average dependency length
    return sum(distances) / len(distances) if distances else 0

def count_subordinate_clauses(sentence):
    """Count the number of subordinate clauses in a sentence."""
    doc = nlp(sentence)
    subordinate_clauses = 0
    for token in doc:
        # Check if the token is a subordinating conjunction or a relative pronoun
        if token.dep_ in ['mark', 'relcl']:
            subordinate_clauses += 1
    return subordinate_clauses



data = []
with open("data/formal_utterances.txt", mode="r") as file:
    lines = file.readlines()

for line in lines:
    data.append([average_dependency_length(line), count_subordinate_clauses(line)])

with open("data/archive/phrase_formal_structural_analysis_results.json", mode="w") as json_file:
    json.dump(data, json_file, indent=4)