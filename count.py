import pandas as pd
from collections import defaultdict

# Load the exported Google Form CSV
df = pd.read_csv('votes.csv')

# Extract only the ranking columns
vote_cols = df.columns[2:]
df = df[vote_cols]

# Get how many ranks were available to give
n_ranks = len(vote_cols)

scores = defaultdict(int)

# Assuming first column is highest rank
for i, col in enumerate(df.columns):
    points = n_ranks - i
    for candidate in df[col]:
        scores[candidate] += points

# Sort candidates by score, descending
ranking = sorted(scores.items(), key=lambda i: i[1], reverse=True)
for cand, score in ranking:
    print(cand, score)