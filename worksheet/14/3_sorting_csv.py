import csv

def sort_records(csv_filename, name_filename):
    with open(csv_filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        data = list(reader)
    header = data[0]
    sorted_data = sorted(data[1:])
    sorted_data.insert(0, header)
    with open(name_filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(sorted_data)