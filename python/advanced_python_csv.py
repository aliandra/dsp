import csv
import pandas as pd

faculty = pd.read_csv('faculty.csv')
faculty.columns = faculty.columns.str.strip()
emails = faculty.email.tolist()
print emails


csvfile = "emails.csv"

with open(csvfile, "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    for email in emails:
        writer.writerow([email]) 
