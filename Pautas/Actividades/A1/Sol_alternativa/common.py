from abc import ABC, abstractmethod
from typing import List, Union


class Index(int):
    pass


class NewNode(ABC):
    @abstractmethod
    def __init__(self, parents_cont: list, parents: List[Union[Index, int]]):
        super().__init__()
        self.parents_cont = parents_cont
        self.parents = parents
        self.is_ready = False
        self.output = None
    
    def get_parents(self):
        parents = []
        for i in self.parents:
            if isinstance(i, Index):
                parents.append(self.parents_cont[i])
        return parents

    def get_outs(self):
        parents = self.get_parents()
        if not all(map(lambda x: x.is_ready, parents)):
            for parent in parents:
                if not parent.is_ready:
                    parent.operar()
        outs = []
        for i in self.parents:
            if isinstance(i, Index):
                outs.append(self.parents_cont[i].output)
            else:
                outs.append(i)  # es dato
        return outs



class Node(ABC):
    @abstractmethod
    def __init__(self, actual, parent_cont, parent_index):
        super().__init__()
        self.actual = actual
        self.parent_cont = parent_cont
        self.parent_index = parent_index
        self.is_ready = False

    @abstractmethod
    def operar(self):
        pass

    def get_parent_out(self):
        if isinstance(self.parent_cont, list):
            if self.parent_cont[self.parent_index].is_ready:
                parent_out = self.parent_cont[self.parent_index].actual
            else:
                parent_out = self.parent_cont[self.parent_index].operar()
        else:  # parent is data!
            parent_out = self.parent_cont
        return parent_out
    
    def get_actual_out(self):
        if self.actual is None:
            return None
        elif isinstance(self.actual, Index):
            return self.parent_cont[self.actual].actual
        # else: