# we will follw the same flow as we did in q4 of regex with pandas again
import pandas as pd
import re
import csv
# first we'll create a data frame from our csv
data = pd.read_csv('faculty.csv')
df = pd.DataFrame(data)
# again we fix the column names
df.rename(columns={'name': 'name', ' degree': 'degree',
 ' title': 'title', ' email': 'email'}, inplace=True)
# we creat the regular expression to find an email address
emailFind = '[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}'

# we use that regex with pandas's str.findall method, which finds the emails,
# and creates a list for each row. we use tolist() on that to encase those in 
# an overall list, and then we use a list comprehension to flatten our list of lists
emailList = [item for sublist in df.email.str.findall(emailFind, flags=re.IGNORECASE).tolist() for item in sublist]

# we define the filename for the csv we are going to write
myfile = open('emails.csv', 'w')
#now we define a writer object poiting to the file we just opened using 
# the csv module, we define '\n' as a delimiter to put each element on it's own line
wr = csv.writer(myfile, delimiter='\n')
# we call our writer with the writerow function and pass our emailList as
# the parameter which writes our list to our newly created csv 
wr.writerow(emailList)
# finally we close our file
myfile.close()
