class Employee:
    def __init__(self, id, name):
        self.id = id    
        self.name = name

    def get_info(self):
        return f"Id: {self.id}, Имя: {self.name}"
    

class Manager(Employee):
    def __init__(self, id, name, department, *args, **kwargs):
        super().__init__(id, name, *args, **kwargs)
        self.department = department

    def manage_project(self):
        return super().get_info() + f", управляет проектами в отделе: {self.department}"
    

class Technician(Employee):
    def __init__(self, id, name, specialization, *args, **kwargs):
        super().__init__(id, name, *args, **kwargs)
        self.specialization = specialization

    def perform_maintenance(self):
        return super().get_info() + f", выполняет техническое обслуживание для специализации: {self.specialization}"
    

class TechManager(Manager, Technician):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.team = []

    def add_employee(self, employee):
        self.team.append(employee)

    def get_team_info(self):
        list_team = "Команда: "
        for i in range (0, len(self.team)):
            list_team += self.team[i].get_info() + "; "
        return list_team

emp = Employee(0, "ddd") 
print(emp.get_info())      

man = Manager(1, "dd", "dfghj")
print(man.get_info())      
print(man.manage_project())      

tech = Technician(2, "dddd", "sdf")
print(tech.get_info())      
print(tech.perform_maintenance()) 

tm =  TechManager(3, "ddddd", "dfgddhj", "wddert")

tm.add_employee(man)
tm.add_employee(tech)

print(tm.get_info())
print(tm.manage_project())      
print(tm.perform_maintenance()) 
print(tm.get_team_info())
