#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)

"""

source => starting airport
destination => next airport

first ticket: {source: "NONE", destination: "some_place"}
first ticket: {source: "some_other_place", destination: "NONE"}

We will get:
tickets = [
  Ticket{ source: "NONE", destination: "ORD" },
  Ticket{ source: "ORD", destination: "CID" },
  Ticket{ source: "CID", destination: "BHM" },
  Ticket{ source: "BHM", destination: "NONE" }
]

Result shoul be:
["ORD", "CID", "BHM", "NONE"]

Destination previous ticket and source of current - some kind of link
["NONE", "ORD"] => ["ORD", "CID"] => ["CID", "BHM"] => ["BHM". "NONE"]

1) loop thru tickets list to add to ht
2) if some from them have source "None" - it goes to first place
3) put all stuff to list in right order
4) return list of values
"""


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

    def __repr__(self):
        return f"(source: {self.source}, dest.: {self.destination})"


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    #route => result list
    route = [None] * length
    
    
    for ticket in tickets:
        source = ticket.source
        destination = ticket.destination
        print(f"[{source}] ==> [{destination}]")

        # ticket to ht
        hash_table_insert(hashtable, source, destination )
        
        if source == "NONE":    
            # if NONE => place at index[0] of route = destination
            route[0] = destination
            print(f"Route [{route[0]}]")
    
    # previous-tickets value => next-tickets key return the value of that key using retrieval
    index = 0
    current_destination = 0

    while True:
        # current destination => route at current index
        current_destination = route[index]
        print(f"Current [{current_destination}]")
        next_destination = hash_table_retrieve(hashtable, current_destination)
        print(f"Next [{next_destination}]")
        index += 1

        route[index] = next_destination
        print(f"Index [{route[index]}]")
        if next_destination == "NONE":
            break
    
    # Cleaning list from the "NONE"
    route.pop()

    return route

ticket_1 = Ticket("NONE", "PDX")
ticket_2 = Ticket("PDX", "DCA")
ticket_3 = Ticket("DCA", "NONE")

tickets = [ticket_1, ticket_2, ticket_3]

print(reconstruct_trip(tickets, 3))