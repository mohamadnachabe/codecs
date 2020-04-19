import sys
from heap import MinHeap


def get_frequencies(text):
    frequencies = {}
    for i in text:
        if i in frequencies:
            frequencies[i] = frequencies[i] + 1
        else:
            frequencies[i] = 1

    return frequencies


def encode(text, coding):
    output = ''
    for i in text:
        output += coding[i]
    return output


def decode(encoded, coding):
    buffer = ''
    output = ''
    for i in encoded:
        buffer += i
        if buffer in coding:
            output += coding[buffer]
            buffer = ''

    return output


class HuffmanEncoder:
    frequencies = {}

    def __init__(self, frequencies):
        self.frequencies = frequencies
        self.nodes = MinHeap()

    def to_nodes(self):
        for i in self.frequencies.keys():
            self.nodes.insert(Node(self.frequencies[i], None, None, i))

    def generate_coding(self):
        d = {}
        e = {}
        tree = self.construct_huffman_tree()
        self.encode_huffman_tree_r(tree, d, e)
        return d, e

    def encode_huffman_tree_r(self, node, d, e, val=''):
        if node.right is None and node.left is None:
            d[node.character] = val
            e[val] = node.character

        if node.left is not None:
            self.encode_huffman_tree_r(node.left, d, e, val + '0')

        if node.right is not None:
            self.encode_huffman_tree_r(node.right, d, e, val + '1')

        return d, e

    def construct_huffman_tree(self):
        self.to_nodes()

        t = Node(0)
        while self.nodes.length() != 1:

            left = self.nodes.pop()
            right = self.nodes.pop()

            if right.character is not None and left.character is None:
                t = Node(left.value + right.value, right, left)
            else:
                t = Node(left.value + right.value, left, right)

            self.nodes.insert(t)

        return t


class Node:
    def __init__(self, value, left=None, right=None, character=None):
        self.value = value
        self.character = character
        self.left = left
        self.right = right

    def __lt__(self, other):
        if self.value == other.value and self.character is not None and other.character is not None:
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


def main():
    command = sys.argv[1]

    if command == 'encode' or command == 'e':
        input_text = sys.argv[2]
        character_frequencies = get_frequencies(input_text)
        huffman_encoder = HuffmanEncoder(character_frequencies)
        coding_dict, decoding_dict = huffman_encoder.generate_coding()

        encoded_text = encode(input_text, coding_dict)
        print(encoded_text)

    elif command == 'table' or command == 't':
        input_text = sys.argv[2]
        character_frequencies = get_frequencies(input_text)
        huffman_encoder = HuffmanEncoder(character_frequencies)
        coding_dict, decoding_dict = huffman_encoder.generate_coding()
        print(str(coding_dict))


if __name__ == '__main__':
    main()
