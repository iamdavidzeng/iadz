#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。

注意空字符串可被认为是有效字符串。
"""

from python_data_structure.stack import Stack


class MySolution(object):

    def __init__(self):
        self.a = Stack()
        self.b = Stack()

    def is_valid(self, s):
        """
        :param s: str
        :return: boolean
        """
        s = s.replace(' ', '')
        mid = len(s) / 2
        a_len = 0
        b_len = -1
        while a_len < mid:
            self.a.push(s[a_len])
            a_len += 1
        while abs(b_len) < mid + 1:
            self.b.push(s[b_len])
            b_len -= 1
        for i in range(len(self.a)):
            valid = self.a.pop() + self.b.pop()
            if valid not in ['{}', '()', '[]']:
                return False
        return True


class NewSolution(object):

    def is_valid(self, s):
        """

        :param s:
        :return:
        """
        stack = []
        mapping = {'}': '{', ']': '[', ')': '('}
        for i in s:
            if mapping.get(i, None):
                char = stack.pop() if stack else '#'
                if mapping[i] != char:
                    return False
            else:
                stack.append(i)
        return not stack


class Solution(object):

    def is_valid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # The stack to keep track of opening brackets.
        stack = []

        # Hash map for keeping track of mappings. This keeps the code very clean.
        # Also makes adding more types of parenthesis easier
        mapping = {")": "(", "}": "{", "]": "["}

        # For every bracket in the expression.
        for char in s:

            # If the character is an closing bracket
            if char in mapping:

                # Pop the topmost element from the stack, if it is non empty
                # Otherwise assign a dummy value of '#' to the top_element variable
                top_element = stack.pop() if stack else '#'

                # The mapping for the opening bracket in our hash and the top
                # element of the stack don't match, return False
                if mapping[char] != top_element:
                    return False
            else:
                # We have an opening bracket, simply push it onto the stack.
                stack.append(char)

        # In the end, if the stack is empty, then we have a valid expression.
        # The stack won't be empty for cases like ((()
        return not stack


if __name__ == '__main__':
    demo = NewSolution()
    if demo.is_valid('{}()[]'):
        print('success')
    else:
        print('fail')
