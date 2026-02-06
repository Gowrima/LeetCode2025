# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        The result is undefined if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        The result is undefined if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """


class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        """
        list = read through the list until there is an integer,

        [1, [1, 2], [[1]]]
        1 = depth 1
        1 = depth 2
        1 = depth 3

        depth = 1 * 1 = 1
        cur_depth = 1

        cur_depth += 1

        if item is an int:
            return item * curDepth

        for item in nestedList:
            if item is int:
                sum_ = item * curDepth
            else:
                sum_ = depthSum(item, curDepth)

        return sum_

        case 1: [-100, 1,2,3,4,5........100]
        case 2: [[[[[[[[[[[[[[[[[1]]]]]]]]]]]]]]]]]
        """
        # [5, [6]]
        def helper(nestedlist, depth, cur_sum):  # [6], 2, 5
            # print(type(nestedlist))
            for elem in nestedlist:  # [6]
                if elem.isInteger():
                    cur_sum += depth * elem.getInteger()  # cursum = 5
                else:
                    cur_sum = helper(elem.getList(), depth + 1, cur_sum)  # [6], 1+1=2, 5

            return cur_sum  # 22

        return helper(nestedList, 1, 0)
