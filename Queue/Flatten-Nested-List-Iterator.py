# 341

# You are given a nested list of integers nestedList. Each element is either an integer or a list 
# whose elements may also be integers or other lists. Implement an iterator to flatten it.

# Implement the NestedIterator class:

# NestedIterator(List<NestedInteger> nestedList) Initializes the iterator with the nested list nestedList.
# int next() Returns the next integer in the nested list.
# boolean hasNext() Returns true if there are still some integers in the nested list and false otherwise.
# Your code will be tested with the following pseudocode:

# initialize iterator with nestedList
# res = []
# while iterator.hasNext()
#     append iterator.next() to the end of res
# return res
# If res matches the expected flattened list, then your code will be judged as correct.

import collections

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.deq = collections.deque(nestedList)

    def FixDeque(self):
        last = self.deq.popleft()
        for e in last.getList()[::-1]:
            self.deq.appendleft(e)    
    
    def next(self) -> int:
        first = self.deq[0]
        if first.isInteger():
            self.deq.popleft()
            return first.getInteger()
        else:
            self.FixDeque()
            return self.next()
        
    def hasNext(self) -> bool:
        while self.deq and not self.deq[0].isInteger():
            self.FixDeque()
        return self.deq