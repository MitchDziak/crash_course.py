nums = {
    'mitch': 8,
    'shannon': 8,
    'ashton': 24,
    'wiese': 12,
    'val': 6,
    }

print([key for key in nums.keys()][0].title() + 
    "'s favorite number is " + str(nums['mitch']))
    
print([key for key in nums.keys()][1].title() + 
    "'s favorite number is " + str(nums['shannon']))
    
print([key for key in nums.keys()][2].title() + 
    "'s favorite number is " + str(nums['ashton']))
    
print([key for key in nums.keys()][3].title() + 
    "'s favorite number is " + str(nums['wiese']))
    
print([key for key in nums.keys()][4].title() + 
    "'s favorite number is " + str(nums['val']))
