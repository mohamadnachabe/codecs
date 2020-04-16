huffman = {'A': 10,
           'E': 15,
           'I': 12,
           'S': 3,
           'T': 4,
           'P': 13,
           '\\n': 1}


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def find_bottom_n(n):
    minimum_n = []
    for k in huffman.keys():
        if len(minimum_n) == n:
            tmp, index = maximum(minimum_n)

            if huffman[k] < tmp:
                minimum_n[index] = k
        else:
            minimum_n.append(k)

    return minimum_n


def remove_entries_from_huffman(to_remove):
    for k in to_remove:
        if k in huffman.keys():
            huffman.pop(k)


def maximum(array):
    max_n = 0
    index = -1
    for i in range(len(array)):
        if huffman[array[i]] > max_n:
            max_n = huffman[array[i]]
            index = i
    return max_n, index


def huff_2():
    bottom_2 = find_bottom_n(2)

    m, i = maximum(bottom_2)
    right = Node(bottom_2[i], None, None)
    left = Node(bottom_2[len(bottom_2) - 1 - i], None, None)

    huffman_tree_head = Node(huffman[bottom_2[0]] + huffman[bottom_2[1]], left, right)
    remove_entries_from_huffman(bottom_2)
    return huffman_tree_head


def huff_1(huffman_tree_head):
    while huffman_tree_head.value < maximum(list(huffman.keys()))[0]:
        bottom_1 = find_bottom_n(1)
        huffman_tree_head = \
            Node(huffman_tree_head.value + huffman[bottom_1[0]], Node(bottom_1[0], None, None), huffman_tree_head)
        remove_entries_from_huffman(bottom_1)
    return huffman_tree_head


def find_smallest_subtree(trees):
    smallest = trees[0]
    for i in range(1, len(trees)):
        if trees[i].value < smallest.value:
            smallest = trees[i]

    return smallest


def encode_huffman_tree_r(node, d, val=''):

    if node.right is None and node.left is None:
        d[node.value] = val

    if node.left is not None:
        encode_huffman_tree_r(node.left, d, val + '0')

    if node.right is not None:
        encode_huffman_tree_r(node.right, d, val + '1')

    return d


def construct_huffman_tree():
    hs = []
    while len(huffman.keys()) != 1:
        h_ = huff_2()
        h = huff_1(h_)
        hs.append(h)

    smallest_subtree = find_smallest_subtree(hs)
    hs.remove(smallest_subtree)

    remainder_k = list(huffman.keys())[0]
    remainder_v = huffman[remainder_k]

    hs.append(Node(smallest_subtree.value + remainder_v, Node(remainder_k, None, None), smallest_subtree))

    ht = Node(0, None, None)
    for i in range(len(hs) - 1):
        ht = Node(hs[i].value + hs[i + 1].value, hs[i], hs[i + 1])

    return ht


if __name__ == '__main__':
    huffman_tree = construct_huffman_tree()

    huffman_encoding = {}
    encode_huffman_tree_r(huffman_tree, huffman_encoding)

    print(huffman_encoding)
