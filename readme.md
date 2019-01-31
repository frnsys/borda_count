Borda count voting, implemented in two ways:

- If the number of points per rank is based on the number of candidates in the election
- If the number of points per rank is based on the number of ranks voters could assign

These _do not_ necessarily lead to the same overall ranking.

This assumes a CSV file called `votes.csv` where the rankings start in the third column (column index 2).
