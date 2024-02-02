class Solution:
  target = None
  target_count = 0

  def removeDuplicates(self, nums: list[int]) -> int:
    nums[:] = [num for num in nums if self.evaluateTarget(num) == True]

    return len(nums)
  
  def evaluateTarget(self, new: int) -> bool:
    if self.target is None:
      self.target = new
      self.target_count = 1
      return True
    elif self.target != new:
      self.target = new
      self.target_count = 1
      return True
    elif self.target == new and self.target_count < 2:
      self.target_count+=1
      return True
    else:
      return False
    

nums=[0,0,1,1,1,1,2,3,3]
number_of_unique_elements = Solution().removeDuplicates(
  nums=nums
)

print(nums)
print(number_of_unique_elements)
    
