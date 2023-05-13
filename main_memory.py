class main_memory:
    def __init__(self) -> None:
        self.mem = {}

    def store(self, address, value:int):
        if address % 4 != 0:
            raise Exception(f"Address {address} is not a valid address!")
        if value >= 2^32:
            raise Exception(f"Value {value} too big for a 32-bit memory!")
        self.mem[address] = value

    def load(self, address):
        if address % 4 != 0:
            raise Exception(f"Address {address} is not a valid address!")
        if address not in self.mem:
            raise Exception(f"Address {address} not yet in memory!")
        return self.mem[address]