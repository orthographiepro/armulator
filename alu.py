from register import register as Register
from command import command as Command

class Alu:
    
    def __init__(self, register, command) -> None:
        self.register = register
        self.command = command
        self.target = get_reg


    def get_value(self, value):
        if (value[0] != "#"):
            raise Exception("")
        return int(value[0:])

    def alu_add(self, target, summand1, summand2):
        try:
            s2 = self.get_value(summand2)
        except:
            s2 = self.register.read(summand2)
        self.register.write(self.get_reg(target), self.register.read(self.get_reg(summand1))+s2)
    
    def alu_sub(self, target, sub1, sub2):
        try:
            s2 = self.get_value(sub2)
        except:
            s2 = self.register.read(sub2)
        self.register.write(self.get_reg(target), self.register.read(self.get_reg(sub1))-s2)

    def alu_mov(self, target, value):
        self.register.write(target, self.get_value(value))
    
if __name__ == "__main__":
    alu = Alu(Register(), Command())