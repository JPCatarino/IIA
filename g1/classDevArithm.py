# Desenvolvimento de Classes
# JPCatarino 2019

# Expressões aritméticas 

class const:

    def __init__(self, val):
        self.val = val
    
    def __str__(self):
            return "Constant = " + str(self.val)
    
    def eval(self, x=1):
        return self.val 

        
class var:
    
    def __init__(self, val = None):
        self.val = val
    
    def __str__(self):
        return "Var = " + str(self.val)

    def eval(self, x=1):
        return self.val * x

class sum:

    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def __str__(self):
        return "Sum of " + str(self.a) + " and " + str(self.b)

    def eval(self, x=1):
        return self.a.eval(x) + self.b.eval(x)

class prod:

    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def __str__(self):
        return "Product of " + str(self.a) + " and " + str(self.b)

    def eval(self, x=1):
        return self.a.eval(x) * self.b.eval(x)

