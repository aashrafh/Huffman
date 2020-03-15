from ReadInput import Input as I
from huffman_tree import HuffmanTree 

def recurse (Node,code = ''):
    if Node.symbol != None:
        encodingArray[Node.symbol] = code
        return
    recurse(Node.right,code + '1')
    recurse(Node.left,code + '0')
    
    
    
Input = I('input.txt')
Input2 = I('input.txt')
probability = Input.constructProbability()
encodingArray = probability.copy()
tree = HuffmanTree()
tree.get_nodes_heap(probability)
tree.construct_tree()
firstNode = tree.heap[0]
inputString = Input2.getString()
if len(probability) == 1:
    recurse(firstNode,'0')
else:
     recurse(firstNode)
outputString = ''

print(encodingArray)

for char in inputString:
    outputString += encodingArray[char]

ouput = open ('output.txt','w+')
ouput.write(outputString)
ouput.close()
