from collections import namedtuple

User = namedtuple('Demo', 'name age')

c = User('Jayanth', 24)
print(c)
print(type(c))
print(User)
