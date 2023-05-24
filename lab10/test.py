import csv

zipdir = {}
with open('data/historia_przejazdow_2021-09.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip file header

        for row in reader:
            rental_id: int = int(row[0])
            try:
                zipdir[rental_id] += 1
            except:
                zipdir[rental_id] = 1

outlines = []
for k, v in zipdir.items():
    if v > 1:
        outlines.append(k)
        
print(outlines)
