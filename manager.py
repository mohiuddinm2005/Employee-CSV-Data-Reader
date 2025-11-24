# Mustafa Mohiuddin
# 10/09/2025
"""The Person class below will run a .csv file and sort employee information
efficeintly and gracefully. It will self sufficeintly sort first naeme, lastname, age, salary, gender,
and reads the infromation.

The program can handle upper and lower input with the employee information, effectively sorting
it in grammatical fashion. The desired output results in a user choice to select an employee category
"""


class Person:
    def __init__(self, data):
        # Transform and validate input data
        self.first = self._transform_name(data[0])
        self.mid = self._transform_name(data[1])
        self.last = self._transform_name(data[2])
        self.gender = self._validate_gender(data[3])
        self.age = self._validate_age(data[4])
        self.salary = self._validate_salary(data[5])

    def _transform_name(self, name):
        return name.capitalize() if name else "NONE" # returns the name

    def _validate_gender(self, gender):
        if gender and gender.upper() in ['M', 'F']: # returns the gender
            return gender.upper()
        return "U"  # Default to unknown

    def _validate_age(self, age):
        try:
            age = int(age)            # returns the age of the employee
            return age if 20 <= age <= 70 else -1
        except ValueError:
            return -1

    def _validate_salary(self, salary):
        try:
            salary = int(salary)      # returns employee salary
            return salary if 20000 <= salary <= 100000 else -1
        except ValueError:
            return -1

    def personStr(self):
        return f"{self.first},{self.mid},{self.last},{self.gender},{self.age},{self.salary}"

    def __str__(self):
        return f"Name: {self.first} {self.mid} {self.last}, Gender: {self.gender}, Age: {self.age}, Salary: {self.salary}"

    # Getters and setters for the name, age, salary
    def setFName(self, fname): self.first = self._transform_name(fname)
    def getFName(self): return self.first

    def setMid(self, mid): self.mid = self._transform_name(mid)
    def getMid(self): return self.mid

    def setLName(self, lname): self.last = self._transform_name(lname)
    def getLName(self): return self.last

    def setGender(self, gender): self.gender = self._validate_gender(gender)
    def getGender(self): return self.gender

    def setAge(self, age): self.age = self._validate_age(age)
    def getAge(self): return self.age

    def setSalary(self, salary): self.salary = self._validate_salary(salary)
    def getSalary(self): return self.salary

def menu():
    print("\n," +  "=" * 40)
    print("Employee system")
    print("")
    print("1. Calculate minimum Salary: ")
    print("2. Calculate maximum salary: ")
    print("3. Count males and females: ")
    print("4. Calculate average salary: ")
    print("0. Exit")
    print("="* 40)
    choice = input("Enter your choice: ")
    return choice

def readData():
    import csv
    people = []
    with open('data.txt', mode='r') as file:
        csvFile = csv.reader(file)
        print("Reading data from disk...")
        count = 0
        for row in csvFile:
            person = Person(row)
            people.append(person)
            count += 1
        print(f"{count} records read from disk")
    return people

def calcMin(data):
    min_salary = min(person.salary for person in data if person.salary != -1)
    print(f"Minimum Salary: ${min_salary}")

def calcMax(data):
    max_salary = max(person.salary for person in data if person.salary != -1)
    print(f"Maximum Salary: ${max_salary}")
def totalCounts(data):
    males = sum(1 for person in data if person.gender == 'M')
    females = sum(1 for person in data if person.gender == 'F')
    print(f"Total Males: {males}, Total Females: {females}")

def averageSalary(data):
    valid_salaries = [person.salary for person in data if person.salary != -1]
    avg_salary = sum(valid_salaries) / len(valid_salaries) if valid_salaries else 0
    print(f"Average Salary: ${avg_salary:.2f}")


data = readData()

run = True
while run:
    match int(menu()):
        case 0:
            run = False
        case 1:
            calcMin(data)
        case 2:
            calcMax(data)
        case 3:
            totalCounts(data)
        case 4:
            averageSalary(data)
        case _:
            input("Invalid selection, hit enter to try again.")
def writeData(data):
    print("Writing data to file...")
    with open('data2.txt', mode='w') as file:
        for person in data:
            file.write(person.personStr() + "\n")
    print(f"{len(data)} records written to disk.")
