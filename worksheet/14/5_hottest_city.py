import csv

def hottest_city(csv_filename):
    ans = {}
    max_temp = float('-inf')
    hottest_cities = []
    
    with open(csv_filename) as file:
        reader = csv.reader(file)
        next(reader) # skip header
        for line in reader:
            city = line[0]
            temps = [float(temp) for temp in line[1:]]
            max_temp_city = max(temps)
            if max_temp_city > max_temp:
                max_temp = max_temp_city
                hottest_cities = [city]
            elif max_temp_city == max_temp:
                hottest_cities.append(city)
                
    return max_temp, sorted(hottest_cities)
