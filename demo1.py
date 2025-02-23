from demo import sruthi 
class child1(sruthi):
    def __init__(self,id,name,salary):
        super().__init__(id,name)
        self.salary = salary 
    def empSalary(self):
        return self.salary,self.name
x=child1(1,"Lohith",10000)
