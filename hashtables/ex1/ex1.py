#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)

"""
input: weights = [ 4, 6, 10, 15, 16 ], length = 5, limit = 21
output: [ 3, 1 ]  # since these are the indices of weights 15 and 6 whose sum equals 21

limit => limit of 2 weights
output: [index of highel weight, index of lover weight]

limit = 21
weights    [ 4, 6, 10, 15, 16 ]
indexes    | 0| 1| 2 | 3 |  4 |
return: [3,1]

15 + 6 = 21
higher weight + lover weight = limit

we cannot use nested loops, so we need to use hashtables insteat

1) loop thru weights limit - weight = difference and find the index
2) insert to hashtable hash_table_insert
3) compare weight value - in weight list to hashtable hash_table_retrieve
"""



def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
