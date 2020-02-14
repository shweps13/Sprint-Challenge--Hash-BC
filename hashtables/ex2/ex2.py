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
2) if some of them have source "None" - it goes to first place
3) put all stuff to list in right order
"""


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

    pass
