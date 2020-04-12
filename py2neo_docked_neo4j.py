# -*- coding: utf-8 -*-
"""...
"""
from py2neo import Database, Graph
from py2neo import Node, Relationship

if __name__ == '__main__':
    default_db = Database(uri='bolt://localhost:7687')
    default_db.forget_all()
    # conf = default_db.config()
    # grap = default_db.default_graph()
    auth = ('neo4j', 'alxfed')
    data = Graph(auth=auth, secure=False) #host='bolt://localhost:7687', encrypted=False,
    data.delete_all()
    a = Node("Person", name="Alice", age=33)
    a.remove_label('Person')
    b = Node("Person", name="Bob", age=44)
    KNOWS = Relationship.type("KNOWS")
    data.merge(KNOWS(a, b), "Person", "name")
    print('\ndone')