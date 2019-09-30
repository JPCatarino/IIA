# Desenvolvimento de classes para simular uma arvore geanologica
# JPCatarino - 2019

class familyMember:

    def __init__(self, x, y):
        self.x = x 
        self.y = y

    def __str__ (self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"
    

class Dad(familyMember):

    def __init__ (self, x, y):
        super().__init__(x, y)

    def __str__(self):
        return "Dad" + super().__str__()

class Mom(familyMember):

    def __init__(self, x, y):
        super().__init__(x, y)
    
    def __str__(self):
        return "Mom" + super().__str__()

class Child(familyMember):

    def __init__(self, x, y):
        super().__init__(x, y)
    
    def __str__(self):
        return "Mom" + super().__str__()

class Family:
    
    def __init__ (self, root = familyMember()):
        self.root = root
    
    def __str__(self):
        pass 



def main():

    print(Dad(1, 2))
    print(Mom(1, 2))

if __name__ == "__main__":
    main()
