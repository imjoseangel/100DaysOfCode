#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)


def canConstruct(target: str, wordBank: list) -> bool:

    table = [False] * (len(target) + 1)
    table[0] = True

    i = 0
    while i <= len(target):
        try:
            if table[i] is True:
                for word in wordBank:
                    if target[i: i + len(word)] == word:
                        table[i + len(word)] = True
        except IndexError:
            pass
        i += 1

    return table[len(target)]


def main():
    print(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))  # True
    print(canConstruct("skateboard", [
          "bo", "rd", "ate", "t", "ska", "sk", "boar"]))  # False
    print(canConstruct("enterapotentpot", [
          "a", "p", "ent", "enter", "ot", "o", "t"]))  # True
    print(canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
                       ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"]))  # False


if __name__ == '__main__':
    main()
