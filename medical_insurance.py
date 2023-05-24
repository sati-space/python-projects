import csv

with open('insurance.csv') as insurance_doc:
    insurance_contents = insurance_doc.read()

print(insurance_contents)