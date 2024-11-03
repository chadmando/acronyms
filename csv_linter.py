import csv
import sys

def main(input_file):
    data = import_csv(input_file)
    linted_data = []
    
    for line in data:
        line['Acronym'] = (line['Acronym']).upper()
        line['Meaning'] = (line['Meaning']).title()
        line['Context'] = (line['Context']).title().strip()
        linted_data.append(line)

    linted_data = sorted(linted_data, key=lambda a: a['Acronym'])
    export_csv(input_file, linted_data)

def import_csv(csv_file):
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        data = []
        for row in reader:
            data.append(row)
    
        return data

def export_csv(csv_file, data):

    with open(csv_file, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        for row in data:
            writer.writerow(row)


if __name__=='__main__': 
    main(sys.argv[1])