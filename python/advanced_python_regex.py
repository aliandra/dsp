import pandas as pd
import re


def read_data():
    """
    Reads in and cleans faculty.csv
    """
    df = pd.read_csv('faculty.csv')
    df.columns = df.columns.str.strip()
    df.degree = df.degree.str.replace('.', '')
    df.degree = df.degree.str.strip()
    return df


def freq_dict(x):
    """
    creates dictionary that maps key to frequency
    """
    d = dict()
    for item in x:
        d[item] = d.get(item, 0) + 1
    return d


def print_dict(d):
    for key, value in d.items():
        print key, '=', value


# Q1. Find how many different degrees there are, and their frequencies

faculty = read_data()

degrees = []
for item in faculty.degree:
    if item != '0':
        degrees.extend(item.split())

degree_dict = freq_dict(degrees)

print 'There are %d different degrees:' % len(degree_dict)
print_dict(degree_dict)


# Q2. Find how many different titles there are, and their frequencies:

titles = [re.sub(' (of|is) .*', '', x) for x in faculty.title]
titles_dict = freq_dict(titles)

print 'There are %d different titles: ' % len(titles_dict)
print_dict(titles_dict)


# Q3. Search for email addresses and put them in a list.

emails = list(faculty.email)

print '\n'.join(emails)


# Q4. Find how many different email domains there are

domains = [re.sub('.*@', '', x) for x in emails]
domains = set(domains)

print 'There are %d different domains:' % len(domains)
print '\n'.join(domains)
