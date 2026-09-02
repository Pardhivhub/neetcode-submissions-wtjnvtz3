class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        def house_rob(nums):
            prev2=0
            prev1=0
            for money in nums:
                take=money+prev2
                skip=prev1
                curr=max(skip,take)
                prev2=prev1
                prev1=curr
            return prev1
        case1=house_rob(nums[1:])
        case2=house_rob(nums[:-1])
        return max(case1,case2)
        