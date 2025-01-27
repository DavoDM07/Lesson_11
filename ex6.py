#Write a function that counts the number of words in a sentence

def sentence_words(words):
    sum = 0
    words = words.split()
    for a in words:
        sum += 1
    return sum

print(sentence_words(input()))
