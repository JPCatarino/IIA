from constraintsearch import * 

def bikeHat_constraint(f1, c1, f2, c2):
    b1, h1 = c1
    b2, h2 = c2
    fc1 = [b1, h1]
    fc2 = [b2, h2]
    
    if f1 in fc1:
        return False
    if f2 in fc2:
        return False

    if b1 == h1 or b2 == h2:
        return False

    if b1 == b2 or h1 == h2:
        return False

    return True
 

def make_graph(friends):
    return { (p,n):bikeHat_constraint for p in friends for n in friends if (p!=n) }


def make_domains(friends):
    domain = {}
    bikes = friends
    hats = friends
    for friend in friends:
        domain[friend] = []
        for bike in bikes:
            for hat in hats:
                domain[friend].append((bike, hat))
    return domain

friends = ["André", "Bernardo", "Claúdio"]

cs = ConstraintSearch(make_domains(friends), make_graph(friends))

print(cs.search())