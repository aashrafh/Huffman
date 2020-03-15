from ReadInput import Input as I
from huffman_tree import HuffmanTree


def constructProbability(fileName):
    text = open(fileName, "r").read()
    freq = {}
    for char in text:
        if char not in freq:
            freq[char] = 1
        else:
            freq[char] = freq[char] + 1
    return freq


Input = I()
probability = constructProbability("input.txt")
tree = HuffmanTree()
tree.get_nodes_heap(probability)
tree.construct_tree()
code = tree.get_codes()
print(probability)
print(code)
