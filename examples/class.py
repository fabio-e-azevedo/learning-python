from __future__ import annotations
from typing import Type, TypeVar


T = TypeVar('T', bound='People')


class People:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
    
    def __str__(self) -> str:
        return f'Name is {self.name}, Age {self.age}'
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name='{self.name}', age={self.age})"
    
    def __add__(self, other: People) -> People:
        if not isinstance(other, People):
            return NotImplemented
        
        new_name = f"{self.name} + {other.name}"
        new_age = self.age + other.age
        return People(name=new_name, age=new_age)
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, People):
            return NotImplemented
        return (self.name, self.age) == (other.name, other.age)

    def __hash__(self) -> int:
        # A documentação do Python recomenda que, se você sobrescrever __eq__, você também deve sobrescrever __hash__
        return hash((self.name, self.age))


def create_dead_duck(myclass: Type[T]) -> T:
    return myclass('Dead Duck', 50)
    
    
a = People('Bob Cuspe', 40)
b = create_dead_duck(People)

print(a)
print(b)
c = eval(repr(b))
print(repr(b))

print(a + b)

print(f'a is equal to b? {a == b}')
print(f'b is equal to c? {b == c}')

peoples = {}
peoples[a] = a.name
peoples[b] = b.name

print(peoples)
print(peoples.get(c))
