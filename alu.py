from register import register as Register
from command import command as Command
import re

class Alu:
    
    def __init__(self, register, cpu) -> None:
        self.register = register
        self.cpu = cpu

    def command(self, command):
        t = command.command_type
        suf = self.suffix(command)
        # TODO Command with regex
        # if (command.f)
        # elif t == "b":
        #     self.cpu.branch(command.first)
        # elif t == "add":
        #     self.alu_add(command.target, command.first, command.second)
        # elif t == "sub":
        #     self.alu_sub(command.target, command.first, command.second)
        # elif t == "mov":
        #     self.alu_mov(command.target, command.first)
        # elif t == "cmp":
        #     self.alu_cmp(command.first)


    def suffix(self, command):
        m = re.match(r'^\w+((eq|ne|cs|hs|cc|lo|mi|pl|vs|vc|hi|ls|ge|lt|gt|le)?(s)?)?$', command[-3:])
        m.group(1), 
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

    def alu_cmp(self, cpr1, cpr2):
        s1 = self.register.read(cpr1)
        try:
            s2 = self.get_value(cpr2)
        except:
            s2 = self.register.read(cpr2)
        if (s1 == s2):
            self.register.set_flag("z", True)
        # TODO flags missing
