from collections import Counter

# Guiao de representacao do conhecimento
# -- Redes semanticas
# 
# Inteligencia Artificial & Introducao a Inteligencia Artificial
# DETI / UA
#
# (c) Luis Seabra Lopes, 2012-2020
# v1.9 - 2019/10/20
#


# Classe Relation, com as seguintes classes derivadas:
#     - Association - uma associacao generica entre duas entidades
#     - Subtype     - uma relacao de subtipo entre dois tipos
#     - Member      - uma relacao de pertenca de uma instancia a um tipo
#

class Relation:
    def __init__(self,e1,rel,e2):
        self.entity1 = e1
#       self.relation = rel  # obsoleto
        self.name = rel
        self.entity2 = e2
    def __str__(self):
        return self.name + "(" + str(self.entity1) + "," + \
               str(self.entity2) + ")"
    def __repr__(self):
        return str(self)


# Subclasse Association
class Association(Relation):
    def __init__(self,e1,assoc,e2):
        Relation.__init__(self,e1,assoc,e2)

#   Exemplo:
#   a = Association('socrates','professor','filosofia')

class AssocOne(Association):
    def __init__(self,e1,assoc,e2):
        Association.__init__(self,e1,assoc,e2)

class AssocNum(Association):
    def __init__(self,e1,assoc,e2):
        assert e2.isnumeric(str(e2))
        Association.__init__(self,e1,assoc,e2)

# Subclasse Subtype
class Subtype(Relation):
    def __init__(self,sub,super):
        Relation.__init__(self,sub,"subtype",super)


#   Exemplo:
#   s = Subtype('homem','mamifero')

# Subclasse Member
class Member(Relation):
    def __init__(self,obj,type):
        Relation.__init__(self,obj,"member",type)

#   Exemplo:
#   m = Member('socrates','homem')

# classe Declaration
# -- associa um utilizador a uma relacao por si inserida
#    na rede semantica
#
class Declaration:
    def __init__(self,user,rel):
        self.user = user
        self.relation = rel
    def __str__(self):
        return "decl("+str(self.user)+","+str(self.relation)+")"
    def __repr__(self):
        return str(self)

#   Exemplos:
#   da = Declaration('descartes',a)
#   ds = Declaration('darwin',s)
#   dm = Declaration('descartes',m)

# classe SemanticNetwork
# -- composta por um conjunto de declaracoes
#    armazenado na forma de uma lista
#
class SemanticNetwork:
    def __init__(self,ldecl=[]):
        self.declarations = ldecl
    def __str__(self):
        return my_list2string(self.declarations)
    def insert(self,decl):
        if isinstance(decl.relation, AssocOne):
            if self.query_local(e1= decl.relation.entity1, rel= decl.relation.name) != []:
                return None
        self.declarations.append(decl)
    def query_local(self,user=None,e1=None,rel=None,e2=None):
        self.query_result = \
            [ d for d in self.declarations
                if  (user == None or d.user==user)
                and (e1 == None or d.relation.entity1 == e1)
                and (rel == None or d.relation.name == rel)
                and (e2 == None or d.relation.entity2 == e2) ]
        return self.query_result
    def show_query_result(self):
        for d in self.query_result:
            print(str(d))
    
    # Ex1
    def getAssociations(self):
        return list(set([d.relation.name for d in self.declarations if isinstance(d.relation, Association)]))
    
    # Ex2 
    def getObjects(self):
        return list(set([d.relation for d in self.declarations if isinstance(d.relation, Member)]))

    # Ex3 
    def getUsers(self):
        return list(set(declaration.user for declaration in self.query_local()))    
    
    # Ex4
    def getTypes(self):
        ent1T = [d.relation.entity1 for d in self.query_local(rel = 'subtype')]
        ent2T = [d.relation.entity2 for d in self.query_local() if d.relation.name in ["subtype", "member"]]
        return list(set(ent1T + ent2T))

    # Ex5 
    def getEntityLocalAssocs(self, entity):
        pass

    # Ex6 
    def getUserDecRel(self, user):
        pass

    # Ex7
    def getUserUnAssocs(self, user):
        pass

    # Ex8 
    def getLocalAssocUsers(self, entity):
        return list(set([(d.relation.name, d.user) for d in self.query_local() if d.name not in ["member", "subtype"] and (d.relation.entity1 == entity or d.relation.entity2 == entity)]))

    # Ex9
    def predecessor(self, entA, entB):
        local_predecessor = [d.relation.entity2 for d in self.query_local()
                if d.relation.name in ["member", "subtype"]
                and d.relation.entity1 == entB]  

        if entA in local_predecessor:
            return True
        
        return any([self.predecessor(entA, pred) for pred in local_predecessor])

    # Ex10
    def predecessor_path(self, entA, entB):
        local_predecessor = [d.relation.entity2 for d in self.query_local()
                if d.relation.name in ["member", "subtype"]
                and d.relation.entity1 == entB]  
        
        if not local_predecessor:
            return None
        
        if entA in local_predecessor:
            return [entA, entB]

        path = [pathToP + [entB] for pathToP in [self.predecessor_path(entA, pred) for pred in local_predecessor] if pathToP]        
        
        return path.pop()
    
    # Ex11
    def query(self, entity, rel = None):
        local = [self.query(d.relation.entity2, rel) \
        for d in self.declarations if d.relation.name in ["member", "subtype"] and d.relation.entity1 == entity]

        return [item for sublist in local for item in sublist] +\
             [d for d in self.declarations if d.relation.entity1 == entity and d.relation.name == rel]
    

    # Ex11B
    def query2(self, entity, rel = None):
        local = [self.query2(d.relation.entity2, rel) \
        for d in self.declarations if (isinstance(d.relation, Member) or isinstance(d.relation, Subtype)) and d.relation.entity1 == entity]

        return [item for sublist in local for item in sublist if isinstance(item.relation, Association)] +\
             self.query_local(e1=entity, rel=rel)
    
    # Ex12
    def query_cancel(self, entity, rel = None):
        local = [self.query_cancel(d.relation.entity2, rel) \
        for d in self.declarations if (isinstance(d.relation, Member) or isinstance(d.relation, Subtype)) and d.relation.entity1 == entity]

        local_decl = self.query_local(e1=entity, rel=rel)

        local_rels = [d.relation.name for d in local_decl]

        return [item for sublist in local for item in sublist if item.relation.name not in local_rels] + local_decl

    # Ex13
    def query_down(self, entity, rel= None, skip = True):
        local = [self.query_down(d.relation.entity1, rel, False) \
        for d in self.declarations if (isinstance(d.relation, Member) or isinstance(d.relation, Subtype)) and d.relation.entity2 == entity]

        l = [] if skip else self.query_local(e1=entity, rel=rel)

        return [item for sublist in local for item in sublist] + l
    
    # Ex14
    def query_induce(self, entity, rel=None):
        suc = self.query_down(entity, rel)
        c = Counter([s.relation.entity2 for s in suc])
        for common in c.most_common(1):
            return common[0]




# Funcao auxiliar para converter para cadeias de caracteres
# listas cujos elementos sejam convertiveis para
# cadeias de caracteres
def my_list2string(list):
   if list == []:
       return "[]"
   s = "[ " + str(list[0])
   for i in range(1,len(list)):
       s += ", " + str(list[i])
   return s + " ]"
    

