import re 
from command import *

class program_parser:
    def __init__(self, programm_file: str) -> None:
        self.filename = programm_file
        self.command_list = []
        self.label_lookup = {}


    def parse(self) -> tuple:
        file = open(self.filename)
        line_counter = 0
        
        for line in file:
            label_index = self.check_label(line)
            if label_index > 0:
                label = line[0:label_index]
                self.label_lookup[label] = line_counter
                continue

            comment_index = self.check_comment(line)
            if not comment_index == -1:
                line = line[comment_index : ]

            if line.isspace():
                continue    # unnecessary??

            argument_list = re.split(r'\w+', line)
            
            self.command_list.append(self.resolve_command(argument_list))

            line_counter += 1   
        
        file.close()
        return (self.command_list, self.label_lookup)


    def check_label(self, line: str) -> int:
        if ":" in line:
            return line.index(":")
        return 0
    
    def check_comment(self, line: str) -> int:
        if "//" in line:
            return line.index("")
        return -1
        # TODO: multiline comments

    def resolve_command(self, arguments) -> command:
        c = command()
        c.command_type = arguments[0]
        c.target = arguments[1]
        c.first = arguments[2]
        
        if len(arguments) > 3:
            c.second = arguments[1]