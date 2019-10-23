from constraintsearch import *

mapaA = {
    'A' : 'BDE',
    'B' : 'ACE', 
    'C' : 'BDE',
    'D' : 'ACE',
    'E' : 'ABDC'
}

mapaB = {
    "A": "BDE",
    "B": "ACE",
    "C": "BDEF",
    "D": "ACEF",
    "E": "ABCDF",
    "F": "CDE"
}

mapaC = {
    "A": "BDEF",
    "B": "ACF",
    "C": "BDFG",
    "D": "ACEG",
    "E": "ADFG",
    "F": "ABCEG",
    "G": "CDEF"
}

def map_constraint(m1, c1, m2, c2):
    return c1 != c2

def make_graph(mapa):
    return { (p,n):map_constraint for p in mapa for n in mapa[p] }

def make_domains(mapa, colors):
    return {country:colors for country in mapa}

ex = [mapaA, mapaB, mapaC]
colors = "rgb"
for alin in ex:
    cs = ConstraintSearch(make_domains(alin, colors), make_graph(alin))
    print(cs.search())