#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


def get_indices_of_item_weights(weights, length, limit):
    # hashtable capacity is 16
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    # loop through the length of the weights array
    for i in range(len(weights)):

        # get the value from key at i  
        # from the hash table, subtract the limit from value of weight[i]
        wght = weights[i]
        idx = hash_table_retrieve(ht, limit - wght)
        
        # if limit - value at wght[i] is true, push the value of wght[i] and the index
        # at which the makes the value true, into a tuple, return the tuple.
        if idx != None:
            answer = (i, idx)
           
            return answer

        # insert hash table position of value of weight[i] and i
        hash_table_insert(ht, wght, i)

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
