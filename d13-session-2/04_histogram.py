import matplotlib.pyplot as plt
import numpy as np

# Histogram: distribution of 1000 random exam scores
np.random.seed(0)                                # reproducible randomness
scores = np.random.normal(loc=70, scale=10, size=1000)   # mean=70, std=10

plt.hist(scores, bins=20, color="skyblue", edgecolor="black")

plt.title("Distribution of Exam Scores")
plt.xlabel("Score")
plt.ylabel("Number of Students")

plt.show()
