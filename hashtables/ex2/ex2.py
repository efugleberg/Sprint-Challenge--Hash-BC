#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


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
    # loop through your tickets, set the source of None as the first
    # destination (route[0]) of your trip
    for i in range(length):
        src = tickets[i].source
        dest = tickets[i].destination
        if src == 'NONE':
            route[0] = dest
        hash_table_insert(hashtable, src, dest)
    
    # loop through all tickets greater than list index 0
    # from the hashtable, retrieve the value of route[i-1], assign that value
    # as the current destination in route, return route
    for i in range(length):
        if i > 0:
            destination = hash_table_retrieve(hashtable, route[i-1])
            route[i] = destination

    return route




