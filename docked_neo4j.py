# -*- coding: utf-8 -*-
"""...
"""
from neo4j import GraphDatabase

driver = GraphDatabase.driver("bolt://localhost:7687", encrypted=False, auth=("neo4j", "alxfed"))

def add_friend(tx, name, friend_name):
    tx.run("merge (a:Person {name: $name}) "
           "merge (a)-[:knows]->(friend:Person {name: $friend_name})",
           name=name, friend_name=friend_name)

def print_friends(tx, name):
    for record in tx.run("match (a:Person)-[:knows]->(friend) where a.name = $name "
                         "return friend.name order by friend.name", name=name):
        print(record["friend.name"])


if __name__ == '__main__':
    with driver.session() as session:
        session.write_transaction(add_friend, "Arthur", "Guinevere")
        session.write_transaction(add_friend, "Arthur", "Lancelot")
        session.write_transaction(add_friend, "Arthur", "Merlin")
        session.read_transaction(print_friends, "Arthur")

    driver.close()
    print('\ndone')