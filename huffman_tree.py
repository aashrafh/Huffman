import heapq


class Node:
    def __init__(self, symbol, probability):
        self.symbol = symbol
        self.probability = probability
        self.left = None
        self.right = None

    def __lt__(self, node):
        return self.probability < node.probability

    def __eq__(self, node):
        if(node == None):
            return False
        if(not isinstance(node, Node)):
            return False
        return self.probability == node.probability


class HuffmanTree:
    def __init__(self):
        self.heap = []
        self.encoding_array = {}

    def get_nodes_heap(self, freq_array):
        for key in freq_array:
            huffman_node = Node(key, freq_array[key])
            heapq.heappush(self.heap, huffman_node)

    def construct_tree(self):
        while(len(self.heap) > 1):
            first_huffman_node = heapq.heappop(self.heap)
            second_huffman_node = heapq.heappop(self.heap)
            both_node = Node(None, first_huffman_node.probability +
                             second_huffman_node.probability)
            both_node.left = first_huffman_node
            both_node.right = second_huffman_node
            heapq.heappush(self.heap, both_node)
        return self.heap

    def recurse(self, node, code=''):
        if node.symbol != None:
            self.encoding_array[node.symbol] = code
            return
        self.recurse(node.left, code+'0')
        self.recurse(node.right, code+'1')

    def get_codes(self):
        self.recurse(heapq.heappop(self.heap))
        return self.encoding_array
