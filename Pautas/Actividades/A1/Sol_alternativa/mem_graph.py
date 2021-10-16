from typing import List, Union

from common import NewNode, Index


class NodeMem(NewNode):
    def __init__(self, parents_cont: list, parents: List[Union[Index, int]], mem):
        super().__init__(parents_cont, parents)
        self.mem = mem


class M(NodeMem):
    def operar(self):
        outs = self.get_outs()  # tiene largo 1
        if isinstance(outs[0], int):
            self.output = self.mem[outs[0] % len(self.mem)]
        elif isinstance(outs[0], str):
            # print(outs[0])
            self.output = outs[0] + self.mem.get(outs[0], "\b"*len(outs[0]) + "segfault core dumped.")
        self.is_ready = True
        return self.output


if __name__ == "__main__":
    x = []
    x.extend([
        M(x, [130], ["a"] * 130 + ["I"]),
        M(x, [Index(0)], {"I": "I"}),
        M(x, [Index(1)], {"II": "C"}),
        M(x, [Index(2)], {"IIC": "2"}),
        M(x, [Index(3)], {"IIC2": "1"}),
        M(x, [Index(4)], {"IIC21": "1"}),
        M(x, [Index(5)], {"IIC211": "5"}),
    ])
    print(x[-1].operar())