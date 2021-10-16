from abc import ABC, abstractmethod

class Node(ABC):
    @abstractmethod
    def __init__(self):
        super().__init__()


### TEXT!

class TextNode(Node):
    def __init__(self, letter):
        super().__init__()
        self.letter = letter

class Append(TextNode):
    def operar(self, text):
        return text + self.letter


class Perpend(TextNode):
    def operar(self, text):
        return self.letter + text


class Reverse(Node):
    def __init__(self):
        super().__init__()
    
    def operar(self, text):
        return text[::-1]


def operar_text(nodos, primer_input):
    salida = primer_input
    for nodo in nodos:
        salida = nodo.operar(salida)
    return salida


### MATH!

class NumNode(Node):
    def __init__(self, num1, num2):
        super().__init__()
        self.num1 = num1
        self.num2 = num2

class Add(NumNode):
    def operar(self):
        return self.num1 + self.num2


class Multiply(NumNode):
    def operar(self):
        return self.num1 * self.num2


def operar_math(nodos, primer_input):
    salida = primer_input
    for nodo, num in nodos:
        salida = nodo(salida, num).operar()
    return salida


### MEM!

class NodeMem(Node):
    def __init__(self, mem):
        super().__init__()
        self.mem = mem
    
    def operar(self, entrada):
        return self.mem[entrada]


def operar_memoria(nodos, primer_input):
    salida = primer_input
    for nodo in nodos:
        if isinstance(salida, str):
            salida = salida + nodo.operar(salida)
        else:
            salida = nodo.operar(salida)
    return salida

if __name__ == "__main__":
    text = [
        Perpend("a"),
        Perpend("c"),
        Append("t"),
        Append("a"),
        Perpend("n"),
        Perpend("e"),
        Perpend("_"),
        Append("_"),
        Perpend("e"),
        Append("p"),
        Append("r"),
        Append("o"),
        Append("g"),
        Append("r"),
        Perpend("m"),
        Append("a"),
        Append("m"),
        Append("a"),
        Append("r"),
    ]
    salida_text = operar_text(text, "n")
    print(salida_text)

    nums = [
        (Multiply, 4),
        (Add, 20),
        (Add, 60),
        (Multiply, 3),
        (Add, 10),
        (Multiply, 2),
        (Add, 46),
        (Add, 1),
    ]
    salida_num = operar_math(nums, 5)
    print(salida_num)

    mems = [
        NodeMem(["a"] * 130 + ["I"]),
        NodeMem({"I": "I"}),
        NodeMem({"II": "C"}),
        NodeMem({"IIC": "2"}),
        NodeMem({"IIC2": "1"}),
        NodeMem({"IIC21": "1"}),
        NodeMem({"IIC211": "5"}),
    ]
    salida_mem = operar_memoria(mems, 130)
    print(salida_mem)
