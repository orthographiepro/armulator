from program_parser import program_parser
from register import register
from alu import Alu

class cpu:
    def __init__(self, program_file: str) -> None:
        self.command_list = []
        self.label_lookup = {}
        self.parser = program_parser(program_file)
        self.reg = register()
        self.alu = Alu(self.reg, self)
        self.con = True

    def run(self):
        command_tuple = self.parser.parse()
        self.command_list = command_tuple[0]
        self.label_lookup = command_tuple[1]

        self.reg.write("pc",self.label_lookup["main"])

        while self.con:
            self.alu.command(self.command_list[self.reg.read("pc")])

    def branch(self, label:str):
        self.reg.write("pc",self.label_lookup[label])

    def end(self):
        self.con = False
