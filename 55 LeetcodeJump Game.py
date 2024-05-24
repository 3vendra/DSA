def canJumpRecursion(self, nums: List[int]) -> bool:
  """using recusion Output will be time limit exceed"""
    lastindex=len(nums)-1
    index=0
    def recursion(nums,index):
        if(index==lastindex):
            return True
        if nums[index] == 0:
            return False
        
        for i in range(0,nums[index]):
            if recursion(nums, index + i+1):
                return True
        return False
    return recursion(nums, 0)

canJumpRecursion([2,3,1,1,4])


