list_of_data = {'temp': "500", "humidity":  '30', "city": "Los Angeles"}

# lista = list_of_data
# print( lista)
# lista['temp'] = str( float(lista['temp']) - 273.1 )
# 	# if key == 'pressure': 
# 	# 	lista[key] = str( float(lista[key]) - 300 )
# 	# if key == 'humidity': 
# 	# 	lista[key] = str( float(lista[key]) - 20 )
# list_of_data = lista
# print (" LISTA!!!" ) 
# print(list_of_data)




lista = list_of_data
for key in lista:
	if key == "temp": 
		lista[key] = str( float(lista[key]) - 273.1 )
	if key == 'pressure': 
		lista[key] = str( float(lista[key]) - 300 )
	if key == 'humidity': 
		lista[key] = str( float(lista[key]) - 20 )
list_of_data = lista
print (" LISTA!!!" ) 
print(list_of_data)