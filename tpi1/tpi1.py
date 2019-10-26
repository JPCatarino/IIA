# Jorge Catarino
# 85028

from tree_search import *
from functools import reduce
from math import floor, ceil

class MyTree(SearchTree):

    def __init__(self,problem, strategy='breadth',max_nodes=None): 
        SearchTree.__init__(self, problem, strategy)
        SearchNode.depth = 0
        SearchNode.cost = 0
        SearchNode.evalfunc = 0
        SearchNode.children = None
        self.solution_length = 0
        self.total_nodes = 1
        self.root.cost = 0
        self.root.depth = 0
        self.root.evalfunc = problem.domain.heuristic(problem.initial, problem.goal)
        self.non_terminal_nodes = 1
        self.terminal_nodes = 0
        self.solution_cost = 0
        self.max_nodes = max_nodes

    def astar_add_to_open(self,lnewnodes):
        self.open_nodes = sorted(self.open_nodes + lnewnodes, key = lambda node: node.evalfunc)

    def effective_branching_factor(self):
        return self.total_nodes ** (1/self.solution_length)
        
    def update_ancestors(self,node):
        if node.children:
            if len(node.children) > 1:
                node.evalfunc = reduce((lambda n1, n2: min(n1,n2)), list(map(lambda v : v.evalfunc, node.children)))
            else:
                node.evalfunc = node.children[0].evalfunc
        if node.parent:
            self.update_ancestors(node.parent)
        
    def discard_worse(self):       
        nwnc = list(filter(lambda x: x.children == None, self.open_nodes))
        ntm = list(set(map(lambda x: x.parent, nwnc)))

        ntmnone = [c for c in ntm if all(map(lambda x: x.children == None, c.children))]
        maxV = reduce((lambda n1, n2: max(n1,n2)), list(map(lambda x : x.evalfunc, ntmnone)))
        trm = list(set(filter(lambda x: x.evalfunc == maxV, ntmnone)))[0]
        
        self.terminal_nodes -= len(trm.children)

        tValue = len(trm.children)
        lValue = len(self.open_nodes)

        self.open_nodes = [c for c in self.open_nodes if c not in trm.children ]
        trm.children = None

        
        self.non_terminal_nodes -=1
        self.terminal_nodes +=1
        self.add_to_open([trm])
                  

    def search2(self):
        while self.open_nodes != []:
            node = self.open_nodes.pop(0)
            node.children = []

            if self.problem.goal_test(node.state):
                self.solution_length = node.depth
                self.solution_cost = node.cost
                return self.get_path(node)
            lnewnodes = []
            for a in self.problem.domain.actions(node.state):
                newstate = self.problem.domain.result(node.state,a)
                if newstate not in self.get_path(node):
                    newnode = SearchNode(newstate,node)
                    lnewnodes.append(newnode)
                    lnewnodes[-1].cost = node.cost + self.problem.domain.cost(node.state, a)
                    lnewnodes[-1].depth = node.depth + 1
                    lnewnodes[-1].children = None
                    lnewnodes[-1].evalfunc = newnode.cost + self.problem.domain.heuristic(newstate, self.problem.goal)

                    node.children.append(newnode)
                    self.update_ancestors(lnewnodes[-1])
            
            if len(lnewnodes):
                self.total_nodes += len(lnewnodes) 
            
            if node.children:
                self.non_terminal_nodes += 1
                self.terminal_nodes += len(node.children)
            
            self.terminal_nodes -= 1

            self.add_to_open(lnewnodes)

            if self.max_nodes:
                while self.terminal_nodes + self.non_terminal_nodes > self.max_nodes:
                    self.discard_worse()
        return None

    # shows the search tree in the form of a listing
    def show(self,heuristic=False,node=None,indent=''):
        if node==None:
            self.show(heuristic,self.root)
            print('\n')
        else:
            line = indent+node.state
            if heuristic:
                line += (' [' + str(node.evalfunc) + ']')
            print(line)
            if node.children==None:
                return
            for n in node.children:
                self.show(heuristic,n,indent+'  ')


