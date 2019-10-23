
# Module: tree_search
# 
# This module provides a set o classes for automated
# problem solving through tree search:
#    SearchDomain  - problem domains
#    SearchProblem - concrete problems to be solved
#    SearchNode    - search tree nodes
#    SearchTree    - search tree with the necessary methods for searhing
#
#  (c) Luis Seabra Lopes
#  Introducao a Inteligencia Artificial, 2012-2019,
#  Inteligência Artificial, 2014-2019

from abc import ABC, abstractmethod
import sys

# Dominios de pesquisa
# Permitem calcular
# as accoes possiveis em cada estado, etc
class SearchDomain(ABC):

    # construtor
    @abstractmethod
    def __init__(self):
        pass

    # lista de accoes possiveis num estado
    @abstractmethod
    def actions(self, state):
        pass

    # resultado de uma accao num estado, ou seja, o estado seguinte
    @abstractmethod
    def result(self, state, action):
        pass

    # custo de uma accao num estado
    @abstractmethod
    def cost(self, state, action):
        pass

    # custo estimado de chegar de um estado a outro
    @abstractmethod
    def heuristic(self, state, goal):
        pass

    # test if the given "goal" is satisfied in "state"
    @abstractmethod
    def satisfies(self, state, goal):
        pass


# Problemas concretos a resolver
# dentro de um determinado dominio
class SearchProblem:
    def __init__(self, domain, initial, goal):
        self.domain = domain
        self.initial = initial
        self.goal = goal
    def goal_test(self, state):
        return self.domain.satisfies(state,self.goal)

# Nos de uma arvore de pesquisa
class SearchNode:
    def __init__(self,state,parent,depth,cost,heuristic): 
        self.state = state
        self.parent = parent
        self.depth = depth
        self.cost = cost
        self.heuristic = heuristic

    def in_parent(self, state):
        if self.parent == None:
            return False
        
        return self.parent.state == state or self.parent.in_parent(state)    

    def __str__(self):
        return f"no({self.state}, {self.parent}, {self.depth}, {self.cost}, {self.heuristic})"
    def __repr__(self):
        return str(self)

# Arvores de pesquisa
class SearchTree:

    # construtor
    def __init__(self,problem, strategy='breadth'): 
        self.problem = problem
        root = SearchNode(problem.initial, None, 0, 0, problem.domain.heuristic(problem.initial, problem.goal))
        self.open_nodes = [root]
        self.strategy = strategy
        self.length = 0
        self.terminal = 1
        self.non_terminal = 0
        self.ramification = 0
        self.cost = 0
        self.highest_cost_nodes = [root]
        self.average_depth = 0

    # obter o caminho (sequencia de estados) da raiz ate um no
    def get_path(self,node):
        if node.parent == None:
            return [node.state]
        path = self.get_path(node.parent)
        path += [node.state]
        return(path)

    # procurar a solucao
    def search(self, limit = sys.maxsize):
        total_depth = 0
        nodes = 0
        while self.open_nodes != []:
            node = self.open_nodes.pop(0)

            if node.cost > self.highest_cost_nodes[0].cost:
                self.highest_cost_nodes = [node]
            elif node.cost == self.highest_cost_nodes[0].cost:
                self.highest_cost_nodes.append(node)

            self.length += 1
            if self.problem.goal_test(node.state):
                self.ramification = (self.non_terminal + self.terminal - 1) / self.non_terminal
                self.cost = node.cost
                self.average_depth = total_depth/(self.terminal + self.non_terminal)
                return self.get_path(node)
            lnewnodes = []
            for a in self.problem.domain.actions(node.state):
                newstate = self.problem.domain.result(node.state,a)
                if not node.in_parent(newstate) and node.depth < limit:
                    lnewnodes += [SearchNode(newstate,node,node.depth + 1, node.cost + self.problem.domain.cost(node.state, a), self.problem.domain.heuristic(newstate, self.problem.goal))]
            
            if len(lnewnodes):
                self.terminal += len(lnewnodes)
            else: 
                self.non_terminal += 1
            total_depth += node.depth
            self.terminal -= 1
            self.add_to_open(lnewnodes)
        return None

    # juntar novos nos a lista de nos abertos de acordo com a estrategia
    def add_to_open(self,lnewnodes):
        if self.strategy == 'breadth':
            self.open_nodes.extend(lnewnodes)
        elif self.strategy == 'depth':
            self.open_nodes[:0] = lnewnodes
        elif self.strategy == 'uniform':
            self.open_nodes = sorted(self.open_nodes + lnewnodes, key = lambda node: node.cost)
        elif self.strategy == 'greedy':
            self.open_nodes = sorted(self.open_nodes + lnewnodes, key = lambda node: node.heuristic)
        elif self.strategy == 'astar':
            self.open_nodes = sorted(self.open_nodes + lnewnodes, key = lambda node: node.heuristic + node.cost)