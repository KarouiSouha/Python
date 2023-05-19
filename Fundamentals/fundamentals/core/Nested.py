#1.1
x = [ [5,2,3], [10,8,9] ] 
x[1][0]=15
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
#1.2
students[0]["last_name"] = "Bryant"
print(students)
#1.3
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
sports_directory["soccer"][0] = "Andres"
print(sports_directory)
#1.4
z = [ {'x': 10, 'y': 20} ]
z[0]["y"] = 30
print(z)
#2
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
"""
def iterateDictionary(some_list):
    for i in range(0,len(some_list)):
        for key in some_list[i].key():
            print(key,some_list[i][key])"""
#3
def iterateDictionary2(key_name, some_list):
    for arr in some_list:
        print(arr[key_name])
iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)
#4


def printInfo(some_dict):
       for key, value in some_dict.items():
        val_length = len(some_dict[key])
        key_name = key.upper()

        print(val_length, key_name)

        for i in range(val_length):
            print(some_dict[key][i])
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)

