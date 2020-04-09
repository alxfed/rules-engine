# -*- coding: utf-8 -*-
"""...
"""
from py2neo import Graph, Node, Relationship

if __name__ == '__main__':
    auth = ('neo4j', 'alxfed')
    db = Graph(auth=auth) #host='bolt://localhost:7687', encrypted=False,
    a = Node("Person", name="Alice", age=33)
    b = Node("Person", name="Bob", age=44)
    KNOWS = Relationship.type("KNOWS")
    db.merge(KNOWS(a, b), "Person", "name")
    print('\ndone')