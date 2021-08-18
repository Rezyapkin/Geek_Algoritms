'''
Задание 2.
Закодируйте любую строку из трех слов по алгоритму Хаффмана.
'''

from collections import Counter


class Node:
    def __init__(self, letter = None, left_child=None, right_child=None):
        self.letter = letter
        self.left_child = left_child
        self.right_child = right_child


class HuffmanTree:

    @staticmethod
    def _get_node(node_or_str):
        return node_or_str if isinstance(node_or_str, Node) else Node(node_or_str)

    def fill_code_letters(self, node, code=''):
        if node is None:
            return
        if node.letter is not None:
            self.letters[node.letter] = code
        self.fill_code_letters(node.left_child, code + '0')
        self.fill_code_letters(node.right_child, code + '1')

    def __init__(self, message):
        self.message = message
        cnt = Counter(message)
        self.root = Node(None)
        while len(cnt) > 1:
            mins = cnt.most_common()[:-3:-1]
            cnt[Node(None, self._get_node(mins[0][0]), self._get_node(mins[1][0]))] = mins[0][1] + mins[1][1]
            del cnt[mins[0][0]]
            del cnt[mins[1][0]]

        first = cnt.most_common(1)
        self.root = Node(None) if len(first) == 0 or not isinstance(first[0][0], Node) else first[0][0]
        if len(first) > 0 and not isinstance(first[0][0], Node):
            self.root.left_child = Node(first[0][0])

        self.letters = {}
        self.fill_code_letters(self.root)

    def get_code(self, string):
        code = ''
        for letter in string:
            if letter not in self.letters:
                raise ValueError('Строка содержит недопустимый символ')
            code += self.letters[letter]
        return code

    def decode(self, code):
        result = ''
        node = self.root
        for letter in code:
            if letter not in ['0', '1']:
                raise ValueError('Код может содержать только нули и единицы')
            node = node.left_child if letter == '0' else node.right_child
            if node.letter is not None:
                result += node.letter
                node = self.root

        return result


tree = HuffmanTree('Hello my friends')
print(tree.get_code('Hi'))
print(tree.decode(tree.get_code('Hiiii')))







