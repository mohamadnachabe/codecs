import unittest

from huffman import HuffmanEncoder


class MyTestCase(unittest.TestCase):
    def test_something(self):
        frequencies = {'A': 10,
                       'E': 15,
                       'I': 12,
                       'S': 3,
                       'T': 4,
                       'P': 13,
                       '\\n': 1}

        expected = {'I': '00', 'P': '01', 'E': '10', 'A': '110', 'T': '1110', '\\n': '11110', 'S': '11111'}

        encoder = HuffmanEncoder(frequencies)
        huffman_tree = encoder.construct_huffman_tree()

        huffman_encoding = {}
        encoder.encode_huffman_tree_r(huffman_tree, huffman_encoding)

        print(huffman_encoding)

        self.assertEqual(expected, huffman_encoding)


if __name__ == '__main__':
    unittest.main()
