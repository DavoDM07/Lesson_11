#Write a function that nds the index of a given element in a list. If the element is not
#present, return -1.

def numbers_index(numbers, num):
    for i in range(0, len(numbers)):
        if numbers[i] == num:
            return i
print(numbers_index([4,5,2,1,6,15,3], 6))
