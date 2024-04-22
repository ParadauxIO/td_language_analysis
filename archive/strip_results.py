import json

with open("../data/archive/phrase_dail_structural_analysis_results.json", mode="r") as file:
    lines = file.read()
    parsed_json = json.loads(lines)

with open("../data/presented/structual/num-clauses/dail.txt", mode="w") as file:
    for array in parsed_json:
        file.write(str(array[1]) + "\n")

