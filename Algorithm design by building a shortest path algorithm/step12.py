#Modify your for loop to take two loop variables and print both of them inside the loop body.

copper = {
    'species': 'guinea pig',
    'age': 2
}
copper['food'] = 'hay'
copper['species'] = 'Cavia porcellus'

for i,j in copper.items():
    print(i,j)