

from semantic_network import *
from bayes_net import *
from functools import reduce


class MySN(SemanticNetwork):


    def query_dependents(self,entity):
        # Get all dependencies for local entity.
        deps = list(set([d.relation.entity1 for d in self.query_local(rel="depends", e2=entity)]))

        # Entity may have a subtype, and the subtype dependencies must be considered and added
        subDeps = list(map(lambda x: self.query_dependents(x.relation.entity1),self.query_local(rel="subtype", e2=entity)))
        deps += [item for elem in [d for d in subDeps] for item in elem]

        # It's necessary to cross each local dependency and check for their subtypes and actual dependencies
        # For dependencies with subtypes, remove entity and add entity subtypes
        # Add dependencies dependecies 
        for d in deps:
            hasSubs = self.query_local(rel = "subtype", e2=d)
            if hasSubs:
                if d in deps:
                    deps.remove(d)
                deps += [sub.relation.entity1 for sub in hasSubs]
            hasDeps = self.query_local(rel="depends", e2=d)
            if hasDeps:
                deps += [dp.relation.entity1 for dp in hasDeps]
        
        return list(set(deps))

    def query_causes(self, entity):
        # Get local dependency
        deps = self.query_local(e1 = entity , rel="depends")
        res = []
        
        # Get dependency for every depency and append that to the res list
        for d in deps:
            res += self.query_causes(d.relation.entity2)
            res.append(d.relation.entity2)
        
        # Get subtype
        stypes = self.query_local(e1=entity, rel="subtype")
        
        # Get dependencies for each subtype of the current entity and add to the list 
        for s in stypes:
            res += self.query_causes(s.relation.entity2)
        return list(set(res))


    def query_causes_sorted(self,entity):
        # Get causes and each tech
        causes = self.query_causes(entity)
        techs = list(set([d.user for d in self.query_local(rel="debug_time")]))
        causesUnsorted = []
        # For every cause we gotta calculate the average time to fix
        for cause in causes:
            timeList = [] 
            for tech in techs:
                timeList += [d.relation.entity2 for d in self.query_local(user=tech, rel="debug_time", e1=cause)]
            causesUnsorted.append((cause, reduce(lambda x, y: x + y, timeList) / len(timeList)))
        # Return sorted list of causes, first by numeric then by alphabetic order
        return sorted(causesUnsorted, key=lambda x: (float(x[1]), x[0]))           
        


class MyBN(BayesNet):

    def markov_blanket(self,var):
        mkblkt = []
        
        # Get var parents
        mkblkt += self.get_parents(var)
        
        # Get children and children parents 
        children = self.get_children(var)
        cParents = [item for elem in list(map(lambda x: self.get_parents(x), children)) for item in elem]
        
        # Remove self from children parents
        cParents.remove(var)
        
        # Add them to the MKBLNKT
        mkblkt += list(set(children + cParents))

        return mkblkt
        
    # Aux Function to get var parents
    def get_parents(self, var):
        var_parents = self.dependencies[var]
        # Check for each value of the dictionary all the parent values
        return list(set([prt[0] for key in var_parents.keys() for prt in key]))

    # Aux Function to get var children
    def get_children(self, var):
        return list(set([dep for dep in self.dependencies.keys() if var in self.get_parents(dep)]))
        
