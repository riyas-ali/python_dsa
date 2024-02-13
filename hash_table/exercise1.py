arr = []

with open("nyc_weather.csv", "r") as f:
    for line in f:
        tokens = line.split(',')
        try:
            temperature = int(tokens[1])
            arr.append(temperature)
        except:
            print("Invalid temperature. Ignore the row")

weather_dict = {}

with open("nyc_weather.csv", "r") as f:
    for line in f:
        tokens = line.split(',')
        day = tokens[0] 
        try:
            temperature = int(tokens[1].rstrip('\n'))
            weather_dict[day] = temperature
        except:
            print("Invalid temperature. Ignore the row")


average = sum(arr[0:7])/len(arr[0:7]) # average weather
maximum_temperature = max(arr[0:10])   # maximum temperature
jan_9_temperature = weather_dict['Jan 9']
jan_4_temperature = weather_dict['Jan 4']
print(average)
print(maximum_temperature)
print(jan_9_temperature)
print(jan_4_temperature)