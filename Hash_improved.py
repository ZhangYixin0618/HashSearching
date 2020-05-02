import random


def hash_table(list1):
    # Implanting reminder hashing method
    # the hashmap size is always the twice of the original list
    # if original item = 'a' and it's in index 1, convert it to its original value 97 then exchange two digits -> 79
    # then mod it by the length of hash table -> 79 % 20 = 19
    # so hash_table[19] = 1 -> index in original list
    # if the 19th index place is already be occupied, call rehash
    hashmap = [None] * len(list1) * 2
    # count rehash times
    rehash_count = 0
    for index in range(0, len(list1)):
        hash_item = int(str(''.join(reversed(str(ord(list1[index])))))) % (len(hashmap))
        if hashmap[hash_item] is None:
            hashmap[hash_item] = index
        else:
            rehash(hashmap, hash_item, list1[index], index)
            rehash_count += 1
        pass
    print('rehash count:', rehash_count)
    return hashmap


def rehash(hashmap, index, rehash_item, index_org):
    # Implanting linear probe rehashing
    # go through the hash table to find a slot which is not occupied
    # e.g. if [16] is occupied ->look for [17] -> if occupied -> look for [18] -> until an unoccupied slot is found
    # if an empty slot is not found, return to the beginning of the list
    while not (hashmap[index] is None):
        if index < len(hashmap) - 1:
            index += 1
        else:
            index = 0
        pass
    else:
        hashmap[index] = index_org


def hash_search(original_list, hashmap, item):
    # calculate the hash of the wanted item
    # this hash is also the index in the hashmap
    # check if the item with hashmap index in the original list is the item we are looking for
    # if yes, return the original index
    # if not, then the item has been rehashed, call linear probe
    # if the corresponding index in hashmap is None, then item is not found, return -1, -1
    hash_item = int(str(''.join(reversed(str(ord(item)))))) % (len(hashmap))
    print('hash of item', hash_item)
    if hashmap[hash_item] is None:
        return -1, -1
    if item == original_list[hashmap[hash_item]]:
        return hashmap[hash_item], hash_item
    else:
        return linear_probe(original_list, hashmap, item, hash_item, hash_item)


def linear_probe(original_list, hashmap, item, hash_item, hash_item_original):
    # works the same as linear probe rehashing
    # e.g. if [16] is not the index we are looking for, check [17], if not, check [18]
    # go to [0] if searth to the end of the list
    # if has probed the same time as the length -> go through whole list and found no result
    # return -1, -1 -> failed to find
    probe_count = 0
    while True:
        try:
            if original_list[hashmap[hash_item]] != item:
                probe_count += 1
                hash_item = probing(len(hashmap), hash_item, probe_count)
                if hash_item == -1:
                    print('probe count', probe_count)
                    return -1, -1
                continue
            else:
                print('probe count', probe_count)
                return hashmap[hash_item], hash_item_original
        except TypeError:
            probe_count += 1
            hash_item = probing(len(hashmap), hash_item, probe_count)
            if hash_item == -1:
                print('probe count', probe_count)
                return -1, -1

def probing(length, hash_item, probe_count):
    if probe_count == length:
        return -1
    elif hash_item < length - 1:
        hash_item += 1
    else:
        hash_item = 0
    return hash_item


# random.seed(5)
# Creating a random 10-element a-z list
a = random.sample(range(ord('a'), ord('z') + 1), k=10)
a = list(map(lambda a: chr(a), a))
print(a)
hash_a = hash_table(a)
print(hash_a)

item_wanted = random.choice(a)
index_item, hash_item = hash_search(a, hash_a, item_wanted)
print('searching for', item_wanted)
if index_item == -1 or hash_item == -1:
    print('item not found')
print(item_wanted, 'should in hash index', hash_item)
print(item_wanted, 'is in index', index_item)
