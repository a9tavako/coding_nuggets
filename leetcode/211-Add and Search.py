from typing import Dict, Optional

class Node:

    def __init__(self, c: str = "", terminal: bool = False):
        self.kids: Dict[str, 'Node'] = {}
        self.val = c
        self.word_end = terminal


class WordDictionary:

    def __init__(self):
        self.root = Node("*")
        

    def addWord(self, word: str) -> None:
        current = self.root
        n = len(word)
        for index, c in enumerate(word):
            is_end = (index == n-1)
            if c not in current.kids:
                new_node = Node(c, is_end)
                current.kids[c] = new_node
                current = new_node
                continue
            if is_end:
                current.kids[c].word_end = True
            current = current.kids[c]
            
    def search(self, word: str) -> bool:
        current_level = [self.root]
        for index, c in enumerate(word):
            if not current_level:
                return False
            next_level = []
            if c != ".":
                for node in current_level:
                    if c in node.kids:
                        next_level.append(node.kids[c])
            else:
                for node in current_level:
                    for c in node.kids:
                        next_level.append(node.kids[c])

            current_level = next_level

        return any(node.word_end for node in current_level)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)