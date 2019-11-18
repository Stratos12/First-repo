class Pc:
#class attribute
    type = 'machine'

#Constructor
    def __init__(self,cpu,architecture,ram):
        self.cpu = cpu
        self.architecture = architecture
        self.ram = ram

#Instance method
    def description(self):
        return self.architecture, self.cpu, self.ram


list1 = []


def add_pc():
    print("entered function")
    cpu = input()
    architecture = input()
    ram = input()
    clazz = Pc(cpu, architecture, ram)
    list1.append(clazz)
    return


add_pc()