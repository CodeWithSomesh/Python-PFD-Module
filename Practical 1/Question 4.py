# Define a class Employee with the following:
# ▪ 3 private attributes: name, age and salary.
# ▪ A constructor that initializes the name, age and salary from the
# parameter list.
# ▪ A method called increment that accept an increment amount as
# parameter and increase the salary of the employee.
# ▪ A method named higherThan that compares one employee’s salary with
# another employee’s salary. The method shall return true if the salary is
# higher, otherwise it shall return false.


# Write a main program to create 2 Employees objects. Give increment of
# RM500 to the first employee. Determine is first employee’s salary is higher
# than second employee’s salary by calling the higherThan method.

class Employee:
    # Constructor
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def increment(self, incrementAmount):
        self.salary += incrementAmount
        return self.salary

    def higherThan(self, employer2salary):
        if self.salary > employer2salary:
            return True
        else:
            return False

if __name__ == "__main__":

    employee1 = Employee('Sara', 22, 5000)
    employee2 = Employee('Dora', 42, 5000)

    incrementAmount = int(input("Enter Increment Amount: RM"))
    employee1.increment(incrementAmount)
    print(f"{employee1.name} received RM{incrementAmount} as increment, and her total salary now is RM{employee1.salary}")
    print()
    higherThan = employee1.higherThan(employee2.salary)
    if higherThan:
        print("True")
    else:
        print("False")


