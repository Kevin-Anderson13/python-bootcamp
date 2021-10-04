# 1.  Update Values in Dictionaries and Lists

x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# Change the value 10 to 15 in x.
x[1][0] = 15
print(x)

# Change the lasn_name of the first student from Jordan to Bryant
students[0]['last_name'] = "Bryant"
print(students)

# In the sports_directory, change Messi to Andres
sports_directory['soccer'][0] = 'Andres'
print( sports_directory['soccer'])

# Change value 20 in z to 30
z[0]['y'] = 30
print(z)



# 2.  Iterate Through a List of Dictionaries
# Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops  #through each dictionary in the list and prints each key and the associated value. For example, given the #following list:

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterate_dictionary(list):
    for x in range(0, len(list)):
        # declare string for printed iteration
        iteration = ""
        # iterate through dictionary using for loop and key/value
        for key, value in list[x].items():
            # assign value using f - string
            iteration += f" {key} - {value},"
        # print iteration
        print(iteration)

# call function
iterate_dictionary(students)



# 3.  Get Values from a list of dictionaries
# Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key #name, the function prints the value stored in that key for each dictionary. For example, iterateDictionary2
#('first_name', students) should output:

def iterate_dictionary2(key_value,list):
    # iterate through dictionary
    for x in range(0, len(list)):
        for key, value in list[x].items():
            if key == key_value:
                # All we're printing is the value of the first or last name, so no need to create a whole iteration string.
                print(value)
#  Call functions
iterate_dictionary2('first_name',students)
iterate_dictionary2('last_name',students)



# 4. Iterate Through a dictionary with list values
# Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key along with the size of its list, and then prints the associated values within each key's list. For example:

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def print_info(dict):
    # iterate through each dojo item.. locations and instructors...
    for key, value in dict.items():
        # print f - string for how many items in each list...
        print(f"{len(value)} {key.upper()}")
        # loop through each item in each list...
        for x in range(0, len(value)):
            # print each item in each list
            print(value[x])
#  Call function
print_info(dojo)


