#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    for i in range(len(weights)):
        wght = weights[i]
        idx = hash_table_retrieve(ht, limit - wght)
        if idx != None:
            answer = (i, idx)
            return answer
        hash_table_insert(ht, wght, i)

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
