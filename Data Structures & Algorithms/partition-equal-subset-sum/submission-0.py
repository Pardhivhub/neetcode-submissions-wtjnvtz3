class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total=sum(nums)
        if  total%2!=0:
            return False
        target=total//2
        dp={}
        def subset(i,target):
            if target==0:
                return True
            if i<0:
                return False
            if (i,target) in dp:
                return dp[(i,target)]
            if nums[i]>target:
                dp[(i,target)]=subset(i-1,target)
            else:
                take=subset(i-1,target-nums[i])
                not_take=subset(i-1,target)
                dp[(i,target)]=take or not_take
            return dp[(i,target)]
        return subset(len(nums)-1,target)

        