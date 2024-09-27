class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    """
    Prefix Tree

    Stores strings as paths in a tree, where each node represents a character.
    Shared prefixes are merged, saving space. Enables O(m) operations for
    insertion, search, and prefix matching, where m is string length.
    """

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        """Insert a word into the trie."""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search(self, prefix: str):
        """Search for all words with a given prefix."""
        # Traverse to the node representing the end of the prefix
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        # Return all words with the given prefix 
        return self._dfs(node, prefix)

    def _dfs(self, node: TrieNode, prefix: str):
        results = []
        if node.is_end:
            results.append(prefix)
        for char, child in node.children.items():
            results.extend(self._dfs(child, prefix + char))
        return results
