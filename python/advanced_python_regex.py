import pandas as pd
import re

faculty = pd.read_csv('faculty.csv')

#remove whitespace and periods
faculty.columns = faculty.columns.str.strip()
faculty.degree = faculty.degree.str.replace('.', '')
faculty.degree = faculty.degree.str.strip()


####Q1. Find how many different degrees there are, and their frequencies

#create list containing all degrees
degrees = []
for item in faculty.degree.tolist():
    if item != '0':
        degrees.extend(item.split())

# function to create dictionary where value is the frequency of the key
def freq_dict(x):
    d = dict()
    for item in x:
        if item not in d:
            d[item] = 1
        else:
            d[item] += 1
    return d

degree_dict = freq_dict(degrees) # create dictionary of degrees and frequency

print 'There are ' + str(len(degree_dict)) + ' different degrees: '
print degree_dict




####Q2. Find how many different titles there are, and their frequencies:
    
titles = faculty.title.tolist()  #create list containing titles
titles = [re.sub(' (of|is) .*', '', x) for x in titles]  #extract just the title
titles_dict = freq_dict(titles)  #create dictionary of titles and frequency

print 'There are ' + str(len(titles_dict)) + ' different titles: '
print titles_dict



####Q3. Search for email addresses and put them in a list.
emails = faculty.email.tolist()
print emails



####Q4. Find how many different email domains there are
domains = [re.sub('.*@', '', x) for x in emails]
domains = set(domains)
           
print 'There are ' + str(len(domains)) + ' different domains: '
print domains