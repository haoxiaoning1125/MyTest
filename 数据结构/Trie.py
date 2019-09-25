# coding=utf-8
# trie树


class Trie:
    def __init__(self):
        self.root = dict()

    def insert(self, word):
        node = self.root
        for s in word:
            if s in node.keys():
                node = node[s]
            else:
                node[s] = dict()
                node = node[s]
        node['is_word'] = True

    def search(self, word):
        node = self.root
        for s in word:
            if s in node.keys():
                node = node[s]
            else:
                return False
        if 'is_word' in node.keys():
            return True
        else:
            return False

    def starts_with(self, prefix):
        node = self.root
        for s in prefix:
            if s in node.keys():
                node = node[s]
            else:
                return False
        return True

    def find_tips(self, prefix):
        node = self.root
        for s in prefix:
            if s in node.keys():
                node = node[s]
            else:
                return False
            tips = []
            self.loop_find_tips(node, prefix, tips)
            return tips

    def loop_find_tips(self, node, prefix, tips):
        if 'is_word' in node and node['is_word']:
            tips.append(prefix)
            return
        for s in node.keys():
            self.loop_find_tips(node[s], prefix + s, tips)


if __name__ == '__main__':
    trie = Trie()
    trie.insert('Python')
    trie.insert('C')
    trie.insert('Java')
    trie.insert('PHP')
    trie.insert('Ruby')
    trie.insert('Golang')
    for i in trie.find_tips('P'):
        print i
    # print trie.root
