from collections import defaultdict
from itertools import product

# Defintion of the trie tree
class Trie:
    def __init__(self):

        # Initialize a dict to store all child trie nodes
        self.children = defaultdict(lambda: Trie())

        # A flag to mark if the current node is the end of a word
        self.isWord = False

    def add(self, word):

        # Initialize the current node
        node = self

        # Iterate through all characters in a word 
        for c in word:

            # Go to the next node
            node = node.children[c]

        # Mark the last node as the end of a word
        node.isWord = True


class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:

        # Initialize a trie and add all words into it
        trie = Trie()
        for word in words:
            trie.add(word)

        # Find length of rows and cols
        m, n = len(board), len(board[0])

        # Initialize sets of result and visited nodes
        res, visited = set(), set()

        # A helper function for directional movement
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # DFS through the trie tree
        def dfs(row, col, word, node, pNode):

            # If the current node is out of bound or it is already visited or the character isn't in the trie tree, end the search
            if (
                not (0 <= row < m)
                or not (0 <= col < n)
                or (row, col) in visited
                or board[row][col] not in node.children
            ):
                return

            # Update the current node and parent node
            node, pNode = node.children[board[row][col]], node

            # Add the current character onto the word
            word += board[row][col]

            # If we have reached the end of a word, add it into the result
            if node.isWord:
                res.add(word)

            # Mark the current node as visited
            visited.add((row, col))

            # Visit next nodes
            for dRow, dCol in directions:
                nRow, nCol = row + dRow, col + dCol
                dfs(nRow, nCol, word, node, pNode)

            # Unmark the current node as visited
            visited.remove((row, col))

            # Prune the trie tree and remove all visited node from the leaf
            if pNode and not node.children:
                pNode.children.pop(board[row][col])

        # Iterate through all entires in the board and use it as the starting node
        for row, col in product(range(m), range(n)):
            dfs(row, col, "", trie, None)

        return res