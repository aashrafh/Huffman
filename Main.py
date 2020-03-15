from ReadInput import Input as I
from huffman_tree import HuffmanTree
encodingArray = {}


def recurse(Node, code=''):
    if Node == None:
        return
    if Node.symbol != None:
        encodingArray[Node.symbol] = code
        return
    recurse(Node.left, code+'0')
    recurse(Node.right, code+'1')


Input = I()
probability = {
    'A': 5,
    'f': 1,
    'd': 3,
    ' ': 9,
    'a': 56
}  # Input.constructProbability('input.txt')
tree = HuffmanTree()
tree.get_nodes_heap(probability)
tree.construct_tree()
firstNode = tree.heap[0]
recurse(firstNode)
print(probability)
print(encodingArray)
