from __future__ import annotations

class People:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
    
    def __str__(self) -> str:
        return f'Name is {self.name}, Age {self.age}'
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name='{self.name}', age={self.age})"
    
    def __add__(self, people: People) -> str:
        return f'{self.name} + {people.name} = {self.age + people.age}'
    
    def __eq__(self, people: People) -> bool:
        if people.__class__ is self.__class__:
            return (self.name, self.age) == (people.name, people.age)
        else:
            return NotImplemented
    
    
    
a = People('Bob Cuspe', 40)
b = People('Dead Duck', 30)


print(a)
print(b)
c = eval(repr(b))
print(repr(b))

print(a + b)

print(f'a is equal to b? {a == b}')