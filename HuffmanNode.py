__author__ = 'arsia'

# huffman node can be a letter, or have no value at all and just be a node
# huffman node MUST have a frequency (int)
# huffman node MUST have a left and right child pointer, but it's possible for both to be None if it's a leaf
# if one child is None, both must be None, because you can't have a letter under another letter
class HuffmanNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None
