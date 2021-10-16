from typing import List, Union

from common import NewNode, Index


class NodeText(NewNode):
    def __init__(self, parents_cont: List[NewNode], parents: List[Union[Index, int]]):
        super().__init__(parents_cont, parents)


class I(NodeText):
    def operar(self):
        outs = self.get_outs()  # tiene largo 2
        self.output = outs[1] + outs[0]
        self.is_ready = True
        return self.output


class D(NodeText):
    def operar(self):
        outs = self.get_outs()  # tiene largo 2
        self.output = outs[0] + outs[1]
        self.is_ready = True
        return self.output


class R(NodeText):
    def operar(self):
        outs = self.get_outs()  # tiene largo 1
        self.output = outs[0][::-1]  # lo doy vuelta
        self.is_ready = True
        return self.output


if __name__ == "__main__":
    x = []  # aquí creo la variable para poder referenciarla después
    # esto me permite no tener una variable por cada nodo sino una para el grafo completo
    x.extend([
        D(x, ["a", "n"]),
        I(x, [Index(0), "c"]),
        D(x, [Index(1), "t"]),
        D(x, [Index(2), "a"]),
        I(x, [Index(3), "n"]),
        I(x, [Index(4), "e"]),
        I(x, [Index(5), "_"]),
        D(x, [Index(6), "_"]),
        I(x, [Index(7), "e"]),
        D(x, [Index(8), "p"]),
        D(x, [Index(9), "r"]),
        D(x, [Index(10), "o"]),
        D(x, [Index(11), "g"]),
        D(x, [Index(12), "r"]),
        I(x, [Index(13), "m"]),
        D(x, [Index(14), "a"]),
        D(x, [Index(15), "m"]),
        D(x, [Index(16), "a"]),
        D(x, [Index(17), "r"]),
    ])
    print(x[-1].operar())
