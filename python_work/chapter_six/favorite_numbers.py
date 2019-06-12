# Defines dictionary of people's favorite numbers
nums = {
    'mitch': [8, 2, 14],
    'shannon': [8, 69, 420],
    'ashton': [24, 360, 44],
    'wiese': [12, 12, 12, 1, 2],
    'val': [6]
    }

# Prints a statement containing person's name and favorite numbers.
# Loops to include everybody in the dictionary.
# If the amount of favorite numbers is 1, it is gramatically correct.
for name, numbers in nums.items():
    if len(numbers) < 2:
        print("\n" + name.title() + "'s favorite number is: ")
    else:
        print("\n" + name.title() + "'s favorite numbers are: ")
    for number in numbers:
        print(" " + str(number))

# Below lines are an older version.

# print([key for key in nums.keys()][0].title() + 
    # "'s favorite numbers are " + str(nums['mitch']))
    
# print([key for key in nums.keys()][1].title() + 
    # "'s favorite numbers are " + str(nums['shannon']))
    
# print([key for key in nums.keys()][2].title() + 
    # "'s favorite numbers are " + str(nums['ashton']))
    
# print([key for key in nums.keys()][3].title() + 
    # "'s favorite number is " + str(nums['wiese']))
    
# print([key for key in nums.keys()][4].title() + 
    # "'s favorite number is " + str(nums['val']))
