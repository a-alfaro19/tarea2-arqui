from Memory import Memory
from Stats import Stats


class CISC:
    """
    CISC architecture representation.
    """
    def __init__(self, mem: Memory):
        """ Create a new CISC instance. """
        self.mem = mem
        self.stats = Stats()

    def SUMMEM(self, src_pair_base: int, dest_addr: int):
        """ Add two vectors and stores the result in a given address.

        :param src_pair_base: Vectors address
        :param dest_addr: Destination address
        :return: None
        """
        a = self.mem.read(src_pair_base)
        b = self.mem.read(src_pair_base + 1)
        self.mem.write(dest_addr, a + b)
        self.stats.instructions += 1
        self.stats.cycles += 3 # SUMMEM = 3 cycles

    def run_program(self, interleaved_base: int, result_base: int, n: int):
        """ Runs the program using the CISC architecture."""
        for i in range(n):
            pair_base = interleaved_base + 2 * i
            self.SUMMEM(pair_base, result_base + i)