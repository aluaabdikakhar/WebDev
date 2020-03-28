def same_first_last(nums):
  for i in range(len(nums)):
    if(len(nums) == 0):
      return False
    elif(nums[0] == nums[len(nums) - 1]):
      return True
    else:
      return False
