class register:
    def __init__(self) -> None:
        self.register = [None]*16
        self.cpsr = {
            "n" : False,
            "z" : False,
            "c" : False,
            "v" : False
        }

    def write(self, address, value:int):
        if address not in address_dict:
            raise Exception(f"Adress {address} not in adress-dictionary!")
        if value >= 2**32:
            raise Exception(f"Value {value} too big for a 32-bit register!")
        self.register[address_dict[address]] = value

    def read(self, address):
        if address not in address_dict:
            raise Exception(f"Adress {address} not in adress-dictionary!")
        return self.register[address_dict[address]]

    def set_flag(self, flag, value:bool):
        if flag not in self.cpsr:
            raise Exception(f"Flag {flag} not a valid (or implemented) flag!")
        self.cpsr[flag] = value
        
        
    def get_flag(self, flag):
        if flag not in self.cpsr:
            raise Exception(f"Flag {flag} not a valid (or implemented) flag!")
        return self.cpsr[flag]
        
    
address_dict = {
    "r0" : 0,
    "r1" : 1,
    "r2" : 2,
    "r3" : 3,
    "r4" : 4,
    "r5" : 5,
    "r6" : 6,
    "r7" : 7,
    "r8" : 8,
    "r9" : 9,
    "r10" : 10,
    "r11" : 11,
    "r12" : 12,
    "r13" : 13,
    "r14" : 14,
    "r15" : 15,
    "sp" : 13,
    "lr" : 14,
    "pc" : 15
}