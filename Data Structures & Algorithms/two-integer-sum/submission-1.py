class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash={}
        for i,num in enumerate(nums):
            compliment=target-num
            if compliment in hash:
                return [hash[compliment],i]
            hash[num]=i

        