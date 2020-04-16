def find_smallest_subtree(trees):
    smallest = trees[0]
    for i in range(1, len(trees)):
        if trees[i].value < smallest.value:
            smallest = trees[i]

    return smallest


class HuffmanEncoder:
    frequencies = {}

    def __init__(self, frequencies):
        self.frequencies = frequencies

    def find_bottom_n(self, n):
        minimum_n = []
        for k in self.frequencies.keys():
            if len(minimum_n) == n:
                tmp, index = self.maximum(minimum_n)

                if self.frequencies[k] < tmp:
                    minimum_n[index] = k
            else:
                minimum_n.append(k)

        return minimum_n

    def remove_entries_from_huffman(self, to_remove):
        for k in to_remove:
            if k in self.frequencies.keys():
                self.frequencies.pop(k)

    def maximum(self, array):
        max_n = 0
        index = -1
        for i in range(len(array)):
            if self.frequencies[array[i]] > max_n:
                max_n = self.frequencies[array[i]]
                index = i
        return max_n, index

    def huff_2(self):
        bottom_2 = self.find_bottom_n(2)

        m, i = self.maximum(bottom_2)
        right = Node(bottom_2[i], None, None)
        left = Node(bottom_2[len(bottom_2) - 1 - i], None, None)

        huffman_tree_head = Node(self.frequencies[bottom_2[0]] + self.frequencies[bottom_2[1]], left, right)
        self.remove_entries_from_huffman(bottom_2)
        return huffman_tree_head

    def huff_1(self, huffman_tree_head):
        while huffman_tree_head.value < self.maximum(list(self.frequencies.keys()))[0]:
            bottom_1 = self.find_bottom_n(1)
            huffman_tree_head = \
                Node(huffman_tree_head.value + self.frequencies[bottom_1[0]],
                     Node(bottom_1[0], None, None), huffman_tree_head)
            self.remove_entries_from_huffman(bottom_1)
        return huffman_tree_head

    def encode_huffman_tree_r(self, node, d, val=''):
        if node.right is None and node.left is None:
            d[node.value] = val

        if node.left is not None:
            self.encode_huffman_tree_r(node.left, d, val + '0')

        if node.right is not None:
            self.encode_huffman_tree_r(node.right, d, val + '1')

        return d

    def construct_huffman_tree(self):
        hs = []
        while len(self.frequencies.keys()) != 1:
            h_ = self.huff_2()
            h = self.huff_1(h_)
            hs.append(h)

        smallest_subtree = find_smallest_subtree(hs)
        hs.remove(smallest_subtree)

        remainder_k = list(self.frequencies.keys())[0]
        remainder_v = self.frequencies[remainder_k]

        hs.append(Node(smallest_subtree.value + remainder_v, Node(remainder_k, None, None), smallest_subtree))

        ht = Node(0, None, None)
        for i in range(len(hs) - 1):
            ht = Node(hs[i].value + hs[i + 1].value, hs[i], hs[i + 1])

        return ht


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

