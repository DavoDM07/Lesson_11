#Write a function that calculates the sum of squares of numbers from 1 to n

def exponent_nums_sum(nums):
    sum = 0
    for i in nums:
        sum += i ** 2
    return sum
print(exponent_nums_sum([1,2,3,4,5,6,7,8,9,10]))

