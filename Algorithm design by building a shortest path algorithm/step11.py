#Modify your for loop to iterate over copper.items() instead of copper.values().

copper = {
    'species': 'guinea pig',
    'age': 2
}
copper['food'] = 'hay'
copper['species'] = 'Cavia porcellus'

for i in copper.items():
    print(i)