# 1. Update values in dictionaries and lists
x = [ [5,2,4], [10,8,9]]
students = [
    {"first_name": "Michael", "last_name": "Jordan"},
    {"first_name": "John", "last_name": "Rosales"},
]
sports_directory = {
    "basketball": ["Kobe", "Jordan", "James", "Curry"],
    "soccer": ["Messi", "Ronaldo", "Rooney"]
}
z = [ {"x": 10, "y": 20} ]
#   Change value of 10 in x to 15;
x[1][0] = 15
#   Change the last_name of the first student to "Bryant"
students[1]["last_name"] = "Bryant"
#   In sports_directory, change "Messi" to "Andres"
sports_directory["soccer"][0] = "Andres"
#   Change value 20 in z to 30
z[0]["y"] = 30

# 2. Iterate Through a List of Dictionaries
students = [
    {"first_name": "Michael", "last_name": "Jordan"},
    {"first_name": "John", "last_name": "Rosales"},
    {"first_name": "Mark", "last_name": "Guillen"},
    {"first_name": "KB", "last_name": "Tonel"}
]
def interateDictionary(li):
    for i in range(len(students)):
        print(f"first_name - {students[i]['first_name']}, last_name - {students[i]['last_name']}")

interateDictionary(students)
# Should output:
# first_name - Michael, last_name - Jordan
# etc

# Get Values From a List of Dictionaries
def iterateDictionary2(keyName,someList):
    for i in range(len(someList)):
        print(someList[i][keyName])
iterateDictionary2("first_name",students)
iterateDictionary2("last_name",students)

# 4. Iterate through a Dictionary with List Values
dojo = {
    "locations": ["San Jose", "Seattle", "Dallas", "Chicago", "Tulsa", "DC", "Burbank"],
    "instructors": ["Michael", "Amy", "Eduardo", "Josh", "Graham", "Patrick", "Minh", "Devon"]
}
def printInfo(someDict):
    dictList = list(someDict.items())
    # print(dictList)
    for i in range(len(someDict)):
        print(f"{len(dictList[i][1])} {dictList[i][0].upper()}")
        
        for j in range(len(dictList[i][1])):
            print(f"{dictList[i][1][j]}")
            
    return False
printInfo(dojo)