import collections
class Input:
    def __init__(self,fileName):
        self.file = open(fileName)
        
    def getString(self):
        chars = []
        for string in self.file:
            for char in string:
                chars.append(char)
        return chars
    
    def constructProbability(self):
        #used to count occurancies of an element in a list
        freq = collections.Counter(self.getString())

        #calculating the probability array
        for char in freq:
            freq[char] = freq[char]/len(freq)
        return freq
