from typing import List, Dict, Tuple


class Memory:
    """
    Memory model as a list of dictionaries.

    Structure:
        Memory = [
                {base_addr_a: val, base_addr + 1: val, ...},
                {base_addr_b: val, base_addr_b + 1: val, ...},
                {base_addr_result: val, base_addr_result + 1: val, ...},
            ]
    """
    def __init__(self):
        """ Initializes an empty memory. """
        self.cells:  List[Dict[int, int]] = []

    def _find_idx(self, addr: int) -> int:
        """ Finds the dictionary that contains the given address.

        :param addr: The address to search for.
        :return: The index of the dictionary that contains the given address.
        """
        for i, d in enumerate(self.cells):
            if addr in d:
                return i
        return -1

    def read(self, addr: int) -> int:
        """ Reads the value at 'addr' from the memory at 'addr'.

        :param addr: Dir to find.
        :return: Value at 'addr'.
        """
        i = self._find_idx(addr)
        if i == -1:
            raise KeyError(f"Address {addr} not initialized on memory")
        return self.cells[i][addr]

    def write(self, addr: int, value: int) -> None:
        """ Writes the value at 'addr' to the memory at 'addr'.

        :param addr: Address to write.
        :param value: Value to write.
        :return: None.
        """
        i = self._find_idx(addr)
        if i == -1:
            self.cells.append({addr: value})
        else:
            self.cells[i][addr] = value

    def dump_range(self, start: int, length: int) -> List[Tuple[int, int]]:
        """ Returns a list of tuples containing (addr, val) in a given range.

        :param start: The starting address to start at.
        :param length: The length of the range.
        :return: A list of tuples containing (addr, val) in a given range.
        """
        out = []
        for a in range(start, start + length):
            try:
                out.append((a, self.read(a)))
            except KeyError:
                out.append((a, None))
        return out