from huffman_tree import HuffmanTree

def construct_probability(input_string):
    freq = {}
    for char in input_string:
        if char not in freq:
            freq[char] = 1
        else:
            freq[char] += 1
    return freq


input_string = open("input.txt", "r").read()
probability = construct_probability(input_string)
encoding_array = {}
if len(probability) == 1:
    encoding_array.update({list(probability)[0]:'0'})
else:
    tree = HuffmanTree()
    tree.get_nodes_heap(probability)
    tree.construct_tree()
    encoding_array = tree.get_codes()

# Encode
output_string = ""
for char in input_string:
    output_string += encoding_array[char]
ouput = open('binary_output.bin', 'w')
ouput.write(output_string)
ouput.close()


# Decode
decoder = {}
for key in encoding_array:
    decoder[encoding_array[key]] = key
encoded_input = open('binary_output.bin', 'r').read()
t = ""
decoded_text = ""
for i in range(len(encoded_input)):
    t += str(encoded_input[i])
    if t in decoder:
        decoded_text += decoder[t]
        t = ""
decoded_file = open('decoded_output.out', 'w')
decoded_file.write(decoded_text)
decoded_file.close()
