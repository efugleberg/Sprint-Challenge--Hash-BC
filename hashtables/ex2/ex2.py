#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    
    for i in range(length):
        src = tickets[i].source
        dest = tickets[i].destination
        if src == 'NONE':
            route[0] = dest
        hash_table_insert(hashtable, src, dest)
    
    for i in range(length):
        if i > 0:
            destination = hash_table_retrieve(hashtable, route[i-1])
            route[i] = destination

    return route


