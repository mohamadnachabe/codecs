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
        huffman_encoding, huffman_decoding = huffman_encoder.generate_coding()

        print(huffman_encoding)

        self.assertEqual(expected_encoding, huffman_encoding)

    def test_something_2(self):
        frequencies = {'C': 2,
                       'B': 6,
                       'E': 7,
                       '_': 10,
                       'D': 10,
                       'A': 11}

        huffman_encoder = HuffmanEncoder(frequencies)
        huffman_encoding, huffman_decoding = huffman_encoder.generate_coding()

        print(huffman_encoding)

        # self.assertEqual(expected_encoding, huffman_encoding)


if __name__ == '__main__':
    unittest.main()
