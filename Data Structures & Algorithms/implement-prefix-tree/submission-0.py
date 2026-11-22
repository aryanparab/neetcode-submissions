class Node:
    def __init__(self,val=""):
        self.val = val
        self.next = {}
class PrefixTree:

    def __init__(self):
        self.hm = set()

    def insert(self, word: str) -> None:
        self.hm.add(word)
        return None

    def search(self, word: str) -> bool:
        if word in self.hm:
            return True
        return False


    def startsWith(self, prefix: str) -> bool:
        ll = len(prefix)
        for i in self.hm:
            if i[:ll] == prefix:return True
        return False
        
        