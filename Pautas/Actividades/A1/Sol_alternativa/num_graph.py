from typing import List, Union
from functools import reduce

from common import NewNode, Index


class NodeMath(NewNode):
    def __init__(self, parents_cont: list, parents: List[Union[Index, int]]):
        super().__init__(parents_cont, parents)
    

class Add(NodeMath):
    def operar(self):
        outs = self.get_outs()
        self.output = sum(outs)
        self.is_ready = True
        return self.output


class Multiply(NodeMath):
    def operar(self):
        outs = self.get_outs()
        self.output = reduce(lambda x, y: x * y, outs)
        self.is_ready = True
        return self.output


if __name__ == "__main__":
    # 5, 4, 20, 60, 3, 10, 2, 46, 1
    # OUT: 667
    x = []
    x.extend([
        Multiply(x, [5, 4]),            # 5, 4
        Add(x, [Index(0), 20]),         # 20
        Add(x, [Index(1), 60]),         # 60
        Multiply(x, [Index(2), 3]),     # 3
        Add(x, [Index(3), 10]),         # 10
        Multiply(x, [Index(4), 2]),     # 2
        Add(x, [Index(5), 46]),         # 46
        Add(x, [Index(6), 1]),          # 1; out!
    ])
    print(x[-1].operar())