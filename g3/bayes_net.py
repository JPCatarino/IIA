from itertools import product

class BayesNet:

    def __init__(self, ldep=None):  # Why not ldep={}? See footnote 1.
        if not ldep:
            ldep = {}
        self.dependencies = ldep

    # Os dados estao num dicionario (var,dependencies)
    # em que as dependencias de cada variavel
    # estao num dicionario (mothers,prob);
    # "mothers" e' um frozenset de pares (mothervar,boolvalue)
    def add(self,var,mothers,prob):
        self.dependencies.setdefault(var,{})[frozenset(mothers)] = prob

    # Probabilidade conjunta de uma dada conjuncao 
    # de valores de todas as variaveis da rede
    def jointProb(self,conjunction):
        prob = 1.0
        for (var,val) in conjunction:
            for (mothers,p) in self.dependencies[var].items():
                if mothers.issubset(conjunction):
                    prob*=(p if val else 1-p)
        return prob

    def ancestors(self, var):
        tmpAnc = self.get_parents(var)
        anc = tmpAnc + list(map(lambda x: self.get_parents(x), tmpAnc))
        return [item for elem in anc for item in elem]

    def get_parents(self, var):
        var_parents = self.dependencies[var]
        # Check for each value of the dictionary all the parent values
        return list(set([prt[0] for key in var_parents.keys() for prt in key]))

    def conjunctions(self, listvar):
        lcomb = product([True, False], repeat=len(listvar))
        return list(map(lambda c: list(zip(listvar, c)), lcomb))
    
    # TODO: Actually calculate individual probability
    def indProb(self, var, val):
        C = self.conjunctions(self.ancestors(var))
        prob = 0.0
        for c in C:
            prob += self.jointProb(c+[(var, val)])
        return prob




# Footnote 1:
# Default arguments are evaluated on function definition,
# not on function evaluation.
# This creates surprising behaviour when the default argument is mutable.
# See:
# http://docs.python-guide.org/en/latest/writing/gotchas/#mutable-default-arguments

