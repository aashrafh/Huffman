from ReadInput import Input as I
from huffman_tree import HuffmanTree 
def recurse (Node,code = ''):
    if Node.symbol != None:
        encodingArray[Node.symbol] = code
        return
    recurse(Node.left,code+'0')
    recurse(Node.right,code+'1')
    
    
Input = I()
probability = Input.constructProbability('input.txt')
tree = HuffmanTree()
tree.get_nodes_heap(probability)
tree.construct_tree()
firstNode = tree.heap[0]
encodingArray = probability.copy()
recurse(firstNode)
print(probability)
print(encodingArray)