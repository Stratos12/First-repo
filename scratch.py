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



a = Pc(3200,64,4096)
print(a.cpu,a.architecture,a.ram)
