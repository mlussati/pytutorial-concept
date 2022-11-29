"""
Pilha estrutura de dados
"""
class Pilha():
    def __init__(self) -> None:
        self.items = []

    def push(self, item) -> None:
        self.items.append(item)

    def pop(self) -> list:
        return self.items.pop()
    
    def is_empty(self) -> list:
        return self.items == []

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def get_pilha(self) -> list:
        return self.items

# minhaPilha = Pilha()
# minhaPilha.push("A")
# minhaPilha.push("B")
# print(minhaPilha.get_pilha())
# minhaPilha.push("C")
# print(minhaPilha.get_pilha())
# minhaPilha.pop()
# print(minhaPilha.get_pilha())

# minhaPilha = Pilha()
# print(minhaPilha.is_empty()) 

minhaPilha = Pilha()
minhaPilha.push("A")
minhaPilha.push("B")
minhaPilha.push("C")
minhaPilha.push("D")
print(minhaPilha.peek())