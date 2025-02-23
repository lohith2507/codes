from demo1 import child1 
class child2(child1):
    def __init__(self, id, name, salary,age):
        super().__init__(id, name, salary)
        self.age = age 
    def ageDisplay(self):
        return self.age,self.name
y = child2(1,"Lohith",10000,23)
print(y.display())
print(y.empSalary())
print(y.ageDisplay())