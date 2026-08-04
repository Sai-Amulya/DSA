# Python is dynamically typed - no need to declare data type - can be changed as well mid program
x = 1
print(x)
x = 'abc'
print(x)

# Multiple assignments - ok to have multiple types in a single line 
n, m = 1, 'xyz'
print(n)
print(m)

# Increment
y = 1
y = y + 1
print(y)
y += 1        # x++ gives error
print(y)

# if statements dont need parantheses for condition or braces -> elif 
# parantheses needed for multi-line conditions -> && is and in python -> || is or in python
z = 10
if z == 0:
    print("zero")
elif z == 1:
    print("one")
else:
    print("not binary")

n,m = 1,2
if ((n > 2 and 
    n != m) or n == m):
    n += 1

# while loop - similar to other languages - prints 0 to 4
a = 0
while (a < 5):
    print (a)
    a += 1
# for - range 2 and 3 parameters - implicit increment
for i in range (0, 5):
    print (i)
# increment 2
for i in range (0, 5, 2):
    print (i)
# decrement 1 - last parameter -1 mandatory
for i in range (4, -1, -1):
    print (i)

# Math 
# Division is decimal by default
print (3 / 2 )  # 1.5, other lang -> 1
print (3 // 2)  # ROUND DOWN -> 1
print (-3 // 2) # ROUND DOWN -> -2 , expected is -1
print (int(-3 / 2)) # Workaround -> -1 
# Modulo for negative integers
print (10 % 3) # 1 as expected 
print (-10 % 3) # -2 -> not as intended 
# Workaround for modulo is to use fmod from math
import math
print (math.fmod(-10,3)) # -1
# Useful helper math functions
print (math.floor(3/2)) # 1
print (math.ceil(3/2)) # 2
print (math.pow(2,3)) # 8
print (math.sqrt(16)) # 4
# Max and Min integers are infinities--> Hence no overflow
float("inf")
float("-inf")
print(math.pow(2,200))
# But still less than infinity
print (math.pow(2,200) < float("inf")) # True


# Lists - dynamic arrays - can be like stack - append, pop, insert - O(n), reassign with index - const. time
# All 1s in array, -1 is last element 
# slicing, unpacking - no on left = no on right
arr = [1, 2, 3]
print (arr)
arr.append(4)   # [1, 2, 3, 4]
print (arr)
arr.append(5)   # [1, 2, 3, 4, 5]
print (arr)
arr.pop()       # [1, 2, 3, 4]
print (arr)
arr.insert(1, 7)    # [1, 7, 2, 3, 4]
print (arr)
arr[0] = 5      # [5, 7, 2, 3, 4]
print (arr)
arr1 = [1] * 4  # [1, 1, 1, 1]
print(arr1)
print(arr[-1])  # last element: 4
print(arr[1:3])    # index one to index 2 - 3 not included -> [7,2]
p, q, r = [1, 2, 3] # Unpacking
print (p, q, r)

# Loop through arrays - using index, without index, using index & value -> iterate through multiple arrays using zip
# using index
for i in range(len(arr)):
    print (arr[i])
# without index
for num in arr:
    print(num)
# using index & value
for i, n in enumerate(arr):
    print ((i, n))
nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
for n1, n2 in zip(nums1,nums2):
    print (n1, n2)

# Reverse, sort, sort reverse, sort strings, custom sort
# key is lambda which is a function without a name and we're gonna take every single element and call it x and return from that
# the length of x and this is the key thats gonna be used to sort the string
# so each string is gonna be mapped to its length and the strings are sorted based on that length - by default in asc order
nums = [2, 1, 7]
nums.reverse()
print (nums)
nums.sort()
print(nums)
nums.sort(reverse = True)
print(nums)
arr3 = ["doe", "alice", "jane", "bob"]
arr3.sort()
print(arr3)
arr3.sort(key = lambda x: len(x))
print(arr3)                         # is gonna be bob then doe even if doe appears before bob in the list

# List comprehension - to initialize a list  & 2-D list comprehension
arr = [i for i in range(5)] #[0, 1, 2, 3, 4]
print(arr)
arr = [i + i for i in range(5)]     #[0, 2, 4, 6, 8]
print(arr)
arr4 = [[0] * 4 for i in range(4)]
print (arr4) # [[0 0 0 0] [0 0 0 0] [0 0 0 0] [0 0 0 0]]
arr5 = [[0] * 4] * 4    # prints the same, but modifying one row would change in all other rows - not creating unique rows

# Strings are similar to arrays. Slice. But immutable - cannot replace in index, can be added, convert str to int and vice versa, ASCII - ord, .join() list with a delimiter
str0 = "abc"
print (str0[0:2])   # ab
# str[2] = 'd' # not possible as strings are immutable
str0 += "def"
print (str0) # abcdef
str1 = "123"
str2 = "456"
print (int(str1) + int(str2))   # 579
str3 = 123
str4 = 456
print (str(str1) + str(str2))   # 123456
print (ord("a"))    # 97
print (ord("b"))    # 98
strings = ["ab", "cd", "ef"]
print (" ".join(strings))   # ab cd ef 
print ("".join(strings))    # abcdef

# Queues - double ended -> append, pop(like stack), appendleft, popleft(constant time unlike with a stack)
from collections import deque
queue = deque()
queue.append(1)
queue.append(2)
print(queue)    # 1 2
queue.pop()
print(queue)    # 1
queue.appendleft(2)
print(queue)    # 2 1
queue.appendleft(3)
print(queue)    # 3 2 1
queue.popleft()
print(queue)    # 2 1 

# Hashset - search, add, remove in constant time, no duplicates, len, in, remove, list to set, set comprehension
'''A set is implemented as a hash table. When you add 'a', 'b', 'c', Python computes a hash for each string and uses 
that hash to decide which "slot" it goes into internally. When you print the set, items come out in whatever order 
their slots happen to be in — which depends on the hash values, not the order you wrote them in.
- It's not random each run (within the same Python version/session) — 
string hashing is deterministic within a run, but Python randomizes string hash seeds between runs for security reasons 
(to prevent hash-collision attacks). So you might see {'a', 'b', 'c'} one time you run the script and {'c', 'b', 'a'} 
another time.'''
mySet = set()
mySet.add(1)
mySet.add(2)
print(mySet)    # 1 2 
print(len(mySet))   # 2
print(1 in mySet)   # True
print(3 in mySet)   # False
mySet.remove(2)
print(mySet)    # 1 
mySet1 = set(['a', 'b', 'c'])
print(mySet1)   # a, b, c
mySet2 = {i for i in range(5)}
print(mySet2)   # 0, 1, 2, 3, 4

# HashMap (aka dict) - search, insert, remove in constant time, No duplicate keys, len is no. of keys, value can be modified
# in for search, pop to remove with key name- to remove key, insert the key with the value and pop the unwanted key value pair
# three ways to declare: manually declaring each key value, using curly braces, dict comprehension
# Looping : key, value with .values, key, value using .items
mydict = {}
mydict["alice"] = 88
mydict["bob"] = 77
print (mydict)
print (len(mydict)) # 2
mydict["alice"] = 80
print(mydict["alice"])
print ("alice" in mydict)   # True 
mydict.pop("alice")
print ("alice" in mydict)   # False
myMap = {"alex": 90, "ben": 70}
print (myMap)
myMap1 = { i: i+2 for i in range(5)}
print(myMap1)
for key in myMap:
    print(key, myMap[key])
for val in myMap.values():
    print(val)
for key,val in myMap.items():
    print(key,val)

# Tuples: like arrays but immutable, indexed but not modify, used as key for hashmap/set as list cant be and use tuple to search
tup = (1, 2, 3)
print (tup)     # 1 2 3
print(tup[0])   # 1
print(tup[-1])  # 3
# tup[0] = 0 is not possible
myMap = {(1,2): 3}
print(myMap[(1,2)])
mySet = set()
mySet.add((1,2))
print((1,2) in mySet)
# myMap[[3,4]] = 5 is not possible as lists cant be keys

# Heaps: mostly used to find min, max from a set of values, arrays under the hood, heapq.heappush, heappop, loop: while len pop
# minheap by default, to make maxheap, * -1 while pushing and popping, heapify to build heap from a list- linear time 
''' heapq implements a min-heap using a binary tree stored in a flat list, where the only guarantee is 
heap[i] <= heap[2*i+1] and heap[i] <= heap[2*i+2], every parent is ≤ both its children.
Since it is "every" parent, the first element will always be the least. Here, if directly printed without pop, the first element 
will be least but the others wont be sorted as they just need to satisfy the minheap rule.
But if you pop it, everytime the first element is the least of all and hence it is printed in sorted form. '''
import heapq
minHeap = []
heapq.heappush(minHeap, 3)
heapq.heappush(minHeap, 2)
heapq.heappush(minHeap, 4)
print(minHeap)  # 2 3 4
print(minHeap[0])   # 2
while len(minHeap):
    print(heapq.heappop(minHeap))   # 2 3 4 
maxHeap = []
heapq.heappush(maxHeap, -3)
heapq.heappush(maxHeap, -2)
heapq.heappush(maxHeap, -4)
print(maxHeap)
print(-1 * maxHeap[0])  # 4 
while len(maxHeap):
    print(-1 * heapq.heappop(maxHeap))   # 4 3 2 
arr = [2, 1, 8, 4, 5]
heapq.heapify(arr)
print(arr)
while arr:
    print(heapq.heappop(arr))   # 1 2 4 5 8

# Functions- def keyword, nested functions have access to outer variables - dont even have to pass the parameters
def outer(a,b):
    c = "c"
    def inner():
        return a + b + c
    return inner()
print(outer("a", "b"))

# Can modify objects but not reassign unless using nonlocal keyword
def double(arr, val):
    def helper():
        # Modifying array works
        for i, n in enumerate(arr):
            arr[i] *= 2
        # will only modify val in the helper scope
        # val *= 2
        # this will modify val outside helper scope
        nonlocal val
        val *= 2
    helper()
    print(arr, val)
nums = [1, 2]
val = 3
double (nums, val)

# Classes
class MyClass:
    # Constructor
    def __init__(self, nums):
        # Create member variables
        self.nums = nums
        self.size = len(nums)
    # self keyword required as param
    def getLength(self):
        return self.size
    def getDoubleLength(self):
        return 2 * self.getLength()
obj = MyClass([1, 2, 3, 4])
print(obj.nums)         # [1, 2, 3, 4]
print(obj.getLength())  # 4
print(obj.getDoubleLength())    # 8






