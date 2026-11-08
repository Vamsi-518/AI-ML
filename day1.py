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
        ###Day 2 Mock Test (Strings & Recursion)###
#Given a string s, return True if it is a palindrome after converting all uppercase letters to lowercase and removing non-alphanumeric characters.
#Given two strings s and t, determine if t is an anagram of s
#Find the longest common prefix among an array of strings.
#Find the nth Fibonacci number using recursion.
#Return the first non-repeating character from a string.

def isPalindrome(s):
    cleaned = ""
    for ch in s:
        if ch.isalnum():
            cleaned += ch.lower()
    return cleaned == cleaned[::-1]
print(isPalindrome("A man, a plan, a canal: Panama"))

"""
from collections import Counter
def isAnagram(s, t):
    return Counter(s) == Counter(t)
print(isAnagram("listen", "silent"))
"""
"""
def longestCommonPrefix(strs):
    prefix = strs[0]
    for word in strs[1:]:
        while not word.startswith(prefix):
            prefix = prefix[:-1]
    return prefix
print(longestCommonPrefix(["flower","flow","flight"]))
"""
def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]
print(fibonacci(6))

from collections import Counter

def firstUnique(s):
    freq = Counter(s)
    for ch in s:
        if freq[ch] == 1:
            return ch
    return -1
print(firstUnique("swiss"))

             ###Day 3 Mock Test: Searching & Sorting

#Given a sorted array and a target element, return its index. If not found, return -1.
#Return the index if the target is found. Otherwise return the index where it would be inserted.
#A peak element is greater than its neighbors. Find any peak element index.
#Find the kth largest element in an array.
#Merge all overlapping intervals.

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
print(binary_search([1,3,5,7,9], 7))

def search_insert(nums, target):
    left, right = 0, len(nums)-1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left
print(search_insert([1,3,5,6], 2))


def findPeakElement(nums):
    left, right = 0, len(nums)-1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return left
print(findPeakElement([1,2,3,1]))


def findKthLargest(nums, k):
    nums.sort(reverse=True)
    return nums[k-1]
print(findKthLargest([3,2,1,5,6,4], 2))


def merge(intervals):
    intervals.sort()
    result = [intervals[0]]
    for start, end in intervals[1:]:
        if start <= result[-1][1]:
            result[-1][1] = max(result[-1][1], end)
        else:
            result.append([start, end])
    return result
print(merge([[1,3],[2,6],[8,10],[15,18]]))