class PrefixTree:

    def __init__(self):
        self.children = [None] * 26
        self.endsHere = False

    def insert(self, word: str) -> None:
        curr = self
        for c in word:
            if not curr.children[ord(c) - ord('a')]:
                curr.children[ord(c) - ord('a')] = PrefixTree()
            curr = curr.children[ord(c) - ord('a')]

        curr.endsHere = True
        return

    def search(self, word: str) -> bool:
        curr = self
        for c in word:
            char_index = ord(c) - ord('a')
            if not curr.children[char_index]:
                return False
            curr = curr.children[char_index]
        return curr.endsHere

    def startsWith(self, prefix: str) -> bool:
        curr = self
        for c in prefix:
            char_index = ord(c) - ord('a')
            if not curr.children[char_index]:
                return False
            curr = curr.children[char_index]
        return True

# insert apple
# curr = self
# self.children[0] = None, initialize, curr = self.children[0]
# self.children[p - a] = None, initialize, curr = self.children[p - a]
# self.children[p - a] = None, initialize, curr = self.children[p - a]
# self.children[l - a] = None, initialize, curr = self.children[l - a]
# self.children[e - a] = None, initialize, curr = self.children[e - a]
# currently on self.children[e - a], curr.endsHere = True

# search apple
# curr = self
# self.children[a] exists, curr = self.children[a]
# self.children[p] exists, curr = self.children[p]

        