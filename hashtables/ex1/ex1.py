#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)

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
    index = 0

    for weight in weights:
        # Find the difference
        difference = limit - weight
        # print("-==", index, "weight: ", weight, "difference = ", difference, "==-")

        # Check difference in hash table to check a key
        check_ht = hash_table_retrieve(ht, difference)
        # it will give value of key
        # [ 4,    6,    10,    15,    16 ]
        # [4-0] [6-1] [10-2] [15-3] [16-4]

        if check_ht is not None:
            print("inside", index, check_ht )
            return(index, check_ht)

        hash_table_insert(ht, weight, index)

        # print(ht)
        index += 1

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")

print(get_indices_of_item_weights([4, 6, 10, 15, 16], 5, 21))