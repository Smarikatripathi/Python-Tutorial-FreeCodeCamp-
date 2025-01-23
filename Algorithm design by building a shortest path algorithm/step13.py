#Just before your for loop, use the del keyword to delete the 'age' key and its value from copper.

copper = {
    'species': 'guinea pig',
    'age': 2
}
copper['food'] = 'hay'
copper['species'] = 'Cavia porcellus'
del copper['age']
for i, j in copper.items():
    print(i, j)