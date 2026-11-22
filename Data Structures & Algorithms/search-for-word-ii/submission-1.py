class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None  # Stores the word when a complete word end is reached

class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        # 1. Build the Trie
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = word

        rows, cols = len(board), len(board[0])
        result = []

        # 2. Backtracking DFS
        def dfs(r, c, parent):
            char = board[r][c]
            curr_node = parent[char]

            # Check if a word is found
            if curr_node.word:
                result.append(curr_node.word)
                curr_node.word = None  # Prevent duplicate entries in result

            # Mark cell as visited
            board[r][c] = '#'

            # Explore all 4 directions
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] in curr_node.children:
                    dfs(nr, nc, curr_node)

            # Restore cell (backtrack)
            board[r][c] = char

            # Optimization: Prune leaf nodes to speed up search
            if not curr_node.children:
                parent.pop(char)

        # 3. Traversal from each cell
        for r in range(rows):
            for c in range(cols):
                if board[r][c] in root.children:
                    dfs(r, c, root)

        return result