class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def get_info(self):
        return self.name,self.id
class Manager(Employee):
    def __init__(self, name, id,department, *args):
        super().__init__(name, id,*args)
        self.department=department
    def manage_project(self):
        return (f'{self.name} управляет проектом')
    def get_info(self):
        info=super().get_info()
        return (info,self.department)
class Technican(Employee):
    def __init__(self, name, id, specialization,*args):
        super().__init__(name, id,*args)
        self.specialization=specialization
    def perform_maintenance(self):
       print(f'{self.name} выполняет техническое обслуживание')
    def get_info(self):
        info=super().get_info()
        return (info,self.specialization)
class TechManager(Manager,Technican):
    def __init__(self, name, id, department,specialization,employees=[]):
        super().__init__(name, id, department,specialization)
        self.employees=employees
    def add_employee(self,new_employee):
        self.employees.append(new_employee)
    def get_info(self):
        return (self.name, self.id, self.department,self.specialization)
    def team(self):
        for i in self.employees:
            print(i.get_info())
em=TechManager('Петр',1235,'IT','главный работяга')
em1=Manager('Джо', 1204,'IT')
em.add_employee(em1)
print(em.get_info())
em.team()