#Write a function that calculates the average of a list of numbers

def arithmetic_mean(numbers):
    key = 0
    for i in numbers:
        key += i
    return int(key/len(numbers))
print(arithmetic_mean([1,2,4,15,6,8]))