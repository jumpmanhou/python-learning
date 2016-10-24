class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        
        self.dfs(nums,3,0,0,[],res)
        
        return res
        
    def dfs(self,nums,k,target,index,path,res):
        if k<0:
            return 
        if k==0 and target ==0:
            res.append(path)
            
        for i in range(index,len(nums)):
        
            if i > index and nums[i]==nums[i-1]:
                continue
            
            self.dfs(nums,k-1,target-nums[i],i+1,path+[nums[i]],res)

s = Solution()
print(s.threeSum([-1, 0, 1, 2, -1, -4]))