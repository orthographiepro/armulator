class register:
    def __init__(self) -> None:
        self.register = [None]*16
        self.cpsr = {
            "n" : False,
            "z" : False,
            "c" : False,
            "v" : False
        }

    def write(address, value):
        pass

    def read(address):
        pass

    def set_flag(flag, value):
        pass

    def get_flag(flag):
        pass
        
    
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