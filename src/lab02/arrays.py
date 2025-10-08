def min_max(nums):
    if len(nums)!=0:
        if all(isinstance(x,(int,float)) for x in nums):
            min_nums=min(nums)
            max_nums=max(nums)
            return tuple([min_nums,max_nums])
    else:
        return 'ValueError'

def unique_sorted(nums):
    if all(isinstance(x,(int,float)) for x in nums):
        return list(sorted(set(nums)))

def flatten(nums):
    if all(isinstance(x,(list,tuple)) for x in nums):
        flatten_nums=[]
        for item in nums:
            flatten_nums.extend(item)
        return flatten_nums
    else:
        return 'TypeError'