# we're going to use pandas here because it's awesome
import pandas as pd
import re
# first we'll create a data frame from our csv
data = pd.read_csv('faculty.csv')
df = pd.DataFrame(data)
# we'll take a look to see what we have

# print(df)
# print(df.columns)

# some of the names begin with white space, I know I'll forget that 
# down the line and mess up,  so we'll change that

df.rename(columns={'name': 'name', ' degree': 'degree',
 ' title': 'title', ' email': 'email'}, inplace=True)

# next we will do a quick value count on degree and title to see what we get
# print(df['degree'].value_counts())
# print(df['title'].value_counts())

# it seems many professors have multiple degrees, good for them!
# the naming conventions are inconsistent, regex will certainly help us here,
# lets build a list of degrees and the expressions to find them
# we will use the pandas str.count method to pass our regex's,
# and we will run a sum on the reult

RegexListDegree = [
['PhD' , '(Ph)+(\.*D\.*)'],
['ScD' , '(Sc)+(\.*D\.*)'],
['MS' , '(MS)+'],
['MD' , '(MD)+'],
['MPH' , '(MPH)+'],
['BSEd' , '(B\.+S\.+Ed.)+'],
['JD' , '(J\.*D\.*)'],
['noDegree', '(0)']
]

# calling this with the above regexes will iterate through df.degree
# and print a list of degrees and their frequency
def printCountDegree(regexes):
	for item in regexes:
		print(item[0], ':', df.degree.str.count(item[1]).sum())

# create seprate data frame dfDegrees for the degree counts just in case
dfDegrees = pd.DataFrame(columns = ['degree', 'count'])
dfDegrees['degree'] = [item[0] for item in RegexListDegree]
dfDegrees['count'] = [df.degree.str.count(item[1]).sum() for item in RegexListDegree]

# now we create regexs for the titles we saw in df.title.value_counts()
RegexListTitle = [
['Professor', '(\AProfessor)'],
['Associate', '(Associate Professor)'],
['Assistant', '(Assistant Professor)']]

# calling this with the above regexs will iterate through df.title
# and print a list of titles and their frequencies 
def printCountTitle(regexes):
	for item in regexes:
		print(item[0], ':', df.title.str.count(item[1]).sum())


# create seprate data frame dfTitles for the title counts 
dfTitles = pd.DataFrame(columns = ['title', 'count'])
dfTitles['title']= [item[0] for item in RegexListTitle]
dfTitles['count'] = [df.title.str.count(item[1]).sum() for item in RegexListTitle]

# now we're interested in finding emails, so we create a regex for that
emailFind = '[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}'

# with that regex how about a sweet one liner to find all emails,
# and flatten them into a list. How deliciously pythonic. #thanksWesMcKinny
emailList = [item for sublist in df.email.str.findall(emailFind, flags=re.IGNORECASE).tolist() for item in sublist]

# print(emailList)

# now we write a regex to capture just the domains
domainFind = '@[A-Z0-9.-]+\.[A-Z]{2,}'
# probably isn't as pythonic as it could be, but it's late.
# first we roll through with pd.str.findall to get a list of everyone's email domain
domainLst = [item for sublist in df.email.str.findall(domainFind, flags=re.IGNORECASE).tolist()for item in sublist]
# next we use dictionary comprehension to get a count of each unique domain
countDict = {x:domainLst.count(x) for x in domainLst}
# the question asked for a list, so we will call items() to return one from our dict 
countList = list(countDict.items())
# and we've got it, print to console and call it a day 

# print(countList)
