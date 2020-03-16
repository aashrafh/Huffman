from huffman_tree import HuffmanTree


def construct_probability(input_string):
    freq = {}
    for char in input_string:
        if char not in freq:
            freq[char] = 1
        else:
            freq[char] = freq[char]+1

    return freq


input_string = open("input.txt", "r").read()
probability = construct_probability(input_string)
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
decoded_output = ""
temp_str = ""
encoded_file = open("binary_output.bin", "rb")
char = encoded_file.read(1)
while char:
    temp_str = temp_str + str(char)
    if temp_str in encoding_array:
        print("temp_str")
        decoded_output = decoded_output + encoding_array[temp_str]
        temp_str = ""
    char = encoded_file.read(1)

print(decoded_output)
decoded_output_file = open('decoded_output.txt', 'w+')
decoded_output_file.write(decoded_output)
decoded_output_file.close()
