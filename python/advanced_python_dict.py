import pandas as pd
import re

faculty = pd.read_csv('faculty.csv')

#remove whitespace
faculty.columns = faculty.columns.str.strip()
faculty.degree = faculty.degree.str.strip()

####Q6.  Create a dictionary in the below format:
#### faculty_dict = { 'Ellenberg': [['Ph.D.', 'Professor', 'sellenbe@upenn.edu'], ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu']], 'Li': [['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'], ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'], ['Ph.D.', 'Professor', 'hongzhe@upenn.edu']]}
#### Print the first 3 key and value pairs of the dictionary:
    
faculty_mod = pd.DataFrame.copy(faculty)
faculty_mod.name = [re.sub('.* ', '', x) for x in faculty.name]  #extract just the last name
faculty_mod.title = [re.sub(' (of|is) .*', '', x) for x in faculty.title]  #extract just the title

def directory(x):
    d = dict()
    for i in range(0, len(x)):
        name = x.iloc[i][0]
        if name not in d:
            d[name] = [[x.iloc[i][1], x.iloc[i][2], x.iloc[i][3]]]
        else:
            new = [x.iloc[i][1], x.iloc[i][2], x.iloc[i][3]]
            d[name].append(new)
    return d

faculty_dict = directory(faculty_mod)

def print3(d):
    count = 0
    for key in d:
        print key, d[key]
        count += 1
        if count == 3:
            break
    return d

print3(faculty_dict)
    



####Q7.  The previous dictionary does not have the best design for keys.  Create a new dictionary with keys as:
#### professor_dict = {('Susan', 'Ellenberg'): ['Ph.D.', 'Professor', 'sellenbe@upenn.edu'], ('Jonas', 'Ellenberg'): ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu'], ('Yimei', 'Li'): ['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'], ('Mingyao','Li'): ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'], ('Hongzhe','Li'): ['Ph.D.', 'Professor', 'hongzhe@upenn.edu'] }
#### Print the first 3 key and value pairs of the dictionary:
    
faculty_mod.name = [tuple(x.rsplit(' ', 1)) for x in faculty.name]
professor_dict = directory(faculty_mod)
print3(professor_dict)




####Q8.  It looks like the current dictionary is printing by first name.  Print out the dictionary key value pairs based on alphabetical orders of the last name of the professors

keys_sorted = sorted(professor_dict.keys(), key = lambda t: t[-1])
for i in keys_sorted:
    print i, professor_dict[i]

