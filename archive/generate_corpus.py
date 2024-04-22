import csv
import json

utterances = []

# Open the TSV file
with open('../data/archive/TD-GinoKenny-PeopleBeforeProfitSolidarity.tsv', newline='') as file:
    tsv_reader = csv.reader(file, delimiter='\t')

    # Iterate over each row in the TSV file
    for row in tsv_reader:
        # Each row is a list of strings
        # You can process the data here
        question = row[6]
        points = question.split(".")
        utterances = utterances + points


with open('../data/dail_utterances.txt', 'w') as file:
    for row in utterances:
        utterance = row.strip()
        if utterance == "speeches": # Ignore the header
            continue
        if len(utterance) < 5: # Ignore one-word utterances
            continue
        file.write(row.strip() + "\n")

