class Node:
    def __init__(self, symbol, probability):
        self.symbol = symbol
        self.probability = probability
        self.left = None
        self.right = None

    def set_symbol(self, symbol):
        self.symbol = symbol

    def set_probability(self, probability):
        self.probability = probability

    def set_left(self, left):
        self.left = left

    def set_right(self, right):
        self.right = right

    def get_symbol(self):
        return self.symbol

    def get_probability(self):
        return self.probability

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right
