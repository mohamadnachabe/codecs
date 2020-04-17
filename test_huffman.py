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

        expected_encoding = {'I': '00',
                             'P': '01',
                             'E': '10',
                             'A': '110',
                             'T': '1110',
                             '\\n': '11110',
                             'S': '11111'}

        huffman_encoder = HuffmanEncoder(frequencies)
        huffman_encoding = huffman_encoder.encode()

        print(huffman_encoding)

        self.assertEqual(expected_encoding, huffman_encoding)


if __name__ == '__main__':
    unittest.main()
