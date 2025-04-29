# 1773
# You are given an array items, where each items[i] = [typei, colori, namei] describes the type, color, and name of the 
# ith item. You are also given a rule represented by two strings, ruleKey and ruleValue.

# The ith item is said to match the rule if one of the following is true:

# ruleKey == "type" and ruleValue == typei.
# ruleKey == "color" and ruleValue == colori.
# ruleKey == "name" and ruleValue == namei.
# Return the number of items that match the given rule.


class Solution:
    def countMatches(self, items: list[list[str]], ruleKey: str, ruleValue: str) -> int:

        counter = 0
        if ruleKey == 'type':
            i = 0
        elif ruleKey == 'color':
            i = 1
        else: 
            i = 2

        for j in items:
            if j[i] == ruleValue:
                counter += 1

        return counter                    
  