# we will follw the same flow as we did in q4 of regex with pandas again
import pandas as pd
# first we'll create a data frame from our csv
data = pd.read_csv('faculty.csv')
df = pd.DataFrame(data)

df.rename(columns={'name': 'name', ' degree': 'degree',
 ' title': 'title', ' email': 'email'}, inplace=True)

emailFind = '[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}'

# with that regex how about a sweet one liner to find all emails,
# and flatten them into a list. How deliciously pythonic. #thanksWesMcKinny
emailList = [item for sublist in df.email.str.findall(emailFind, flags=re.IGNORECASE).tolist() for item in sublist]

# now we will creat a clean data frame to write directly to csv
dfEmail = pd.DataFrame()
dfEmail = emailList
print(dfEmail)