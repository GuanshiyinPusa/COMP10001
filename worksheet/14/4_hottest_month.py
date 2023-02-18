import csv

def max_city_temp(csv_filename, city):
    with open(csv_filename) as file:
        reader = csv.reader(file)
        header = next(reader)
        data = {row[0]: [float(x) for x in row[1:]] for row in reader}
    
    if city not in data:
        raise ValueError(f"City '{city}' not found in data")
    
    return max(data[city])
