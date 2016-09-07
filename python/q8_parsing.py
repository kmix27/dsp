# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.


import pandas as pd

data = pd.read_csv('football.csv')

df = pd.DataFrame(data)

df['scoringDiff'] = abs(df.Goals - df['Goals Allowed'])

lowest = df.scoringDiff.idxmin(axis=1)

print(df.Team[lowest] + ', diffrence of:', df.scoringDiff[lowest])
