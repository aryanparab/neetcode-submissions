class Node:
    def __init__(self,val=""):
        self.val = val
        self.next = {}
class PrefixTree:

    def __init__(self):
        self.start = Node()

    def insert(self, word: str) -> None:
        current= self.start
        for i in range(len(word)):
            if word[i] not in current.next:
                current.next[word[i]] = Node(word[i])
            current = current.next[word[i]]
        current.next["/0"]=Node()
    def search(self, word: str) -> bool:
        current = self.start
        for i in range(len(word)):
            if word[i] not in current.next:return False
            current = current.next[word[i]]
        if "/0" not in current.next:return False
        return True
    def startsWith(self, word: str) -> bool:
        current = self.start
        for i in range(len(word)):
            if word[i] not in current.next:return False
            current = current.next[word[i]]
        return True
        