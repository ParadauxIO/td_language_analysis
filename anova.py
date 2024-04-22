from scipy import stats

corpusA = []
corpusB = []
corpusC = []

complexityType = "linguistic"
measure = "cttr"

with open(f"data/presented/{complexityType}/{measure}/dail.txt", mode="r") as file:
    lines = file.readlines()
    for line in lines:
        corpusA.append(float(line))

with open(f"data/presented/{complexityType}/{measure}/formal.txt", mode="r") as file:
    lines = file.readlines()
    for line in lines:
        corpusB.append(float(line))

with open(f"data/presented/{complexityType}/{measure}/dail.txt", mode="r") as file:
    lines = file.readlines()
    for line in lines:
        corpusC.append(float(line))

# Perform ANOVA
f_value, p_value = stats.f_oneway(corpusA, corpusB, corpusC)
print('F-value:', f_value)
print('P-value:', p_value)

with open(f"data/presented/{complexityType}/{measure}/anova.txt", mode="w") as file:
    file.write(f"F-value: {f_value}\nP-value: {p_value}\n")