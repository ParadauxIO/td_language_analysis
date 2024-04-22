import numpy as np
from scipy import stats

# Given list of numbers
numbers = []

with open("data/presented/linguistic/ttr/formal.txt", mode="r") as file:
    strings = file.readlines()
    for string in strings:
        numbers.append(float(string))

# Calculate basic statistics
mean = np.mean(numbers)
median = np.median(numbers)
std_dev = np.std(numbers)
variance = np.var(numbers)

# Confidence interval (95% confidence)
confidence_interval = stats.t.interval(0.95, len(numbers)-1, loc=mean, scale=stats.sem(numbers))

# Hypothesis testing: Test if the mean of the dataset is significantly different from 2.0
# Null hypothesis H0: mean = 2.0
# Alternative hypothesis H1: mean != 2.0
t_stat, p_value = stats.ttest_1samp(numbers, 2.0)

print(f"Mean: {round(mean, 3)}")
print(f"Median: {round(median, 3)}")
print(f"Standard Deviation: {round(std_dev, 3)}")
print(f"Variance: {round(variance, 3)}")
print(f"95% Confidence Interval: {round(confidence_interval[0], 3)} — {round(confidence_interval[1], 3)}")