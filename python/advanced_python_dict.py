import pandas as pd
import re
from collections import defaultdict
# first we'll create a data frame from our csv
data = pd.read_csv('faculty.csv')
df = pd.DataFrame(data)

df.rename(columns={'name': 'name', ' degree': 'degree',
 ' title': 'title', ' email': 'email'}, inplace=True)


# create a new column of last names to use a dict keys
df['lastName'] = [item[-1] for item in df['name'].str.strip().str.split(' ')]

# this removes 'of biostatistics'. I tried to do this with .split() and
# couldn't figure out how to get it back into a string from a list.
# probably not hard to do, this works for now, but I need to learn that
df['simpTitle']=[item[:-17] for item in df['title'].str.strip()]

# this merges degree, simpTitle, and email to a list for simplicity later on
df['merged']= df[['degree', 'simpTitle', 'email']].values.tolist()
# print(df['merged'])

# I played around with a bunch of metods to creat the dictionary, I kept running
# into issues surrounding the need for multiple values assigned to one key
# I found this method on stack exchange and it works well, first it groups
# the dataframe by lastname using groupby() and assigns that to g.  from there
# we create the variable facculty_dict and we pass the grouped version of our 
# merged column to which we apply a lambda function where we turn it into a list
# we then pass that to the pandas to_dict() function which gives us what we're looking for
g = df.groupby('lastName')
faculty_dict = g['merged'].apply(lambda s: s.tolist()).to_dict()
# print(faculty_dict)

# Finally we use a dictionary comprehension to return the first 3 key value pairs
# we apply sorted() to the keys so that we can index them, it throws a TypeError
# without that addition
firstThree = {k: faculty_dict[k] for k in sorted(faculty_dict.keys())[:3]}

# in order to re-design the keys as 'last name, first name' 
# first we'll create a column in our dataframe with that format
df['firstName'] = [item[0] for item in df['name'].str.strip().str.split(' ')]
# print(df['firstName'])

# combine the last name and first name columns, and make the result a tuple
df['firstLast'] = df[['firstName','lastName']].apply(tuple, axis=1)

# tuple is seperated into individual letters, creates the dict,  but the key is wrong
g2 = df.groupby('firstLast')
professor_dict = g2['merged'].apply(lambda s: s.tolist()).to_dict()
# print(sorted(df.lastName))

# sorts by first name
firstThreeProfessor = {k: professor_dict[k] for k in sorted(professor_dict.keys())[:5]}

# print(firstThreeProfessor)

# sorts by last name
firstThreeByLast = {k: professor_dict[k] for k in sorted(professor_dict.keys(),key=lambda x: x[1])[:3]}

# print(firstThreeByLast)
