import collections
class Input:
    def constructProbability(self,fileName):
        file = open (fileName)
        numberOfChars = 0
        freq = []
        for string in file:
            for char in string:
                numberOfChars += 1
                freq.append(char)

        #used to count occurancies of an element in a list
        freq = collections.Counter(freq)

        #calculating the probability array
        for char in freq:
            freq[char] = freq[char]/numberOfChars
        return freq


#freq is the probability array