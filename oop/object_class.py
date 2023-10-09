class Employee:
    def __init__(self, first_name, last_name, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender

    def email(self):
        return (f"{self.first_name}.{self.last_name}@company.com").lower()



emp_1 = Employee("Oluleke","Adetoroye", 29, "male")

print(emp_1.email())

