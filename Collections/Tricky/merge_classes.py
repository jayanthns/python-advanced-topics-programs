class A(object):
    
    def __init__(self, args):
        self.a = 'a'
        self.args = args
    
    def getattA(self):
        return self.a, self.args

class B(object):
    b = 'b'
    def __init__(self, args):
        self.b_init = args

    def getattB(self):
        return self.b

C = type('C', (A,B), dict(c='c'))
print(C)