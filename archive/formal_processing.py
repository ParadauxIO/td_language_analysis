lines = []
processed = []
# Read in the data
with open('../data/archive/formal_raw', newline='', mode="r") as file:
    lines += file.readlines()

for line in lines:
    line = line.strip()
    # Remove single words/empty lines
    if len(line) < 5:
        continue
    processed += line.split(".")

with open('../data/social_utterances.txt', newline='', mode="w") as file:
    for line in processed:
        if len(line) < 5:
            continue
        new_line = line.strip() + "\n"
        file.write(new_line)

print(lines)