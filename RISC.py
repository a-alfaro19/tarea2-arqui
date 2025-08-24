from Memory import Memory
from Stats import Stats


class RISC:
    """
    RISC architecture representation.
    """
    def __init__(self, mem: Memory):
        """ Create a new RISC instance. """
        self.mem = mem
        self.stats = Stats()

    def LOAD(self, addr: int) -> int:
        """ Load the given address from the given register.
        :param addr: The address to load.
        :return: Value of the given address.
        """
        val = self.mem.read(addr)
        self.stats.instructions += 1
        self.stats.cycles +=1
        return val

    def STORE(self, addr: int, value: int) -> None:
        """ Store the given value in the given register.
        :param addr: The address to store.
        :param value: Value to store.
        :return: None
        """
        self.mem.write(addr, value)
        self.stats.instructions += 1
        self.stats.cycles += 1

    def ADD(self, x: int, y: int) -> int:
        """ Adds two the given values.
        :param x: Value to add.
        :param y: Value to add.
        :return: Result of the addition.
        """
        self.stats.instructions += 1
        self.stats.cycles += 1
        return x + y

    def run_program(self, a_base: int, b_base: int, result_base: int, n: int):
        """ Runs the program using the RISC architecture. """
        for i in range(n):
            v_a = self.LOAD(a_base + i)
            v_b = self.LOAD(b_base + i)
            v_result = self.ADD(v_a, v_b)
            self.STORE(result_base + i, v_result)