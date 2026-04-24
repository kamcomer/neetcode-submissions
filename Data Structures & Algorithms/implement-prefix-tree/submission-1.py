class TrieNode:
    def __init__(self, val, next):
        self.is_end = val
        self.next = {}


class PrefixTree:
    def __init__(self):
        self.root = TrieNode(True, {})

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.next:
                node.next[c] = TrieNode(False, {})
            node = node.next[c]
        node.is_end = True
        
    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            if c not in node.next:
                return False
            node = node.next[c]

        if not node.is_end:
            return False
        return True

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            if c not in node.next:
                return False
            node = node.next[c]

        return True
