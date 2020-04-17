def find_smallest_subtree(trees):
    smallest = trees[0]
    for i in range(1, len(trees)):
        if trees[i].value < smallest.value:
            smallest = trees[i]

    return smallest


class HuffmanEncoder:
    frequencies = {}
    nodes = [] # todo use a priority queue instead

    def __init__(self, frequencies):
        self.frequencies = frequencies

    def to_nodes(self):
        self.nodes = []
        for i in self.frequencies.keys():
            self.nodes.append(Node(self.frequencies[i], None, None, i))

    def encode(self):
        d = {}
        tree = self.construct_huffman_tree_2()
        self.encode_huffman_tree_r(tree, d)
        return d

    def encode_huffman_tree_r(self, node, d, val=''):
        if node.right is None and node.left is None:
            d[node.character] = val

        if node.left is not None:
            self.encode_huffman_tree_r(node.left, d, val + '0')

        if node.right is not None:
            self.encode_huffman_tree_r(node.right, d, val + '1')

        return d

    def construct_huffman_tree_2(self):
        self.to_nodes()

        t = Node(0)
        while len(self.nodes) != 1:
            self.nodes = sorted(self.nodes)

            left = self.nodes[0]
            right = self.nodes[1]

            if right.character is not None and left.character is None:
                t = Node(left.value + right.value, right, left)
            else:
                t = Node(left.value + right.value, left, right)

            self.nodes.remove(left)
            self.nodes.remove(right)
            self.nodes.append(t)

        return t


class Node:
    def __init__(self, value, left=None, right=None, character=None):
        self.value = value
        self.character = character
        self.left = left
        self.right = right

    def __lt__(self, other):
        if self.value == other.value and self.character is not None and other.value is not None:
            return ord(self.character) < ord(other.character)
        else:
            return self.value < other.value

    def __eq__(self, other):
        return self.value == other.value

    def __str__(self):
        if self.character is not None:
            return self.character + self.value
        else:
            return self.value