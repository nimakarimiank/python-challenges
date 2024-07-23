class Solution(object):
    from typing import List

    def twoSum( self, nums:List[int], target):
            """
            :type nums: List[int]
            :type target: int
            :rtype: List[int]
            """
            for i in range(len(nums)):
                    if i+1 < len(nums):
                            first = nums[i]
                            try:
                                    is_remainder = nums[i+1:].index(target - first)
                                    print(first)
                                    print(f"remainder is {target-first} ")
                                    if is_remainder != None:
                                            print("inside if")
                                            second_index = nums[i+1:].index(target - first)+i+1
                                            return [i, second_index]
                            except:
                                    print("index returned nothing")
                                    continue                
                            

                    