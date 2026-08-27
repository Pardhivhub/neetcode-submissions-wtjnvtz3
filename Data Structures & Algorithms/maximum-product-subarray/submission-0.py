class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        current_max=nums[0]
        current_min=nums[0]
        answer=nums[0]
        for num in nums[1:]:
            old_max=current_max
            old_min=current_min
            current_max=max(num,old_max*num,old_min*num)
            current_min=min(num,old_max*num,old_min*num)
            answer=max(answer,current_max)
        return answer