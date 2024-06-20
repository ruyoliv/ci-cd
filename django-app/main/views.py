from django.shortcuts import render
# import json to load json data to python dictionary
import json
# urllib.request to make a request to api
import urllib.request




# Sample JSON data
json_data = '{"name": "Alice", "age": 30, "city": "Los Angeles"}'

# Parse the JSON data
data = json.loads(json_data)

# Specify the field key to update
field_key = 'age'

# Update the specified field value
if field_key in data:
    data[field_key] += 1

# Convert the modified data back to JSON
modified_json = json.dumps(data)

print('Before Modifying:', json_data)
print('After Modifying:', modified_json)



def ajustes(lista):
    lista['main']['temp']  = lista['main']['temp'] = int(lista['main']['temp'] ) - int(273.1) 
    lista['main']['pressure']  = lista['main']['pressure'] = int(lista['main']['pressure'] ) - 273.1 
    return lista


def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        ''' api key might be expired use your own api_key
            place api_key in place of appid="your api_key here "  '''

        # source contain json data from api

        source = urllib.request.urlopen(
            'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=48a90ac42caa09f90dcaeee4096b9e53').read()

        # converting json data to dictionary

        list_of_data = json.loads(source)

        lista = list_of_data
        list_of_data = ajustes(list_of_data)

        # data for variable list_of_data
        data = {
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + ' ' + str(list_of_data['coord']['lat']),
            "temp": str(list_of_data['main']['temp']) + ' C', #k',
            "pressure": str(list_of_data['main']['pressure']),
            "name": str(list_of_data['name']),
            "humidity": str(list_of_data['main']['humidity']),
            #"humidity": str(list_of_data),
        }
        print(data)
    else:
        data={}
    return render(request, "main/index.html",data)





# def index(request):
#     if request.method == 'POST':
#         city = request.POST['city']
#         ''' api key might be expired use your own api_key
#             place api_key in place of appid="your api_key here "  '''

#         # source contain json data from api

#         source = urllib.request.urlopen(
#             'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=48a90ac42caa09f90dcaeee4096b9e53').read()

#         # converting json data to dictionary

#         list_of_data = json.loads(source)

#         # data for variable list_of_data
#         data = {
#             "country_code": str(list_of_data['sys']['country']),
#             "coordinate": str(list_of_data['coord']['lon']) + ' ' + str(list_of_data['coord']['lat']),
#             "temp": str(list_of_data['main']['temp']) + 'k',
#             "pressure": str(list_of_data['main']['pressure']),
#             "humidity": str(list_of_data['main']['humidity']),
#         }
#         print(data)
#     else:
#         data={}
#     return render(request, "main/index.html",data)
