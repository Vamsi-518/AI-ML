###                                 ****DAY_ONE****
"""
x = 20
y = int(input("Enter a number"))
y = int(input("Enter anumber:"))
print(x+y)

"""
"""
#find 3 nummber to comparee
print("Enter 3 nummber to comparee")
x = int(input("First number"))
y = int(input("Second number"))
z = int(input("Third number"))
if(x>y and x>z):
      print(x,"is the highest number")
elif(y>z and y>x):
    print(y,"is the highest number")
else:
    print(z,"has the highest value")
"""
"""
#normal if -else
# if the first value is greater and is greater than 150 add 10 to the value

x= 100
y= 200
if(x>y):
    print(x, " is greater")
    if(x>150):
        x=x+10
        print("Enhanced x: ",x)
else:
    print(y, " is greater")
"""
                   ####Day 1 Mock Test: Arrays & Hashing (Infosys Style)####

#Contains Duplicate
#Missing Number
#Given an array and a target, return indices of two numbers that add up to the target.
#Majority Element
#Best Time to Buy and Sell Stock
"""
def containsDuplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
print(containsDuplicate([1,2,3,1]))
"""
#
"""
def missingNumber(nums):
    n = len(nums)
    expected = n * (n + 1) // 2
    actual = sum(nums)
    return expected - actual
print(missingNumber([3,0,1]))
"""
#
"""
def twoSum(nums, target):
    mp = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in mp:
            return [mp[diff], i]
        mp[num] = i
print(twoSum([2,7,11,15], 9))
"""
#
"""
def majorityElement(nums):
    candidate = None
    count = 0
    for num in nums:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1
    return candidate
print(majorityElement([2,2,1,1,1,2,2]))
"""
#
"""
def majorityElement(nums):
    candidate = None
    count = 0
    for num in nums:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1
    return candidate
print(majorityElement([2,2,1,1,1,2,2]))
"""
