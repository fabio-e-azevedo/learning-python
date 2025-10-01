import inspect
from attrs import define, frozen, field, Factory

@define(kw_only=True)
class User:
    id: int = 0
    name: str = field(default="")
    email: str = field(repr=False)
    
print(inspect.getsource(User.__init__))

user = User(id=1, name="Dead Duck", email="dead@duck.com")

print(user)
