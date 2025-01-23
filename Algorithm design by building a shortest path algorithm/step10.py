#Modify your for loop to iterate over copper.values() instead of copper and look at the output.
copper = {
    'species': 'guinea pig',
    'age': 2
}
copper['food'] = 'hay'
copper['species'] = 'Cavia porcellus'

for i in copper.values():
    print(i)