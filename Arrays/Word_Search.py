"""
LeetCode Problem “Word Search” (https://leetcode.com/problems/word-search/)

Given an m×n board of characters and a string word, return True if word exists in the board.
The word must be constructed from letters of sequentially adjacent cells (horizontally or vertically)
without revisiting the same cell.

Time Complexity: O(m·n·4^L), where L = len(word)  
Space Complexity: O(L) for the recursion stack (or explicit stack)
"""

from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        :param board: List[List[str]] – 2D grid of characters
        :param word: str – the target word to search for
        :return: bool – True if the word exists in the grid, False otherwise

        Approach:
        - Use an explicit stack to perform DFS from each cell matching word[0].
        - Track the path in `stack` and which neighbors have been tried for each position
          in `visited_moves` to enable backtracking.
        """
        m = len(board)       # number of rows
        n = len(board[0])    # number of columns

        # Try each cell as the starting point
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    stack = [(i, j)]               # path of coordinates matching word prefix
                    visited_moves = {(i, j): []}  # which neighbors we've attempted for each cell

                    # DFS until path length equals word length or no moves left
                    while stack:
                        # full match found
                        if len(stack) == len(word):
                            return True

                        temp = stack[-1]               # current cell
                        w_ind = len(stack) - 1         # index in word matched so far
                        next_char = word[w_ind + 1]    # next character to match

                        # Up
                        if (temp[0] - 1 >= 0
                            and board[temp[0] - 1][temp[1]] == next_char
                            and (temp[0] - 1, temp[1]) not in visited_moves[temp]
                            and (temp[0] - 1, temp[1]) not in visited_moves):
                            visited_moves[temp].append((temp[0] - 1, temp[1]))
                            stack.append((temp[0] - 1, temp[1]))
                            visited_moves[(temp[0] - 1, temp[1])] = []

                        # Left
                        elif (temp[1] - 1 >= 0
                              and board[temp[0]][temp[1] - 1] == next_char
                              and (temp[0], temp[1] - 1) not in visited_moves[temp]
                              and (temp[0], temp[1] - 1) not in visited_moves):
                            visited_moves[temp].append((temp[0], temp[1] - 1))
                            stack.append((temp[0], temp[1] - 1))
                            visited_moves[(temp[0], temp[1] - 1)] = []

                        # Down
                        elif (temp[0] + 1 < m
                              and board[temp[0] + 1][temp[1]] == next_char
                              and (temp[0] + 1, temp[1]) not in visited_moves[temp]
                              and (temp[0] + 1, temp[1]) not in visited_moves):
                            visited_moves[temp].append((temp[0] + 1, temp[1]))
                            stack.append((temp[0] + 1, temp[1]))
                            visited_moves[(temp[0] + 1, temp[1])] = []

                        # Right
                        elif (temp[1] + 1 < n
                              and board[temp[0]][temp[1] + 1] == next_char
                              and (temp[0], temp[1] + 1) not in visited_moves[temp]
                              and (temp[0], temp[1] + 1) not in visited_moves):
                            visited_moves[temp].append((temp[0], temp[1] + 1))
                            stack.append((temp[0], temp[1] + 1))
                            visited_moves[(temp[0], temp[1] + 1)] = []

                        else:
                            # No valid moves from current cell → backtrack
                            popped = stack.pop()
                            del visited_moves[popped]

        # no path matched the word
        return False
