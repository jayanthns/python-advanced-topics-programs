from collections import namedtuple

User = namedtuple('Demo', 'name age', rename=True)

c = User('Jayanth', 24)
print(c.name)
print(User._fields)
