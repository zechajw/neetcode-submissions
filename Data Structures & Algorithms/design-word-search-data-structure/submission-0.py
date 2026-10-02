class WordDictionary:

    def __init__(self):
        self.children = [None] * 26
        self.ends_here = False

    def addWord(self, word: str) -> None:
        curr = self
        for c in word:
            char_index = ord(c) - ord('a')
            if not curr.children[char_index]:
                curr.children[char_index] = WordDictionary()
            curr = curr.children[char_index]
        curr.ends_here = True

    def search(self, word: str) -> bool:
        def dfs(node: WordDictionary, index: int) -> bool:
            if index >= len(word):
                return node.ends_here

            if word[index] == ".":
                for child in node.children:
                    if child and dfs(child, index + 1):
                        return True
                return False
            else:
                char_index = ord(word[index]) - ord('a')
                child = node.children[char_index]
                return child is not None and dfs(child, index + 1)

        
        return dfs(self, 0)