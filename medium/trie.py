LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

class TrieNode:
    def __init__(self, letter: str, is_word: bool = False) -> None:
        self.letter = letter
        self.next_letters = {}
        self.is_word = is_word


class Trie:

    def __init__(self):
        self.root = TrieNode('~', False)
        
    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char in node.next_letters:
                node = node.next_letters[char]
            else:
                node.next_letters[char] = TrieNode(char)
                node = node.next_letters[char]
        node.is_word = True

    def search_pre(self, word: str) -> bool:
        node = self.root
        for letter in word:
            if letter in node.next_letters:
                node = node.next_letters[letter]
            else:
                return None
        return node
    
    def search(self, word: str) -> bool:
        search_node = self.search_pre(word)
        if search_node.is_word:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        if self.search_pre(prefix):
            return True
        else:
            return False


# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert('apple')
print(obj.search('apple'))
print(obj.startsWith('apz'))
# print(obj.root.letter)
# print(obj.root.next_letters['a'].letter)
# print(obj.root.next_letters['a'].next_letters['p'].letter)
# print(obj.root.next_letters['a'].next_letters['p'].next_letters['p'].letter)
# print(obj.root.next_letters['a'].next_letters['p'].next_letters['p'].next_letters['l'].letter)

# param_2 = obj.search('apple')
# param_3 = obj.startsWith('app')

